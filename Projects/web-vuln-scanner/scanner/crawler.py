import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def crawl(base_url, session, max_pages=20):
    visited = set()
    forms = []
    queue = [base_url]

    while queue and len(visited) < max_pages:
        url = queue.pop(0)
        visited.add(url)

        r = session.get(url, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")

        for a in soup.find_all("a", href=True):
            link = urljoin(url, a["href"])
            if link not in visited:
                queue.append(link)

        for form in soup.find_all("form"):
            forms.append((url, form))

    return visited, forms