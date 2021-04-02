#Simple stock graph
#This will take in multiple stock tickers and graph it on a plot
#purpose is to allow users to compare their favorite stock relative to other stocks within the same
#sector.


####TODO: implement ticker for indexes.  Use stooq: f = web.DataReader('^DJI', 'stooq')

import pandas_datareader.data as web
import datetime as dt
import matplotlib.pyplot as plt

list = []
start = dt.datetime(2020, 1, 1)
current = dt.datetime.now()


while True:

    input_stock = input("Please enter in a stock ticker.  Press q and ENTER when done entering stocks! ")

    if input_stock.strip().lower() == 'q':
        break

    if input_stock.upper() in list:
        print("You entered a duplicate ticker!  Please enter in another ticker! \n")
        continue

    try:
        web.DataReader(input_stock, 'yahoo', start, current)
        print("Entering " + input_stock.upper() + " into the list...\n")
        list.append(input_stock.upper())
    except:
        print("Unable to retrieve stock data!  Please enter the ticker symbol again!\n")

print(f"Your stocks that you inputted: {list}...  Generating graph now...")


#need to graph the charts now

for index in list:
    web.DataReader(index, 'yahoo', start, current)['Close'].plot(label=index)

plt.legend()
plt.show()