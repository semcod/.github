from contextlib import ExitStack, redirect_stdout, redirect_stderr
from io import StringIO
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import sync
from config import OrgConfig

CFG = OrgConfig('autogrammar', 'Autogrammar', 'https://autogrammar.github.io', [])


class SyncTests(unittest.TestCase):
    def test_private_repository_never_enables_pages(self):
        with patch.object(sync, 'extract_description', return_value=('Description', [])), patch.object(sync, 'run_gh', return_value=subprocess.CompletedProcess([], 0, '{"private":true}', '')), patch.object(sync, 'update_repo_metadata'), patch.object(sync, 'has_pages') as pages:
            result = sync.sync_repository(CFG, 'imgl', None, False)
        pages.assert_not_called()
        self.assertEqual(result['pages'], 'skip')

    def test_missing_visibility_fails_before_any_mutation(self):
        with patch.object(sync, 'extract_description', return_value=('Description', [])), patch.object(sync, 'run_gh', return_value=subprocess.CompletedProcess([], 0, '{}', '')), patch.object(sync, 'update_repo_metadata') as update:
            with self.assertRaises(RuntimeError):
                sync.sync_repository(CFG, 'imgl', None, False)
        update.assert_not_called()

    def test_metadata_only_never_sets_homepage_or_enables_pages(self):
        with patch.object(sync, 'extract_description', return_value=('Description', [])), patch.object(sync, 'run_gh', return_value=subprocess.CompletedProcess([], 0, '', '')) as gh, patch.object(sync, 'has_pages') as pages:
            sync.sync_repository(CFG, 'imgl', None, False, True)
        self.assertNotIn('--homepage', gh.call_args.args[0])
        pages.assert_not_called()

    def test_repository_failure_returns_nonzero(self):
        with ExitStack() as stack:
            stack.enter_context(patch.object(sys, 'argv', ['sync.py', '--org', 'autogrammar', '--repository', 'imgl', '--metadata-only']))
            stack.enter_context(patch.object(sync, 'load_org_config', return_value=CFG))
            stack.enter_context(patch.object(sync, 'list_org_repos', return_value=[{'name': 'imgl'}]))
            stack.enter_context(patch.object(sync, 'sync_repository', side_effect=RuntimeError('permission denied')))
            profile = stack.enter_context(patch.object(sync, 'write_profile'))
            stack.enter_context(redirect_stdout(StringIO()))
            stack.enter_context(redirect_stderr(StringIO()))
            self.assertEqual(sync.main(), 1)
            profile.assert_not_called()

    def test_profile_owner_mismatch_prevents_all_sync_effects(self):
        with patch.object(sys, 'argv', ['sync.py', '--org', 'autogrammar']), patch.object(sync, 'load_org_config', return_value=CFG), patch.object(sync.subprocess, 'check_output', return_value='git@github.com:semcod/.github.git\n'), patch.object(sync, 'list_org_repos') as listing, redirect_stderr(StringIO()):
            with self.assertRaises(SystemExit) as failure:
                sync.main()
            self.assertEqual(failure.exception.code, 2)
        listing.assert_not_called()
