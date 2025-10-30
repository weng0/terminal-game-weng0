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

    # Kollidieren: Bitte ausbessern
    def check_ifCollide_Boden(self, fn_obj_unten): # fn_obj2_pos = z.B. Wand
        collide = False
        if fn_obj_unten+1 == self.y_pos:
            collide = True
        return collide

class Wand(Tetris_Rand):
    def __init__(self, mul, y, x):
        super().__init__(mul, y, x)

    def check_ifCollide_Wand(self, fn_obj_seite):
        collide = False
        # R / L
        # Welche Seiten
        if fn_obj_seite+1 == self.x_pos:
            collide = True
        if fn_obj_seite-1 == self.x_pos:
            collide = True
        return collide
    
    def draw_Rechts(self, stdscr_fn, symbol):  # symbol = z.B.  "|"
        for i in range(self.mul):
            stdscr_fn(self.y_pos+i, self.x_pos, symbol)