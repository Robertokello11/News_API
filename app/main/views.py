from flask import render_template, request, redirect, url_for
from . import main
from ..request import get_headlines, get_source, get_category, article_source

# our views


@main.route('/')
def index():
    '''
    Root function returning index/home page with data
    '''
    source = get_source()
    headlines = get_headlines()
    return render_template('index.html', headlines=headlines)


@main.route('/article/<id>')
def article(id):
    '''
    View article page function that returns the various article details page and its data
    '''
    # title= 'Articles'
    articles = article_source(id)
    return render_template('article.html', articles=articles, id=id)


@main.route('/categories/<cat_name>')
def category(cat_name):
    '''
    function to return the categories.html page and its content
    '''
    category = get_category(cat_name)
    title = f'{cat_name}'
    cat = cat_name

    return render_template('categories.html', title=title, category=category, cat=cat_name)

# from flask import render_template
# from app import app
# from .request import get_news


# # Views
# @app.route('/')
# def index():

#     '''
#     View root page function that returns the index page and its data
#     '''

#     # Getting popular movie
#     popular_movies = get_news('top')
#     print(top_news)

#     title = 'Home - Welcome to The best news Review Website Online'
#     return render_template('index.html', title = title,top = top_news)

# def news(news_id):

#     '''
#     View news page function that returns the news details page and its data
#     '''
#     return render_template('news.html',id = news_id)
