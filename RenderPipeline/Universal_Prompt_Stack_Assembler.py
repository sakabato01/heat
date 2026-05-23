from pathlib import Path
from collections import OrderedDict
import re

# =========================================================
# UNIVERSAL PROMPT STACK ASSEMBLER
# =========================================================

MODULE_DIR = Path("./modules")

STACK_FILE = Path("./active_stack.md")

OUTPUT_DIR = Path("./output")
OUTPUT_DIR.mkdir(exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "final_prompt.md"


# =========================================================
# Parse Active Stack
# =========================================================

def parse_stack_file(path):

    stack = OrderedDict()

    current_section = None

    with open(path, "r", encoding="utf-8") as f:

        for raw_line in f:

            line = raw_line.strip()

            if not line:
                continue

            # Ignore comments
            if line.startswith("#"):
                continue

            # Section
            if line.endswith(":"):

                current_section = line[:-1]

                stack[current_section] = []

                continue

            # Module
            if current_section:
                stack[current_section].append(line)

    return stack


# =========================================================
# Load Module
# =========================================================

def load_module(module_name):

    path = MODULE_DIR / f"{module_name}.md"

    if not path.exists():
        raise FileNotFoundError(f"Module not found: {path}")

    with open(path, "r", encoding="utf-8") as f:
        return f.read()


# =========================================================
# Extract Rules
# =========================================================

def extract_rules(content):

    suppression = []
    priority = []

    suppression_match = re.search(
        r"\[SuppressionRules\](.*?)\[Priority\]",
        content,
        re.DOTALL
    )

    if suppression_match:

        lines = suppression_match.group(1).strip().splitlines()

        for line in lines:

            line = line.strip()

            if line and not line.startswith("["):
                suppression.append(line)

    priority_match = re.search(
        r"\[Priority\](.*)",
        content,
        re.DOTALL
    )

    if priority_match:

        lines = priority_match.group(1).strip().splitlines()

        for line in lines:

            line = line.strip()

            if line and not line.startswith("["):
                priority.append(line)

    return suppression, priority


# =========================================================
# Deduplicate Rules
# =========================================================

def deduplicate(items):

    seen = set()

    output = []

    for item in items:

        normalized = item.lower()

        if normalized not in seen:

            seen.add(normalized)

            output.append(item)

    return output


# =========================================================
# Remove RULES block from module body
# =========================================================

def remove_rules(content):

    cleaned = re.sub(
        r"# RULES.*",
        "",
        content,
        flags=re.DOTALL
    ).strip()

    return cleaned


# =========================================================
# Build Final Prompt
# =========================================================

def build_prompt(stack):

    output = []

    all_suppression = []
    all_priority = []

    output.append("# GENERATED PROMPT STACK\n")

    for section, modules in stack.items():

        output.append("\n# ==================================================")
        output.append(f"# {section.upper()}")
        output.append("# ==================================================\n")

        for module_name in modules:

            content = load_module(module_name)

            suppression, priority = extract_rules(content)

            all_suppression.extend(suppression)
            all_priority.extend(priority)

            cleaned_content = remove_rules(content)

            output.append(f"\n<!-- MODULE: {module_name} -->\n")

            output.append(cleaned_content)

            output.append("\n")

    # =====================================================
    # MERGED RULES
    # =====================================================

    output.append("\n# ==================================================")
    output.append("# MERGED RULES")
    output.append("# ==================================================\n")

    merged_suppression = deduplicate(all_suppression)
    merged_priority = deduplicate(all_priority)

    output.append("[SuppressionRules]\n")

    for item in merged_suppression:
        output.append(item)

    output.append("\n")

    output.append("[Priority]\n")

    for item in merged_priority:
        output.append(item)

    output.append("\n")

    return "\n".join(output)


# =========================================================
# Main
# =========================================================

def main():

    print("======================================")
    print("UNIVERSAL PROMPT STACK ASSEMBLER")
    print("======================================")

    stack = parse_stack_file(STACK_FILE)

    print("\nLoaded Stack:\n")

    for section, modules in stack.items():

        print(f"{section}:")

        for module in modules:
            print(f"  - {module}")

    final_prompt = build_prompt(stack)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(final_prompt)

    print("\n======================================")
    print(f"Generated: {OUTPUT_FILE}")
    print("======================================")


if __name__ == "__main__":
    main()
