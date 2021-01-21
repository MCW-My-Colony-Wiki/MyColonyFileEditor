import os
from shutil import rmtree

from ..tools.path import run_here

__all__ = [
	'del_pyc'
]

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
	
	def delete_pyc():
		os.chdir('..')
		targets = folder_finder('.', '__pycache__')
	
		for target in targets:
			rmtree(target)
			print(f"Deleted folder '{target}'")
	
	with run_here(delete_pyc):
		pass
