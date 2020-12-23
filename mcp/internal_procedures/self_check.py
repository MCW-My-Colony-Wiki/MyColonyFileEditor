import os
from ..tools import run_here, rel_chdir

__all__ = [
	'check_source'
]

@run_here
def check_source():
	rel_chdir('../source')