import pygame


pygame.init() #초기화

#게임 화면 크기
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기

screen = pygame.display.set_mode((screen_width,screen_height))


#화면 타이틀 설정
pygame.display.set_caption("nojam-game") #게임 이름

# 이벤트 루프
running = True #게임이 진행중인가

while running:
    for event in pygame.event.get(): #이벤트가 발생했는지 확인
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생했다면
            running = False #게임이 진행중인가 확인하는 변수에 False값을 넣는다

#게임 종료
pygame.quit()

