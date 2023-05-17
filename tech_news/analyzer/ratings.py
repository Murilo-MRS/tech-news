from collections import Counter
from tech_news.database import search_news


# Requisito 10
def top_5_categories():
    category_count = Counter(
        [new["category"] for new in search_news({})]
    ).most_common(5)

    category_count.sort(key=lambda x: (-x[1], x[0]))

    return [category[0] for category in category_count]
