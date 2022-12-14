import pygame

class Renderer:
    """Pelin pelikentän teksteistä vastaava näkymä"""

    def __init__(self, player, level, screen):
        """Luokan konstruktori"""
        self._player = player
        self._screen = screen
        self._level = level

    def render(self, points, lives):

        pygame.mouse.set_visible(0)
        self._screen.fill((255, 255, 255))
        self._level._all_units.draw(self._screen)
        self._screen.blit(self._player._player, (self._player.rect.x, self._player.rect.y))
        self.render_game_text(f'LIVES: {lives} POINTS: {points} PRESS "Q" TO QUIT ', [
                        150, 845], 25, (0, 0, 0), 'arial black')
        pygame.display.update()

    def render_game_text(self, words, pos, size, colour, font_name):
        """Luo pelinäytölle tekstit"""
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        self._screen.blit(text, pos)
