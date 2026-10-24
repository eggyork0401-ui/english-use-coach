import csv
import importlib.util
import io
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills/english-use-coach/scripts/export_anki.py"
spec = importlib.util.spec_from_file_location("export_anki", SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class ExportTests(unittest.TestCase):
    def test_roundtrip_chinese_quotes_and_tags(self):
        card = {"front": '表达“确认”时说 "confirm"', "back": "Could you confirm?", "tags": ["会议", "follow-up", "会议"]}
        result = module.render_cards([card])
        data = "\n".join(line for line in result.splitlines() if not line.startswith("#"))
        rows = list(csv.reader(io.StringIO(data), delimiter="\t"))
        self.assertEqual(rows, [[card["front"], card["back"], "会议 follow-up"]])
        self.assertIn("#tags column:3\n", result)
        self.assertIn("#html:false\n", result)

    def test_empty_optional_tags_keeps_third_column(self):
        text = module.render_cards([{"front": "请求", "back": "Could you help?"}])
        row = next(csv.reader([text.splitlines()[-1]], delimiter="\t"))
        self.assertEqual(row, ["请求", "Could you help?", ""])

    def test_reject_invalid_schema_and_unsafe_fields(self):
        invalid = [[], {}, ["text"], [{"front": "x"}],
                   [{"front": " ", "back": "y"}],
                   [{"front": "x\ty", "back": "z"}],
                   [{"front": "x", "back": "a\nb"}],
                   [{"front": "#separator:Comma", "back": "x"}],
                   [{"front": "x", "back": "<b>y</b>"}],
                   [{"front": "x", "back": "y", "tags": "english"}],
                   [{"front": "x", "back": "y", "tags": ["two words"]}],
                   [{"front": "x", "back": "y", "typo": 1}],
                   [{"front": "x", "back": "y"}, {"front": " x ", "back": "z"}]]
        for case in invalid:
            with self.subTest(case=case), self.assertRaises(ValueError):
                module.render_cards(case)

    def test_preserve_existing_file_unless_explicit_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            src, dst = Path(tmp) / "in.json", Path(tmp) / "out.tsv"
            src.write_text(json.dumps([{"front": "x", "back": "y"}]), encoding="utf-8")
            dst.write_text("existing", encoding="utf-8")
            with self.assertRaises(FileExistsError):
                module.export_cards(src, dst)
            self.assertEqual(dst.read_text(), "existing")
            self.assertEqual(module.export_cards(src, dst, overwrite=True), 1)
            self.assertIn("x\ty\t\n", dst.read_text())

    def test_invalid_input_does_not_touch_destination(self):
        with tempfile.TemporaryDirectory() as tmp:
            src, dst = Path(tmp) / "in.json", Path(tmp) / "out.tsv"
            src.write_text('[{"front":"x"}]', encoding="utf-8")
            with self.assertRaises(ValueError):
                module.export_cards(src, dst)
            self.assertFalse(dst.exists())

    def test_same_path_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            src = Path(tmp) / "in.json"
            src.write_text("[]", encoding="utf-8")
            with self.assertRaises(ValueError):
                module.export_cards(src, src, overwrite=True)
            self.assertEqual(src.read_text(), "[]")

    def test_cli_sample_cards(self):
        with tempfile.TemporaryDirectory() as tmp:
            dst = Path(tmp) / "out.tsv"
            sample = ROOT / "skills/english-use-coach/assets/sample-cards.json"
            result = subprocess.run([sys.executable, str(SCRIPT), str(sample), str(dst)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(len([line for line in dst.read_text(encoding="utf-8").splitlines() if not line.startswith("#")]), 3)
            result = subprocess.run([sys.executable, str(SCRIPT), str(sample), str(dst)], capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
