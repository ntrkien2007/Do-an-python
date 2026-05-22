import pygame, sys, random, os

pygame.init()

# ===== Cau Hinh =====
W, H = 1280, 720
BLOCK = 20

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Ran San Moi")

font = pygame.font.SysFont("Arial", 40)
clock = pygame.time.Clock()

# ===== Mau =====
GRASS1 = [(110,200,110),(100,190,100)]
GRASS2 = [(50,130,50),(40,120,40)]
WHITE = (255,255,255)
RED = (255,0,0)
GRAY = (200,200,200)

# ===== Do Kho =====
difficulty = "Thuong"
speed_map = {"De":10,"Thuong":15,"Kho":25}

# ===== High Score =====
file = "highscore.txt"
highscore = int(open(file).read()) if os.path.exists(file) else 0

# ===== Tao Nen =====
def tao_nen(colors):
    s = pygame.Surface((W,H))
    for x in range(0,W,BLOCK):
        for y in range(0,H,BLOCK):
            pygame.draw.rect(s, random.choice(colors),(x,y,BLOCK,BLOCK))
    return s

bg_menu = tao_nen(GRASS1)
bg_game = tao_nen(GRASS2)

# ===== Trang Thai =====
state = "menu"

# ===== Game Data =====
snake = [(100,100)]
direction = (BLOCK,0)
food = (200,200)
score = 0

# ===== Nut =====
btn_play = pygame.Rect(100,100,300,60)
btn_diff = pygame.Rect(100,200,300,60)
btn_exit = pygame.Rect(100,300,300,60)

# ===== Main Loop =====
while True:
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # ===== MENU =====
        if state == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if btn_play.collidepoint(mouse):
                    snake = [(100,100)]
                    direction = (BLOCK,0)
                    food = (random.randrange(0,W,BLOCK),
                            random.randrange(0,H,BLOCK))
                    score = 0
                    state = "game"

                elif btn_diff.collidepoint(mouse):
                    difficulty = "De" if difficulty=="Kho" else \
                                 "Thuong" if difficulty=="De" else "Kho"

                elif btn_exit.collidepoint(mouse):
                    pygame.quit()
                    sys.exit()

        # ===== GAME =====
        elif state == "game":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP: direction=(0,-BLOCK)
                if event.key == pygame.K_DOWN: direction=(0,BLOCK)
                if event.key == pygame.K_LEFT: direction=(-BLOCK,0)
                if event.key == pygame.K_RIGHT: direction=(BLOCK,0)

        # ===== GAME OVER =====
        elif state == "over":
            if event.type == pygame.MOUSEBUTTONDOWN:
                state = "menu"

    # ===== VE MENU =====
    if state == "menu":
        screen.blit(bg_menu,(0,0))

        pygame.draw.rect(screen, GRAY if btn_play.collidepoint(mouse) else WHITE, btn_play)
        pygame.draw.rect(screen, GRAY if btn_diff.collidepoint(mouse) else WHITE, btn_diff)
        pygame.draw.rect(screen, GRAY if btn_exit.collidepoint(mouse) else WHITE, btn_exit)

        screen.blit(font.render("Bat Dau Choi",1,(0,0,0)),(110,110))
        screen.blit(font.render(f"Do Kho: {difficulty}",1,(0,0,0)),(110,210))
        screen.blit(font.render("Thoat Tro Choi",1,(0,0,0)),(110,310))
        screen.blit(font.render(f"Diem So Cao Nhat: {highscore}",1,WHITE),(100,400))

    # ===== VE GAME =====
    elif state == "game":
        screen.blit(bg_game,(0,0))

        head = (snake[0][0]+direction[0], snake[0][1]+direction[1])

        # thua
        if (head in snake or head[0]<0 or head[0]>=W or head[1]<0 or head[1]>=H):
            if score > highscore:
                highscore = score
                open(file,"w").write(str(highscore))
            state = "over"
        else:
            snake.insert(0,head)

            if head == food:
                score += 1
                food = (random.randrange(0,W,BLOCK),
                        random.randrange(0,H,BLOCK))
            else:
                snake.pop()

        for s in snake:
            pygame.draw.rect(screen,(0,255,0),(*s,BLOCK,BLOCK))
        pygame.draw.rect(screen,RED,(*food,BLOCK,BLOCK))

        screen.blit(font.render(f"Diem: {score}",1,WHITE),(10,10))
        screen.blit(font.render(f"Diem So Cao Nhat: {highscore}",1,WHITE),(10,50))

    # ===== VE GAME OVER =====
    elif state == "over":
        screen.blit(bg_game,(0,0))
        screen.blit(font.render("Ban Da Thua",1,WHITE),(500,250))
        screen.blit(font.render(f"Diem: {score}",1,WHITE),(500,320))
        screen.blit(font.render("Click De Ve Menu",1,WHITE),(400,400))

    pygame.display.flip()
    clock.tick(speed_map[difficulty])