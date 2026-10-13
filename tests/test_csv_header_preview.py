import importlib.util
import io
import json
import contextlib
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location('header_sample', Path(__file__).resolve().parents[1] / 'csv_header_preview.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class HeaderPreviewTests(unittest.TestCase):
    def test_cli_runs_without_writing_files(self):
        import subprocess
        import sys
        import tempfile
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run([sys.executable, str(Path(module.__file__).resolve()), ' A ', 'a'], cwd=directory, text=True, capture_output=True, check=True)
            self.assertEqual(json.loads(result.stdout)['headers'][1]['proposed'], 'a_2')
            self.assertEqual(list(Path(directory).iterdir()), [])

    def test_collision_order_matches_existing_tool(self):
        values = ['a', 'a', 'a_2', 'a', ' A ']
        original = values.copy()
        actual = module.preview_headers(values)
        self.assertEqual([x['proposed'] for x in actual], ['a', 'a_2', 'a_2_2', 'a_3', 'a_4'])
        self.assertEqual([x['original'] for x in actual], original)
        self.assertEqual(values, original)
        self.assertEqual([x['position'] for x in actual], [1, 2, 3, 4, 5])

    def test_lossy_and_empty_names_are_visible(self):
        result = module.preview_headers(['', '名', 'é', 'USD $', 'USD €'])
        self.assertEqual([x['proposed'] for x in result], ['column', 'column_2', 'column_3', 'usd', 'usd_2'])
        self.assertEqual(result[1]['original'], '名')

    def test_cli_valid_json_and_warning(self):
        stream = io.StringIO()
        with contextlib.redirect_stdout(stream):
            self.assertEqual(module.main([' Client Name ', 'Client-Name']), 0)
        result = json.loads(stream.getvalue())
        self.assertIn('can lose', result['warning'])
        self.assertEqual(result['headers'][1]['proposed'], 'client_name_2')

    def test_cli_requires_headers(self):
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as error:
            module.main([])
        self.assertEqual(error.exception.code, 2)

if __name__ == '__main__':
    unittest.main()
