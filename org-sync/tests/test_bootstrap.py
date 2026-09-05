import importlib.util
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('bootstrap', ROOT / 'scripts/bootstrap_triggers.py')
bootstrap = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bootstrap)


class BootstrapTests(unittest.TestCase):
    def repository(self, root, remote):
        subprocess.run(['git', 'init', '-q', str(root)], check=True)
        subprocess.run(['git', '-C', str(root), 'remote', 'add', 'origin', remote], check=True)
        return root

    def test_migrated_repository_does_not_use_directory_owner(self):
        with tempfile.TemporaryDirectory() as directory:
            root = self.repository(Path(directory), 'git@github.com:autogrammar/imgl.git')
            self.assertEqual(bootstrap.ensure_trigger(root, 'semcod', False, True), 'owner_mismatch')
            self.assertFalse((root / '.github').exists())

    def test_managed_repository_does_not_reinstall_broken_trigger(self):
        with tempfile.TemporaryDirectory() as directory:
            root = self.repository(Path(directory), 'https://github.com/autogrammar/imgl.git')
            self.assertEqual(bootstrap.ensure_trigger(root, 'autogrammar', False, True), 'centrally_scheduled')
            self.assertFalse((root / '.github').exists())

    def test_dirty_work_is_preserved(self):
        with tempfile.TemporaryDirectory() as directory:
            root = self.repository(Path(directory), 'git@github.com:semcod/goal.git')
            (root / 'draft.txt').write_text('unrelated work')
            self.assertEqual(bootstrap.ensure_trigger(root, 'semcod', False, True), 'dirty_checkout')
            self.assertFalse((root / '.github').exists())
