import requests
from bs4 import BeautifulSoup

def fetch_web_content(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}  
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        paragraphs = soup.find_all("p")[:5]
        content = "\n".join([p.get_text(strip=True) for p in paragraphs])

        return content if content else "No relevant content found."
    
    except requests.RequestException as e:
        print(f"Error fetching content: {e}")
        return None
