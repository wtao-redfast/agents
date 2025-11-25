from bs4 import BeautifulSoup
import requests
from markdownify import markdownify as md
from urllib.parse import urlparse
import os

def html2Markdown(url, path):
    try:
        if not os.path.exists(path):
            response = requests.get(url)
            markdown = md(response.text)
            with open(path, "w") as f:
                f.write(markdown)
        print(f"Converted: {url} to markdown at {path}")
    except Exception as e:
        print(f"@@@@@Error: converting {url} to markdown: {e}")

def getRecurlyEngageDocs():
    response = requests.get('https://docs.recurly.com/recurly-engage/docs/overview-recurly-engage')
    soup = BeautifulSoup(response.text, "html.parser")

    subDocs = soup.find_all("li", class_="Sidebar-item23D-2Kd61_k3")
    for subDoc in subDocs:
        children = subDoc.find_all("a")
        for child in children:
            href = child.attrs["href"]
            path = f'output/{os.path.basename(href)}.md'
            html2Markdown("https://docs.recurly.com" + href, path)
