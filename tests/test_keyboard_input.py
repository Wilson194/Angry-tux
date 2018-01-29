from angrytux.controller.Keyboard import Keyboard
import pygame
import pytest


class Remember:
    """
    Class for remembering created command
    """


    def __init__(self):
        self.created_command = None


    def remember(self, command):
        self.created_command = command


class DummyEvent:
    """
    Dummy event that replace pygame event
    """


    def __init__(self, key_value):
        self.key_value = key_value


    @property
    def type(self):
        return pygame.KEYDOWN


    @property
    def key(self):
        return self.key_value


@pytest.mark.parametrize(['command', 'key'],
                         [('CannonUpCommand', pygame.K_UP),
                          ('CannonDownCommand', pygame.K_DOWN),
                          ('CannonAngleDownCommand', pygame.K_RIGHT),
                          ('CannonAngleUpCommand', pygame.K_LEFT),
                          ('ShootCommand', pygame.K_SPACE),
                          ('ChangeCannonStateCommand', pygame.K_c),
                          ('CannonStrengthUpCommand', pygame.K_p),
                          ('CannonStrengthDownCommand', pygame.K_o),
                          ('UndoCommand', pygame.K_u),
                          ('GravityUpCommand', pygame.K_g),
                          ('GravityDownCommand', pygame.K_f),
                          ])
def test_keyboard_input_create_correct_commands(monkeypatch, command, key):
    keyboard = Keyboard()

    remember = Remember()
    dummy_event = DummyEvent(key)

    monkeypatch.setattr(pygame.event, 'get', lambda: [dummy_event])
    monkeypatch.setattr(keyboard, '_add_command', remember.remember)
    keyboard.tick()

    assert remember.created_command.__class__.__name__ == command
