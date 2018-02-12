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
