import pygame as pg

from pendulum import Pendulum
import const


def main() -> None:
    pg.init()
    screen = pg.display.set_mode(
        (const.WIDTH, const.HEIGHT),
        pg.HWSURFACE | pg.DOUBLEBUF
    )
    pg.display.set_caption("Pendulum")
    clock = pg.time.Clock()

    pendulum = Pendulum((const.WIDTH, const.HEIGHT))

    running = True
    while running:
        clock.tick(const.FPS)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        screen.blit(pendulum, (0, 0))
        pendulum.update()
        pg.display.flip()


if __name__ == "__main__":
    main()
