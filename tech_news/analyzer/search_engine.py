from datetime import datetime
from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    """case insentive https://sparkbyexamples.com/
    mongodb/mongodb-query-case-insensitive/"""
    news_list = search_news({"title": {"$regex": title, "$options": "i"}})
    formated_list = [(new["title"], new["url"]) for new in news_list]
    return formated_list


# Requisito 8
def search_by_date(date):
    """https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
    - /datetime.html#datetime.date.fromisoformat"""
    try:
        datetime.fromisoformat(date)
    except ValueError:
        raise ValueError("Data inválida")
    else:
        date_to_format = datetime.strptime(date, "%Y-%m-%d")
        date_to_search = date_to_format.strftime("%d/%m/%Y")
        news_list = search_news({"timestamp": date_to_search})
        formated_list = [(new["title"], new["url"]) for new in news_list]
        return formated_list


# Requisito 9
def search_by_category(category):
    news_by_category = search_news(
        {"categories": {"$regex": category, "$options": "i"}}
    )
    formated_list = [(new["title"], new["url"]) for new in news_by_category]
    return formated_list
