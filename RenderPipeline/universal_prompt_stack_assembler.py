from pathlib import Path


# =========================================================
# ROOT
# =========================================================

ROOT = Path(__file__).parent.resolve()

STACK_FILE = ROOT / "Active_Stack.md"

OUTPUT_FILE = ROOT / "prompt.md"


# =========================================================
# STACK PARSER
# =========================================================

def parse_stack(text: str) -> dict:

    stack = {}

    current_section = None

    for raw_line in text.splitlines():

        line = (
            raw_line
            .strip()
            .replace("\ufeff", "")
        )

        # Skip empty
        if not line:
            continue

        # Skip comments
        if line.startswith("#"):
            continue

        # New section
        if line.endswith(":"):

            current_section = line[:-1].strip()

            stack[current_section] = []

            continue

        # Module entry
        if current_section:

            stack[current_section].append(line)

    return stack


# =========================================================
# MODULE LOADER
# =========================================================

def load_module(relative_path: str) -> str:

    path = ROOT / relative_path

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

def build(stack: dict) -> str:

    blocks = []

    for section_name, modules in stack.items():

        blocks.append(
            "# =================================================="
        )

        blocks.append(
            f"# {section_name.upper()}"
        )

        blocks.append(
            "# ==================================================\n"
        )

        for module_path in modules:

            content = load_module(module_path)

            blocks.append(content)

            blocks.append("\n")

    return "\n".join(blocks)


# =========================================================
# OUTPUT
# =========================================================

def export_prompt(text: str):

    OUTPUT_FILE.write_text(
        text,
        encoding="utf-8"
    )

    print("===================================")
    print("Prompt assembly completed.")
    print(f"Output: {OUTPUT_FILE}")
    print("===================================")


# =========================================================
# MAIN
# =========================================================

def main():

    if not STACK_FILE.exists():

        raise FileNotFoundError(
            f"Stack file not found: {STACK_FILE}"
        )

    stack_text = STACK_FILE.read_text(
        encoding="utf-8"
    )

    stack = parse_stack(stack_text)

    final_prompt = build(stack)

    export_prompt(final_prompt)


# =========================================================
# ENTRY
# =========================================================

if __name__ == "__main__":
    main()