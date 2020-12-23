import requests
from bs4 import BeautifulSoup as bs
import json
import os
import time

from ..tools import run_here
from ..operate.package import load_config
from ..operate.unit import get_unit

__all__ = [
	'check_update'
]

config_data = load_config()

@run_here
def get_pack_game_version():
	os.chdir('..')
	with open('pack_info.json', 'r', encoding = 'UTF-8') as pi:
		pack_info = json.load(pi)
		pack_game_version = pack_info['game_version']
	return pack_game_version

@run_here
def get_latest_game_version():
	def request_html():
		timeout = config_data['timeout']
		html = None
		
		while html is None:
			try:
				page = requests.get('https://market.ape-apps.com/my-colony.html', timeout = timeout)
				if page.status_code == requests.codes.ok:
					html = bs(page.text, 'lxml')
			except requests.Timeout:
				timeout = timeout + 1
		
		with open(f'cache/html/{str(bs(page.text, "lxml").title)[7:-8]}.html', 'w') as f:
			f.write(page.text)
		
		return html
	
	try:
		os.chdir('..')
		filemtime = os.path.getmtime('cache/html/My Colony - Ape Market.html')
		now_time = time.time()
		if now_time-filemtime >= 86400:
			html = request_html()
		else:
			html = bs(open('cache/html/My Colony - Ape Market.html'), 'lxml')
	except FileNotFoundError:
		html = request_html()
	
	download_options = html.find_all(class_ = 'appDownloadItem')
	
	for option in download_options:
		if 'html5' in str(option):
			centereds = option.find_all(class_ = 'centered')
			
			for centered in centereds:
				if 'Tag' != centered.contents[0].__class__.__name__:
					latest_game_version = str(centered.contents[0])
					break
			
			break
	
	return latest_game_version

@run_here
def get_game_file_version():
	game_file_version = get_unit('game', 'meta', 'buildVersion')
	return game_file_version

@run_here
def update_pack_game_version():
	if get_pack_game_version() != get_game_file_version():
		os.chdir('..')
		with open('pack_info.json') as pi:
			pack_info = json.load(pi)
		
		pack_info['game_version'] = get_game_file_version()
		
		with open('pack_info.json', 'w') as pi:
			json.dump(pack_info, pi, indent = '\t', ensure_ascii = False)

@run_here
def update_game_file(file):
	baseurl = 'https://www.apewebapps.com/apps/my-colony/{version}/{file}.js'
	page = requests.get(baseurl.format(version = get_latest_game_version(), file = file), timeout = config_data['timeout'])
	page.encoding = 'UTF-8'
	os.chdir('..')
	
	with open(f'source/{file}.js', 'w') as file:
		file.write(page.text)
	
	update_pack_game_version()

def check_update():
	if config_data['show_update_process']:
		print('mcp check_update process')
		print('	Checking update...')

	pack_game_version = get_pack_game_version()
	latest_game_version = get_latest_game_version()
	
	if pack_game_version != latest_game_version:
		if config_data['show_update_process']:
			print('	Update founded, updating...')
		
		update_game_file('strings')
		update_game_file('game')
		
		if config_data['show_update_process']:
			print(f'	Update completed, from v{pack_game_version} update to v{latest_game_version}')
		
		update_pack_game_version()
	else:
		if config_data['show_update_process']:
			print(f'	Local game files have been updated to latest version(v{get_pack_game_version()})')

def update():
	pass