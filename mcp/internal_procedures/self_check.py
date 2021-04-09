import os
import json

from requests import get, Timeout, URLRequired, codes

from ..tools.path.run_here import run_here
from ..tools.data.format_attr import format_source_data
from ..config import load_config
from ..exceptions import PageNotWorkError

__all__ = [
	"check_source"
]

def get_page(url):
	timeout = load_config('timeout')
	
	while True:
		try:
			page = get(url, timeout = timeout)
			break
		except Timeout:
			timeout = timeout + 1
		except URLRequired:
			print(f'Invalid URL: {url}')
			return
	
	if page.status_code == codes.ok:
		return page
	
	raise PageNotWorkError(f"{url} is not work")

def get_version_number(version_type = 'all'):
	#Try get page
	page = get_page('https://coloniae.space/static/json/mycolony_version.json')
	type_key = {
		'latest': 'mycolony_version',
		'stable': 'mycolony_stable_version'
	}
	
	version_data = json.loads(page.text)
	
	if version_type == 'all':
		version_number = {
			'latest': version_data['mycolony_version'],
			'stable': version_data['mycolony_stable_version']
		}
	elif version_type in type_key:
		version_number = version_data[type_key[version_type]]
	else:
		raise ValueError(f"Invalid version_type {version_type}")
	
	return version_number

def download_source(*files, version = get_version_number(load_config('update_from'))):
	downloading = "[mcp][download_source] Downloading '{file}'"
	
	@run_here
	def save_source(file):
		page = get_page(f'https://www.apewebapps.com/apps/my-colony/{version}/{file}.js')
		page.encoding = 'UTF-8'
		
		os.chdir('..')
		
		with open(f'source/{file}.json', 'w', encoding = 'UTF-8') as source_file:
			source_file.write(format_source_data(page.text))
	
	if type(files) is tuple:
		for file in files:
			print(downloading.format(file = file))
			save_source(file)
	elif files is str:
		print(downloading.format(file - files))
		save_source(files)

@run_here
def check_source():
	source_folder = 'source'
	creative_source_folder = '[mcp][check_source] Creative source folder'
	download_start = '[mcp][check_source] Missing source file, trying to download...'
	download_complete = '[mcp][check_source] Download complete'
	
	os.chdir('..')
	
	if not os.path.exists(source_folder):
		print(download_start)
		print(creative_source_folder)
		os.mkdir(source_folder)
		download_source('game', 'strings')
		print(download_complete)
		return
	
	listdir = os.listdir(source_folder)
	
	if len(listdir) != 2:
		print(download_start)
		if 'game.json' not in listdir:
			download_source('game')
		if 'strings.json' not in listdir:
			download_source('strings')

check_source()