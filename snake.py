import random


'''''
0 stands for empty
2 stands for apple
1 stands for snake
'''''''''
class snake_board:
    def __init__(self, size,apples_amount = 0) -> None:
        self.size : str = f'{size}x{size}'
        self.size_int : int = size
        self.board : list = [[0 for i in range(size)] for j in range(size)]
        self.apple : list = []
        self.add_apple(apples_amount)
        

    def __repr__(self) -> str:
        return_string = ''
        for i in self.board:
            for j in i:
                return_string += ' '+ str(j)
            return_string += '\n'
        return return_string

    def add_apple(self,amount : int):
        list1 = []
        for i in range(amount):
            
            temp = self.__add_apple()
            self.apple.append(temp)
            list1.append(temp)
        return list1

    def __add_apple(self) -> int:
        location_row : int = random.choice(self.board)
        index = random.randint(0, len(location_row)-1)
        if location_row[index] != 0:
            self.__add_apple()
            return
        location_row[index] = 1
        return (location_row , index)

class snake:
    def __init__(self, board : snake_board) -> None:
        self.locations = []  
        self.board = board
        start = self.start_location()
        self.locations.append(start)    
        self.dir = 'left'
        self.place()

    def start_location(self):
        row = random.randint(0, len(self.board.board)-1)
        index = random.randint(0, len(self.board.board)-1)
        if self.board.board[row][index] == 2:
            self.start_location()
            return
        return (row,index)

    def move(self,side):
        new_location = []
        if side == 'u':
            move = self.locations[0]
            if move[0]-1 < 0:
                raise Exception('you lost')
            if (move[0]-1,move[1]) in self.locations:
                raise Exception('poop')

            if self.board.board[move[0]-1][move[1]] == 1:
                print('eat')

                #apple
                new_location.append((move[0]-1,move[1]))
                for place in range(len(self.locations)):
                    new_location.append(self.locations[place])
                self.locations = new_location
                self.board.add_apple(1)    

            else:
                new_location.append((move[0]-1,move[1]))
                for place in range(len(self.locations)-1):
                    new_location.append(self.locations[place])
                self.locations = new_location


        elif side == 'r':
            move = self.locations[0]
            if move[1]+1 > len(self.board.board):
                raise Exception('you lost')
            if (move[0],move[1]+1) in self.locations:
                raise Exception('poop')

            if self.board.board[move[0]][move[1]+1] == 1:
                print('eat')

                new_location.append((move[0],move[1]+1))
                for place in range(len(self.locations)):
                    new_location.append(self.locations[place])
                self.locations = new_location
                self.board.add_apple(1)    

            else:
                new_location.append((move[0],move[1]+1))
                for place in range(len(self.locations)-1):
                    new_location.append(self.locations[place])
                self.locations = new_location

        elif side == 'l':
            move = self.locations[0]
            if move[1]-1 < 0:
                raise Exception('you lost')
            if (move[0],move[1]-1) in self.locations:
                raise Exception('poop')

            if self.board.board[move[0]][move[1]-1] == 1:
                print('eat')

                new_location.append((move[0],move[1]-1))
                for place in range(len(self.locations)):
                    new_location.append(self.locations[place])
                self.locations = new_location
                self.board.add_apple(1)     
            else:
                new_location.append((move[0],move[1]-1))
                for place in range(len(self.locations)-1):
                    new_location.append(self.locations[place])
                self.locations = new_location

        elif side == 'd': # side is bottom.
            move = self.locations[0]
            if move[0]+1 > len(self.board.board):
                raise Exception('you lost')
            if (move[0]+1,move[1]) in self.locations:
                raise Exception('poop')

            if self.board.board[move[0]+1][move[1]] == 1:
                print('eat')
                new_location.append((move[0]+1,move[1]))
                for place in range(len(self.locations)):
                    new_location.append(self.locations[place])
                self.locations = new_location      
                self.board.add_apple(1)          
            else:
                new_location.append((move[0]+1,move[1]))
                for place in range(len(self.locations)-1):
                    new_location.append(self.locations[place])
                self.locations = new_location
        self.place()

    def place(self):
        for row in range(len(self.board.board)):
            for index in range(len(self.board.board)):
                if self.board.board[row][index] == 2:
                    self.board.board[row][index] = 0
        for i in self.locations:
            self.board.board[i[0]][i[1]] = 2



    # allowed_inputs = ['d','u','r','l']
    # test_board : snake.snake_board = snake.snake_board(14)
    # snake_test : snake.snake = snake.snake(test_board)
    # test_board.add_apple(1)
    # print(test_board)
    # while True: # snake game  
    #     try:
    #         move_input = input('enter the side to move to... ')
    #         if move_input == 'quit': break
    #         if move_input not in allowed_inputs:
    #             print('bad input')
    #         snake_test.move(move_input)
    #         print(test_board)
    #     except:
    #         print('you have lost')
    #         break        

