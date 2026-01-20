import selenium.webdriver as webdriver
from selenium.webdriver.edge.service import Service
import time
import os
from pathlib import Path
from bs4 import BeautifulSoup

def scrape_website(website):
    print("Launching edge browser...")

    # Using Path to handle Windows paths correctly
    edge_driver_path = str(Path("edgedriver_win64/msedgedriver.exe").absolute())
    
    # Verifying the driver exists
    if not os.path.exists(edge_driver_path):
        raise FileNotFoundError(f"Edge driver not found at: {edge_driver_path}")
    
    options = webdriver.EdgeOptions()
    driver = webdriver.Edge(service=Service(edge_driver_path), options=options)

    try:
        driver.get(website)
        print("Page loaded")
        html = driver.page_source
        time.sleep(10)

        return html
    finally:
        driver.quit()

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )    

    return cleaned_content

def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i : i+max_length] for i in range(0, len(dom_content), max_length)
    ]
