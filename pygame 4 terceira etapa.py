import os.path, random, math

import pygame

pygame.init()
W, H = 800, 600
win = pygame.display.set_mode((W, H))

pygame.display.set_caption("Mini Asteroids Expandido")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)

HIGHSCORE_FILE = "highscore.txt"
if os.path.exists(HIGHSCORE_FILE):
    with open(HIGHSCORE_FILE, "r") as f:
        highscore = int(f.read())
else:
    highscore = 0


x_player, y_player = W // 2, H // 2
player_speed = 3
player_lives = 3
score = 0

bullets = []
last_shot = 0
shot_cooldown = 300
bullet_speed = 8

asteroids = []
asteroid_types = [
    {"size": 20, "speed": 3, "points": 15, "color": (200, 200, 255)},
    {"size": 35, "speed": 2, "points": 10, "color": (180, 180, 180)},
    {"size": 50, "speed": 1.5, "points": 5, "color": (150, 150, 150)}
]

powerups = []
powerup_active = False
powerup_timer = 0

STATE_MENU = 0
STATE_GAME = 1
STATE_GAMEOVER = 2
game_state = STATE_MENU


def spawn_asteroid():
    t = random.choice(asteroid_types)
    x = random.randint(0, W)
    y = random.choice([-50, H+50])
    angle = math.atan2(H//2 - y, W//2 - x)
    asteroids.append([x, y, t["speed"], t["size"], angle, t["points"], t["color"]])


def spawn_powerup():
    x = random.randint(50, W-50)
    y = random.randint(50, H-50)
    powerups.append((x, y, "shield"))


def reset_game():
    global player_pos, player_lives, score, asteroids, bullets, powerups
    player_pos = [W//2, H//2]
    player_lives = 3
    score = 0
    asteroids = []
    bullets = []
    powerups = []

    for _ in range(6):
        spawn_asteroid()


running = True
spawn_timer = 0
spawn_interval = 2000
last_powerup = 0
powerup_interval = 10000



while running:
    dt = clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if game_state == STATE_MENU and event.key == pygame.K_RETURN:
                reset_game()
                game_state = STATE_GAME
            elif game_state == STATE_GAMEOVER and event.key == pygame.K_RETURN:
                reset_game()
                game_state = STATE_GAME

    if game_state == STATE_GAME:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            x_player += player_speed
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            x_player -= player_speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            y_player += player_speed
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            y_player -= player_speed


        if pygame.mouse.get_pressed()[0] and pygame.time.get_ticks() - last_shot > shot_cooldown:
            last_shot = pygame.time.get_ticks()

            mouse_x, mouse_y = pygame.mouse.get_pos()
            dx = mouse_x - x_player
            dy = mouse_y - y_player
            dist = math.hypot(dx, dy)

            vx = dx / dist
            vy = dy / dist

            bullets.append([x_player, y_player, vx * bullet_speed, vy * bullet_speed])

        for b in bullets:
            b[0] += b[2]
            b[1] += b[3]

        bullets = [b for b in bullets if 0 < b[0] < W and 0 < b[1] < H]


        for a in asteroids:
            a[0] += math.cos(a[4]) * a[2]
            a[1] += math.sin(a[4]) * a[2]

        spawn_timer += dt
        if spawn_timer > spawn_interval:
            spawn_asteroid()
            spawn_timer = 0
            if spawn_interval > 1000:
                spawn_interval -= 50

        if pygame.time.get_ticks() - last_powerup > powerup_interval:
            spawn_powerup()
            last_powerup = pygame.time.get_ticks()

        if powerup_active and pygame.time.get_ticks() > powerup_timer:
            powerup_active = False

    win.fill((0, 0, 20))

    if game_state == STATE_MENU:
        title = font.render("MINI ASTEROIDS", True, (255, 255, 255))
        prompt = font.render("Pressiona ENTER para começar", True, (100, 200, 200))

        win.blit(title, (W // 2 - 100, H // 2 - 40))
        win.blit(prompt, (W // 2 - 100, H // 2))

    elif game_state == STATE_GAME:
        pygame.draw.circle(win, (0, 255, 0), (x_player, y_player), 20)
        for bullet in bullets:
            pygame.draw.circle(win, (255, 255, 0), (int(bullet[0]), int(bullet[1])), 5)

        for a in asteroids:
            pygame.draw.circle(win, a[6], (int(a[0]), int(a[1])), a[3])


        hud = font.render(f"Score: {score} Vidas: {player_lives}", True, (255, 255, 255))
        win.blit(hud, (10, 10))

    pygame.display.flip()

pygame.quit()





