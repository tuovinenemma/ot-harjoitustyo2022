import pygame

class Start:
    """Pelin alkunäytöstä vastaava näkymä"""
    def __init__(self, events, clock):
        """Luokan konstruktori. Luo aloitusnäytön"""
        pygame.init()
        self._clock = clock
        self._state = "start"
        self._width = 700
        self._height = 875
        self._events = events
        self._monsters_count = 0
        self._screen = pygame.display.set_mode((self._width, self._height))

    def _start_game(self):
        self._start_text2()
        pygame.display.update()


    def _start_screen(self):
        """Näyttää näkymän ja käynnistää haluttaessa pelin"""
        self._start_game()
        while True:
            self._events._handle_events()
            if self._events._key_pressed == "b":
                self._monsters_count = 10
                self._start_text3()
                pygame.display.update()
            if self._events._key_pressed == "h":
                self._monsters_count = 15
                self._start_text3()
                pygame.display.update()
            if self._events._key_pressed == "space":
                return
            pygame.display.update()
            self._clock.tick(60)

    def _game_starting(self):
        if self._state == "start":
            self._starting()
            pygame.display.update()


    def _render(self):
        self._difficulty()

    def _start_text1(self, words, screen, pos, size, colour, font_name, middle=False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        if middle:
            pos[0] = pos[0]-text_size[0]//2
            pos[1] = pos[1]-text_size[1]//2
        screen.blit(text, pos)

    def _start_text2(self):
        pygame.mouse.set_visible(0)
        self._screen.fill((255, 255, 255))
        self._start_text1('THE MAZE RUNNER', self._screen, [self._width//2, self._height//2-150], 45, (0, 0, 0), 'arial black', middle=True)
        self._start_text1('PRESS "B" TO CHOOSE BEGINNER', self._screen, [self._width//2, self._height//2-40], 30, (0, 0, 0), 'arial black', middle=True)
        self._start_text1('PRESS "H" TO CHOOSE HARD', self._screen, [self._width//2, self._height//2-1], 30, (0, 0, 0), 'arial black', middle=True)

    def _start_text3(self):
        pygame.mouse.set_visible(0)
        self._screen.fill((255, 255, 255))
        self._start_text1('PRESS SPACE BAR TO ENTER THE MAZE', self._screen, [self._width//2, self._height//2-40], 30, (0, 0, 0), 'arial black', middle=True)