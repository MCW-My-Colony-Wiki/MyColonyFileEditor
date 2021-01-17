import os
from glob import glob
from shutil import rmtree

from ..tools.path import run_here

__all__ = [
	'del_pyc'
]

@run_here
def del_pyc():
	def folder_finder(path, target):
		targets = []
		
		for folder in os.listdir(path):
			if os.path.isdir(folder) and folder == target:
				targets.append(os.path.abspath(f'{path}/{folder}'))
			elif os.path.isdir(folder):
				sub_folder_targets = folder_finder(folder, target)
				
				if sub_folder_targets != []:
					targets = targets + sub_folder_targets
		
		return targets
	
	os.chdir('..')
	
	targets = folder_finder('.', '__pycache__')
	
	for target in targets:
		rmtree(target)
		print(f"Deleted folder '{target}'")
