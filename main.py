import pygame,sys

# Kiem tra ban trung chua
def check(x1,y1,x2,y2):
    if y2 <= y1 + 64 and x2 >= x1 -26 and x2 <= x1 +26:
        return True
    else:
        return False

# Lay ten nguoi choi 
def get_Start():
    name =''

    text_Name = pygame.image.load('name.png')
    text_Exit = pygame.image.load('exit.png')
    text_Play = pygame.image.load('play.png')
    

    pygame.mixer.music.load('bg.mp3')
    pygame.mixer.music.play(-1,0,5)

    screen.fill((0,0,0))
    bg = pygame.image.load('bg.jpg')
    bg_X = 0
    bg_Y = 0
    
    mouse_X = 0
    mouse_Y = 0

    run = True
    while run:
        fpss.tick(60)
        screen.blit(bg, (bg_X, bg_Y))
        screen.blit(text_Name,(180,200))
        screen.blit(text_Play,(300,280))
        screen.blit(text_Exit,(300,340))
        
        for event in pygame.event.get():
            if event.type == 256:
                pygame.display.quit()
                pygame.mixer.quit()
                pygame.font.quit()
                sys.exit()
            if event.type == 1025:
                mouse_X = event.pos[0]
                mouse_Y = event.pos[1]
                if mouse_X > 300 and mouse_X < 410 and mouse_Y > 280 and mouse_Y < 330:
                    return name
                if mouse_X > 300 and mouse_X < 410 and mouse_Y > 340 and mouse_Y < 390:
                    pygame.display.quit()
                    pygame.mixer.quit()
                    pygame.font.quit()
                    sys.exit()
            if event.type == 768:
                if ((event.key >= 97 and event.key <= 122) or (event.key >= 48 and event.key <= 57)) and len(name) < 8:
                        name += event.unicode
                if event.key == 8:
                    name = name[:-1]
            if event.type == 769:
                pass
        show_Name = font.render(str(name), True, (0, 0, 0))
        screen.blit(show_Name,(300,207))
        pygame.display.update()

# Bat dau choi
def main_Proces():
    name = get_Start()
    if name == '':
        name = 'Hieu'
    show_Name = font.render(name, True, (255, 255, 255))

    pygame.mixer.music.load('bgingame.mp3')
    pygame.mixer.music.play(-1)

    lose = pygame.mixer.Sound('lose.mp3')
    explosion = pygame.mixer.Sound('explosion.wav')
    bullet_Sound = pygame.mixer.Sound('bullet.wav')

    loss = pygame.image.load('loss.png')

    text_Replay = pygame.image.load('replay.png')
    text_Exit = pygame.image.load('exit.png')

    bg = pygame.image.load('bgingame.jpg')
    bg_X = 0
    bg_Y = 0

    bullet = pygame.image.load('bullet.png')
    bullet_X = 0
    bullet_Y = 512

    enemy = pygame.image.load('enemy.png')
    enemy_X = [10,100,210,310,410]
    enemy_Y = [1,1,1,1,1]
    enemy_Change_X = [5,5,5,5,5]
    bullet_State = True

    player = pygame.image.load('player.png')
    player_X = 320
    player_Y = 512
    player_Change = 0

    score = 0
    
    run = True

    while True:
        fpss.tick(60)
        screen.blit(bg, (bg_X, bg_Y))
        screen.blit(show_Name,(10,40))
        for event in pygame.event.get():
            if event.type == 256:
                pygame.display.quit()
                pygame.mixer.quit()
                pygame.font.quit()
                sys.exit()
            if event.type == 1025:
                mouse_X = event.pos[0]
                mouse_Y = event.pos[1]
                if mouse_X > 300 and mouse_X < 410 and mouse_Y > 380 and mouse_Y < 430:
                    if run == False:
                        run = True 
                        score = 0
                        pygame.mixer.music.play(-1)
                        run = True
                        player_X = 320
                        player_Y = 512
                        enemy_X = [10,100,210,310,410]
                        enemy_Y = [1,1,1,1,1]
                        enemy_Change_X = [5,5,5,5,5]
                if mouse_X > 300 and mouse_X < 410 and mouse_Y > 440 and mouse_Y < 590:
                    if run == False:
                        pygame.display.quit()
                        pygame.mixer.quit()
                        pygame.font.quit()
                        sys.exit()
            if event.type == 768 :
                if event.key == 1073741904:
                    player_Change = -5
                if event.key == 1073741903:
                    player_Change = 5
                if event.key == 32 and bullet_State:
                    bullet_Sound.play()
                    bullet_State = False
                    bullet_X = player_X
            if event.type == 769:
                if event.key == 1073741904 or event.key == 1073741903:
                    player_Change = 0
        player_X += player_Change
        if player_X <= 0:
            player_X = 0
        elif player_X >= 640:
            player_X = 640

        if bullet_State == False:
            screen.blit(bullet,(bullet_X,bullet_Y))
            bullet_Y -= 20
            if bullet_Y <= 10:
                bullet_State = True
                bullet_Y = 512
        if run:
            for i in range(5):
                enemy_X[i] += enemy_Change_X[i]
                if enemy_X[i] > 640:
                    enemy_Y[i] += 35
                    enemy_Change_X[i] = -enemy_Change_X[i]
                if enemy_X[i] < 0:
                    enemy_Y[i] += 35
                    enemy_Change_X[i] = -enemy_Change_X[i]
                if enemy_Y[i] >= 450:
                    run = False
                    pygame.mixer.music.pause()
                    lose.play()
                    
        if run:
            for i in range(5):   
                screen.blit(enemy,(enemy_X[i],enemy_Y[i]))
                screen.blit(player,(player_X,player_Y))
        else :
            screen.blit(loss,(0,0))
            screen.blit(text_Replay,(300,380))
            screen.blit(text_Exit,(300,440))
        for i in range(5):
            if check(enemy_X[i],enemy_Y[i],bullet_X,bullet_Y):
                explosion.play()
                bullet_State = True
                enemy_X[i] = 10
                enemy_Y[i] = 1
                enemy_Change_X[i] = 5
                bullet_Y = 512
                if score < 1000:
                    score += 1
        show_Score = font.render("Score : " + str(score), True, (255, 255, 255))
        screen.blit(show_Score, (10, 10))
        pygame.display.update()
if __name__ == "__main__":
    pygame.display.init()
    pygame.font.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((704,576))
    pygame.display.set_caption('Space Invanders')
    font = pygame.font.Font('freesansbold.ttf', 32)
    fpss = pygame.time.Clock()
    main_Proces()
