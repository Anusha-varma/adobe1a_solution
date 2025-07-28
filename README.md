# Adobe India Hackathon - Round 1A Solution

## 🚀 Objective
Extract structured outline (Title, H1, H2, H3 with page numbers) from any PDF (≤50 pages).

## ⚙️ Tech Stack
- Python 3.10
- PyMuPDF (fitz)

## 🐳 Build & Run Instructions

### 1. Build Docker image
```bash
docker build --platform linux/amd64 -t adobe1a:latest .
```

### 2. Run Docker container
```bash
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none adobe1a:latest
```

## 📤 Output Format (sample)
```json
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "What is AI?", "page": 2 },
    { "level": "H3", "text": "History of AI", "page": 3 }
  ]
}
```