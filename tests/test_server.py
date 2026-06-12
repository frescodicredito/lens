"""Server smoke tests.

py_compile only checks syntax; it never imports server.py. These tests actually
import the FastMCP server (catching import-time and tool-registration errors) and
exercise a representative set of tools end to end, asserting they return valid JSON.

Requires fastmcp (installed via `uv sync`).

Run with pytest:  pytest tests/test_server.py
Run standalone:   python tests/test_server.py
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import server  # noqa: E402

EXPECTED_TOOL_COUNT = 25


def _tool_names():
    return [n for n in dir(server) if n.startswith("lens_") and callable(getattr(server, n))]


def test_server_imports_and_registers_tools():
    names = _tool_names()
    assert len(names) == EXPECTED_TOOL_COUNT, (
        f"expected {EXPECTED_TOOL_COUNT} lens_* tools, found {len(names)}: {sorted(names)}"
    )


def test_read_tools_return_valid_json():
    for call in (
        server.lens_list_constraints(),
        server.lens_list_topologies(),
        server.lens_list_personas(),
        server.lens_get_constraint("inversion"),
        server.lens_get_topology("cascade"),
        server.lens_get_persona("cto-skeptic"),
        server.lens_efficacy_report(),
    ):
        json.loads(call)  # raises if a tool returned non-JSON


def test_compose_tools_work():
    constraints = json.dumps([{"type": "inversion"}, {"type": "premortem"}])
    result = json.loads(server.lens_compose_prompt("Test topic", constraints, "perspective_card", 4))
    assert "system_prompt" in result and "## Active constraints" in result["system_prompt"]

    persona = json.loads(server.lens_compose_persona("cto-skeptic", "Test topic"))
    assert "system_prompt" in persona

    suggested = json.loads(server.lens_suggest_constraints("Test topic", "stress-test the idea"))
    assert isinstance(suggested, (list, dict))


def test_invalid_input_is_handled_gracefully():
    # Unknown ids and bad JSON must return an error object, not raise.
    assert "error" in json.loads(server.lens_get_constraint("does_not_exist"))
    assert "error" in json.loads(server.lens_get_persona("../../etc/passwd"))
    assert "error" in json.loads(server.lens_compose_prompt("t", "not json", "raw", 3))


def _run_all():
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    failures = 0
    for t in tests:
        try:
            t()
            print(f"PASS {t.__name__}")
        except AssertionError as e:
            failures += 1
            print(f"FAIL {t.__name__}: {e}")
    print(f"\n{len(tests) - failures}/{len(tests)} passed")
    return failures


if __name__ == "__main__":
    sys.exit(1 if _run_all() else 0)
