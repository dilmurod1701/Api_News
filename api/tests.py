from django.test import TestCase
from rest_framework.test import APIClient
from selenium import webdriver

from .models import NewsData

# Create your tests here.


class TestModels(TestCase):
    def setUp(self) -> None:
        NewsData.objects.create(title='nam gap tincmi', content='shu bittasi kochada yurib pichoqlab ketibdi', link='https://kun.uz.com')
        NewsData.objects.create(title='shok ana xolos', content='gaz ochip qoldi', link='https://ozbekiston.com')
        NewsData.objects.create(title='ana xolos', content='falonchieva folanchi olib qopti', link='https://daryo.uz.com')
        NewsData.objects.create(title='serikboy bankni omaripti', content='bank qorovullari va xodimlari uxlab yotganda serikboy vaziyatdan foydalanib pul ogirlapti', link='https://mantiq-left-uzb.uz.com')
        NewsData.objects.create(title='tez buni oqing', content='Endi Ozbekistonda svet suv gaz ochmaskan deyishimni kutkanmdiz', link='https://UZB.com')
        NewsData.objects.create(title='buni oqishingiz shart', content='Olikboev Olik Google ga Software Engineering bolib kiripti', link='https://bbc.com')

    def test_title(self):
        obj1 = NewsData.objects.get(title='nam gap tincmi')
        obj2 = NewsData.objects.get(title='shok ana xolos')
        obj3 = NewsData.objects.get(title='ana xolos')
        obj4 = NewsData.objects.get(title='serikboy bankni omaripti')
        obj5 = NewsData.objects.get(title='tez buni oqing')
        obj6 = NewsData.objects.get(title='buni oqishingiz shart')
        self.assertEquals(obj1.title, 'nam gap tincmi')
        self.assertEquals(obj2.title, 'shok ana xolos')
        self.assertEquals(obj3.title, 'ana xolos')
        self.assertEquals(obj4.title, 'serikboy bankni omaripti')
        self.assertEquals(obj5.title, 'tez buni oqing')
        self.assertEquals(obj6.title, 'buni oqishingiz shart')

    def test_content(self):
        obj1 = NewsData.objects.get(content='shu bittasi kochada yurib pichoqlab ketibdi')
        obj2 = NewsData.objects.get(content='gaz ochip qoldi')
        obj3 = NewsData.objects.get(content='falonchieva folanchi olib qopti')
        obj4 = NewsData.objects.get(content='bank qorovullari va xodimlari uxlab yotganda serikboy vaziyatdan foydalanib pul ogirlapti')
        obj5 = NewsData.objects.get(content='Endi Ozbekistonda svet suv gaz ochmaskan deyishimni kutkanmdiz')
        obj6 = NewsData.objects.get(content='Olikboev Olik Google ga Software Engineering bolib kiripti')
        self.assertEquals(obj1.content, 'shu bittasi kochada yurib pichoqlab ketibdi')
        self.assertEquals(obj2.content, 'gaz ochip qoldi')
        self.assertEquals(obj3.content, 'falonchieva folanchi olib qopti')
        self.assertEquals(obj4.content, 'bank qorovullari va xodimlari uxlab yotganda serikboy vaziyatdan foydalanib pul ogirlapti')
        self.assertEquals(obj5.content, 'Endi Ozbekistonda svet suv gaz ochmaskan deyishimni kutkanmdiz')
        self.assertEquals(obj6.content, 'Olikboev Olik Google ga Software Engineering bolib kiripti')

    def test_link(self):
        obj1 = NewsData.objects.get(link='https://kun.uz.com')
        obj2 = NewsData.objects.get(link='https://ozbekiston.com')
        obj3 = NewsData.objects.get(link='https://daryo.uz.com')
        obj4 = NewsData.objects.get(link='https://mantiq-left-uzb.uz.com')
        obj5 = NewsData.objects.get(link='https://UZB.com')
        obj6 = NewsData.objects.get(link='https://bbc.com')
        self.assertEquals(obj1.link, 'https://kun.uz.com')
        self.assertEquals(obj2.link, 'https://ozbekiston.com')
        self.assertEquals(obj3.link, 'https://daryo.uz.com')
        self.assertEquals(obj4.link, 'https://mantiq-left-uzb.uz.com')
        self.assertEquals(obj5.link, 'https://UZB.com')
        self.assertEquals(obj6.link, 'https://bbc.com')


class TestView(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        NewsData.objects.create(title='nam gap tincmi', content='shu bittasi kochada yurib pichoqlab ketibdi', link='https://kun.uz.com')
        NewsData.objects.create(title='shok ana xolos', content='gaz ochip qoldi', link='https://ozbekiston.com')
        NewsData.objects.create(title='ana xolos', content='falonchieva folanchi olib qopti', link='https://daryo.uz.com')
        NewsData.objects.create(title='serikboy bankni omaripti', content='bank qorovullari va xodimlari uxlab yotganda serikboy vaziyatdan foydalanib pul ogirlapti', link='https://mantiq-left-uzb.uz.com')
        NewsData.objects.create(title='tez buni oqing', content='Endi Ozbekistonda svet suv gaz ochmaskan deyishimni kutkanmdiz', link='https://UZB.com')
        NewsData.objects.create(title='buni oqishingiz shart', content='Olikboev Olik Google ga Software Engineering bolib kiripti', link='https://bbc.com')

    def test_view(self):
        response = self.client.get('http://127.0.0.1:8000/api/news')
        self.assertNotEquals(response.json()[0]['title'], response.json()[1]['title'])
        self.assertNotEquals(response.json()[0]['content'], response.json()[1]['content'])
        self.assertNotEquals(response.json()[0]['link'], response.json()[1]['link'])
        self.assertNotEquals(response.json()[1]['title'], response.json()[2]['content'])
        self.assertNotEquals(response.json()[6]['content'], response.json()[9]['content'])
        self.assertNotEquals(response.json()[10]['link'], response.json()[10]['title'])
        self.assertNotEquals(response.json()[4]['title'], response.json()[10]['title'])


class NewsSelenium(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        NewsData.objects.create(title='nam gap tincmi', content='shu bittasi kochada yurib pichoqlab ketibdi', link='https://kun.uz.com')
        NewsData.objects.create(title='shok ana xolos', content='gaz ochip qoldi', link='https://ozbekiston.com')
        NewsData.objects.create(title='ana xolos', content='falonchieva folanchi olib qopti', link='https://daryo.uz.com')
        NewsData.objects.create(title='serikboy bankni omaripti', content='bank qorovullari va xodimlari uxlab yotganda serikboy vaziyatdan foydalanib pul ogirlapti', link='https://mantiq-left-uzb.uz.com')
        NewsData.objects.create(title='tez buni oqing', content='Endi Ozbekistonda svet suv gaz ochmaskan deyishimni kutkanmdiz', link='https://UZB.com')
        NewsData.objects.create(title='buni oqishingiz shart', content='Olikboev Olik Google ga Software Engineering bolib kiripti', link='https://bbc.com')

    def test_news_page(self):
        self.client = APIClient()
        response = webdriver.Chrome()
        response.get('http://127.0.0.1:8000/api/news')
        assert 'title' in response.page_source
        assert 'content' in response.page_source
        assert 'link' in response.page_source
