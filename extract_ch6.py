import fitz

doc = fitz.open("1-input/ar-basaar.pdf")
with open("chapter6_arabic.txt", "w", encoding="utf-8") as f:
    for i in range(336, 352):  # Pages 337-352 (0-indexed: 336-351)
        page = doc[i]
        text = page.get_text()
        f.write(f"=== PAGE {i + 1} ===\n")
        f.write(text)
        f.write("\n\n")
print("Extracted Chapter 6 Arabic text (pages 337-352)")
