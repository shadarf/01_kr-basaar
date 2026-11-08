import re

with open("2-translation/04_Chapter-4.md", "r", encoding="utf-8") as f:
    content = f.read()

# Check which sections are empty
sections = content.split("§")
for i, sec in enumerate(sections[1:], 1):
    if (
        ">[!summary] Arabic Text\n>" in sec
        and ">[!summary] English Text\n>" in sec
        and ">[!summary] Kurdish Text\n>" in sec
    ):
        # Check if there's actual content after the markers
        lines = sec.split("\n")
        has_arabic = any(
            line.strip()
            and not line.strip().startswith(">")
            and not line.strip().startswith("---")
            and not line.strip().startswith("```")
            for line in lines[:20]
        )
        if not has_arabic:
            print(f"Section {i}: EMPTY")
