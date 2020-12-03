import requests
from bs4 import BeautifulSoup as bs
import json
import os
import time

from . import core
from .config import _load_config, config

run_here = core.run_here()

def get_pack_game_version():
	run_here.start()
	
	with open('pack_info.json', 'r', encoding = 'UTF-8') as pi:
		pack_info = json.load(pi)
	pack_game_version = pack_info['game_version']
	
	run_here.end()
	
	return pack_game_version

def _get_game_file_version():
	run_here.start()
	
	with open('game_file/game.js') as gf:
		for line in gf.readlines():
			if 'Version' in line:
				game_file_version = line.split(':')[1].replace(',', '').strip().replace('"', '')
	
	run_here.end()
	
	return game_file_version

def _get_latest_game_version():
	def update_cache():
		config_data = _load_config()
		html = None
		timeout = config_data['timeout']
		adjust_config = False
		
		while html == None:
			try:
				page = requests.get('https://market.ape-apps.com/my-colony.html', timeout = config_data['timeout'])
				if page.status_code == requests.codes.ok:
					html = bs(page.text, 'lxml')
			except Timeout:
				config(timeout = config_data['timeout']+1)
				adjust_config = True
		
		if adjust_config == True:
			config(timeout = timeout)
		
		run_here.start()
		
		with open(f'cache/html/{str(bs(page.text, "lxml").title)[7:-8]}.html', 'w') as f:
			f.write(page.text)
		
		run_here.end()
		return html
	
	try:
		run_here.start()
		
		filemtime = os.path.getmtime('cache/html/My Colony - Ape Market.html')
		now_time = time.time()
		if now_time-filemtime >= 86400:
			update_cache()
		else:
			html = bs(open('cache/html/My Colony - Ape Market.html'), 'lxml')
		
		run_here.end()
	except FileNotFoundError:
		html = update_cache()
	
	download_options = html.find_all(class_ = 'appDownloadItem')
	for option in download_options:
		if 'html5' in str(option):
			centereds = option.find_all(class_ = 'centered')
			for centered in centereds:
				if 'Tag' not in str(type(centered.contents[0])):
					latest_game_version = str(centered.contents[0])
					break
			break
	
	return latest_game_version

def _update_pack_game_version():
	if get_pack_game_version() != _get_game_file_version():
		run_here.start()
		
		with open('pack_info.json') as pi:
			pack_info = json.load(pi)
		pack_info['game_version'] = _get_game_file_version()
		
		with open('pack_info.json', 'w') as pi:
			json.dump(pack_info, pi, indent = '\t')
		
		run_here.end()
	else:
		return True

def _update_game_file(file):
	baseurl = 'https://www.apewebapps.com/apps/my-colony/{version}/{file}.js'
	config = _load_config()
	page = requests.get(baseurl.format(version = _get_latest_game_version(), file = file), timeout = config['timeout'])
	page.encoding = 'UTF-8'
	run_here.start()
	
	with open(f'game_file/{file}.js', 'w') as file:
		file.write(page.text)
	
	run_here.end()
	
	_update_pack_game_version()

def del_cache():
	cache_paths = ['cache/html', 'cache/data']
	
	run_here.start()
	for path in cache_paths:
		file_list = os.listdir(path)
		
		for file_name in file_list:
			os.remove(f'{path}/{file_name}')
	run_here.end()
	
	return file_list

def check_update():
	config = _load_config()
	
	if config['show_update_message']:
		print('# mcp check_update process')
		print('	Checking update...')

	pack_game_version = get_pack_game_version()
	latest_game_version = _get_latest_game_version()
	
	if pack_game_version != latest_game_version:
		if config['show_update_message']:
			print('	Update founded, updating...')
		
		_update_game_file('strings')
		_update_game_file('game')
		
		if config['show_update_message']:
			print(f'	Update completed, from v{pack_game_version} update to v{latest_game_version}')
		
		_update_pack_game_version()
	else:
		if config['show_update_message']:
			print(f'	Local game files have been updated to latest version(v{get_pack_game_version()})')
