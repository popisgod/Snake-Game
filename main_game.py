from pickle import NONE
import time
import arcade
import snake
import sys 
# Set how many rows and columns we will have
ROW_COUNT = 15
COLUMN_COUNT = 15

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 30
HEIGHT = 30

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 5

# Do the math to figure out our screen dimensions
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN
SCREEN_TITLE = "Array Backed Grid Example"


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height, title,snake,board):
        """
        Set up the application.
        """
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.snake = snake
        self.board = board
        self.board.add_apple(1)
        self.moving = 0
        super().__init__(width, height, title)
        self.on_draw()
        self.side = None        
        self.snake_move()
        # Create a 2 dimensional array. A two dimensional
        # array is simply a list of lists.
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        self.clear()

        # Draw the grid
        for row in range(len(self.board.board)):
            for column in range(len(self.board.board)):
                # Figure out what color to draw the box
                if self.board.board[row][column] == 0:
                    color = arcade.color.WHITE
                elif self.board.board[row][column] == 1:
                    color = arcade.color.RED
                elif self.board.board[row][column] == 2:
                    color = arcade.color.GREEN
                # Do the math to figure out where the box is
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP:
            self.up_pressed = True
            self.side = 'd'
        elif key == arcade.key.DOWN:
            self.down_pressed = True
            self.side = 'u'
        elif key == arcade.key.LEFT:
            self.left_pressed = True
            self.side = 'l'
        elif key == arcade.key.RIGHT:
            self.right_pressed = True
            self.side = 'r'


    def snake_move(self):
        while True:
            if self.side != None:
                try:
                    time.sleep(0.1)
                    self.snake.move(self.side)
                    self.on_draw()               
                except: 
                    arcade.finish_render



def main():
    test_board : snake.snake_board = snake.snake_board(15)
    snake_test : snake.snake = snake.snake(test_board)
    print('hello')
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE,snake_test,test_board)
    arcade.run()
    
if __name__ == '__main__':
    main()


