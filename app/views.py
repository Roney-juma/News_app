from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_top_headlines,get_source_news,get_category_news,search_news

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    news_sources = get_sources()
    top_headlines=get_top_headlines()[0:15]

    search_article = request.args.get('news_query')
    if search_article:
        return redirect(url_for('.search',news_article=search_article))
    else:    
        return render_template('index.html',sources = news_sources,headlines = top_headlines)