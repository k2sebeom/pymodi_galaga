import modi
from threading import Timer
import pygame
from random import randint
import time

global gamepad, clock, cool_time, jet, background, enemies, bullets, targets
global score

WIDTH, HEIGHT = 512, 700
SPEED, ENEMY_SPEED, BULLET_SPEED = 4, 2, 10
DEADZONE = 5
global SPAWN_TIME
SPAWN_TIME = 3


def cool_off():
    global cool_time
    cool_time = False


def shoot(speaker, x, y):
    global bullets
    speaker.set_tune(700, 100)
    Timer(0.1, lambda: speaker.set_tune(0, 0)).start()
    x, y = x + 45, y
    bullets.append((x, y))


def check_bullets():
    global bullets, gamepad
    i = 0
    while i < len(bullets):
        x, y = bullets[i]
        bullets[i] = (x, y - BULLET_SPEED)
        x, y = bullets[i]
        pygame.draw.line(gamepad, (255, 255, 255), (x, y), (x, y - 10), 4)
        if check_enemy_death(x, y) or y <= 0:
            bullets.pop(i)
        else:
            i -= - 1


def check_enemy_death(b_x, b_y):
    global SPAWN_TIME, score
    for i in range(len(targets)):
        _, x, y = targets[i]
        if x + 40 >= b_x >= x and y + 40 >= b_y >= y:
            targets.pop(i)
            if SPAWN_TIME > 0.7:
                SPAWN_TIME -= 0.1
            score += 1
            return True
    return False


def check_death(p_x, p_y):
    for _, x, y in targets:
        if x + 40 >= p_x >= x - 40 and y + 10 >= p_y:
            return True
    return False


def jet_plane(x):
    global gamepad, clock
    gamepad.blit(jet, (x, HEIGHT - 100))


def spawn_enemy():
    global targets, SPAWN_TIME
    targets.append((randint(0, 1), randint(0, WIDTH - 100), 100))
    Timer(SPAWN_TIME, spawn_enemy).start()


def move_enemies():
    global targets
    i = 0
    while i < len(targets):
        targets[i] = (
            targets[i][0],
            targets[i][1] + randint(-ENEMY_SPEED, ENEMY_SPEED),
            targets[i][2] + ENEMY_SPEED
        )
        if targets[i][2] >= HEIGHT:
            targets.pop(i)
        else:
            i -= -1


def show_enemies():
    global targets, gamepad, enemies
    for t, x, y in targets:
        gamepad.blit(enemies[t], (x, y))


def run_game(bundle):
    global gamepad, clock, jet, cool_time, background, targets, bullets, score
    gyro, speaker, button, led = \
        bundle.gyros[0], bundle.speakers[0], bundle.buttons[0], bundle.leds[0]

    while True:
        if button.get_pressed():
            break
        pygame.display.update()
        pygame.event.get()
        clock.tick(60)

    crashed = False
    cool_time = False
    x = WIDTH // 2
    spawn_enemy()
    led.set_green()
    score = 0
    font = pygame.font.Font('./8bit.ttf', 24)
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
        gamepad.fill((255, 255, 255))
        gamepad.blit(background, (0, 0))
        pitch = gyro.get_pitch()
        if pitch < -DEADZONE:
            x += SPEED
        elif pitch > DEADZONE:
            x -= SPEED
        jet_plane(x)

        gamepad.blit(font.render(str(score), False,
                                 (255, 255, 255)), (WIDTH // 2 - 10, 60))

        if button.get_pressed() and not cool_time:
            shoot(speaker, x, HEIGHT - 100)
            cool_time = True
            Timer(0.2, cool_off).start()
        move_enemies()
        show_enemies()
        check_bullets()

        if check_death(x, HEIGHT - 100):
            led.set_rgb(255, 0, 0)
            break

        pygame.display.update()
        clock.tick(60)

    time.sleep(2)
    over_back = pygame.image.load('./over.png')
    gamepad.blit(over_back, (0, 0))
    gamepad.blit(font.render(str(score), False,
                             (0, 0, 0)), (WIDTH // 2 - 10, HEIGHT // 2 + 20))

    while True:
        if button.get_pressed():
            led.set_off()
            break
        pygame.display.update()
        pygame.event.get()
        clock.tick(60)

    time.sleep(0.1)
    pygame.quit()
    bundle._com_proc.terminate()


def init_game():
    global gamepad, clock, jet, background, enemies, targets, bullets

    bundle = modi.MODI(4)
    pygame.init()
    gamepad = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("PyMODI rox")
    jet = pygame.image.load('./jet.png')
    enemies, targets, bullets = [], [], []
    enemies.append(pygame.image.load('./enemy1.png'))
    enemies.append(pygame.image.load('./enemy2.png'))
    background = pygame.image.load('./background.png')
    clock = pygame.time.Clock()
    start_back = pygame.image.load('./start.png')
    gamepad.blit(start_back, (0, 0))
    pygame.display.update()
    run_game(bundle)


if __name__ == "__main__":
    init_game()