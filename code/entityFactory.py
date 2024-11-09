#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.background import Background
from code.const import WINDOW_WIDTH, WINDOW_HEIGHT
from code.enemy import Enemy
from code.player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Level1Bg{i}', (0,0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WINDOW_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return Player('Player1', (10, WINDOW_HEIGHT / 2 - 30))
            case 'Player2':
                return Player('Player2', (10, WINDOW_HEIGHT / 2 + 30))
            case 'Enemy1':
                return Enemy('Enemy1', (WINDOW_WIDTH + 10, random.randint(40, WINDOW_HEIGHT - 40)))
            case 'Enemy2':
                return Enemy('Enemy2', (WINDOW_WIDTH + 10, random.randint(40, WINDOW_HEIGHT - 40)))
