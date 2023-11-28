from rest_framework import generics
import requests
from bs4 import BeautifulSoup

from .models import NewsData
from .serializers import NewsSerializer
# Create your views here.


class News(generics.ListAPIView):
    """
    it will show all top news in the world
    """
    queryset = NewsData.objects.all()
    serializer_class = NewsSerializer

    def get_queryset(self):
        url = 'https://www.bbc.com/news'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        data = []
        for each in soup.find_all('div', class_='gs-c-promo'):
            title = each.get_text(strip=True)
            link = each.find('a')['href']
            content = each.find('p', class_='gs-c-promo-summary')
            if content:
                content = content.get_text(strip=True)

            model = NewsData(title=title, content=content, link=link)
            model.save()
            data.append(model)

        second_site = 'https://news.yahoo.com/'
        second_response = requests.get(second_site)
        sup = BeautifulSoup(second_response.content, 'html.parser')

        for yahoo in sup.find_all('li', class_='js-stream-content'):
            title = yahoo.find('h3').get_text(strip=True)
            link = yahoo.find('a')['href']
            content = yahoo.find('p')
            if content:
                content = content.get_text(strip=True)

            model = NewsData(title=title, content=content, link=link)
            model.save()
            data.append(model)

        return data
