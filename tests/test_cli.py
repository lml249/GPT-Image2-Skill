from __future__ import annotations

import argparse
import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[1]
CLI_PATH = REPO_ROOT / "src" / "gpt_image_cli" / "cli.py"


def load_cli():
    spec = importlib.util.spec_from_file_location("gpt_image_cli_cli", CLI_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"could not load CLI from {CLI_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ModelOptionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cli = load_cli()

    def parse(self, *args: str):
        with patch("sys.argv", ["gpt-image", "-p", "test prompt", *args]):
            return self.cli.parse_args()

    def test_default_is_sunburst(self) -> None:
        args = self.parse()
        self.assertEqual(args.model, "gpt-image-2.5-sunburst")
        self.assertEqual(args.quality, "high")

    def test_flare_and_legacy_models_are_selectable(self) -> None:
        self.assertEqual(self.parse("--model", "gpt-image-2.5-flare").model, "gpt-image-2.5-flare")
        self.assertEqual(self.parse("--model", "gpt-image-2").model, "gpt-image-2")

    def test_25_quality_and_transparency_options_are_accepted(self) -> None:
        args = self.parse("--quality", "max", "--background", "transparent")
        self.assertEqual(args.quality, "max")
        self.assertEqual(args.background, "transparent")

    def test_legacy_model_rejects_25_only_options(self) -> None:
        with self.assertRaises(SystemExit):
            self.parse("--model", "gpt-image-2", "--quality", "xhigh")
        with self.assertRaises(SystemExit):
            self.parse("--model", "gpt-image-2", "--background", "transparent")

    def test_input_fidelity_is_dropped_for_25_edit(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            image = Path(tmp) / "reference.png"
            image.write_bytes(b"synthetic image")
            args = self.parse("--model", "gpt-image-2.5-sunburst", "-i", str(image), "--input-fidelity", "high")

            class Images:
                def __init__(self) -> None:
                    self.kwargs = None

                def edit(self, **kwargs):
                    self.kwargs = kwargs
                    return object()

            class Client:
                def __init__(self) -> None:
                    self.images = Images()

            client = Client()
            self.cli.call_edit(client, args)
            self.assertNotIn("input_fidelity", client.images.kwargs)

    def test_legacy_model_accepts_supported_quality_and_background(self) -> None:
        args = self.parse("--model", "gpt-image-2", "--quality", "high", "--background", "opaque")
        self.assertEqual(args.model, "gpt-image-2")
        self.assertEqual(args.background, "opaque")


class EndpointRoutingTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cli = load_cli()

    def test_generation_payload_uses_selected_model(self) -> None:
        args = argparse.Namespace(
            model="gpt-image-2.5-flare", prompt="test", size="landscape", quality="medium", n=1,
            background="transparent", moderation="low", output_format="png", output_compression=None, user=None,
        )

        class Images:
            def generate(self, **kwargs):
                self.kwargs = kwargs
                return object()

        class Client:
            def __init__(self):
                self.images = Images()

        client = Client()
        self.cli.call_generate(client, args)
        self.assertEqual(client.images.kwargs["model"], "gpt-image-2.5-flare")
        self.assertEqual(client.images.kwargs["background"], "transparent")


if __name__ == "__main__":
    unittest.main()
