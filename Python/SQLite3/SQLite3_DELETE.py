import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
from dateutil import parser
from matplotlib import style

style.use("ggplot")

conn = sqlite3.connect("tutorial.db")
c = conn.cursor()


def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix Real, datestamp TEXT, keyword TEXT, value REAL)")


def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(145413513451, '11/11/2016', 'Python', 5)")
    conn.commit()
    c.close()
    conn.close()


def dynamic_data_entry():
    unix = time.time()
    date = datetime.datetime.fromtimestamp(unix).strftime("%Y-%m-%d %H:%M:%S")
    keyword = "Python"
    value = random.randrange(0, 10)
    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
              (unix, date, keyword, value))
    conn.commit()


def read_from_db():
    c.execute("SELECT * FROM stuffToPlot WHERE value=3")
    for row in c.fetchall():
        print(row)


def graph_data():
    c.execute("SELECT datestamp, value FROM stuffToPlot")
    dates = []
    values = []

    for row in c.fetchall():
        dates.append(parser.parse(row[0]))
        values.append(row[1])

    plt.plot_date(dates, values, "-")
    plt.show()

def delete_and_update():
    c.execute("SELECT * FROM stuffToPlot")
    [print(row) for row in c.fetchall()]

    c.execute("UPDATE stuffToPlot SET value=99 WHERE value=3")
    conn.commit()

    c.execute("SELECT * FROM stuffToPlot")
    [print(row) for row in c.fetchall()]

    c.execute("DELETE FROM stuffToPlot WHERE value=99")
    conn.commit()

    c.execute("SELECT * FROM stuffToPlot")
    [print(row) for row in c.fetchall()]



delete_and_update()
c.close()
conn.close()
