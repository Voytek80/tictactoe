import random


class Mouse_position:
    def __init__(self):
        self.position = (0,0)
        self.square = [0] * 9       # list of all the squares in the game





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

        print(self.valid_move)

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
        print(self.square)

