# Personal Portfolio Website

This project is a personal portfolio website built with Python and FastAPI, using Jinja2 for templating. It is designed to be elegant, professional, and fully responsive for both desktop and mobile devices. The color palette avoids blue and uses modern, professional shades. The site includes Home, About, Login, and other relevant sections for showcasing skills and experience.

## Features
- FastAPI backend
- Jinja2 templating for HTML
- Responsive design (mobile & desktop)
- Professional color palette (no blue)
- Pages: Home, About, Login, Skills, Projects, Contact

## Getting Started
1. Create a virtual environment:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```sh
   pip install fastapi uvicorn jinja2 python-multipart passlib[bcrypt]
   ```
3. Run the server:
   ```sh
   uvicorn main:app --reload
   ```
4. Open your browser at http://127.0.0.1:8000

## Folder Structure
- `main.py` - FastAPI app entry point
- `templates/` - Jinja2 HTML templates
- `static/` - CSS, images, and other static files
- `.github/copilot-instructions.md` - Copilot custom instructions

## Customization
- Update content in `templates/` to reflect your skills and experience.
- Replace placeholder images in `static/images/` with your own.

---

© 2025 Anupam Kumar. All rights reserved.
