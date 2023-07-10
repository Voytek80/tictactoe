class Mouse_position:
    def __init__(self):
        self.position = (0,0)


    def squares(self):
        self.x, self.y = self.position
        if (self.x < 200 and self.y < 200):
            return "1"
        elif (self.x < 400 and self.y < 200):
            return "2"
        elif (self.x < 600 and self.y < 200):
            return "3"
        elif (self.x < 200 and self.y < 400):
            return "4"
        elif (self.x < 400 and self.y < 400):
            return "5"
        elif (self.x < 600 and self.y < 400):
            return "6"
        elif (self.x < 200 and self.y < 600):
            return "7"
        elif (self.x < 400 and self.y < 600):
            return "8"
        elif (self.x < 600 and self.y < 600):
            return "9"