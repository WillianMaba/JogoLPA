#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.display

from code.Score import Score
from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.level import Level
from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            score = Score(self.window)
            menu =Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                player_score = [0, 0]  # [Player 1, Player2]
                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return = level.run(player_score)
                if level_return:
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    level_return = level.run(player_score)
                    #adicionando o level 3
                    if level_return:
                        level = Level(self.window, 'Level3', menu_return, player_score)
                        level_return = level.run(player_score)
                        if level_return:
                            score.save(menu_return, player_score)

            elif menu_return == MENU_OPTION[3]:
                score.show()

            elif menu_return == MENU_OPTION[4]:
                pygame.quit()  # Close window
                quit()  # End pygame
            else:
                pygame.quit()  # Close window
                quit()  # End pygame
