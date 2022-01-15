import requests
from bs4 import *
import sqlite3

from requests import Response


def TextNews():
    links = ['https://www.theregister.com/security/headlines.rss', 'https://www.zdnet.com/news/rss.xml',
             'https://www.darkreading.com/rss.xml', 'https://www.eff.org/rss/updates.xml',
             'https://torrentfreak.com/feed/', 'https://nakedsecurity.sophos.com/feed', 'http://feeds.feedburner.com/TheHackersNews?format=xml']

    for link in links:
        print(link)
        source1: Response = requests.get(link)
        soup1s = BeautifulSoup(source1.content, features='xml')
        articles = soup1s.findAll('item')
        i = 0
        for article in articles:
            link1 = article.link.text
            headline = article.title.text
            description = article.description.text
            date = article.pubDate.text
            date = (str(date))
            link1 = (str(link1))
            headline = (str(headline))
            description = (str(description))
            print(headline)
            i = i + 1
            insertintodatabase(link1, description, headline, date)



def telegram_bot_sendtext(bot_message):
    bot_token = ''
    bot_chatID = ''
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()


def insertintodatabase(link, description, headline, date):
    conn = sqlite3.connect('news.db')
    c = conn.cursor()
    parameters = (headline, description, date, link)
    c.execute("INSERT OR IGNORE INTO news VALUES(?,?,?,?)", parameters)
    conn.commit()
    if c.rowcount == 1:
        telegram_bot_sendtext(headline + description + date + link)
        print(c.rowcount, headline, "was inserted.")
    # else:
    #     print("duplicate Row not inserted")
    #     conn.close()
    #     return
    c.execute("SELECT * FROM news")
    conn.close()


while 1 == 1:
    TextNews()
