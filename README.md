# 📄 PubMed Fetcher: Automated Paper Extraction using PubMed API

## 🧠 Project Title

**PubMed Fetcher — A CLI Tool to Fetch Research Papers from PubMed**

---

## ✅ Objective

The goal of this project is to **automate the retrieval of PubMed research papers** using flexible queries and store them in a structured CSV format, including academic metadata and organizational affiliations.

---

## 🔍 Features

* ✅ Supports **full PubMed query syntax**
* ✅ Fetch papers by topic and **date range**
* ✅ Export results to CSV file
* ✅ Extracts:

  * PubMed ID
  * Title
  * Publication Date
  * Non-academic Authors
  * Company Affiliations
  * Corresponding Author Email
* ✅ CLI utility: `get-papers-list`
* ✅ Built with **Poetry**, and easy to install

---

## 🧱 Code Structure

```text
pubmed_fetcher_project/
├── pubmed_fetcher/
│   ├── __init__.py
│   ├── fetcher.py
│   ├── parser.py
│   ├── utils.py
│   ├── writer.py
├── __pycache__/                # Automatically generated (can be ignored in docs)
├── cli.py                      # Entry point for CLI
├── .gitignore
├── LICENSE                     # MIT License
├── poetry.lock                 # Poetry dependency lock file
├── pyproject.toml              # Project configuration and dependencies
├── README.md                   # Project documentation

```

## ⚙️ Setup Instructions

### 🔧 Prerequisites

* Python 3.10+
* Poetry (`pip install poetry`)

### 🔌 Installation

```bash
git clone https://github.com/satyampal123-sp/pubmed_fetcher_project.git
cd pubmed_fetcher_project
poetry install
```

---

## 🚀 Usage

To run the tool and export results to CSV:

```bash
poetry run get-papers-list "AI AND medical imaging" -d -f ai_imaging.csv
```

### 📌 Parameters:

| Argument        | Description                  |
| --------------- | ---------------------------- |
| `query`         | PubMed query string          |
| `-f <filename>` | CSV output file name         |
| `-d`            | Enables verbose/debug output |

---

## 📁 Output Format (CSV)

Each row contains:

* **PubmedID**
* **Title**
* **Publication Date**
* **Non-academic Author(s)**
* **Company Affiliation(s)**
* **Corresponding Author Email**

---

## 🧪 Testing

Run tests using:

```bash
poetry run pytest
```

---

## 🔄 Version Control

* The project uses Git and is hosted on GitHub
* Version control tracks commits, branches, and tags

GitHub Repo:
[https://github.com/satyampal123-sp/pubmed\_fetcher\_project](https://github.com/satyampal123-sp/pubmed_fetcher_project)

---

## 📦 Dependency Management

All dependencies are listed and managed via **Poetry** in `pyproject.toml`.

To add new packages:

```bash
poetry add <package-name>
```

---

## 📌 Key Technologies

* Python
* Entrez API (`Bio.Entrez`)
* CSV
* Regular Expressions
* CLI (`argparse`)
* Poetry

---

## 👤 Author

**Satyam Pal**
BCA Student | NSHM College of Management and Technology
Email: [satyampal123.sp@gmail.com](mailto:satyampal123.sp@gmail.com)

---

## 📜 License

This project is licensed under the **MIT License**.

---

Would you like me to generate this as a `README.md` file for your GitHub repo?
