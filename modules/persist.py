from tinydb import TinyDB, Query
from utils import get_db_table

def persist_new_articles(articles):
    table = get_db_table()
    for article in articles:
        if table.contains(Query().title == str(article['title'])) == False:
            table.insert({
                'title': article['title'],
                'description': article['description'],
                'link': article['link'],
                'sent': False
            })
            print('New article added: ' + article['title'])
        else:
            print('Article already exists: ' + article['title'])
