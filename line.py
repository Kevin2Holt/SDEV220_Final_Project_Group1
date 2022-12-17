class Line:
    start_x = 0
    start_y = 0
    turn_x = -1
    turn_y = -1
    end_x = 0
    end_y = 0
    does_turn = False

    def __init__(self, x1, y1, x2, y2, x3=-1, y3=-1):
        self.start_x = x1
        self.start_y = y1
        self.end_x = x2
        self.end_y = y2
        self.turn_x = x3
        self.turn_y = y3
        if (x3 >= 0) and (y3 >= 0):
            self.does_turn = True

    def has_turn(self):
        return self.does_turn
