import tkinter as tk
import urllib
import json
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.animation as animation
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc
from matplotlib import style
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg

# Styles
matplotlib.use('TkAgg')
style.use('ggplot')

# Font sizes
LARGE_FONT = ("Candara", 12)
NORM_FONT = ("Candara", 10)
SMALL_FONT = ("Candara", 8)

# Graph
f = plt.figure()
a = f.add_subplot(111)

# Defaults
exchange = "BTC-e"
data_counter = 9000
program_name = "btce"
resample_size = "15Min"
data_pace = "1d"
pane_count = 1
candle_width = 0.008
top_indicator = "none"
bottom_indicator = "none"
middle_indicator = "none"
dark_colour = "#183A54"
light_colour = "#00A3E0"
chart_load = True
EMAs, SMAs = [], []


# Method: Used to show how a tutorial could be implemented for an application
def tutorial():
    def leave_mini(tutor):
        tutor.destroy()

    def page2():
        leave_mini(tut)
        tut2 = tk.Tk()

        def leave_mini2(tutor):
            tutor.destroy()

        def page3():
            leave_mini2(tut2)
            tut3 = tk.Tk()
            tut3.wm_title("PART 3!")

            label3 = tk.Label(tut3, text="Part 3", font=NORM_FONT)
            label3.pack(side="top", fill="x", pady=10)
            button3 = tk.Button(tut3, text="Done!", command=tut3.destroy)
            button3.pack()
            tut3.mainloop()

        tut2.wm_title("PART 2!")
        label2 = tk.Label(tut2, text="Part 2", font=NORM_FONT)
        label2.pack(side="top", fill="x", pady=10)
        button2 = tk.Button(tut2, text="Next!", command=page3)
        button2.pack()

        tut.mainloop()

    tut = tk.Tk()
    tut.wm_title("Tutorial")
    label1 = tk.Label(tut, text="What do you need help with?", font=NORM_FONT)
    label1.pack(side="top", fill="x", pady=10)
    button1_1 = tk.Button(tut, text="Overview of the application", command=page2)
    button1_1.pack()
    button2_1 = tk.Button(tut, text="How do I trade here?",
                          command=lambda: pop_up_message('Not supported just yet!'))
    button2_1.pack()
    button3_1 = tk.Button(tut, text="Indicator questions/help",
                          command=lambda: pop_up_message('Not supported just yet!'))
    button3_1.pack()

    tut.mainloop()


# Method: Used to choose to load the chart or not
def load_chart(run):
    global chart_load

    if run == "start":
        chart_load = True
    elif run == "stop":
        chart_load = False


# Method: Used to add a top indicator
def add_top_indicator(value):
    global top_indicator
    global data_counter

    if data_pace == "tick":
        pop_up_message("Indicators in Tick Data not available, choose 1 minute tf if you want short term.")

    if value == "none":
        top_indicator = value
        data_counter = 9000
    elif value == "rsi":
        rsiq = tk.Tk()
        rsiq.wm_title("Periods?")
        label = tk.Label(rsiq, text="Choose how many periods you want each RSI calculation to consider.\n"
                                    "These periods are contingent on your current time settings on the chart. "
                                    "1 period = 1 ohlc candlestick.", font=NORM_FONT)
        label.pack(side="top", fill="x", pady=10)

        entry = tk.Entry(rsiq)
        entry.insert(0, 14)
        entry.pack()
        entry.focus_set()

        def callback():
            global top_indicator
            global data_counter
            periods = (entry.get())
            group = ["rsi", periods]
            top_indicator = group
            data_counter = 9000
            rsiq.destroy()

        b = tk.Button(rsiq, text="Submit", width=10, command=callback)
        b.pack()

        tk.mainloop()
    elif value == "macd":
        global top_indicator
        global data_counter
        top_indicator = "macd"
        data_counter = 9000


# Method: Used to a middle indicator
def add_middle_indicator(value):
    global middle_indicator
    global data_counter
    if data_pace == "tick":
        pop_up_message("Indicators in Tick Data not available, choose 1 minute tf if you want short term.")

    if value != "none":
        if middle_indicator == "none":
            if value == "sma":
                midiq = tk.Tk()
                midiq.wm_title("Periods?")
                label = tk.Label(midiq, text="Choose how many periods you want each SMA calculation to consider.\n"
                                             "These periods are contingent on your current time settings.\n"
                                             "1 period = 1 ohlc candlestick.", font=NORM_FONT)
                label.pack(side="top", fill="x", pady=10)
                entry = tk.Entry(midiq)
                entry.insert(0, 10)
                entry.pack()
                entry.focus_set()

                def callback():
                    global middle_indicator
                    global data_counter
                    middle_indicator = []
                    periods = (entry.get())
                    group = ["sma", int(periods)]
                    middle_indicator.append(group)
                    data_counter = 9000
                    midiq.destroy()

                b = tk.Button(midiq, text="Submit", width=10, command=callback)
                b.pack()
                tk.mainloop()
            elif value == "ema":
                midiq = tk.Tk()
                midiq.wm_title("Periods?")
                label = tk.Label(midiq, text="Choose how many periods you want each EMA calculation to consider.\n"
                                             "These periods are contingent on your current time settings.\n"
                                             "1 period = 1 ohlc candlestick.", font=NORM_FONT)
                label.pack(side="top", fill="x", pady=10)
                entry = tk.Entry(midiq)
                entry.insert(0, 10)
                entry.pack()
                entry.focus_set()

                def callback():
                    global middle_indicator
                    global data_counter
                    middle_indicator = []
                    periods = (entry.get())
                    group = ["ema", int(periods)]
                    middle_indicator.append(group)
                    data_counter = 9000
                    midiq.destroy()

                b = tk.Button(midiq, text="Submit", width=10, command=callback)
                b.pack()
                tk.mainloop()
        else:
            if value == "sma":
                midiq = tk.Tk()
                midiq.wm_title("Periods?")
                label = tk.Label(midiq, text="Choose how many periods you want each SMA calculation to consider.\n"
                                             "These periods are contingent on your current time settings.\n"
                                             "1 period = 1 ohlc candlestick.", font=NORM_FONT)
                label.pack(side="top", fill="x", pady=10)
                entry = tk.Entry(midiq)
                entry.insert(0, 10)
                entry.pack()
                entry.focus_set()

                def callback():
                    global middle_indicator
                    global data_counter
                    periods = (entry.get())
                    group = ["sma", int(periods)]
                    middle_indicator.append(group)
                    data_counter = 9000
                    midiq.destroy()

                b = tk.Button(midiq, text="Submit", width=10, command=callback)
                b.pack()
                tk.mainloop()

            if value == "ema":
                midiq = tk.Tk()
                midiq.wm_title("Periods?")
                label = tk.Label(midiq, text="Choose how many periods you want each EMA calculation to consider.\n"
                                             "These periods are contingent on your current time settings.\n"
                                             "1 period = 1 ohlc candlestick.", font=NORM_FONT)
                label.pack(side="top", fill="x", pady=10)
                entry = tk.Entry(midiq)
                entry.insert(0, 10)
                entry.pack()
                entry.focus_set()

                def callback():
                    global middle_indicator
                    global data_counter
                    periods = (entry.get())
                    group = ["ema", int(periods)]
                    middle_indicator.append(group)
                    data_counter = 9000
                    midiq.destroy()

                b = tk.Button(midiq, text="Submit", width=10, command=callback)
                b.pack()
                tk.mainloop()
    else:
        middle_indicator = "none"


# Method: Used to a bottom indicator
def add_bottom_indicator(value):
    global bottom_indicator
    global data_counter

    if data_pace == "tick":
        pop_up_message("Indicators in Tick Data not available, choose 1 minute tf if you want short term.")

    if value == "none":
        bottom_indicator = value
        data_counter = 9000

    elif value == "rsi":
        rsiq = tk.Tk()
        rsiq.wm_title("Periods?")
        label = tk.Label(rsiq, text="Choose how many periods you want each RSI calculation to consider.\n"
                                    "These periods are contingent on your current time settings."
                                    "1 period = 1 ohlc candlestick.", font=NORM_FONT)
        label.pack(side="top", fill="x", pady=10)

        entry = tk.Entry(rsiq)
        entry.insert(0, 14)
        entry.pack()
        entry.focus_set()

        def callback():
            global bottom_indicator
            global data_counter
            periods = (entry.get())
            group = ["rsi", periods]
            bottom_indicator = group
            data_counter = 9000
            rsiq.destroy()

        b = tk.Button(rsiq, text="Submit", width=10, command=callback)
        b.pack()

        tk.mainloop()
    elif value == "macd":
        global bottom_indicator
        global data_counter
        bottom_indicator = "macd"
        data_counter = 9000


# Method: Used to change the time frame
def change_time_frame(time_frame):
    global data_pace
    global data_counter
    if time_frame == '7d' and resample_size == '1Min':
        pop_up_message("Too much data chosen, choose a smaller data time frame or higher ohlc Interval!")
    else:
        data_pace = tf
        data_counter = 9000


# Method: Used to change the sample size
def change_sample_size(size, width):
    global resample_size
    global data_counter
    global candle_width

    if data_pace == '7d' and size == '1Min':
        pop_up_message("Too much data chosen, choose a smaller Data Time Frame or higher ohlc Interval!")

    if data_pace == 'tick':
        pop_up_message("You are currently viewing tick data, not ohlc. Choose a larger Data Time Frame!")
    else:
        resample_size = size
        data_counter = 9000
        candle_width = width


# Method: Used to create a pop-up window with a message
def pop_up_message(message):
    popup = tk.Tk()

    def leave_mini():
        popup.destroy()

    popup.wm_title("!")

    label = tk.Label(popup, text=message, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    button = tk.Button(popup, text="Okay", command=leave_mini)
    button.pack()

    popup.mainloop()


# Method: Used to change the exchange
def change_exchange(new_exchange, new_program):
    global exchange
    global data_counter
    global program_name
    exchange = new_exchange
    program_name = new_program
    data_counter = 9000


# Method: Used to create live graphs for the application
def animate(i):
    global data_counter

    # Method: Used to compute the moving average convergence/divergence
    def compute_macd(x, speed=12, location="bottom"):
        values = {'key': 1, 'prices': x}

        url = "http://seaofbtc.com/api/indicator/macd"
        data = urllib.parse.urlencode(values)
        data = data.encode('utf-8')
        req = urllib.request.Request(url, data)
        resp = urllib.request.urlopen(req)
        resp_data = resp.read()
        new_data = str(resp_data).replace("b", "").replace('[', '').replace(']', '').replace("'", '')

        split = new_data.split('::')

        macd = split[0]
        ema9 = split[1]
        hist = split[2]

        macd = macd.split(", ")
        ema9 = ema9.split(", ")
        hist = hist.split(", ")

        try:
            macd = [float(j) for j in macd]
        except Exception as ex:
            print(str(ex) + "  macd")
        try:
            ema9 = [float(j) for j in ema9]
        except Exception as ex:
            print(str(ex) + "  ema9")
        try:
            hist = [float(j) for j in hist]
        except Exception as ex:
            print(str(ex) + "  hist")

        if location == "top":
            try:
                a0.plot(ohlc['MPLDates'][speed:], macd[speed:], color=dark_colour, lw=2)
                a0.plot(ohlc['MPLDates'][speed:], ema9[speed:], color=light_colour, lw=1)
                a0.fill_between(ohlc['MPLDates'][speed:], hist[speed:], 0, alpha=0.5, facecolor=dark_colour,
                                edgecolor=dark_colour)
                data_label = "MACD"
                a0.set_ylabel(data_label)
            except Exception as ex:
                print(str(ex))
        elif location == "bottom":
            try:
                a3.plot(ohlc['MPLDates'][speed:], macd[speed:], color=dark_colour, lw=2)
                a3.plot(ohlc['MPLDates'][speed:], ema9[speed:], color=light_colour, lw=1)
                a3.fill_between(ohlc['MPLDates'][speed:], hist[speed:], 0, alpha=0.5, facecolor=dark_colour,
                                edgecolor=dark_colour)
                data_label = "MACD"
                a3.set_ylabel(data_label)
            except Exception as ex:
                print(str(ex))

    # Method: Used to update rsi data
    def rsi_indicator(price_data, location="top"):
        values = {}
        if location == "top":
            values = {'key': 1, 'prices': price_data, 'periods': top_indicator[1]}

        elif location == "bottom":
            values = {'key': 1, 'prices': price_data, 'periods': bottom_indicator[1]}

        url = "http://seaofbtc.com/api/indicator/rsi"
        data = urllib.parse.urlencode(values)
        data = data.encode('utf-8')
        req = urllib.request.Request(url, data)
        resp = urllib.request.urlopen(req)
        resp_data = resp.read()
        new_data = str(resp_data).replace("b", "").replace('[', '').replace(']', '').replace("'", '')
        price_list = new_data.split(', ')
        rsi_data = [float(j) for j in price_list]

        if location == "top":
            a0.plot_date(ohlc['MPLDates'], rsi_data, light_colour, label="RSI")
            data_label = "RSI(" + str(top_indicator[1]) + ")"
            a0.set_ylabel(data_label)
        elif location == "bottom":
            a3.plot_date(ohlc['MPLDates'], rsi_data, light_colour, label="RSI")
            data_label = "RSI(" + str(bottom_indicator[1]) + ")"
            a3.set_ylabel(data_label)

    # Method: Used to calculate the moving average
    def moving_average(x, n, value='simple'):
        x = np.asarray(x)
        if value == 'simple':
            weights = np.ones(n)
        else:
            weights = np.exp(np.linspace(-1, 0, n))

        weights /= weights.sum()

        return np.convolve(x, weights, mode='full')[:len(x)]

    if chart_load:
        if pane_count == 1:
            if data_pace == "tick":
                try:
                    if exchange == "BTC-e":
                        a = plt.subplot2grid((6, 4), (0, 0), rowspan=5, colspan=4)
                        a2 = plt.subplot2grid((6, 4), (5, 0), rowspan=1, colspan=4, sharex=a)

                        data_link = 'https://btc-e.com/api/3/trades/btc_usd?limit=2000'
                        data = urllib.request.urlopen(data_link)
                        data = data.readall().decode('utf-8')
                        data = json.loads(data)
                        data = data["btc_usd"]
                        data = pd.DataFrame(data)

                        data["datestamp"] = np.array(data['timestamp']).asvalue('datetime64[s]')
                        all_dates = data["datestamp"].tolist()

                        buys = data[(data['value'] == 'bid')]
                        buy_dates = (buys["datestamp"]).tolist()

                        sells = data[(data['value'] == 'ask')]
                        sell_dates = (sells["datestamp"]).tolist()

                        volume = data["amount"]

                        a.clear()
                        a.plot_date(buy_dates, buys["price"], light_colour, label="buys")
                        a.plot_date(sell_dates, sells["price"], dark_colour, label="sells")
                        a2.fill_between(all_dates, 0, volume, facecolor='#183A54')
                        a.xaxis.set_major_locator(mticker.MaxNLocator(5))
                        a.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
                        plt.setp(a.get_xticklabels(), visible=False)
                        a.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
                                 ncol=2, borderaxespad=0.)
                        title = 'Last Price: ' + str(data["price"][1999])
                        a.set_title(title)

                    if exchange == 'Bitstamp':
                        a = plt.subplot2grid((6, 4), (0, 0), rowspan=5, colspan=4)
                        a2 = plt.subplot2grid((6, 4), (5, 0), rowspan=1, colspan=4, sharex=a)

                        data_link = 'https://www.bitstamp.net/api/transactions/'
                        data = urllib.request.urlopen(data_link)
                        data = data.readall().decode('utf-8')
                        data = json.loads(data)
                        data = pd.DataFrame(data)
                        data["datestamp"] = np.array(data['date'].apply(int)).asvalue("datetime64[s]")
                        datestamps = data["datestamp"].tolist()
                        volume = data["amount"].apply(float).tolist()

                        a.clear()
                        a.plot_date(datestamps, data["price"], '#183A54')
                        a2.fill_between(datestamps, 0, volume, facecolor='#183A54')
                        a.xaxis.set_major_locator(mticker.MaxNLocator(5))
                        a.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
                        plt.setp(a.get_xticklabels(), visible=False)
                        title = exchange + ' Tick Data\nLast Price: ' + str(data["price"][0])
                        a.set_title(title)
                        price_data = data["price"].apply(float).tolist()

                    if exchange == 'Bitfinex':
                        a = plt.subplot2grid((6, 4), (0, 0), rowspan=5, colspan=4)
                        a2 = plt.subplot2grid((6, 4), (5, 0), rowspan=1, colspan=4, sharex=a)

                        data_link = 'https://api.bitfinex.com/v1/trades/btcusd?limit=2000'

                        data = urllib.request.urlopen(data_link)
                        data = data.readall().decode('utf-8')
                        data = json.loads(data)
                        data = pd.DataFrame(data)

                        volume = data["amount"].apply(float).tolist()

                        data["datestamp"] = np.array(data['timestamp']).asvalue("datetime64[s]")
                        all_dates = data["datestamp"].tolist()

                        buys = data[(data['value'] == 'buy')]
                        buy_dates = (buys["datestamp"]).tolist()

                        sells = data[(data['value'] == 'sell')]
                        sell_dates = (sells["datestamp"]).tolist()

                        a.clear()
                        a.plot_date(buy_dates, buys["price"], light_colour, label="buys")
                        a.plot_date(sell_dates, sells["price"], dark_colour, label="sells")
                        a2.fill_between(all_dates, 0, volume, facecolor='#183A54')
                        a.xaxis.set_major_locator(mticker.MaxNLocator(5))
                        a.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
                        plt.setp(a.get_xticklabels(), visible=False)
                        a.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
                                 ncol=2, borderaxespad=0.)

                        title = exchange + ' Tick Data\nLast Price: ' + str(data["price"][0])
                        a.set_title(title)
                        price_data = data["price"].apply(float).tolist()

                    if exchange == 'Huobi':
                        try:
                            a = plt.subplot2grid((6, 4), (0, 0), rowspan=6, colspan=4)

                            data = urllib.request.urlopen(
                                'http://seaofbtc.com/api/basic/price?key=1&tf=1d&exchange=' + program_name).read()

                            data = str(data).replace('b', '').replace("'", '')
                            data = json.loads(data)

                            date_stamp = np.array(data[0]).asvalue("datetime64[s]")

                            df = pd.DataFrame({'Datetime': date_stamp})
                            df['Price'] = data[1]
                            df['Volume'] = data[2]
                            df['Symbol'] = "BTCUSD"
                            df['MPLDate'] = df['Datetime'].apply(lambda date: mdates.date2num(date.to_pydatetime()))
                            df = df.set_index('Datetime')
                            last_price = df['Price'][-1]

                            a.plot_date(df['MPLDate'][-4500:], df['Price'][-4500:], light_colour, label="price")
                            a.xaxis.set_major_locator(mticker.MaxNLocator(5))
                            a.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
                            title = exchange + ' Tick Data\nLast Price: ' + str(last_price)
                            a.set_title(title)
                            price_date = df['Price'].apply(float).tolist()
                        except Exception as ex:
                            print(str(ex))
                except Exception as ex:
                    print(str(ex))
                    data_counter = 9000
            else:
                if data_counter > 12:
                    try:
                        if exchange == 'Huobi':
                            if top_indicator != "none":
                                a = plt.subplot2grid((6, 4), (1, 0), rowspan=5, colspan=4)
                                a0 = plt.subplot2grid((6, 4), (0, 0), sharex=a, rowspan=1, colspan=4)
                            else:
                                a = plt.subplot2grid((6, 4), (0, 0), rowspan=6, colspan=4)
                        else:
                            if top_indicator != "none" and bottom_indicator != "none":
                                # Actual price chart
                                a = plt.subplot2grid((6, 4), (1, 0), rowspan=3, colspan=4)
                                # Volume
                                a2 = plt.subplot2grid((6, 4), (4, 0), sharex=a, rowspan=1, colspan=4)
                                # Top indicator
                                a0 = plt.subplot2grid((6, 4), (0, 0), sharex=a, rowspan=1, colspan=4)
                                # Bottom indicator
                                a3 = plt.subplot2grid((6, 4), (5, 0), sharex=a, rowspan=1, colspan=4)
                            elif top_indicator != "none":
                                a = plt.subplot2grid((6, 4), (1, 0), rowspan=4, colspan=4)
                                a2 = plt.subplot2grid((6, 4), (5, 0), sharex=a, rowspan=1, colspan=4)
                                a0 = plt.subplot2grid((6, 4), (0, 0), sharex=a, rowspan=1, colspan=4)
                            elif bottom_indicator != "none":
                                a = plt.subplot2grid((6, 4), (0, 0), rowspan=4, colspan=4)
                                a2 = plt.subplot2grid((6, 4), (4, 0), sharex=a, rowspan=1, colspan=4)
                                a3 = plt.subplot2grid((6, 4), (5, 0), sharex=a, rowspan=1, colspan=4)
                            else:
                                a = plt.subplot2grid((6, 4), (0, 0), rowspan=5, colspan=4)
                                a2 = plt.subplot2grid((6, 4), (5, 0), sharex=a, rowspan=1, colspan=4)

                        data = urllib.request.urlopen(
                            'http://seaofbtc.com/api/basic/price?key=1&tf=' + data_pace + '&exchange=' + program_name).read()

                        data = str(data).replace('b', '').replace("'", '')
                        data = json.loads(data)

                        date_stamp = np.array(data[0]).asvalue("datetime64[s]")
                        date_stamp = date_stamp.tolist()

                        df = pd.DataFrame({'Datetime': date_stamp})
                        df['Price'] = data[1]
                        df['Volume'] = data[2]
                        df['Symbol'] = "BTCUSD"
                        df['MPLDate'] = df['Datetime'].apply(lambda date: mdates.date2num(date.to_pydatetime()))
                        df = df.set_index('Datetime')

                        ohlc = df['Price'].resample(resample_size, how='ohlc')
                        ohlc = ohlc.dropna()

                        volume_data = df['Volume'].resample(resample_size, how={'volume': 'sum'})

                        ohlc['dateCopy'] = ohlc.index
                        ohlc['MPLDates'] = ohlc['dateCopy'].apply(lambda date: mdates.date2num(date.to_pydatetime()))
                        del ohlc['dateCopy']

                        volume_data['dateCopy'] = volume_data.index
                        volume_data['MPLDates'] = volume_data['dateCopy'].apply(
                            lambda date: mdates.date2num(date.to_pydatetime()))
                        del volume_data['dateCopy']

                        price_data = ohlc['close'].apply(float).tolist()

                        a.clear()
                        if middle_indicator != "none":
                            for each in middle_indicator:
                                ewma = pd.stats.moments.ewma

                                if each[0] == "sma":
                                    sma = pd.rolling_mean(ohlc["close"], each[1])
                                    label = str(each[1]) + " SMA"
                                    a.plot(ohlc['MPLDates'], sma, label=label)
                                if each[0] == "ema":
                                    ewma = pd.stats.moments.ewma
                                    label = str(each[1]) + " EMA"
                                    a.plot(ohlc['MPLDates'], ewma(ohlc["close"], each[1]), label=label)

                            a.legend(loc=0)

                        if top_indicator[0] == "rsi":
                            rsiIndicator(price_data, "top")
                        elif top_indicator == "macd":
                            try:
                                compute_macd(price_data, location="top")
                            except Exception as ex:
                                print(str(ex))

                        if bottom_indicator[0] == "rsi":
                            rsiIndicator(price_data, "bottom")
                        elif bottom_indicator == "macd":
                            try:
                                compute_macd(price_data, location="bottom")
                            except Exception as ex:
                                print(str(ex))

                        csticks = candlestick_ohlc(a, ohlc[['MPLDates', 'open', 'high', 'low', 'close']].values,
                                                   width=candle_width, colorup=light_colour, colordown=dark_colour)
                        a.set_ylabel("price")

                        if exchange != 'Huobi':
                            a2.fill_between(volumeData['MPLDates'], 0, volumeData['volume'],
                                            facecolor='#183A54')  # , alpha=.4)
                            a2.set_ylabel("volume")

                        a.xaxis.set_major_locator(mticker.MaxNLocator(3))
                        a.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
                        plt.setp(a.get_xticklabels(), visible=False)

                        if top_indicator != "none":
                            plt.setp(a0.get_xticklabels(), visible=False)

                        if bottom_indicator != "none":
                            plt.setp(a2.get_xticklabels(), visible=False)

                        x = (len(ohlc['close'])) - 1

                        if data_pace == '1d':
                            title = exchange + ' 1 Day Data with ' + resample_size + ' Bars\nLast Price: ' + str(
                                ohlc['close'][x])
                        if data_pace == '3d':
                            title = exchange + ' 3 Day Data with ' + resample_size + ' Bars\nLast Price: ' + str(
                                ohlc['close'][x])
                        if data_pace == '7d':
                            title = exchange + ' 7 Day Data with ' + resample_size + ' Bars\nLast Price: ' + str(
                                ohlc['close'][x])

                        if top_indicator != "none":
                            a0.set_title(title)
                        else:
                            a.set_title(title)

                        data_counter = 0
                    except Exception as ex:
                        print(str(ex))
                        data_counter = 9000
                else:
                    data_counter += 1


class SeaOfBTCApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Sea of BTC Client")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save settings", command=lambda: pop_up_message('Not supported just yet!'))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="File", menu=filemenu)

        exchange_choice = tk.Menu(menubar, tearoff=1)
        exchange_choice.add_command(label="BTC-e",
                                   command=lambda: change_exchange('BTC-e', 'btce'))
        exchange_choice.add_command(label="Bitfinex",
                                   command=lambda: change_exchange('Bitfinex', 'bitfinex'))
        exchange_choice.add_command(label="Bitstamp",
                                   command=lambda: change_exchange('Bitstamp', 'bitstamp'))
        exchange_choice.add_command(label="Huobi",
                                   command=lambda: change_exchange('Huobi', 'huobi'))
        menubar.add_cascade(label="Exchange", menu=exchange_choice)

        data_tf = tk.Menu(menubar, tearoff=1)
        data_tf.add_command(label="Tick", command=lambda: change_time_frame('tick'))
        data_tf.add_command(label="1 day", command=lambda: change_time_frame('1d'))
        data_tf.add_command(label="3 day", command=lambda: change_time_frame('3d'))
        data_tf.add_command(label="1 Week", command=lambda: change_time_frame('7d'))
        menubar.add_cascade(label="Data Time Frame", menu=data_tf)

        ohlc_i = tk.Menu(menubar, tearoff=1)
        ohlc_i.add_command(label="Tick", command=lambda: changeTimeFrame('tick'))
        ohlc_i.add_command(label="1 minute", command=lambda: changeSampleSize('1Min', 0.0005))
        ohlc_i.add_command(label="5 minute", command=lambda: changeSampleSize('5Min', 0.003))
        ohlc_i.add_command(label="15 minute", command=lambda: changeSampleSize('15Min', 0.008))
        ohlc_i.add_command(label="30 minute", command=lambda: changeSampleSize('30Min', 0.016))
        ohlc_i.add_command(label="1 Hour", command=lambda: changeSampleSize('1H', 0.032))
        ohlc_i.add_command(label="3 Hour", command=lambda: changeSampleSize('3H', 0.096))
        menubar.add_cascade(label="OHLC Interval", menu=ohlc_i)

        top_ind = tk.Menu(menubar, tearoff=1)
        top_ind.add_command(label="None", command=lambda: add_top_indicator('none'))
        top_ind.add_separator()
        top_ind.add_command(label="RSI", command=lambda: add_top_indicator('rsi'))
        top_ind.add_command(label="MACD", command=lambda: add_top_indicator('macd'))
        menubar.add_cascade(label="Top Indicator", menu=top_ind)

        mid_ind = tk.Menu(menubar, tearoff=1)
        mid_ind.add_command(label="None", command=lambda: add_middle_indicator('none'))
        mid_ind.add_separator()
        mid_ind.add_command(label="SMA", command=lambda: add_middle_indicator('sma'))
        mid_ind.add_command(label="EMA", command=lambda: add_middle_indicator('ema'))
        menubar.add_cascade(label="Main Graph Indicator", menu=mid_ind)

        bot_ind = tk.Menu(menubar, tearoff=1)
        bot_ind.add_command(label="None", command=lambda: add_bottom_indicator('none'))
        bot_ind.add_separator()
        bot_ind.add_command(label="RSI", command=lambda: add_bottom_indicator('rsi'))
        bot_ind.add_command(label="MACD", command=lambda: add_bottom_indicator('macd'))
        menubar.add_cascade(label="Bottom Indicator", menu=bot_ind)

        start_stop = tk.Menu(menubar, tearoff=1)
        start_stop.add_command(label="Resume", command=lambda: load_chart('start'))
        start_stop.add_command(label="Pause", command=lambda: load_chart('stop'))
        menubar.add_cascade(label="Resume/Pause Client", menu=start_stop)

        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="Tutorial", command=tutorial)
        menubar.add_cascade(label="Help", menu=help_menu)

        tk.Tk.config(self, menu=menubar)

        self.frames = {}
        for f in (StartPage, BTCePage):
            frame = f(container, self)
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

        tk.Tk.iconbitmap(self, default="dolla.ico")

    # Method: Used to show frame on the container
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="""The Sea of BTC trading client is a client intended to help traders
        interact with their exchanges. We do this by allowing you to enter
        your API keys into the program. We, as in Sea of BTC, never
        see your API information. The program may save them locally, however,
        to make things easier on you. Keep in mind that it is a fantastic idea
        to enable 'IP Whitelisting' if your exchange supports it, and only allow
        trading via your specific IP address. On most exchanges, even if someone
        was to acquire your API key, withdrawals are not possible. Some still
        give the option, so make sure this is turned OFF if your exchange allows it.

        Sea of BTC makes no promise of warranty, satisfaction, performance, or
        anything else. Understand that your use of this client is completely
        at your own risk.""", font=LARGE_FONT)

        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Agree", command=lambda: controller.show_frame(BTCePage))
        button2 = tk.Button(self, text="Disagree", command=quit)
        button1.pack()
        button2.pack()


class BTCePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="BTC-e Exchange Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)


app = SeaOfBTCApp()
app.geometry("1280x720")
ani = animation.FuncAnimation(f, animate, interval=5000)
app.mainloop()
