# universal_prompt_stack_assembler.py

from pathlib import Path


# =========================================================
# ROOT
# =========================================================

ROOT = Path(__file__).parent


# =========================================================
# ACTIVE STACK
# =========================================================

ACTIVE_STACK = [
    "CHARACTER",
    "WORLD",
    "VISUAL",
    "RULES",
]


# =========================================================
# MODULE LOADER
# =========================================================

def load_module(name: str) -> str:
    """
    Load a markdown module from local directory.
    """

    path = ROOT / f"{name}.md"

    if not path.exists():
        raise FileNotFoundError(
            f"Module not found: {path}"
        )

    return path.read_text(
        encoding="utf-8"
    ).strip()


# =========================================================
# PROMPT BUILD
# =========================================================

def build(stack: list[str]) -> str:
    """
    Assemble final prompt stack.
    """

    blocks = []

    for module_name in stack:

        content = load_module(module_name)

        blocks.append(content)

    return "\n\n".join(blocks)


# =========================================================
# OUTPUT
# =========================================================

def export_prompt(text: str):

    output_path = ROOT / "FINAL_PROMPT.md"

    output_path.write_text(
        text,
        encoding="utf-8"
    )

    print(f"[OK] Exported: {output_path}")


# =========================================================
# MAIN
# =========================================================

def main():

    final_prompt = build(ACTIVE_STACK)

    export_prompt(final_prompt)


if __name__ == "__main__":
    main()