import importlib
import os

requests = importlib.import_module('requests')
bs = importlib.import_module('bs4').BeautifulSoup

from ..tools.path import run_here
from ..tools.data import format_source_data
from ..config import load_config

__all__ = [
	
]

def get_page(url):
	timeout = load_config('timeout')
	
	while True:
		try:
			page = requests.get(url, timeout = timeout)
			break
		except requests.Timeout:
			timeout = timeout + 1
		except requests.URLRequired:
			print(f'Invalid URL: {url}')
			return
	
	if page.status_code == requests.codes.ok:
		return page
	print(f'{url} is not work')
	return

def get_latest_version_number():
	#Try get page
	page = get_page('https://market.ape-apps.com/my-colony.html')

	#If page is work, find out latest version number
	if page is not None:
		page = bs(page.text, 'lxml')
		download_options = page.find_all(class_ = 'appDownloadItem')
	
		for option in download_options:
			if 'html5' in str(option):
				centereds = option.find_all(class_ = 'centered')
				
				for centered in centereds:
					if 'Tag' != centered.contents[0].__class__.__name__:
						latest_version_number = str(centered.contents[0])
						break
				break
	else:
		return
	
	return latest_version_number

def download_source(file, *, version = get_latest_version_number()):
	if version is not None:
		page = get_page(f'https://www.apewebapps.com/apps/my-colony/{version}/{file}.js')
		page.encoding = 'UTF-8'
		
		def write_source():
			os.chdir('..')
			with open(f'source/{file}.json', 'w', encoding = 'UTF-8') as source_file:
				source_file.write(format_source_data(page.text))
		
		if page is not None:
			with run_here(write_source):
				pass
			
			return True
		return False
	return False

def check_source():
	os.chdir('..')
	source = 'source'
	
	if not os.path.exists(source):
		os.mkdir(source)
	
	listdir = os.listdir(source)
	
	if 'game.json' not in listdir or 'strings.json' not in listdir:
		print('Missing source file, trying to download...')
		return False
	return True

with run_here(check_source) as exist:
	if not exist:
		download_source('game')
		download_source('strings')
		print('Download complete')
