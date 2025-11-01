class Tetris_Rand:
    def __init__(self, mul, y, x):
        self.x_pos = x
        self.y_pos = y
        self.mul = mul
    
    def get_x(self):
        return self.x_pos
    
    def get_y(self):
        return self.y_pos
    
    def draw(self, stdscr_fn, symbol): # symbol = z.B. "=" oder "=\n"
        drawing = symbol * self.mul
        stdscr_fn(self.y_pos, self.x_pos, drawing)

class Boden(Tetris_Rand):
    def __init__(self, mul, y, x):
        super().__init__(mul, y, x)

    def check_ifCollide_Boden(self, y_pos_u : list):
        collide = False
        for i in y_pos_u:
            if i+1 == self.y_pos:
                collide = True
        return collide

class Wand(Tetris_Rand):
    def __init__(self, mul, y, x):
        super().__init__(mul, y, x)

    def check_ifCollide_Wand(self, x_pos_r_or_l : list):
        collide = False
        for i in x_pos_r_or_l:
            if i+1 == self.x_pos:
                collide = True
            if i-1 == self.x_pos:
                collide = True
        return collide
    
    def draw_Rechts(self, stdscr_fn, symbol):  # symbol = z.B.  "|"
        for i in range(self.mul):
            stdscr_fn(self.y_pos+i, self.x_pos, symbol)