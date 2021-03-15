from setuptools import find_packages, setup

import nlsqli

install_requires = [
    'requests>=2.24',
    'rich>=9.13.0'
]

setup(
    name='nlsqli',
    version=nlsqli.__version__,
    description=nlsqli.__doc__.strip(),
    author=nlsqli.__author__,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'nlsqli = nlsqli.__main__:main',
        ],
    },
    python_requires='>=3.9',
    install_requires=install_requires
)
