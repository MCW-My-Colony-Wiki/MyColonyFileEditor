import setuptools

with open('README.md', 'r', encoding = 'UTF-8') as readme:
	long_description = readme.read()

with open('requirements.txt', 'r', encoding = 'UTF-8') as require:
	requirements = require.read().splitlines()

setuptools.setup(
	name = 'mcp',
	url = 'https://github.com/Euxcbsks/mcp',
	version = '1.0.0',
	author = 'Euxcbsks',
	author_email = 'hawhaw02030746@gmail.com',
	license = 'MIT',
	description = 'mcp - My Colony Python',
	long_description = long_description,
	long_description_content_type = 'text/markdown',
	install_requires = requirements,
	packages = setuptools.find_packages(),
	classifiers = [
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent'
	],
	python_requires = '>=3.6'
)
