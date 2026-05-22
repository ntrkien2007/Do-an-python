import pygame
import sys

# 1. Hằng số (Constants)
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20
SPEED = 10  # Tốc độ này sẽ dễ điều khiển hơn 15

# Màu sắc
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)


class Snake:
    def __init__(self):
        # Vị trí đầu rắn
        self.pos = [100, 60]
        # Thân rắn (danh sách các khối)
        self.body = [[100, 60], [80, 60], [60, 60]]
        self.direction = "RIGHT"
        self.change_to = self.direction

    def change_dir(self, key):
        # Chặn quay đầu 180 độ
        if key == pygame.K_UP and self.direction != "DOWN":
            self.change_to = "UP"
        if key == pygame.K_DOWN and self.direction != "UP":
            self.change_to = "DOWN"
        if key == pygame.K_LEFT and self.direction != "RIGHT":
            self.change_to = "LEFT"
        if key == pygame.K_RIGHT and self.direction != "LEFT":
            self.change_to = "RIGHT"

    def move(self):
        self.direction = self.change_to
        if self.direction == "UP":    self.pos[1] -= BLOCK_SIZE
        if self.direction == "DOWN":  self.pos[1] += BLOCK_SIZE
        if self.direction == "LEFT":  self.pos[0] -= BLOCK_SIZE
        if self.direction == "RIGHT": self.pos[0] += BLOCK_SIZE

        # Cập nhật thân rắn
        self.body.insert(0, list(self.pos))
        self.body.pop()  # Xóa đuôi

    def draw(self, surface):
        for block in self.body:
            pygame.draw.rect(surface, GREEN, (block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))


# --- KHỞI TẠO GAME ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
snake = Snake()

# --- VÒNG LẶP CHÍNH ---
while True:
    screen.fill(BLACK)  # Xóa màn hình bằng màu đen

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            snake.change_dir(event.key)

    snake.move()
    snake.draw(screen)

    pygame.display.update()

    # Giới hạn tốc độ khung hình (FPS)
    clock.tick(SPEED)