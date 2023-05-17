import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1 - Crie a função fetch
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )
        if response.status_code == 200:
            return response.text
        return None
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)
    return selector.css("h2.entry-title a::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    try:
        return selector.css("a.next.page-numbers::attr(href)").get()
    except AttributeError:
        return None


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)
    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css("h1.entry-title::text").get()
    timestamp = selector.css("ul.post-meta li.meta-date::text").get()
    writer = selector.css("ul.post-meta li.meta-author a::text").get()
    reading_time = selector.css(
        "ul.post-meta li.meta-reading-time::text"
    ).get()
    summary = selector.css(
        ".entry-content > p:nth-of-type(1) *::text"
    ).getall()
    category = selector.css(
        ".meta-category .category-style .label::text"
    ).get()

    return {
        "url": url,
        "title": title.strip(),
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": int(reading_time.split(" ")[0]),
        "summary": "".join(summary).strip(),
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    url = "https://blog.betrybe.com/"
    link_list = []
    news_list = []

    while len(link_list) < amount:
        html = fetch(url)
        links = scrape_updates(html)
        link_list.extend(links)
        url_next_page = scrape_next_page_link(html)
        url = url_next_page
# list[:amount] funciona como um slice, pegando apenas a quantidade de links
    for link in link_list[:amount]:
        html = fetch(link)
        news = scrape_news(html)
        news_list.append(news)

    create_news(news_list)
    return news_list
