"""The Codex CLI card: connect checks the endpoint first, a refused key saves nothing,
and the saved key never travels to a newly entered endpoint."""
from _paths import ROOT, SERVER  # noqa: F401
import asyncio
import os
import tempfile
from unittest.mock import patch

os.environ["JAVIS_STATE_DIR"] = tempfile.mkdtemp(prefix="javis-cc-connect-")

import config as cfg  # noqa: E402
import main  # noqa: E402


class Request:
    def __init__(self, body):
        self.body = body

    async def json(self):
        return self.body


class Response:
    def __init__(self, status_code=200):
        self.status_code = status_code

    def json(self):
        return {"data": [{"id": "gw-model"}]}


seen = []


class Client:
    def __init__(self, **kwargs):
        pass

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        pass

    async def get(self, url, headers):
        seen.append((url, headers.get("Authorization")))
        return Response(401 if "rejected.example" in url else 200)


async def check():
    with patch("httpx.AsyncClient", Client), patch("main.find_codex_cli", lambda: "codex"):
        first = await main.codex_cli_connect(Request({
            "name": "9router", "base": "http://localhost:20128/v1", "key": "tok-1"}))
        assert first["ok"], first
        # Same endpoint, blank key: the saved key stays.
        again = await main.codex_cli_connect(Request({
            "name": "9router", "base": "http://localhost:20128/v1", "key": ""}))
        assert again["ok"], again
        # A different endpoint saves nothing when the key there is refused.
        rejected = await main.codex_cli_connect(Request({
            "name": "bad", "base": "https://rejected.example/v1", "key": "new-key"}))
        assert not rejected["ok"]
        missing = await main.codex_cli_connect(Request({"name": "", "base": "http://x/v1"}))
        assert not missing["ok"]
    assert seen[0] == ("http://localhost:20128/v1/models", "Bearer tok-1"), seen[0]
    assert seen[1] == ("http://localhost:20128/v1/models", "Bearer tok-1"), seen[1]
    m = cfg.read_settings()["model"]
    assert m["codex_cli_name"] == "9router"
    assert m["codex_cli_base"] == "http://localhost:20128/v1"
    assert m["codex_cli_key"] == "tok-1"
    # Live list remembered under the card's own catalog key.
    cat = cfg.read_settings()["model"]["catalog"]
    assert cat["codex-cli"] == ["gw-model"], cat


asyncio.run(check())
print("OK - codex-cli connect checks first, key stays bound to its endpoint")
