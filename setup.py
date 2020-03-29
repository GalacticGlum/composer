from setuptools import setup

setup(
    name='composer',
    version='1.0.0',
    py_modules=['cli'],
    entry_points='''
        [console_scripts]
        composer=cli:main
    '''
)