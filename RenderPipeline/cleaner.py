from pathlib import Path
import re


# =========================================================
# ROOT
# =========================================================

ROOT = Path(__file__).parent.resolve()

INPUT_FILE = ROOT / "prompt.md"

OUTPUT_FILE = ROOT / "prompt_cleaned.txt"


# =========================================================
# FILTER RULES
# =========================================================

# Remove lines containing these keywords
REMOVE_CONTAINS = [

    "STATUS:",
    "SCOPE:",
    "Purpose",
    "Controls:",
    "Must remain",
    "Must NOT",
    "Defines:",
    "Examples:",
    "Recommended Direction:",
    "Controls:",
    "Priority",
    "SuppressionRules",
    "OWNERSHIP",
    "GLOBAL PRIORITY",
    "GLOBAL SUPPRESSION",
    "RUNTIME",
    "ASSEMBLY",
]

# Remove section names
REMOVE_SECTION_PATTERN = re.compile(
    r"^#+"
)

# Remove markdown separators
REMOVE_SEPARATOR_PATTERN = re.compile(
    r"^-{3,}$"
)

# Remove bracket section headers
REMOVE_BRACKET_PATTERN = re.compile(
    r"^\s*##\s*\[.*?\]"
)


# =========================================================
# CLEAN LINE
# =========================================================

def clean_line(line: str) -> str:

    line = line.strip()

    # Empty
    if not line:
        return ""

    # Markdown section
    if REMOVE_SECTION_PATTERN.match(line):
        return ""

    # Separator
    if REMOVE_SEPARATOR_PATTERN.match(line):
        return ""

    # [Section]
    if REMOVE_BRACKET_PATTERN.match(line):
        return ""

    # Remove meta keywords
    for keyword in REMOVE_CONTAINS:

        if keyword in line:
            return ""

    # Remove bullets
    line = re.sub(
        r"^[-•]\s*",
        "",
        line
    )

    # Remove > quote syntax
    line = re.sub(
        r"^>\s*",
        "",
        line
    )

    # Remove trailing commas
    line = line.rstrip(",")

    return line


# =========================================================
# TOKEN EXTRACTION
# =========================================================

def extract_tokens(text: str) -> list:

    tokens = []

    for raw_line in text.splitlines():

        line = clean_line(raw_line)

        if not line:
            continue

        # Skip very short lines
        if len(line) < 3:
            continue

        tokens.append(line)

    return tokens


# =========================================================
# DEDUPE
# =========================================================

def dedupe(tokens: list) -> list:

    seen = set()

    result = []

    for token in tokens:

        key = token.lower()

        if key in seen:
            continue

        seen.add(key)

        result.append(token)

    return result


# =========================================================
# FINAL FORMAT
# =========================================================

def build_prompt(tokens: list) -> str:

    return ",\n".join(tokens)


# =========================================================
# MAIN
# =========================================================

def main():

    if not INPUT_FILE.exists():

        raise FileNotFoundError(
            f"Input file not found: {INPUT_FILE}"
        )

    text = INPUT_FILE.read_text(
        encoding="utf-8"
    )

    tokens = extract_tokens(text)

    tokens = dedupe(tokens)

    final_prompt = build_prompt(tokens)

    OUTPUT_FILE.write_text(
        final_prompt,
        encoding="utf-8"
    )

    print("===================================")
    print("Prompt cleaning completed.")
    print(f"Output: {OUTPUT_FILE}")
    print("===================================")


# =========================================================
# ENTRY
# =========================================================

if __name__ == "__main__":
    main()