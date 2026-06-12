"""Lens quickstart — compose a constrained prompt without any MCP setup.

Run from the repo root:

    python examples/quickstart.py

This demonstrates the core of Lens (constraints -> structured prompt) using the
composer directly, so you can verify the system works in ~10 seconds before
wiring it into Claude Code as an MCP server.
"""

import sys
from pathlib import Path

# Allow running directly from the repo without installing the package.
sys.path.insert(0, str(Path(__file__).parent.parent))

from constraints.composer import compose_prompt, suggest_constraints  # noqa: E402


def main():
    topic = "Should a B2B SaaS startup add a free tier?"

    # 1. Let Lens suggest constraints for the topic (heuristic, no history needed).
    suggested = suggest_constraints(topic=topic, goal="stress-test the decision")
    print("=" * 70)
    print("SUGGESTED CONSTRAINTS")
    print("=" * 70)
    print(suggested)
    print()

    # 2. Compose a structured prompt from two explicit constraints.
    constraints = [
        {"type": "premortem"},
        {"type": "inversion"},
    ]
    result = compose_prompt(
        constraints=constraints,
        topic=topic,
        output_format="perspective_card",
        intensity=4,
    )

    print("=" * 70)
    print("COMPOSED SYSTEM PROMPT")
    print("=" * 70)
    print(result["system_prompt"])
    print()

    if result["warnings"]:
        print("WARNINGS:", result["warnings"])
    else:
        print("WARNINGS: none")

    print("\nMETADATA:", result["metadata"])


if __name__ == "__main__":
    main()
