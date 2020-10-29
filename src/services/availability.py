from src.models.country import Country
from src.models.feed import Feed

# hard-coded list of available countries
countries = [
    Country('US', 'United States'),
    Country('UK', 'United Kingdom'),
    Country('FR', 'France'),
    Country('PT', 'Portugal'),
    Country('JP', 'Japan')
]

# hard-coded dictionary of available feeds by country
feeds = {
    'US': [
        Feed('New York Times', 'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'),
        Feed('CNN', 'http://rss.cnn.com/rss/cnn_topstories.rss')
    ],
    'UK': [
        Feed('The Guardian', 'https://www.theguardian.com/world/rss'),
        Feed('Daily Mail', 'https://www.dailymail.co.uk/articles.rss'),
        Feed('BBC', 'http://feeds.bbci.co.uk/news/technology/rss.xml?edition=uk')
    ],
    'FR': [
        Feed('Le Monde', 'https://www.lemonde.fr/international/rss_full.xml')
    ],
    'PT': [
        Feed('Jornal de Noticias', 'http://feeds.jn.pt/JN-Ultimas'),
        Feed('O Jogo', 'http://feeds.ojogo.pt/OJ-Internacional')
    ],
    'JP': []
}


