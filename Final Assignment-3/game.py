#   Author: Catherine Leung
#   This is the game that you will code the bots to play.  You can also play against your bot
#   To run the game you will need pygames installed.  See: https://pypi.org/project/pygame/
#   Once you have pygames, you can run the game by using the command:
#   python game.py
#   
#   the gem images used are from opengameart.org by qubodup
#   https://opengameart.org/content/rotating-crystal-animation-8-step,
#   https://creativecommons.org/licenses/by/3.0/


# Edits Made : Added Resetting the game functionality.
import pygame
import sys
import math

from a1_partd import overflow
from a1_partc import Queue
from player1 import PlayerOne
from player2 import PlayerTwo

class Dropdown:
    def __init__(self, x, y, width, height, options):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.options = options
        self.current_option = 0

    def draw(self, window):
        pygame.draw.rect(window, BLACK, (self.x, self.y, self.width, self.height), 2)
        font = pygame.font.Font(None, 36)
        text = font.render(self.options[self.current_option], 1, BLACK)
        window.blit(text, (self.x + 5, self.y + 5))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if self.x < x < self.x + self.width and self.y < y < self.y + self.height:
                self.current_option = (self.current_option + 1) % len(self.options)

    def get_choice(self):
        return self.current_option

class Board:
    def __init__(self,width,height, p1_sprites, p2_sprites):
        self.width = width
        self.height = height
        self.board = [[0 for _ in range(width)] for _ in range(height)]
        self.p1_sprites = p1_sprites
        self.p2_sprites = p2_sprites
        self.board[0][0] = 1
        self.board[self.height-1][self.width-1] = -1
        self.turn = 0

    def get_board(self):
        current_board = []
        for i in range(self.height):
            current_board.append(self.board[i].copy())
        return current_board

    def valid_move(self, row,col,player):
        if row >= 0  and row < self.height and col >= 0 and col < self.width and (self.board[row][col]==0 or self.board[row][col]/abs(self.board[row][col]) == player):
            return True
        return False

    def add_piece(self, row, col, player):
        if self.valid_move(row, col, player):
            self.board[row][col] += player
            self.turn += 1
            return True
        return False

    def check_win(self):
        if(self.turn > 0):
            num_p1 = 0
            num_p2 = 0
            for i in range(self.height):
                for j in range(self.width):
                    if(self.board[i][j] > 0):
                        if num_p2 > 0:
                            return 0
                        num_p1 += 1
                    elif(self.board[i][j] < 0):
                        if num_p1 > 0:
                            return 0
                        num_p2 += 1
            if(num_p1 == 0):
                return -1
            if(num_p2== 0):
                return 1
        return 0

    def do_overflow(self,q):
        oldboard = []
        for i in range(self.height):
            oldboard.append(self.board[i].copy())
        numsteps = overflow(self.board, q)
        if(numsteps != 0):
            self.set(oldboard)
        return numsteps
    
    def set(self, newboard):
        for row in range(self.height):
            for col in range(self.width):
                self.board[row][col] = newboard[row][col]

    def draw(self, window, frame):
        for row in range(GRID_SIZE[0]):
            for col in range(GRID_SIZE[1]):
                rect = pygame.Rect(col * CELL_SIZE + X_OFFSET, row * CELL_SIZE+Y_OFFSET, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(window, BLACK, rect, 1)
        for row in range(self.height):
            for col in range(self.width):
                if self.board[row][col] != 0:
                    rpos = row * CELL_SIZE + Y_OFFSET
                    cpos = col * CELL_SIZE + X_OFFSET
                    if self.board[row][col] > 0:
                        sprite = p1_sprites
                    else:
                        sprite = p2_sprites
                    if abs(self.board[row][col]) == 1:
                        cpos += CELL_SIZE //2 - 16
                        rpos += CELL_SIZE //2 - 16
                        window.blit(sprite[math.floor(frame)], (cpos, rpos))
                    elif abs(self.board[row][col]) == 2:
                        cpos += CELL_SIZE //2 - 32
                        rpos += CELL_SIZE //2 - 16
                        window.blit(sprite[math.floor(frame)], (cpos, rpos))
                        cpos += 32
                        window.blit(sprite[math.floor(frame)], (cpos, rpos))

                    elif abs(self.board[row][col]) == 3:
                        cpos += CELL_SIZE //2 - 16
                        rpos += 8
                        window.blit(sprite[math.floor(frame)], (cpos, rpos))
                        cpos = col * CELL_SIZE + X_OFFSET + CELL_SIZE //2 - 32
                        rpos += CELL_SIZE //2
                        window.blit(sprite[math.floor(frame)], (cpos, rpos))
                        cpos += 32
                        window.blit(sprite[math.floor(frame)], (cpos, rpos))
                    elif abs(self.board[row][col]) == 4:
                        cpos += CELL_SIZE //2 - 32
                        rpos += 8
                        window.blit(sprite[math.floor(frame)], (cpos, rpos))
                        rpos += CELL_SIZE //2
                        window.blit(sprite[math.floor(frame)], (cpos, rpos))
                        cpos += 32
                        window.blit(sprite[math.floor(frame)], (cpos, rpos))
                        rpos -= CELL_SIZE //2
                        window.blit(sprite[math.floor(frame)], (cpos, rpos))



# Button Class
class Button:
    def __init__(self, x, y, width, height, text=''):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, window):
        pygame.draw.rect(window, (0, 0, 0), (self.x, self.y, self.width, self.height), 0)
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 30)
            text = font.render(self.text, 1, (255, 255, 255))
            window.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def is_over(self, pos):
        if self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height:
            return True
        return False

# Rest of your classes (Dropdown, Board, etc.) go here

# Constants
GRID_SIZE = (5, 6)
CELL_SIZE = 100
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
X_OFFSET = 0
Y_OFFSET = 100
FULL_DELAY = 5

# hate the colours?  there are other options.  Just change the lines below to another colour's file name.  
# the following are available blue, pink, yellow, orange, grey, green
p1spritesheet = pygame.image.load('blue.png')
p2spritesheet = pygame.image.load('pink.png')
p1_sprites = []
p2_sprites = []
player_id = [1 , -1]
for i in range(8):
    curr_sprite = pygame.Rect(32*i,0,32,32)
    p1_sprites.append(p1spritesheet.subsurface(curr_sprite))
    p2_sprites.append(p2spritesheet.subsurface(curr_sprite))    


frame = 0
# Initialize Pygame
pygame.init()
window = pygame.display.set_mode((1200,800))


pygame.font.init()
font = pygame.font.Font(None, 36)  # Change the size as needed
bigfont = pygame.font.Font(None, 108)
# Create the game board
# board = [[0 for _ in range(GRID_SIZE[0])] for _ in range(GRID_SIZE[1])]
player1_dropdown = Dropdown(900, 50, 200, 50, ['Human', 'AI'])
player2_dropdown = Dropdown(900, 110, 200, 50, ['Human', 'AI'])
restart_button = Button(900, 200, 200, 50, 'Restart')
status=["",""]
current_player = 0
board = Board(GRID_SIZE[1], GRID_SIZE[0], p1_sprites, p2_sprites)
# Game loop
running = True
overflow_boards = Queue()
overflowing = False
numsteps = 0
has_winner = False
bots = [PlayerOne(), PlayerTwo()]
grid_col = -1
grid_row = -1
choice = [None, None]
# Game Loop
running = True
while running:
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if restart_button.is_over(pos):
                # Reset game state
                current_player = 0
                board = Board(GRID_SIZE[1], GRID_SIZE[0], p1_sprites, p2_sprites)
                has_winner = False
                overflowing = False
                continue

        player1_dropdown.handle_event(event)
        player2_dropdown.handle_event(event)
        choice = [player1_dropdown.get_choice(), player2_dropdown.get_choice()]
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            row = y - Y_OFFSET
            col = x - X_OFFSET
            grid_row, grid_col = row // CELL_SIZE, col // CELL_SIZE

    win = board.check_win()
    if win != 0:
        winner = 1
        if win == -1:
            winner = 2
        has_winner = True

    if not has_winner:
        if overflowing:
            status[0] = "Overflowing"
            if not overflow_boards.is_empty():
                if repeat_step == FULL_DELAY:
                    next = overflow_boards.dequeue()
                    board.set(next)
                    repeat_step = 0
                else:
                    repeat_step += 1
            else:
                overflowing = False

                # goes between 0 and 1
                current_player = (current_player + 1) % 2

        else:
            status[0] = "Player " + str(current_player + 1) + "'s turn"
            make_move = False
            if choice[current_player] == 1:
                (grid_row,grid_col) = bots[current_player].get_play(board.get_board())
                status[1] = "Bot chose row {}, col {}".format(grid_row, grid_col)
                if not board.valid_move(grid_row, grid_col, player_id[current_player]):
                       has_winner = True
                       # if p1 makes an invalid move, p2 wins.  if p2 makes an invalid move p1 wins
                       winner = ((current_player + 1) % 2) + 1 
                else:
                    make_move = True
            else:
                if board.valid_move(grid_row, grid_col, player_id[current_player]):
                    make_move = True

            if make_move:
                board.add_piece(grid_row, grid_col, player_id[current_player])
                numsteps = board.do_overflow(overflow_boards)
                if numsteps != 0:
                    overflowing = True
                    repeat_step = 0
                else:
                    current_player = (current_player + 1) % 2
                grid_row = -1
                grid_col = -1   
            # Rest of your event handling code

    # Game logic goes here

    # Drawing the game
    window.fill(WHITE)
    board.draw(window, frame)
    player1_dropdown.draw(window)
    player2_dropdown.draw(window)
    restart_button.draw(window)   # Draw the restart button

    # Additional drawing code (for status, winner, etc.)

    pygame.display.update()
    pygame.time.delay(100)

pygame.quit()
sys.exit()
