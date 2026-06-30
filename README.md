# Web Analyzer

A simple web-based website analyzer built with **Flask**, **SQLite**, **BeautifulSoup**, and **Tailwind CSS 4**.

The application analyzes a target website in read-only mode, extracts useful metadata and page information, stores scan results in a SQLite database, and provides a history of previous scans.

---

## Features

* Website analysis
* Read-only crawling
* SQLite database storage
* Scan history
* Detailed report page
* SEO metadata extraction
* HTTP response information
* Heading extraction (H1–H6)
* CSS & JavaScript asset detection
* Image detection
* Internal & external link analysis
* Email & phone extraction
* Social media link detection
* Open Graph extraction
* Twitter Card extraction
* JSON-LD extraction
* robots.txt detection
* sitemap.xml detection
* HTML hash generation

---

## Technologies

* Python 3.11+
* Flask
* Flask-SQLAlchemy
* SQLite
* Requests
* BeautifulSoup4
* lxml
* Tailwind CSS 4

---

## Project Structure

```
web-analyzer/
│
├── app.py
├── models.py
├── database.db
├── scraper/
│   └── scraper.py
│
├── templates/
│   ├── index.html
│   ├── reports.html
│   └── report.html
│
├── static/
│   └── css/
│       └── output.css
│
├── package.json
├── requirements.txt
└── README.md
```

---

## Installation

Clone the project.

```bash
git clone https://github.com/Mhyar-nsi/Web-Analyzer.git
cd web-analyzer
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate the virtual environment.

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install Python dependencies.

```bash
pip install Flask Flask-SQLAlchemy requests beautifulsoup4 lxml
```

Install Tailwind CSS.

```bash
npm install
```

---

## Build Tailwind CSS

Run:

```bash
npx @tailwindcss/cli \
-i ./static/css/input.css \
-o ./static/css/output.css \
--watch
```

Keep this process running while developing.

---

## Run the Project

Start the Flask server.

```bash
python app.py
```

Open your browser.

```
http://127.0.0.1:5000
```

---

## Available Routes

| Route          | Description          |
| -------------- | -------------------- |
| `/`            | Website analyzer     |
| `/reports`        | Scan history         |
| `/report/<id>` | Detailed scan report |

---

## Database

The project uses SQLite.

Database file:

```
database.db
```

Tables are created automatically on the first run.

---

## Notes

* The analyzer performs **read-only** requests.
* It does not attempt to bypass authentication.
* It does not execute intrusive or destructive actions.
* Only publicly accessible content is analyzed.

---

## License

This project is intended for educational purposes.
