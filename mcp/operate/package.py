import os

from ..tools.path import run_here
from ..source import Source

__all__ = [
	'get_package_source_version'
]

@run_here
def get_package_source_version():
	return Source('game').data['meta']['buildVersion']