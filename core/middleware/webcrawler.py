from core.tasks import *
from django.utils.deprecation import MiddlewareMixin

class WebCrawlerMiddleware(MiddlewareMixin):

    def process_request(self, request):
        print("starting crawl")
        try:
            Crawl()
            print("crawl terminate")
            return None
        except :
            print("crawl error")
            return None