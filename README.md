# AI-Powered-Wed-scrapper-and-parser
This application allows users to scrape content from any website and parse specific information into structured formats like Excel or PowerPoint.

A powerful, local web scraping tool built with **Streamlit**, **Selenium**, and **Ollama**. This application allows users to scrape content from any website, clean the DOM data, and use Large Language Models (LLMs) to parse specific information into structured formats like Excel or PowerPoint.

## 🚀 Features

* **GUI Interface:** Easy-to-use web interface built with Streamlit.
* **Dynamic Scraping:** Uses Selenium (Edge Driver) to handle JavaScript-heavy websites.
* **Smart Cleaning:** Automatically removes scripts, styles, and clutter from HTML using BeautifulSoup.
* **AI Parsing:** Leverages local LLMs (via Ollama) to extract specific data based on natural language prompts.
* **Export Options:** Download results directly to **Excel** (`.xlsx`) or **PowerPoint** (`.pptx`).

## 🛠️ Prerequisites

Before running the application, ensure you have the following installed:

1.  **Python 3.9+**
2.  **Microsoft Edge Browser** (installed on your system).
3.  **Ollama**: This project uses local LLMs to parse data.
    * Download from [ollama.com](https://ollama.com).
    * Pull a model (e.g., Llama 3): `ollama pull llama3`.

## Dependencies
pip install streamlit selenium beautifulsoup4 pandas python-pptx openpyxl

## 🛠️ Run
streamlit run main.py
