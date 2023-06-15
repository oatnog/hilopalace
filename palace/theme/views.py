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

    titles = [title.text for title in soup.select('.entry-title')]
    images: list = [image['src'] for image in soup.select('.post-image')]

    results = soup.find_all('article')
    print(f'Found {len(results)} articles')

    movies: list = []

    # skip first Title entry, as it's page title not the entry title
    for article, link, title in zip(results, images, titles[1:]):
        postid = [
            value[5:]
            for value in article['class']
            if value.startswith('post-')
        ]

        movie_info = [para.text.strip() for para in article.find_all('p')]
        movies.append(
            {
                'id': postid[0],
                'title': title,
                'info': movie_info,
                'image': link,
            }
        )

    # pprint(movies)
    return render(
        request=request,
        template_name='base.html',
        context={'movies': movies},
    )
