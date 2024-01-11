import time 
from pygame import* 
import os 
import sys 
import random 
 
init() 
square_size=40 
square_amount=15 
game_height=600 
game_width=600 
score=0 
screen=display.set_mode((square_size*square_amount,square_size*square_amount)) 
 
image_pos1=(game_width//9,game_height//1.3) 
image_pos2=(game_width//1.3,game_height//1.9) 
image_pos3=(game_width//7,game_height//1.9) 
image_pos4=(game_width//1.2,game_height//1.3) 
font_path=r"joystix monospace.otf" 
track=r"soundtrack.mp3"
crunch=mixer.Sound(r"crunch sound.mp3")
crash=mixer.Sound(r"crash.mp3")
mixer.music.load(track)
mixer.music.play(-1)
font_size1=80 
font_size2=30 
font1=font.Font(font_path,font_size1) 
font2=font.Font(font_path,font_size2) 
 
class APPLE: 
    def __init__(self): 
        self.x=random.randint(4,12) 
        self.y=random.randint(4,12) 
        self.pos= math.Vector2(self.x,self.y) 
 
    def draw_apple(self): 
        apple=Rect(self.pos.x*square_size,self.pos.y*square_size,square_size,square_size) 
        draw.rect(screen,(207,5,6),apple) 
        if self.pos==G.snake.snake[:]:
            self.x==random.randint(4,12)
            self.y==random.randint(4,12)

 
    def new_apple(self): 
        self.x  = random.randint(1, 15) 
        self.y = random.randint(1, 15) 
        self.pos = math.Vector2(self.x, self.y) 
        if self.pos==G.snake.snake[:]:
            self.x==random.randint(1,15)
            self.y==random.randint(1,15)
 
class SNAKE: 
    def __init__(self): 
        self.snake=[math.Vector2(5,5),math.Vector2(4,5),math.Vector2(3,5)] 
        self.D= math.Vector2(0,0) 
        self.growth=False 
        self.score=0 
    def draw_snake(self): 
        for square in self.snake: 
            a=square.x*square_size 
            b=square.y*square_size 
            snake= Rect(a,b,square_size,square_size) 
            draw.rect(screen,(40, 33,240),snake) 
    def snake_movement(self): 
        if self.growth== True: 
            snake2 = self.snake[:] 
            snake2.insert(0, snake2[0] + self.D) 
            self.snake = snake2[:] 
            self.growth = False 
            self.score+=1 
 
        if self.growth==False: 
            snake2 = self.snake[:-1] 
            snake2.insert(0, snake2[0] + self.D) 
            self.snake = snake2[:] 
 
    def grow(self): 
        self.growth=True 
 
class GAME: 
    def __init__(self): 
        self.snake=SNAKE() 
        self.apple=APPLE() 
 
    def draw(self): 
        self.snake.draw_snake() 
        self.apple.draw_apple() 
        self.draw_score() 
    def game(self): 
        self.snake.snake_movement() 
        self.apple_collision() 
        self.wall_collision() 
 
 
 
 
 
    def main_menu(self): 
        while True: 
            for e in event.get(): 
                if e.type == QUIT: 
                    quit() 
            screen.fill((8, 117, 2)) 
            display.set_caption("Menu") 
            text = font1.render("Snake", True, (255, 255, 255)) 
            text_rect = text.get_rect(center=(game_width // 2, game_height // 4)) 
            screen.blit(text, text_rect) 
            
            text2 = font2.render("press Space to start", True, (255, 255, 255)) 
            text2_rect = text2.get_rect(center=(game_width // 2, game_height // 2)) 
            screen.blit(text2, text2_rect) 
            text3 = font2.render("press Backspace to quit", True, (255, 255, 255)) 
            text3_rect = text3.get_rect(center=(game_width // 2, game_height // 1.5)) 
            screen.blit(text3, text3_rect) 
            display.update() 
 
            K = key.get_pressed() 
            if K[K_BACKSPACE]: 
                quit() 
            if K[K_SPACE]: 
                self.play_game() 
 
    def play_game(self): 
        M=USEREVENT 
        time.set_timer(M,600) 
 
        while True: 
            for e in event.get(): 
                if e.type == QUIT: 
                    quit() 
                    exit() 
                if e.type == M: 
                    G.game() 
                if e.type == KEYDOWN: 
                    if e.key == K_LEFT: 
                        G.snake.D = math.Vector2(-1, 0) 
                    if e.key == K_RIGHT: 
                        G.snake.D = math.Vector2(1, 0) 
                    if e.key == K_DOWN: 
                        G.snake.D = math.Vector2(0, 1) 
                    if e.key == K_UP: 
                        G.snake.D = math.Vector2(0, -1) 
            screen.fill((8, 117, 2)) 
            display.set_caption("Snake") 
            G.draw() 
            G.game() 
            display.update() 
            time.Clock().tick(10) 
 
 
    def game_over(self): 
        while True: 
            for e in event.get(): 
                if e.type == QUIT: 
                    quit() 
                screen.fill((8, 117, 2)) 
                display.set_caption("Game Over") 
                text1 = font1.render("Game Over", True, (255, 255, 255)) 
                text1_rect = text1.get_rect(center=(game_width // 2, game_height // 4)) 
                screen.blit(text1, text1_rect) 
                text2 = font2.render(f"Score: {self.snake.score}", True, (255, 255, 255)) 
                text2_rect = text2.get_rect(center=(game_width // 2, game_height // 2)) 
                screen.blit(text2, text2_rect) 
                text3 = font2.render("Press Escape to close",True,(255,255,255)) 
                text3_rect = text3.get_rect(center=(game_width // 2, game_height // 1.5)) 
                screen.blit(text3, text3_rect) 
                if e.type == KEYDOWN: 
                    if e.key == K_ESCAPE: 
                        exit() 
                display.update() 
 

    def apple_collision(self): 
        if self.apple.pos.x==self.snake.snake[0].x and self.apple.pos.y==self.snake.snake[0].y: 
            self.snake.grow() 
            self.apple.new_apple() 
            mixer.Sound.play(crunch) 
    
 
    def wall_collision(self): 
        if self.snake.snake[0].x==math.Vector2(-1).x or self.snake.snake[0].x==math.Vector2(16).x:
              mixer.Sound.play(crash)
              mixer.music.stop() 
              self.game_over() 
        if self.snake.snake[0].y==math.Vector2(-1).y or self.snake.snake[0].y==math.Vector2(16).y: 
              mixer.Sound.play(crash)
              mixer.music.stop()
              self.game_over() 
 
 
    def snake_collision(self): 
        for square in self.snake.snake[1:]: 
            if square==self.snake.snake[0]: 
                quit() 
 
    def draw_score(self): 
        score_text = font2.render(f"Score: {self.snake.score}", True, (255, 255, 255)) 
        screen.blit(score_text, (10, 10)) 
 
G=GAME() 
 

G.main_menu() 
 