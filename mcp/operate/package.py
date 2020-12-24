import os

from ..tools import run_here
from ..source.data import game

__all__ = [
	'del_pycache'
]

@run_here
def del_pycache():
	pass

@run_here
def get_package_source_version():
	os.chdir('..')
	return game.data['meta']['buildVersion']