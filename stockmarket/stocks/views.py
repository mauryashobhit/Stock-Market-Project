import requests
from django.shortcuts import render
import bs4
from django.http import JsonResponse
import yfinance as yf


def index(request):
    stock_data = {}
    if request.method == "POST":
        symbol = request.POST.get("AAPL")
        api_key = '7HKESRO351LRMW3U'
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}'
        response = requests.get(url)
        stock_data = response.json()
    return render(request, "index.html", {'stock_data': stock_data})

def news(request):
    list=[]
    list1=[]
    results=requests.get("https://economictimes.indiatimes.com/markets/stocks/news")
    soup=bs4.BeautifulSoup(results.text,"lxml")
    details = soup.findAll('div',attrs={"class":"eachStory"})
    title=soup.findAll('div',attrs={"class":"eachStory"})
    for x in title:
        list.append(x.find('h3').text)
    for i in details:
        list1.append(i.find('p').text)
    return render(request,"news.html",context={"list":list,"list1":list1})

def nifty50_data(request):
    ticker = yf.Ticker('^NSEI')
    df = ticker.history(period="1d", interval="1m")  # Intraday, 1-min OHLC
    df = df.dropna(subset=["Open", "High", "Low", "Close"])
    time_labels = [t.strftime('%H:%M') for t in df.index]
    open_prices = df["Open"].tolist()
    high_prices = df["High"].tolist()
    low_prices = df["Low"].tolist()
    close_prices = df["Close"].tolist()
    volumes = df["Volume"].tolist()
    return JsonResponse({
        'labels': time_labels,
        'open': open_prices,
        'high': high_prices,
        'low': low_prices,
        'close': close_prices,
        'volume': volumes})


def niftychart(request):
    return render(request, 'nifty_chart.html')

def screener(request):
    return render(request,'screener.html')

def login(request):
    return render(request,'Login.html')