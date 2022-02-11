from cgi import test
import time
from turtle import right
import arcade
import snake
import pyautogui        
# Set how many rows and columns we will have
ROW_COUNT = 14
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
print(SCREEN_HEIGHT, SCREEN_WIDTH)

class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title,snake,board) -> None:
        """
        Set up the application.
        """
        self.start = False
        self.scores = []
        self.total = time.time
        self.start_time = time.time()
        self.snake = snake
        self.board = board
        super().__init__(width, height, title)
        self.side = 'r'        
        self.flag_stop = False
        arcade.set_background_color(arcade.color.BLACK)
        
    def on_draw(self):
        """
        Render the screen.
        """
        self.clear()
        if self.start:
            self.clear()
            if time.time()-self.start_time > 0.1:
                self.snake_move()
                self.start_time = time.time()
        # This command has to happen before we start drawing
        if self.flag_stop:
            arcade.draw_text("YOU LOST",50.0,375.0,
                         arcade.color.WHITE,60,140,'left') 
            arcade.draw_text(f"YOUR SCORE IS {len(self.snake.locations)-1} ",125.0,325.0,
                         arcade.color.WHITE,20,40,'left')   
            self.scores.append(len(self.snake.locations)-1)
            arcade.draw_text(f"YOUR BEST SCORE IS {max(self.scores)} ",90.0,285.0,
                         arcade.color.WHITE,20,40,'left')               
            arcade.draw_rectangle_filled(245, 180, 200, 50, arcade.color.RED)
            arcade.draw_text('RESTART',185.0,170.0,
                         arcade.color.WHITE,20,20,'left') 
            arcade.draw_rectangle_filled(245, 120, 200, 50, arcade.color.RED)
            arcade.draw_text('MAIN MENU',170.0,110.0,
                         arcade.color.WHITE,20,20,'left') 
            
        if not self.flag_stop:
            for row in range(len(self.board.board)):
                for column in range(len(self.board.board)):
                    # Figure out what color to draw the box
                    # if self.board.board[row][column] == 0:
                    #     color = arcade.color.BROWN
                    color = None
                    if self.board.board[row][column] == 1:
                        color = arcade.color.RED
                    if self.board.board[row][column] == 2:
                        color = arcade.color.GREEN
                    if self.board.board[row][column] == 3:
                        color = arcade.color.PURPLE
                    # Do the math to figure out where the box is
                    x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                    y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2
                    if color != None:
                        arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

    def on_key_press(self, key, modifiers):         
        if not self.flag_stop:
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
                    self.rest()
            

    def rest(self):
        self.clear()
        self.flag_stop = True
        
    def on_mouse_press(self, x, y, button, modifiers):
        print(x,y)        
        # box is 344 205, 145 157

        

        if x > 145 and x < 344 and y > 157 and y < 205:
            self.restart()
 
    def restart(self):
        if self.flag_stop:
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
            self.flag_stop = False
            self.start = False
            self.side = 'r'

def main():
    test_board : snake.snake_board = snake.snake_board(14)
    snake_test : snake.snake = snake.snake(test_board)
    test_board.reset_board()
    snake_test.locations.pop()
    snake_test.locations.append((7,5))
    snake_test.locations.append((7,4))
    snake_test.locations.append((7,3))
    snake_test.locations.append((7,2))
    test_board.board[7][10] = 1
    snake_test.place()
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, 'snake_game',snake_test,test_board)
    arcade.run()
    
if __name__ == '__main__':
    main()


