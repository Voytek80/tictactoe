import random
import pygame


class Mouse_position:
    def __init__(self):
        self.position = (0,0)
        self.square = [0] * 9       # list of all the squares in the game
        self.positions_of_O = [(100, 100), (300, 100), (500, 100),
                               (100, 300), (300, 300), (500, 300),
                               (100, 500), (300, 500), (500, 500)]
        self.screen = pygame.display.set_mode((600, 600))
        self.valid_move = 0





    def squares(self):              # define which square was clicked
        self.x, self.y = self.position
        self.valid_move = 1
        if (self.x < 200 and self.y < 200):
            if self.square[0] == 0:
                self.square[0] = 1
            else:
                self.valid_move = 0
        elif (self.x < 400 and self.y < 200):
            if self.square[1] == 0:
                self.square[1] = 1
            else:
                self.valid_move = 0
        elif (self.x < 600 and self.y < 200):
            if self.square[2] == 0:
                self.square[2] = 1
            else:
                self.valid_move = 0
        elif (self.x < 200 and self.y < 400):
            if self.square[3] == 0:
                self.square[3] = 1
            else:
                self.valid_move = 0
        elif (self.x < 400 and self.y < 400):
            if self.square[4] == 0:
                self.square[4] = 1
            else:
                self.valid_move = 0
        elif (self.x < 600 and self.y < 400):
            if self.square[5] == 0:
                self.square[5] = 1
            else:
                self.valid_move = 0
        elif (self.x < 200 and self.y < 600):
            if self.square[6] == 0:
                self.square[6] = 1
            else:
                self.valid_move = 0
        elif (self.x < 400 and self.y < 600):
            if self.square[7] == 0:
                self.square[7] = 1
            else:
                self.valid_move = 0
        elif (self.x < 600 and self.y < 600):
            if self.square[8] == 0:
                self.square[8] = 1
            else:
                self.valid_move = 0



    def draw_x_coordinates(self, sq):
        if sq == 0:
            return (((20, 20), (180, 180)), ((180, 20), (20, 180)))
        if sq == 1:
            return (((220, 20), (380, 180)), ((380, 20), (220, 180)))
        if sq == 2:
            return (((420, 20), (580, 180)), ((580, 20), (420, 180)))
        if sq == 3:
            return (((20, 220), (180, 380)), ((180,220), (20, 380)))
        if sq == 4:
            return (((220, 220), (380, 380)), ((380, 220), (220, 380)))
        if sq == 5:
            return (((420, 220), (580, 380)), ((580, 220), (420, 380)))
        if sq == 6:
            return (((20, 420), (180, 580)), ((180, 420), (20, 580)))
        if sq == 7:
            return (((220, 420), (380, 580)), ((380, 420), (220, 580)))
        if sq == 8:
            return (((420, 420), (580, 580)), ((580, 420), (420, 580)))

    def computers_move(self):
        if_empty = 1
        random_computer_move = 0
        while if_empty != 0:
            random_computer_move = random.randrange(len(self.square))
            if_empty = self.square[random_computer_move]
        self.square[random_computer_move] = 2

    def check_if_win(self):
        if (self.square[0] == self.square[1] == self.square[2]) and self.square[0] != 0:
            pygame.draw.line(self.screen, "black", (100, 100), (500, 100), 10)
            self.end_game()
        elif self.square[3] == self.square[4] == self.square[5] and self.square[3] != 0:
            pygame.draw.line(self.screen, "black", (100, 300), (500, 200), 10)
            self.end_game()
        elif self.square[6] == self.square[7] == self.square[8] and self.square[6] != 0:
            pygame.draw.line(self.screen, "black", (100, 500), (500, 500), 10)
            self.end_game()
        elif self.square[0] == self.square[3] == self.square[6] and self.square[0] != 0:
            pygame.draw.line(self.screen, "black", (100, 100), (100, 500), 10)
            self.end_game()
        elif self.square[1] == self.square[4] == self.square[7] and self.square[1] != 0:
            pygame.draw.line(self.screen, "black", (300, 100), (300, 500), 10)
            self.end_game()
        elif self.square[2] == self.square[5] == self.square[8] and self.square[2] != 0:
            pygame.draw.line(self.screen, "black", (500, 100), (500, 500), 10)
            self.end_game()
        elif self.square[0] == self.square[4] == self.square[8] and self.square[0] != 0:
            pygame.draw.line(self.screen, "black", (100, 100), (500, 500), 10)
            self.end_game()
        elif self.square[2] == self.square[4] == self.square[6] and self.square[2] != 0:
            pygame.draw.line(self.screen, "black", (500, 100), (100, 500), 10)
            self.end_game()

    def end_game(self):
        pygame.display.flip()
        pygame.time.wait(3000)
        self.screen.fill("cyan")
        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        text_surface = my_font.render('Some Text', False, (0, 0, 0))
        self.screen.blit(text_surface, (0, 0))



    def draw_board(self):
        pygame.draw.line(self.screen, "black", (200, 0), (200, 600), 10)
        pygame.draw.line(self.screen, "black", (400, 0), (400, 600), 10)
        pygame.draw.line(self.screen, "black", (0, 200), (600, 200), 10)
        pygame.draw.line(self.screen, "black", (0, 400), (600, 400), 10)

    def drawXO(self):
        for i, j in enumerate(self.square):
            if j == 1:
                a1, a2 = self.draw_x_coordinates(i)
                b1, b2 = a1
                c1, c2 = a2
                pygame.draw.line(self.screen, "black", b1, b2, 10)
                pygame.draw.line(self.screen, "black", c1, c2, 10)
            elif j == 2:
                pygame.draw.circle(self.screen, "black", self.positions_of_O[i], 80, 10)




