# from datetime import datetime
from tech_news.database import search_news


# def format_list(news):
#     return [(new["title"], new["url"]) for new in news]


# Requisito 7
def search_by_title(title):
    """case insentive https://sparkbyexamples.com/
    mongodb/mongodb-query-case-insensitive/"""
    news_list = search_news({"title": {"$regex": title, "$options": "i"}})
    formated_list = [(new["title"], new["url"]) for new in news_list]
    return formated_list


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
