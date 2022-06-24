import numpy as numpy
import pygame
import sys
from pygame.time import Clock


class MovingObject(pygame.sprite.DirtySprite):
    def __init__(self, s_size, starting_speed, height, gravity, mass):
        super(MovingObject, self).__init__()

        self.is_over = False
        image_size = s_size / 5
        self.images = [
            pygame.transform.scale(pygame.image.load("flame_frames/0.png"), image_size),
            pygame.transform.scale(pygame.image.load("flame_frames/1.png"), image_size),
            pygame.transform.scale(pygame.image.load("flame_frames/2.png"), image_size),
            pygame.transform.scale(pygame.image.load("flame_frames/3.png"), image_size),
            pygame.transform.scale(pygame.image.load("flame_frames/4.png"), image_size),
            pygame.transform.scale(pygame.image.load("flame_frames/5.png"), image_size),
            pygame.transform.scale(pygame.image.load("flame_frames/6.png"), image_size),
            pygame.transform.scale(pygame.image.load("flame_frames/7.png"), image_size),
            pygame.transform.scale(pygame.image.load("flame_frames/8.png"), image_size),
            pygame.transform.scale(pygame.image.load("flame_frames/9.png"), image_size),
            pygame.transform.scale(pygame.image.load("flame_frames/10.png"), image_size),
            pygame.transform.scale(pygame.image.load("flame_frames/12.png"), image_size),
            pygame.transform.scale(pygame.image.load("flame_frames/13.png"), image_size),
            pygame.transform.scale(pygame.image.load("flame_frames/14.png"), image_size),
            pygame.transform.scale(pygame.image.load("flame_frames/15.png"), image_size),
            pygame.transform.scale(pygame.image.load("flame_frames/16.png"), image_size)
        ]

        self.image = self.images[0]
        self.current_image = 0
        self.image.set_colorkey([0, 0, 0])
        self.rect = self.image.get_rect()

        self.s_width, self.s_height = s_size[0] - self.image.get_width() - 50, s_size[1] - self.image.get_height()
        self.gravity = gravity

        widht = self.image.get_width()
        self.rect.x = s_size[0] / 2 - widht / 2
        self.starting_speed = starting_speed
        self.starting_height = height
        self.current_height = 0
        self.current_height_pixel = 0
        self.speed_y = 0
        self.kinetic_energy = 0
        self.mass = mass

    def speed_pos(self, current_time):
        self.speed_y = current_time * self.gravity + self.starting_speed
        self.current_height = (((1 / 2) * self.gravity * (current_time ** 2)) + self.starting_speed * current_time)
        self.current_height_pixel = (self.current_height * self.s_height) / self.starting_height
        self.kinetic_energy = ((1 / 2) * self.mass * self.speed_y ** 2)

    def update(self, time) -> None:
        self.speed_pos(time)
        if self.rect.y < self.s_height:
            self.rect.y = self.current_height_pixel
            if self.current_image != 0 and self.current_image < 16:
                self.image = self.images[self.current_image]
            elif self.current_image == 16:
                self.current_image = 0
                self.image = self.images[self.current_image]
            self.current_image += 1
        else:
            self.is_over = True
            self.speed_y = 0
            print("fin")
        pass


class Program(object):
    def run(self):
        while self.is_running:
            self.clock.tick(16)
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    self.is_running = False
                    break

            self.screen.fill(self.black)
            # draw zone
            if -self.back_ground_pos < 1980 - self.screen_size[1]:
                self.screen.blit(self.back_ground, (0, self.back_ground_pos))
                self.back_ground_pos = -(self.moving_object.current_height * 1980) / self.moving_object.starting_height
            else:
                self.screen.blit(self.back_ground, (0, -(1980 - self.screen_size[1])))
            self.objects_in_screen.draw(self.screen)
            self.moving_object.update(self.pass_time / 16)
            pygame.draw.line(self.screen, (255, 255, 255), (self.screen_size[0]-10, 10),
                             (self.screen_size[0]-10, self.screen_size[1]-10), width=10)
            self.isOver()
            # end of draw zone
            pygame.display.flip()
            self.pass_time += 1
        pygame.quit()

    def __init__(self, start_speed, mass, height, gravity, s_size):
        pygame.init()
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.texts = [0, 0, 0]
        self.tick = 16
        self.back_ground = pygame.image.load("background/background.png")
        self.back_ground = pygame.transform.scale(self.back_ground, (s_size[0], 1980))
        self.back_ground_speed = 1
        self.back_ground_pos = 0

        self.font = pygame.font.SysFont("Segoe Print", 30)
        self.screen_size = numpy.array(s_size)
        self.screen = pygame.display.set_mode(self.screen_size)

        self.clock = Clock()

        self.moving_object = MovingObject(self.screen_size, start_speed, height, gravity, mass)
        self.objects_in_screen = pygame.sprite.Group()
        self.objects_in_screen.add(self.moving_object)
        self.is_running = True
        self.pass_time = 0

    def isOver(self):
        if not self.moving_object.is_over:
            texto_surface_1 = self.font.render(
                "Time: " + (str(round(self.pass_time / 16, 2)) + "s"), 0, (255, 255, 255))
            self.texts[0] = texto_surface_1
            texto_surface_2 = self.font.render(
                "Height: " + (str(round(self.moving_object.current_height, 2)) + "m"), 0, (255, 255, 255))
            self.texts[1] = texto_surface_2
            texto_surface_3 = self.font.render(
                "Speed: " + (str(round(self.moving_object.speed_y, 2)) + "m/s"), 0, (255, 255, 255))
            self.texts[2] = texto_surface_3
        for i in range(len(self.texts)):
            self.screen.blit(self.texts[i], (10, 10 + i * 30))


if __name__ == "__main__":
    program = Program(0.0, 5.0, 60.0, 9.8, [500, 900])
    program.run()