with open("2-translation/04_Chapter-4.md", "r", encoding="utf-8") as f:
    content = f.read()

# Check sections 30-36
for sec_num in range(30, 37):
    marker = "§{}\n\n".format(sec_num)
    idx = content.find(marker)
    if idx >= 0:
        next_marker = content.find("§{}\n\n".format(sec_num + 1), idx)
        if next_marker == -1:
            next_marker = len(content)
        section = content[idx:next_marker]
        has_quran = "﴿" in section or "﴾" in section
        has_arabic = "الحقيقة" in section or "الحقيقة" in section
        with open("verify_sections.txt", "a", encoding="utf-8") as f:
            f.write(
                "Section {}: has_quran={}, has_arabic={}, length={}\n".format(
                    sec_num, has_quran, has_arabic, len(section)
                )
            )
