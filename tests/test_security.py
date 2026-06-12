"""Security regression tests.

Lock the path-traversal hardening: ids that flow into file paths must never
escape their intended directory. If any of these fail, a traversal hole has
been reintroduced.

Run standalone:   python tests/test_security.py
Run with pytest:  pytest tests/test_security.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from constraints.composer import safe_identifier, load_persona  # noqa: E402
from integrations.miner import transform_miner_persona, save_miner_persona  # noqa: E402

TRAVERSAL = [
    "../../etc/passwd",
    "../secrets",
    "/etc/hosts",
    "a/b",
    "a\\b",
    "..",
    ".",
    "",
]


def test_safe_identifier_rejects_traversal():
    for bad in TRAVERSAL:
        try:
            safe_identifier(bad)
            raise AssertionError(f"safe_identifier accepted unsafe id {bad!r}")
        except ValueError:
            pass


def test_safe_identifier_accepts_real_ids():
    for good in ["inversion", "cto-scettico", "lens-20260228-225903-249ddd", "miner-cfo"]:
        assert safe_identifier(good) == good


def test_load_persona_blocks_traversal():
    for bad in ["../../../../etc/hosts", "/etc/hosts", "a/b"]:
        try:
            load_persona(bad)
            raise AssertionError(f"load_persona read traversal id {bad!r}")
        except ValueError:
            pass  # rejected before any file access — correct


def test_miner_slug_is_path_safe():
    for bad_name in ["../../../../tmp/pwn", "a/../../b", "/abs/evil", "..\\..\\x"]:
        pid = transform_miner_persona({"name": bad_name})["id"]
        assert "/" not in pid and "\\" not in pid and ".." not in pid, f"unsafe id {pid!r}"
        assert pid.startswith("miner-")


def test_miner_save_stays_in_templates_dir():
    # A template whose id was forced to traverse must be refused at write time.
    evil = {"id": "../../../../tmp/pwn", "description": "x", "constraints": []}
    try:
        save_miner_persona(evil)
        raise AssertionError("save_miner_persona wrote outside templates dir")
    except ValueError:
        pass


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
