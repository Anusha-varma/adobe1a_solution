def extract_outline(doc):
    font_sizes = {}
    headings = []
    title = ""

    for page_number, page in enumerate(doc, 1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                for span in line["spans"]:
                    text = span["text"].strip()
                    if not text or len(text) < 3:
                        continue

                    size = span["size"]
                    font_sizes[size] = font_sizes.get(size, 0) + 1

    sorted_sizes = sorted(font_sizes.items(), key=lambda x: -x[0])
    sizes = [s[0] for s in sorted_sizes[:3]]

    if sizes:
        title_size = sizes[0]
        h1_size = sizes[0]
        h2_size = sizes[1] if len(sizes) > 1 else sizes[0]
        h3_size = sizes[2] if len(sizes) > 2 else sizes[-1]
    else:
        title_size = h1_size = h2_size = h3_size = 12

    outline = []

    for page_number, page in enumerate(doc, 1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                for span in line["spans"]:
                    text = span["text"].strip()
                    size = span["size"]
                    if not text or len(text) < 3:
                        continue
                    level = None
                    if abs(size - h1_size) < 0.5:
                        level = "H1"
                    elif abs(size - h2_size) < 0.5:
                        level = "H2"
                    elif abs(size - h3_size) < 0.5:
                        level = "H3"

                    if level:
                        outline.append({
                            "level": level,
                            "text": text,
                            "page": page_number
                        })

                    if page_number == 1 and abs(size - title_size) < 0.5 and not title:
                        title = text

    return {
        "title": title if title else "Untitled Document",
        "outline": outline
    }