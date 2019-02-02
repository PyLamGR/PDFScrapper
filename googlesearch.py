from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.parse import urlparse, parse_qs


class GoogleSearch:

    def __init__(self):
        self.url = ""
        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)'
        self.html = ""
        self.links = list()
        self.pdfs = list()

    def query(self, search):
        search = search.replace(' ', '+')
        self.url = "https://www.google.com/search?q=" + search + "&num=100"  # maybe change 100 to 50-80?
        return self.url

    def get_page(self):
        r = Request(self.url)
        r.add_header('User-Agent', self.user_agent)
        response = urlopen(r)
        self.html = response.read()
        response.close()

    def get_results(self):
        hashes = set()
        self.get_page()

        soup = BeautifulSoup(self.html, 'html.parser')

        for anchor in soup.find(id='search').find_all('a'):
            if not anchor.parent or anchor.parent.name.lower() != "h3":
                continue

            try:
                link = anchor['href']
            except KeyError:
                continue

            link = self.filter_result(link)
            if not link:
                continue

            h = hash(link)
            if h in hashes:
                continue
            hashes.add(h)

            self.links.append(link)

    def get_pdfs(self):
        for link in self.links:
            if link.endswith(".pdf"):
                self.pdfs.append(link)

        return self.pdfs

    @staticmethod
    def filter_result(link):
        parse = urlparse(link, 'http')

        if link.startswith('/url'):
            link = parse_qs(parse.query)['q'][0]

            parse = urlparse(link, 'http')
            if parse.netloc and 'google' not in parse.netloc:
                return link
