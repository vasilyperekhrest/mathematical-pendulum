import pygame as pg
import const
import math


class Pendulum(pg.Surface):
    def __init__(self, size=(200, 200), length=200) -> None:
        """
        Initialization

        :param size: The size of the area on which the sphere will be drawn.
        :param length: Length of "thread".
        """
        pg.Surface.__init__(self, size=size)
        self.length = length
        self.g = 1200
        self.dt = 1/60

        self.a = 0
        self.v = 0
        self.phi = 2*math.pi / 3

        self.x1 = size[0] // 2
        self.y1 = size[1] // 3
        self.__calculate()
        self.__draw()

        self.coff = self.g/self.length
        self.speed = 0.000005
        self.coff = 1.0

    def update(self) -> None:
        """
        Angle recalculation.
        """
        self.fill(const.WHITE)
        if self.phi != 0:
            self.a = -(self.g/self.length) * math.sin(self.phi)
            self.v += self.a * self.dt
            self.phi += self.v * self.dt

            self.__calculate()
            self.__draw()
            self.phi *= self.coff
            self.coff -= self.speed

    def __calculate(self):
        self.x2 = self.x1 + self.length * math.cos(self.phi + math.pi / 2)
        self.y2 = self.y1 + self.length * math.sin(self.phi + math.pi / 2)

    def __draw(self) -> None:
        """
        Drawing a pendulum.
        """
        self.line = pg.draw.line(
            self,
            const.SLATEBLUE,
            (self.x1, self.y1),
            (self.x2, self.y2)
        )
        self.circle = pg.draw.circle(self, const.GREEN, (self.x2, self.y2), 9)
