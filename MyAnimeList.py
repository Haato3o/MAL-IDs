import urllib
import urllib.request
from bs4 import BeautifulSoup


def id_manga(manga):
	url = 'https://myanimelist.net/manga.php?q={}'.format(manga.replace(' ', '%20'))
	url = urllib.request.urlopen(url).read().decode('utf-8')
	bSoup = BeautifulSoup(url, 'html.parser')
	mangaId = bSoup.find('a', class_='hoverinfo_trigger').get('href')
	mangaId = mangaId.split('/')
	mangaId = mangaId[4]
	return int(mangaId)

def id_anime(anime):
	url = 'https://myanimelist.net/search/all?q={}'.format(anime.replace(' ', '%20'))
	url = urllib.request.urlopen(url).read().decode('utf-8')
	bSoup = BeautifulSoup(url, 'html.parser')
	animeId = bSoup.find('div', class_='list di-t w100').find('a').get('href')
	animeId = animeId.split('/')
	animeId = animeId[4]
	return int(animeId)

def id_character(name):
	url = 'https://myanimelist.net/character.php?q={}'.format(name.replace(' ', '%20'))
	url = urllib.request.urlopen(url).read().decode('utf-8')
	bSoup = BeautifulSoup(url, 'html.parser')
	charId = bSoup.find('div', class_='picSurround').find('a').get('href')
	charId = charId.split('/')
	charId = charId[4]
	return int(charId)

'''
def getname(anime):
	url = 'https://myanimelist.net/search/all?q={}'.format(anime.replace(' ', '%20'))
	url = urllib.request.urlopen(url).read().decode('utf-8')
	bSoup = BeautifulSoup(url, 'html.parser')
	animeName = bSoup.find('div', class_='list di-t w100').find('a').get('href')
	animeName = animeName.split('/')
	animeName = animeName[5].replace('_', ' ')
	return animeName

def description(id):
	url = 'https://myanimelist.net/anime/{}'.format(id)
	url = urllib.request.urlopen(url).read().decode('utf-8')
	bSoup = BeautifulSoup(url, 'html.parser')
	animeDescription = bSoup.find('span', itemprop='description').get_text()
	return animeDescription

def score(id):
	url = 'https://myanimelist.net/anime/{}'.format(id)
	url = urllib.request.urlopen(url).read().decode('utf-8')
	bSoup = BeautifulSoup(url, 'html.parser')
	animeScore = bSoup.find('span', itemprop='ratingValue').get_text()
	return animeScore

def image(id):
	url = 'https://myanimelist.net/anime/{}'.format(id)
	url = urllib.request.urlopen(url).read().decode('utf-8')
	bSoup = BeautifulSoup(url, 'html.parser')
	animeImage = bSoup.find('img', itemprop='image').get('src')
	return animeImage

def rank(id):
	url = 'https://myanimelist.net/anime/{}'.format(id)
	url = urllib.request.urlopen(url).read().decode('utf-8')
	bSoup = BeautifulSoup(url, 'html.parser')
	animeRank = bSoup.find('div', class_='spaceit po-r js-statistics-info di-ib').get_text().split()
	animeRank = animeRank[1]
	return animeRank

'''


