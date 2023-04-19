import pygame

##############################################################################################초기설정
pygame.init() #초기화

#게임 화면 크기
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기

screen = pygame.display.set_mode((screen_width,screen_height))


#화면 타이틀 설정
pygame.display.set_caption("nojam-game") #게임 이름


#FPS
clock = pygame.time.Clock()
##############################################################################################


# 1 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등등)





# 이벤트 루프
running = True #게임이 진행중인가

while running:
    dt = clock.tick(60) #게임화면의 초당 프레임 수를 설정


    # 2 이벤트 처리 (키보드,마우스 등)
    
    # 3 게임 케릭터 위치 정의
    
    # 4 충돌처리
    
    # 5 화면 크리기




    
    pygame.display.update() #게임화면 다시 그리기!


#게임 종료
pygame.quit()

