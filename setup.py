from setuptools import setup, find_packages

with open('README.rst') as f:
    long_description = ''.join(f.readlines())

setup(
    name='AngryTux',
    version='1.1',
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
    classifiers=[
        'Framework :: Pytest',
        'Framework :: Sphinx',
        'Natural Language :: English',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3.5',
        'Topic :: Games/Entertainment',
        'Topic :: Games/Entertainment :: Arcade',
        'Topic :: Software Development :: Libraries :: pygame'
    ],
    install_requires=['pygame'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite="tests",
    zip_safe=True,
)
