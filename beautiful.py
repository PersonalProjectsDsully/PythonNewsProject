import requests
from bs4 import *
import sqlite3


def TextNews():
    source = requests.get('https://www.zdnet.com/news/rss.xml').text
    source1 = requests.get('https://www.zdnet.com/news/rss.xml')
    soup = BeautifulSoup(source, 'lxml')
    soup1s = BeautifulSoup(source1.content, features='xml')
    articles = soup.findAll('item')
    source1s = soup1s.findAll('item')
    i = 0
    for article in articles:
        link = source1s[i].link.text
        headline = article.title.text
        description = article.find('description').text
        date = article.find('pubdate').text
        i = i + 1
        insertintodatabase(link, description, headline, date)


def telegram_bot_sendtext(bot_message):
    bot_token = ''
    bot_chatID = ''
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()
    #https://gist.github.com/manhay212/987c32b634927a4388ad7aba6b7bcbbf
    #Personal information removed from this function


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
    #     #print("duplicate Row not inserted")
    conn.close()

