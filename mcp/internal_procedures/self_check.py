import os
from ..core import run_here

__all__ = [
	'check_source'
]

@run_here
def check_source():
	if not os.path.exists('source'):
		os.mkdir('source')