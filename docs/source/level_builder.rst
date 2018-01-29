Level builder
==============


You can use created level build for creating your own levels. In the code is abstract class ``LevelCreator``.
With extending this class you can create you own levels. Class have 3 methods.

create_enemies
---------------

This method is for creating enemies. You can create as many enemies as you want and return list of this enemies from this method.

One enemy is created by enemy class:

>>> from angrytux.model.abstract_facotry.CreationFactory import CreationFactory
>>> from angrytux.model.game_objects.Position import Position
>>> CreationFactory().create_dummy_enemy(Position(450, 400))
>>> CreationFactory().create_smart_enemy(Position(700, 700))


where ``CreationFactory`` create proper enemy. You can chose smart or dummy enemy. Behaviour of enemies depends on selected mode.
One parameter is position class which need two parameters, x and y position.

create_obstacles
----------------

This method is for creating obstacles. Is almost same as enemies but for obstacles:

>>> from angrytux.model.game_objects.Obstacle import Obstacle
>>> obstacles.append(Obstacle(Position(400, 10)))

music
-------

Last part is music for level. That is important! You can play your own music with this:

>>> file = os.path.join('angrytux', 'resources', 'sounds', 'song1.mp3')
>>> pygame.mixer.music.load(file)
>>> pygame.mixer.music.play()