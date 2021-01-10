import re
import json
from os import chdir

from .path import run_here

__all__ = [
	'format_source_data',
	'source_data',
	'class_name',
	'format_name'
]

def format_source_data(data):
	data = re.sub(r', *//.*', ',', data) #Remove comment
	data = re.sub(r': *\.', ': 0.', data) #Remove float-like(.1, .2, ...)
	data = data.strip() #Remove space at start and end
	list_data = data.split('\n') #Prepare for get first line and last line
	while '"' not in list_data[1]:
		data = data[len(list_data[0]):-len(list_data[-1])].strip() #Remove first line and last line
		list_data = data.split('\n') #Overwrite list_data with new data
	
	data = data.replace(list_data[0], '{') #Let first line turn into "{"
	data = data.replace(list_data[-1], '}') #Let last line turn into "}"
	
	return data

@run_here
def source_data(file):
	chdir('..')
	with open(f'source/{file}.json', 'r', encoding = 'UTF-8') as source_file:
		return json.loads(source_file.read(), encoding = 'UTF-8')

def class_name(obj):
	if obj is type:
		return type.__class__.__name__
	return obj().__class__.__name__

def format_name(name):
	name = re.sub(r"[\s']", '-', name)
	return name