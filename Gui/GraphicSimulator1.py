import numpy as numpy
import pygame
import sys
from pygame.time import Clock


class MovingObject(pygame.sprite.DirtySprite):
    def __init__(self, s_size):
        super(MovingObject, self).__init__()

        self.is_over = False

        self.image1 = "/home/jesusmal/PycharmProjects/Simulador2.0/Gui/sprites/sonic_frames/sonic1.png"
        self.image1 = pygame.image.load(self.image1).convert()
        self.image2 = "/home/jesusmal/PycharmProjects/Simulador2.0/Gui/sprites/sonic_frames/sonic2.png"
        self.image2 = pygame.image.load(self.image2).convert()

        self.image = self.image1
        self.current_image=self.image1
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (60, 60))

        self.s_width, self.s_height = s_size[0] - self.image.get_width(), s_size[1] - self.image.get_height()

        widht = self.image.get_width()
        self.rect.x = s_size[0] / 2 - widht / 2
        self.speed_y = 1

    def update(self) -> None:
        if self.rect.y < self.s_height:
            self.rect.y += self.speed_y
            if self.current_image==self.image1:
                self.current_image = self.image2
            else:
                self.current_image = self.image1
        else:
            self.is_over = True
            self.speed_y = 0
        pass


class Program(object):
    def run(self):
        while self.is_running:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.black)
            self.objects_in_screen.draw(self.screen)
            self.objects_in_screen.update()
            # end of draw zone
            pygame.display.flip()
            self.clock.tick(60)
            self.pass_time += 1
            print(self.pass_time / 60)
        pygame.quit()

    def __init__(self):
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)

        self.screen_size = numpy.array([600, 600])
        self.screen = pygame.display.set_mode(self.screen_size)

        self.clock = Clock()

        self.moving_object = MovingObject(self.screen_size)
        self.objects_in_screen = pygame.sprite.Group()
        self.objects_in_screen.add(self.moving_object)
        self.is_running = True
        self.pass_time = 0

    def isOver(self):
        pass


if __name__ == "__main__":
    program = Program()
    program.run()
