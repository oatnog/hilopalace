from pprint import pprint
from django.http import HttpResponse
from django.shortcuts import render

from bs4 import BeautifulSoup
import requests

def homePageView(request):

    movies_url = 'https://hilopalace.com/hpt_event_categories/movies/'
    page = requests.get(
        url=movies_url,
        headers={'User-Agent': 'Mozilla/5.0'},
    )

    soup = BeautifulSoup(page.content, 'html.parser')

    # article = soup.article


    results = soup.find_all('article')
    print(f"Found {len(results)} articles")

    movies: dict = {}

    for article in results:
        postid = [value[5:] for value in article['class'] if value.startswith('post-')]
    
        movie_info = [para.text.strip() for para in article.find_all('p')]
        movies[postid[0]] = movie_info
    
    pprint(movies)    
    return render(request=request,template_name='base.html', context={'movies': movies})
