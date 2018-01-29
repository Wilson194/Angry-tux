from setuptools import setup, find_packages

with open('README.rst') as f:
    long_description = ''.join(f.readlines())

setup(
    name='Angry Tux',
    version='1.0',
    description='Simple game for linux users and windows haters.',
    long_description=long_description,
    author='Jan Horáček',
    author_email='horacj10@fit.cvut.cz',
    license='Public Domain',
    url='https://github.com/Wilson194/Angry-tux',
    packages=find_packages(),
    package_data={
        '': ['*.png', '*.jpg', '*.wav', '*.mp3'],
    },
    entry_points={
        'console_scripts': [
            'angrytux = angrytux.main:run',
            'AngryTux = angrytux.main:run',
        ],
    },
    install_requires=['pygame'],
)
