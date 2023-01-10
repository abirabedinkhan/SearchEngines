from importlib.resources import contents
from bs4 import BeautifulSoup
import requests

class GoogleWeb():
    def __init__(self, query:str, number_of_results:int=10, page:int=1, country_code:str="us", **kwargs) -> None:
        """
            param query: The query to be searched
            param number_of_results: The number of results to be returned
            param page: The page number to be searched
            param country_code: The country code to be searched
        """
        self.query:str = query
        self.number_of_results:str = number_of_results
        self.page:int = (page * 10) - 10
        self.country_code:str = country_code
        self.url:str = f"https://12ft.io/api/proxy?ref=&q=https://www.google.com/search?q={self.query}&num={self.number_of_results}&start={self.page}&gl={self.country_code}&safe=active"
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
        """
            Returns a list of web results
        """
        data = []
        results = self.soup.find_all("div", {"class": "Gx5Zad fP1Qef xpd EtOod pkphOe"})
        for result in results:
            try:
                title = getattr(result.find("div", {"class": "BNeawe vvjwJb AP7Wnd"}), "text", None)
                snippet = getattr(result.find("div", {"class": "BNeawe s3v9rd AP7Wnd"}), "text", None)
                url_preview = getattr(result.find("div", {"class": "BNeawe UPmit AP7Wnd"}), "text", None)
                link = result.find("a")['href'].replace("/url?q=", "")
                link = requests.utils.unquote(link[:link.rfind("&sa=U")])

                data.append({
                    "title": title,
                    "snippet": snippet,
                    "url": link,
                    "url_preview": url_preview,
                    "q": self.query
                })
            except Exception as e:
                pass
        return data

    def spell_check(self) -> str:
        """
            Returns a list of suggestions
        """
        try:
            data = self.soup.select(".MUxGbd.v0nnCb.lyLwlc > a > span")
            spelled = getattr(data[0], "text", None)
        except Exception as e:
            spelled = ''
        return spelled

    def get_suggestions(self) -> list:
        """
            Returns a list of suggestions
        """
        data = []
        results = self.soup.find_all("div", {"class": "kjGX2"})
        for result in results:
            try:
                data.append(getattr(result, "text", None))
            except Exception as e:
                pass
        return data

    def input_suggestion(self):
        address = f"https://google.com/complete/search?output=toolbar&hl=es&q={self.query}"
        get_request = requests.get(address, headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'})
        contents = get_request.content.decode('utf-8')
        soup = BeautifulSoup(contents, 'lxml')

        data = []

        results = soup.findAll('completesuggestion')
        for result in results:
            s_data = result.find("suggestion")['data']

            data.append(s_data)

        for row in data:
            if row == None:
                data.remove(row)

        return data

    def data(self) -> dict:
        """
            Returns googles search result
        """
        return {
            "query": self.query,
            "page": (self.page // 10) + 1,
            "country_code": self.country_code,
            "showing_capability": self.number_of_results,
            "showing_results": len(self.get_web_results()),
            "spell_check": self.spell_check(),
            "results": self.get_web_results(),
            "suggestions": self.get_suggestions()
        }
