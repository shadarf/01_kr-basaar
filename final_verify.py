with open("2-translation/04_Chapter-4.md", "r", encoding="utf-8") as f:
    content = f.read()

# Count sections
sections = content.count("§")
# Count Quranic verses
verses = content.count("﴿")
# Count Arabic blocks with content
arabic_blocks = content.count(">[!summary] Arabic Text\n>") - content.count(
    ">[!summary] Arabic Text\n>\n"
)

with open("final_stats.txt", "w", encoding="utf-8") as f:
    f.write("Sections: {}\n".format(sections))
    f.write("Quranic verses: {}\n".format(verses))
    f.write("Arabic blocks with content: {}\n".format(arabic_blocks))
    f.write("File size: {} KB\n".format(len(content) / 1024))
