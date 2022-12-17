class Symbol:
    image = ""
    pos_x = 0
    pos_y = 0
    LINE_MAX = 2
    lines = []

    def __init__(self, x, y, image_path):
        self.pos_x = x
        self.pos_y = y
        self.image = image_path

    def add_line(self, line):
        if len(self.lines) < self.LINE_MAX:
            self.lines.append(line)
