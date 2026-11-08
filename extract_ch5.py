import fitz

doc = fitz.open("1-input/ar-basaar.pdf")
with open("chapter5_arabic.txt", "w", encoding="utf-8") as f:
    for i in range(314, 336):  # Pages 315-336 (0-indexed: 314-335)
        page = doc[i]
        text = page.get_text()
        f.write("=== PAGE {} ===\n".format(i + 1))
        f.write(text)
        f.write("\n\n")
print("Extracted Chapter 5 Arabic text (pages 315-336)")
