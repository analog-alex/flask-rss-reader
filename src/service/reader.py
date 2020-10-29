import feedparser
from flask import Response

from src.repository.elasticsearch import put_in
from src.service import countries, feeds


def read_from_feed(url):
    return feedparser.parse(url)


def find_sources_by_country(country_code):
    # find country and return 404 if no match
    find = [country for country in countries if country.code == country_code]
    if len(find) == 0:
        return Response(status=404)
    country = find[0]

    # get the name of all feeds found for that country
    country_feeds = list(map(lambda x: x.name, feeds.get(country.code)))

    # prepare and send
    return {
        'country': country,
        'feeds': country_feeds
    }


def fetch_all_feeds_by_country(country_code):
    country_feeds = find_sources_by_country(country_code)

    # read all feeds and aggregate them on a single list
    all_news = []
    for news in country_feeds['feeds']:
        all_news.append({
            'name': news.name,
            'entries': read_from_feed(news.url).entries
        })

    return {
        'country': country_feeds['country'],
        'feeds': all_news
    }


def ingest_all_feeds_for_country(country_code):
    country_all_feeds = fetch_all_feeds_by_country(country_code)

    for news in country_all_feeds['feeds']:
        put_in('feeds', country_code, news)

    return {
        'result': 'success'
    }
