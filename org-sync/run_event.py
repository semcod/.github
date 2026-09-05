"""Resolve full repository identities before invoking the metadata synchronizer."""
from __future__ import annotations

import json
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
REPOSITORY = re.compile(r"[A-Za-z0-9][A-Za-z0-9-]*/[A-Za-z0-9_][A-Za-z0-9_.-]*")


def select_targets(event_name: str, event: dict, coordinator: str, config: dict) -> tuple[list[str], bool]:
    if not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9-]*/\.github', coordinator):
        raise ValueError('Expected an organization profile coordinator')
    owner = coordinator.split('/')[0]
    managed = config['scheduled_repositories'] if coordinator == config['coordinator'] else []
    if not all(isinstance(item, str) and REPOSITORY.fullmatch(item) for item in managed):
        raise ValueError('Invalid scheduled repository identity')
    if event_name == 'schedule':
        return [owner, *managed], False
    if event_name == 'workflow_dispatch':
        inputs = event.get('inputs') or {}
        target = inputs.get('repository') or owner
        dry_run = inputs.get('dry_run', False)
        if type(dry_run) is not bool and (not isinstance(dry_run, str) or dry_run not in ('true', 'false')):
            raise ValueError('Invalid dry_run input')
        dry_run = dry_run in (True, 'true')
        if isinstance(target, str) and '/' not in target and target != owner:
            target = owner + '/' + target
    elif event_name == 'repository_dispatch':
        if event.get('action') != 'org-repo-changed':
            raise ValueError('Unsupported dispatch action')
        target = (event.get('client_payload') or {}).get('repository')
        dry_run = False
    else:
        raise ValueError('Unsupported event')
    if target == owner and event_name == 'workflow_dispatch':
        return [owner], dry_run
    if not isinstance(target, str) or not REPOSITORY.fullmatch(target):
        raise ValueError('Expected a full owner/repository identity')
    target = target.lower()
    if target.split('/')[0] != owner.lower() and target not in managed:
        raise ValueError('Repository is outside the managed coordinator scope')
    return [target], dry_run


def run_targets(targets: list[str], dry_run: bool, coordinator: str) -> int:
    failures = 0
    owner = coordinator.split('/')[0]
    for target in targets:
        org, _, name = target.partition('/')
        command = [sys.executable, str(ROOT / 'sync.py'), '--org', org]
        if name:
            command.extend(['--repository', name])
        if org != owner:
            # Foreign projects retain their homepage, Pages and org profile.
            command.extend(['--metadata-only', '--skip-profile'])
        if dry_run:
            command.append('--dry-run')
        result = subprocess.run(command, check=False)
        failures += result.returncode != 0
    return 1 if failures else 0


def main() -> int:
    try:
        config = json.loads((ROOT / 'managed-repositories.json').read_text())
        event = json.loads(Path(os.environ['GITHUB_EVENT_PATH']).read_text())
        coordinator = os.environ['GITHUB_REPOSITORY']
        targets, dry_run = select_targets(os.environ['GITHUB_EVENT_NAME'], event, coordinator, config)
    except (ValueError, KeyError, TypeError, OSError) as error:
        print(f'Invalid sync request: {error}', file=sys.stderr)
        return 1
    return run_targets(targets, dry_run, coordinator)


if __name__ == '__main__':
    raise SystemExit(main())
