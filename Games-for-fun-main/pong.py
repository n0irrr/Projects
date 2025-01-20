import random
import pygame
pygame.init()

#GLOBAL VARIABLES
WIDTH, HEIGHT = 900, 700
FPS = 60
BLACK = (0,0,0)
WHITE = (255, 255 ,255)
ballradius = 8
pwidth, pheight = 30, 150
myfont = pygame.font.SysFont('Callibri', size=80)
p1_score = 0
p2_score = 0

#MAIN WINDOW
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')


class Paddle:
    COLOR = WHITE
    VEL = 10

    def __init__(self, x, y, WIDTH, HEIGHT):
        self.x = x
        self.y = y
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

    def drawit(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.WIDTH, self.HEIGHT))

    def move(self, up=True):
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL


class Ball:
    MAX_VEL = 5
    COLOR = WHITE

    def __init__(self, x, y, radius):
        self.x = self.originalx = x
        self.y = self.originaly = y
        self.radius = radius
        self.xvel = self.MAX_VEL
        self.yvel = 0

    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, [self.x, self.y], self.radius)

    def move(self):
        self.x += self.xvel
        self.y += self.yvel

    def reset(self):
        self.x, self.y = self.originalx, self.originaly
        self.yvel = 0
        self.xvel *= -1


def draw(win, paddles, ball, p1_score, p2_score):
    win.fill(BLACK)
    for paddle in paddles:
        paddle.drawit(win)

    midx = WIDTH//2 - 5
    posy = 15
    for i in range(10):
        pygame.draw.rect(win, WHITE, (midx, posy, 10, 40))
        posy += 70

    show_score1 = myfont.render(f"{p1_score}", True, WHITE)
    win.blit(show_score1, (WIDTH//2 - 100, 50))

    show_score2 = myfont.render(f"{p2_score}", True, WHITE)
    win.blit(show_score2, (WIDTH//2 + (100 - show_score2.get_width()), 50))

    ball.draw(win)

    pygame.display.update()


def move_paddle(keys, lpaddle, rpaddle):
    if keys[pygame.K_w] and lpaddle.y - lpaddle.VEL >= 0:
        up = True
        lpaddle.move(up)
    if keys[pygame.K_s] and lpaddle.y + lpaddle.HEIGHT + lpaddle.VEL <= HEIGHT:
        up = False
        lpaddle.move(up)
    if keys[pygame.K_UP] and rpaddle.y - rpaddle.VEL >= 0:
        up = True
        rpaddle.move(up)
    if keys[pygame.K_DOWN] and rpaddle.y + rpaddle.HEIGHT + rpaddle.VEL <= HEIGHT:
        up = False
        rpaddle.move(up)


def hit_ball(ball, paddle):
    mid_y = paddle.y + paddle.HEIGHT / 2
    difference_in_y = mid_y - ball.y
    reduction_factor = (paddle.HEIGHT / 2) / ball.MAX_VEL
    y_vel = difference_in_y / reduction_factor
    ball.yvel = y_vel * (-1)


def handle_collision(ball, lpaddle, rpaddle):
    if ball.y + ball.radius >= HEIGHT:
        ball.yvel *= -1
    elif ball.y - ball.radius <= 0:
        ball.yvel *= -1

    if ball.xvel > 0:
        if ball.x + ball.radius >= rpaddle.x:
            if ball.y - ball.radius >= rpaddle.y:
                if ball.y + ball.radius <= rpaddle.y + rpaddle.HEIGHT:
                    ball.xvel *= -1
                    hit_ball(ball, rpaddle)

        # towards left paddle
    else:
        if ball.x - ball.radius <= lpaddle.x + lpaddle.WIDTH:
            if ball.y - ball.radius >= lpaddle.y:
                if ball.y + ball.radius <= lpaddle.y + lpaddle.HEIGHT:
                    ball.xvel *= -1
                    hit_ball(ball, lpaddle)


def scoreboard(ball):
    global p1_score, p2_score
    if ball.x + ball.radius >= WIDTH:
        p1_score += 1
        ball.reset()
    elif ball.x - ball.radius <= 0:
        p2_score += 1
        ball.reset()
    if p1_score == 3:
        p1_score, p2_score = 0, 0
    if p2_score == 3:
        p1_score, p2_score = 0, 0

def main():
    run = True
    clock = pygame.time.Clock()
    global p1_score, p2_score

    lpaddle = Paddle(10, (HEIGHT//2 - pheight//2), pwidth, pheight)
    rpaddle = Paddle((WIDTH-10-pwidth), (HEIGHT//2 - pheight//2), pwidth, pheight)
    ball = Ball(WIDTH//2, HEIGHT//2, ballradius)
    draw(screen, [lpaddle, rpaddle], ball, p1_score, p2_score)

    while run:
        clock.tick(FPS)
        draw(screen, [lpaddle, rpaddle], ball, p1_score, p2_score)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        move_paddle(keys, lpaddle, rpaddle)
        ball.move()
        handle_collision(ball, lpaddle, rpaddle)
        scoreboard(ball)
    pygame.quit()


if __name__ == "__main__":
    main()
