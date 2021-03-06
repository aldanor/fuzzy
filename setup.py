#!/usr/bin/env python

# Project skeleton maintained at https://github.com/jaraco/skeleton

import io

import setuptools

with io.open('README.rst', encoding='utf-8') as readme:
	long_description = readme.read()

name = 'Fuzzy'
description = 'Fast Python phonetic algorithms'

params = dict(
	name=name,
	use_scm_version=True,
	author="YouGov, Plc.",
	author_email="jaraco@jaraco.com",
	description=description or name,
	long_description=long_description,
	url="https://github.com/yougov/" + name,
	ext_modules=[
		setuptools.Extension(
			'fuzzy',
			[
				'src/fuzzy.pyx',
				'src/double_metaphone.c'
			]
		),
	],
	python_requires='>=2.7,<3',
	install_requires=[
	],
	extras_require={
		'testing': [
			'pytest>=2.8',
			'pytest-sugar',
		],
		'docs': [
			'sphinx',
			'jaraco.packaging>=3.2',
			'rst.linker>=1.9',
		],
	},
	setup_requires=[
		'setuptools_scm>=1.15.0',
		'cython',
	],
	classifiers=[
		'Development Status :: 4 - Beta',
		'License :: OSI Approved :: MIT License',
		'License :: OSI Approved :: Artistic License',
		'Operating System :: POSIX',
		'Programming Language :: Python :: 2.7',
		'Topic :: Text Processing',
		'Topic :: Text Processing :: General',
		'Topic :: Text Processing :: Indexing',
		'Topic :: Text Processing :: Linguistic',
	],
	entry_points={
	},
)
if __name__ == '__main__':
	setuptools.setup(**params)
