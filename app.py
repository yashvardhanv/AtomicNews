# A very simple Flask Hello World app for you to get started with...
from newsapi import NewsApiClient
# from time import sleep
# from newspaper.article import ArticleException, ArticleDownloadState
from newspaper import Article
from newspaper import Config
from flask import Flask, render_template, url_for, redirect, request
app = Flask(__name__)
art = NewsApiClient(api_key='470a655fe44541d9a294810c9444edd9')
all_art = art.get_top_headlines()
articles = all_art['articles']


@app.route("/",methods=['GET','POST'])
def home():
    return render_template('home.html',articles=articles)


@app.route("/article",methods=['GET'])
def article():
    url = str(request.args.get("art"))
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    config = Config()
    config.browser_user_agent = user_agent
    article = Article(url,config=config)
    article.download()
    article.parse()
    article.nlp()
    # print("ERRORS IN PARSING ARTICLE")
    return render_template('article.html', title='Article',article=article)
