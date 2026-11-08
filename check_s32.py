with open("2-translation/04_Chapter-4.md", "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("§32\n\n")
if idx >= 0:
    next_idx = content.find("§33\n\n", idx)
    section = content[idx : idx + 1000]
    with open("check_s32.txt", "w", encoding="utf-8") as f:
        f.write(section)
