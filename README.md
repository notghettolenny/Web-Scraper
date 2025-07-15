---

# 🌐 Web Scraper: Indeed Job Listings

![Python](https://img.shields.io/badge/built%20with-Python-3776AB?style=flat\&logo=python\&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/library-BeautifulSoup4-4B0082?style=flat)
![Selenium](https://img.shields.io/badge/library-Selenium-43B02A?style=flat\&logo=selenium\&logoColor=white)

This project is a Python script to scrape **Indeed.com** job listings for *Front-end developer* jobs in **Lagos, Nigeria**.

It loads the first page of results using Selenium, extracts job posting URLs, then fetches & parses each job detail page using `requests` and `BeautifulSoup`.

---

## ✨ Features

✅ Scrapes job listings from Indeed Nigeria
✅ Searches for a specific job title & location (default: *JavaScript Developer*, *Lagos*)
✅ Extracts and prints:

* Job title
* Location
* Company name
* Job posting URL
  ✅ Configurable: change job title & location by editing the URL in the script

---

## 🏗️ Tech Stack

| Component          | Technology                                                       |
| ------------------ | ---------------------------------------------------------------- |
| **Language**       | Python 3                                                         |
| **Web Automation** | [Selenium](https://www.selenium.dev/)                            |
| **HTML Parsing**   | [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) |
| **HTTP Requests**  | [requests](https://docs.python-requests.org/)                    |

---

## 📁 Files

* `webscraper.py` – main script to scrape job listings
* `webscraper2.py` – alternate version (if applicable)

---

## 🚀 Getting Started

### 📋 Prerequisites

* Python 3.6+
* Google Chrome
* ChromeDriver (compatible with your Chrome version)

---

### ⚙️ Installation

1️⃣ Clone the repository:

```bash
git clone https://github.com/notghettolenny/Web-Scraper.git
cd Web-Scraper
```

2️⃣ Install Python dependencies:

```bash
pip install selenium beautifulsoup4 requests
```

3️⃣ Download [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) and note its path.
Edit `webscraper.py` and replace the `driver = webdriver.Chrome(...)` line with your local path to `chromedriver`.

---

## 🐍 Usage

Run the scraper:

```bash
python webscraper.py
```

The script will:
✅ Open the Indeed search page for JavaScript Developer in Lagos
✅ Collect links to all jobs on the first page
✅ Visit each job’s page & print its details

---

## 🔄 Customization

To change the job title and location:

* Edit the `job_list` URL at the top of the script:

```python
job_list = "https://ng.indeed.com/jobs?q=your+job+title&l=your+location"
```

For example:

```python
job_list = "https://ng.indeed.com/jobs?q=data+analyst&l=Abuja"
```

---

## 📄 Notes

* The script only scrapes the **first page** of search results.
* Make sure your `chromedriver` version matches your installed Chrome version.
* Use responsibly and respect Indeed’s [terms of service](https://ng.indeed.com/legal).

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Contributing

Pull requests and suggestions are welcome.
Please open an [issue](https://github.com/notghettolenny/Web-Scraper/issues) first to discuss what you’d like to change.

---
