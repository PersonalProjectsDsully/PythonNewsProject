import sqlite3
import beautiful


def main():
    x=1
    if x == 0:
        conn = sqlite3.connect('news.db')
        c = conn.cursor()
        c.execute("""CREATE TABLE news(
                           title text,
                           description text,
                           date text,
                           link TEXT NOT NULL UNIQUE   
            )""")
        c.close()
    beautiful.TextNews()
    conn = sqlite3.connect('news.db')
    c = conn.cursor()
    sqliteselect = "SELECT * from news"
    c.execute(sqliteselect)


main()

