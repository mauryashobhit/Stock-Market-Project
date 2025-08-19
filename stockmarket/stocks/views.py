import requests
from django.shortcuts import render
import bs4
from django.http import JsonResponse
import yfinance as yf


COMPANIES = [
    {"name": "Alphabet (Google)", "ticker": "GOOGL", "allocation": 17},
    {"name": "Microsoft", "ticker": "MSFT", "allocation": 15},
    {"name": "Cisco", "ticker": "CSCO", "allocation": 8},
    {"name": "Amazon", "ticker": "AMZN", "allocation": 12},
    {"name": "Apple", "ticker": "AAPL", "allocation": 13},
    {"name": "Adobe", "ticker": "ADBE", "allocation": 7},
    {"name": "Meta Platforms", "ticker": "META", "allocation": 10},
    {"name": "Netflix", "ticker": "NFLX", "allocation": 6},
    {"name": "Walmart", "ticker": "WMT", "allocation": 7},
    {"name": "JP Morgan Chase", "ticker": "JPM", "allocation": 5},
]

def invest(request):
    amount = float(request.GET["amount"])
    tickers = [c["ticker"] for c in COMPANIES]
    allocations = [c["allocation"] for c in COMPANIES]
    invested = [round(amount * (w/100), 2) for w in allocations]

    # Optionally fetch price data and simulate portfolio growth as before...

    response = {
        "companies": [
            {
                "name": c["name"], "ticker": c["ticker"],
                "allocation": round(c["allocation"],2), "invested": inv
            }
            for c, inv in zip(COMPANIES, invested)
        ],
        # "dates": [...], "values": [...]
    }
    return JsonResponse(response)

def investment(request):
    return render(request,"investment.html")

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