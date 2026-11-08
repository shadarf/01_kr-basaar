with open("2-translation/04_Chapter-4.md", "r", encoding="utf-8") as f:
    content = f.read()

for sec_num in range(30, 37):
    marker = "§{}\n\n".format(sec_num)
    idx = content.find(marker)
    if idx >= 0:
        next_idx = content.find("§{}\n\n".format(sec_num + 1), idx)
        if next_idx == -1:
            next_idx = len(content)
        section = content[idx:next_idx]
        lines = section.split("\n")
        content_lines = [
            l
            for l in lines
            if l.strip()
            and not l.strip().startswith(">")
            and not l.strip().startswith("---")
            and not l.strip().startswith("```")
        ]
        with open("section_lengths.txt", "a", encoding="utf-8") as f:
            f.write(
                "Section {}: {} content lines, total len={}\n".format(
                    sec_num, len(content_lines), len(section)
                )
            )
