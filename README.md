Hello everyone.
This is last task in advance ml course.

Here you can find package, that I create using yfinance.

We have six different commands in my package.

1. get_info(ticker, param=None) - you can choose different number of tickers 
and select parameters that you want to see in your data frame. Default - all parametrs. Ticker must be 'TICKER' or ['TICKER1', 'TICKER2', e.t.c,]
2. get_all_price(ticker, period='Max', interval='1d') This command show you all prices of all tickers that you want. You can choose period and interval.
3. get_close_price(ticker, period='Max', interval='1d') This command show you only 'Close' prices of your tickers
4. close_price_percent(ticker, period='Max', interval='1d') This command show you difference in percents between close prices
5. plot_ticker(ticker, period='Max', interval='1d, perfomance=24) This command plot your tickers, Perfomance = period of time for plot
6. simple_regression(ticker, period='Max') This command fit simple regression and show you difference between real and predict prices

In script.py you can find simple flask.

If you want to run it type "python script.py 7777"
and then 

curl http://0.0.0.0:7777/ -H "Content-Type: application/json" -d '{"plot_ticker": "AAPL"}'
Where in key you need to write command, and in value tickers, that you want to see.