from pathlib import Path
import re

# ==================================================
# CONFIG
# ==================================================

BASE_DIR = Path(__file__).parent.resolve()

STACK_FILE = BASE_DIR / "active_stack.md"
MODULE_DIR = BASE_DIR / "modules"
OUTPUT_DIR = BASE_DIR / "output"

OUTPUT_FILE = OUTPUT_DIR / "final_prompt.md"

# ==================================================
# OUTPUT SETUP
# ==================================================

OUTPUT_DIR.mkdir(exist_ok=True)

# ==================================================
# STACK PARSER
# ==================================================

def parse_stack(stack_text):
    stack = {}

    current_section = None
        
    for raw_line in stack_text.splitlines():
        line =(
        raw_line
        .strip()
        .replace("\ufeff", "")
        )

        # Skip empty lines
        if not line:
            continue

        # Skip comments
        if line.startswith("#"):
            continue

        # Section
        if line.endswith(":"):
            current_section = line[:-1].strip()
            stack[current_section] = []
            continue

        # Module entry
        if current_section:
            stack[current_section].append(line)

    return stack

# ==================================================
# MODULE LOADER
# ==================================================

def load_module(module_name):
    """
    Recursively search modules directory
    for matching md file.
    """

    matches = list(
        MODULE_DIR.rglob(f"{module_name}.md")
    )

    if not matches:
        raise FileNotFoundError(
            f"Module not found: {module_name}"
        )

    if len(matches) > 1:
        raise ValueError(
            f"Multiple modules found for: {module_name}"
        )

    path = matches[0]

    with open(path, "r", encoding="utf-8") as f:
        return f.read()

# ==================================================
# RULE EXTRACTION
# ==================================================

def extract_block(content, block_name):
    pattern = rf"\[{re.escape(block_name)}\](.*?)(?=\n\[|$)"

    match = re.search(
        pattern,
        content,
        re.DOTALL
    )

    if not match:
        return []

    block = match.group(1)

    lines = []

    for line in block.splitlines():
        clean = line.strip()

        if not clean:
            continue

        lines.append(clean)

    return lines

# ==================================================
# RULE MERGING
# ==================================================

def merge_unique(items):
    seen = set()
    result = []

    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result

# ==================================================
# PROMPT BUILDER
# ==================================================

def build_prompt(stack):

    prompt_sections = []

    suppression_rules = []
    priority_rules = []

    for section_name, modules in stack.items():

        prompt_sections.append(
            f"# =================================================="
        )

        prompt_sections.append(
            f"# {section_name.upper()}"
        )

        prompt_sections.append(
            f"# ==================================================\n"
        )

        for module_name in modules:

            content = load_module(module_name)

            prompt_sections.append(content)
            prompt_sections.append("\n")

            # Collect rules
            suppression_rules.extend(
                extract_block(
                    content,
                    "SuppressionRules"
                )
            )

            priority_rules.extend(
                extract_block(
                    content,
                    "Priority"
                )
            )

    # ==================================================
    # MERGED RULES
    # ==================================================

    prompt_sections.append(
        "# =================================================="
    )

    prompt_sections.append(
        "# MERGED GLOBAL RULES"
    )

    prompt_sections.append(
        "# ==================================================\n"
    )

    # Suppression Rules
    merged_suppression = merge_unique(
        suppression_rules
    )

    if merged_suppression:
        prompt_sections.append(
            "[SuppressionRules]"
        )

        for rule in merged_suppression:
            prompt_sections.append(rule)

        prompt_sections.append("")

    # Priority Rules
    merged_priority = merge_unique(
        priority_rules
    )

    if merged_priority:
        prompt_sections.append(
            "[Priority]"
        )

        for rule in merged_priority:
            prompt_sections.append(rule)

        prompt_sections.append("")

    return "\n".join(prompt_sections)

# ==================================================
# MAIN
# ==================================================

def main():

    if not STACK_FILE.exists():
        raise FileNotFoundError(
            "active_stack.md not found"
        )

    with open(STACK_FILE, "r", encoding="utf-8") as f:
        stack_text = f.read()

    stack = parse_stack(stack_text)

    final_prompt = build_prompt(stack)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(final_prompt)

    print("===================================")
    print("Prompt assembly completed.")
    print(f"Output: {OUTPUT_FILE}")
    print("===================================")

# ==================================================
# ENTRY
# ==================================================

if __name__ == "__main__":
    main()