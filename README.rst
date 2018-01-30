Angry Tux game
===============

.. image:: https://travis-ci.com/Wilson194/Angry-tux.svg?token=PdLqtPfyXNo5KfhxbzAS&branch=master
    :target: https://travis-ci.com/Wilson194/Angry-tux


.. image:: https://readthedocs.org/projects/angry-tux/badge/?version=latest
    :target: http://angry-tux.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status


Simple game for linux lovers and Windows haters. If you have some free time you can destroy some windows and
they will donate you with awesome blue screen of death. That is amazing!


Description
------------

Simple game develop because of school project at FIT CTU at Prague. If you have free time, you can shoot some Windows millenium
for no reason. Just because you want.

How to run the game
--------------------

You can easily run the game after installing wiw pip using command ``AngryTux``. After run this script, new window appear and
you can start playing. User control are describe in next part.

You can chose level to play with option ``-l /level_number/``. In default there are only 2 levels, but you can create your own.

Second option what you can chose is creation factory. This change behaviour of whole game and enemies.
You can chose factory with ``-f /factory/`` There are two types of factories:

* simple - simple mode, enemies just stay at one place and moving of missiles is really simple
* realistic - realistic mode, enemies are smart (moving and teleporting) and missiles using ballistic curve for moving


Control
---------

+-----------+-------------------------------------------------------+
| ^ (up)    | Move cannon up                                        |
+-----------+-------------------------------------------------------+
| v (down)  | Move cannon down                                      |
+-----------+-------------------------------------------------------+
| < (left)  | Angle cannon up                                       |
+-----------+-------------------------------------------------------+
| > (right) | Angle cannon down                                     |
+-----------+-------------------------------------------------------+
| **f**     | Increase value of gravity                             |
+-----------+-------------------------------------------------------+
| **g**     | Decrease value of gravity                             |
+-----------+-------------------------------------------------------+
| **o**     | Decrease value of shooting strength                   |
+-----------+-------------------------------------------------------+
| **p**     | Increase value of shooting strength                   |
+-----------+-------------------------------------------------------+
| **c**     | Change shooting state (single shoot / double shoot)   |
+-----------+-------------------------------------------------------+
| **u**     | Undo command (undo previous command)                  |
+-----------+-------------------------------------------------------+
| **s**     | Shoot missile                                         |
+-----------+-------------------------------------------------------+


Documentation
--------------

You can find documentation at page http://angry-tux.readthedocs.io/en/latest/


Pypi
------

You can install game from test https://test.pypi.org/project/AngryTux/

Level creator
--------------

You can create your own level for this game. In code you can find abstract class ``LevelCreator``. If you extend this class,
you can create your own levels. If you want to find more, just look into documentation.