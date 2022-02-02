from html.parser import HTMLParser
from urllib.request import urlopen


from .models import News


class NewsFinder(HTMLParser):
    def __init__(self):
        super().__init__()
        self.infos_link = False
        self.Data = []
        self.Keys = []
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for (attribute, value) in attrs:
                if attribute == 'href':
                    if value.startswith('/news/technology') and len(value.split('-')) == 2 :
                        try:
                            key = int(value.split('-')[1])
                            if key not in self.Keys:
                                self.infos_link = True
                                self.Keys.append(key)
                        except :
                            pass

    def handle_data(self, data):
        if self.infos_link :
            if data:
                self.infos_link = False
                self.Data.append(data)



    def error(self, message):
        pass

    def crawl(self):
        heml_string=''
        response = urlopen('https://www.bbc.com/news/technology')
        html_string = response.read().decode()
        self.feed(html_string)
        return self.Data


def Crawl():
    news = NewsFinder()
    datas = news.crawl()
    for data in datas:
        try:
            News.objects.get(title=data)
            print(data)
        except:
            new = News.objects.create(title=data)
            new.save()
            print(f"nouveau {data}")
