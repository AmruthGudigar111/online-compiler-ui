# Online Python & C Compiler

This project provides an online compiler supporting Python and C with a web-based code editor.

## Features

- Supports Python and C code
- Takes user input via stdin
- Displays output and errors
- Saves last session in browser
- Light/Dark theme toggle

## Getting Started

### Frontend

1. Open `frontend/index.html` in your browser.
2. Or deploy it via GitHub Pages.

### Backend

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run Flask server:

```bash
python app.py
```

### Deployment

- Frontend: GitHub Pages / Netlify
- Backend: Render.com or Railway

Update the API URL in `index.html` if deployed.

## Sample Input

```python
name = input("Enter your name: ")
print("Hello,", name)
```

Input:
```
John
```

Output:
```
Hello, John
```

---
