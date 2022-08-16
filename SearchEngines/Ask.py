from bs4 import BeautifulSoup
import requests

class AskWeb():
    def __init__(self, query:str, **kwargs) -> None:
        self.query = query
        self.kwargs = kwargs
        self.url = f"https://www.ask.com/web?q={self.query}"
        headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
            "x-requested-with": "XMLHttpRequest"
        }
        self.r = requests.get(self.url, headers = headers, params=kwargs)
        self.page_content:str = str(self.r.content, 'utf-8', errors='replace')
        self.soup = BeautifulSoup(self.page_content, "lxml")

    def get_web_results(self) -> list:
        data = []
        results = self.soup.find_all("div", {"class": "PartialSearchResults-item"})
        for result in results:
            try:
                title = getattr(result.find("a", {"class": "PartialSearchResults-item-title-link result-link"}), "text", None)
                snippet = getattr(result.find("div", {"class": "PartialSearchResults-item-details"}), "text", None)
                link = result.find("a")['href']

                data.append({
                    "title": title,
                    "snippet": snippet,
                    "url": link,
                    "q": self.query
                })
            except Exception as e:
                pass
        return data