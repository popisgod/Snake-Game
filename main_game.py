from ast import Return
from cgi import test
import time
from tkinter.tix import Tree
from turtle import right, width
import arcade
import snake
import pyautogui        
# Set how many rows and columns we will have
ROW_COUNT = 16
COLUMN_COUNT = 14

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 30
HEIGHT = 30

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 5

# Do the math to figure out our screen dimensions
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN


def point_in(center,size,point): # first arg is the left bottom corner, second arg is the top right corner 
    last_point = (center[0]+size[0]/2,center[1]+size[1]/2)
    first_point = (center[0]- size[0]/2,center[1]-size[1]/2)
    if point[0] > first_point[0] and point[0] < last_point[0] and point[1] > first_point[1] and point[1] < last_point[1]:
        return Tree
    return False



class MyGame(arcade.Window):
    """
    Main application class.
    """
    difficulty_levels = {0 : 0.125 , 1 : 0.1 , 2 : 0.075 , 3 : 0.05}

    def __init__(self, width, height, title) -> None:
        """
        Set up the application.
        """
        super().__init__(width, height, title)
        #opens the main menu 
        self.menu()
        self.difficulty_level = 1
        self.button_size = (200,50)
        self.total = 0
    def menu(self):
        self.difficulty_page = False
        self.menu_open = True
        self.start = False
        self.scores = [0]
        self.start_time = time.time()     
        arcade.set_background_color(arcade.color.BLACK)
        self.restart()
        self.start_timer = False

    def on_draw(self):
        """
        Render the screen.
        """
        if not self.start_timer and self.start:
            self.total = time.time()
            self.start_timer = True

        self.clear()
        if self.start:
            self.clear()
            if time.time()-self.start_time > self.difficulty_levels[self.difficulty_level] :
                self.snake_move()
                self.start_time = time.time()
        # This command has to happen before we start drawing

        # gui for lost page
        if self.lost_screen:
            
            arcade.draw_text("YOU LOST",50.0,375.0,
                         arcade.color.WHITE,60,140,'left') 
            arcade.draw_text(f"YOUR SCORE IS {len(self.snake.locations)-4} ",125.0,325.0,
                         arcade.color.WHITE,20,40,'left')   
            self.scores.append(len(self.snake.locations)-4)
            arcade.draw_text(f"YOUR BEST SCORE IS {max(self.scores)} ",90.0,285.0,
                         arcade.color.WHITE,20,40,'left')               
            arcade.draw_rectangle_filled(245, 180, 200, 50, arcade.color.RED)
            arcade.draw_text('RESTART',185.0,170.0,
                         arcade.color.WHITE,20,20,'left') 
            arcade.draw_rectangle_filled(245, 120, 200, 50, arcade.color.RED)
            arcade.draw_text('MAIN MENU',170.0,110.0,
                         arcade.color.WHITE,20,20,'left') 
        
        # gui for the game page
        if not self.lost_screen and not self.menu_open and not self.difficulty_page:
            flag = False
            # draws the board
            for row in range(ROW_COUNT):
                flag = not flag
                if row == 15 or row == 14: continue
                for column in range(COLUMN_COUNT):
                    color = None
                    if color == None:
                            if flag:
                                color = arcade.color.AO
                            if not flag:
                                color = arcade.color.APPLE_GREEN
                            flag = not flag
                    # Do the math to figure out where the box is
                    x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                    y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2
                    if color != None:
                        arcade.draw_rectangle_filled( x,y, WIDTH+5, HEIGHT+5, color)
            # drawing the snake and the apple 
            for row in range(ROW_COUNT):  
                if row == 15 or row == 14: continue
                for column in range(COLUMN_COUNT):
                    color = None
                    if color == None:
                        if self.board.board[row][column] == 1:
                            x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                            y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2
                            arcade.draw_circle_filled( x,y, 15, arcade.color.RED)
                            arcade.draw_rectangle_filled(x,y+15,3,7,arcade.color.BLACK)
                        if self.board.board[row][column] == 2:
                            color = arcade.color.SEAL_BROWN	
                        if self.board.board[row][column] == 3:
                            color = arcade.color.PURPLE
                    # Do the math to figure out where the box is
                    x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                    y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2
                    if color != None:
                        arcade.draw_rectangle_filled( x,y, 35,35, color)
            arcade.draw_rectangle_filled(495/2,495,495,3,arcade.color.GREEN)
            arcade.draw_rectangle_filled(324,(565-495)/2+495,4,565-500,arcade.color.GREEN) 
            arcade.draw_rectangle_filled(136,(565-495)/2+495,4,565-500,arcade.color.GREEN)  
            arcade.draw_text(f'score : {len(self.snake.locations)-4}',15.0,510.0,
                         arcade.color.WHITE,17,20,'left') 
            arcade.draw_text(f'best score : {max(self.scores)}',150.0,510.0,
                         arcade.color.WHITE,17,20,'left') 
            
            temp = float((int((time.time()-self.total)*1000)))/1000
            if self.total == 0: temp = 0
            arcade.draw_text(f'timer : {temp}',335.0,510.0,
                         arcade.color.WHITE,17,20,'left') 
        # gui for menu page
        if self.menu_open:
            arcade.draw_rectangle_filled(250, 300, 225, 400, arcade.color.RED)
            arcade.draw_text("SNAKE",160.0,450.0,
                         arcade.color.WHITE,40,140,'left') 
            arcade.draw_text("THE GAME",180.0,410.0,
                         arcade.color.WHITE,20,140,'left') 

            buttons = ['START','DIFFICULTY','MODES','CREDITS']
            y_start = 370
            for button in buttons:
                arcade.draw_rectangle_filled(250, y_start, self.button_size[0], self.button_size[1], arcade.color.BLUE)
                if len(button) > 7:
                      arcade.draw_text(button,175.0,y_start-10, arcade.color.WHITE,20,20,'left')
                      y_start -= 70
                      continue
                arcade.draw_text(button,205.0,y_start-10, arcade.color.WHITE,20,20,'left')
                y_start -= 70
        
        # gui for difficulty page
        if self.difficulty_page:
            arcade.draw_rectangle_filled(250, 300, 225, 400, arcade.color.RED)
            arcade.draw_text("DIFFICULTIES",150.0,430.0,
                         arcade.color.WHITE,22,200,'left')
            buttons = ['EASY','MEDIUM','HARD','DIE!']
            y_start = 370
            for button in buttons:
                arcade.draw_rectangle_filled(250, y_start, self.button_size[0], self.button_size[1], arcade.color.BLUE)
                if len(button) > 7:
                      arcade.draw_text(button,185.0,y_start-10, arcade.color.WHITE,20,20,'left')
                      y_start -= 70
                      continue
                arcade.draw_text(button,205.0,y_start-10, arcade.color.WHITE,20,20,'left')
                y_start -= 70           
  




    def on_key_press(self, key, modifiers):         
        if not self.menu_open:    
            if not self.lost_screen:
                if key == arcade.key.UP:
                    if self.side == 'u' and len(self.snake.locations) > 1:
                        return
                    self.side = 'd'
                    self.start = True
                if  key == arcade.key.DOWN:
                    if  self.side == 'd' and len(self.snake.locations) > 1:
                        return
                    self.side = 'u'
                    self.start = True
                if key == arcade.key.LEFT:
                    if self.side == 'r' and len(self.snake.locations) > 1:
                        return
                    self.side = 'l'   
                    self.start = True
                if key == arcade.key.RIGHT:
                    if  self.side == 'l' and len(self.snake.locations) > 1:
                        return
                    self.side = 'r'
                    self.start = True

    def snake_move(self):
            if self.side != None:
                try:
                    self.snake.move(self.side)
                except: 
                    self.lost()
            
    def lost(self):
        self.clear()
        self.lost_screen = True
        
    def on_mouse_press(self, x, y, button, modifiers):
        print(x,y)    
        # main menu buttons 
        if self.menu_open:  
            if point_in((250,370),self.button_size,(x,y)): #   main menu start button(restarts)
                self.menu_open = False
                return
            if point_in((250,300),self.button_size,(x,y)): # main menu difficulty options caller
                self.difficulty()
                return
        # difficulty page options 
        if self.difficulty_page:
            if point_in((250,370),self.button_size,(x,y)): # easy difficulty 
                self.difficulty_level = 0 
                self.menu()
                return
            if point_in((250,300),self.button_size,(x,y)):  # normal difficulty 
                self.difficulty_level = 1
                self.menu()
                return
            if point_in((250,230),self.button_size,(x,y)):  # Hard difficulty 
                self.difficulty_level = 2  
                self.menu()
                return
            if point_in((250,160),self.button_size,(x,y)):  # die difficulty 
                self.difficulty_level = 3  
                self.menu()  
                return           

        # lost screen buttons, after dying 
        if self.lost_screen:  
            if point_in((245,180),self.button_size,(x,y)): # restart button 
                self.restart()
                return
            if point_in((245,120),self.button_size,(x,y)):  # main menu button 
                self.menu()
                return


    def difficulty(self):
        self.difficulty_page = True
        self.menu_open = False

    def restart(self):
        snake_board = snake.snake_board(14)
        snake_test = snake.snake(snake_board)
        snake_board.reset_board()
        snake_test.locations.pop()
        for i in range(2,6):
            snake_test.locations.append((7,7-i))
        snake_board.board[7][10] = 1   
        snake_test.place()
        self.board = snake_board
        self.snake = snake_test 
        self.lost_screen = False
        self.start = False
        self.side = 'r'
        self.start_timer = False
        self.total = 0


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, 'snake_game')
    arcade.run()
    
if __name__ == '__main__':
    main()


