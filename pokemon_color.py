class Color:
    def __init__(self, red: int, green: int, blue: int) -> None:
        self.red = red
        self.green = green
        self.blue = blue

    def __repr__(self):
        END = '\033[0'
        START = '\033[1;38;2'
        MOD = 'm'
        return f'{START};{self.red};{self.green};{self.blue}{MOD}●{END}{MOD}'

    def __eq__(self, other):
        return self.red == other.red\
                and self.green == other.green\
                and self.blue == other.blue

    def __hash__(self) -> int:
        return hash((self.red, self.green, self.blue))

    def __add__(self, other):
        temp = Color(0, 0, 0)
        temp.red = min(self.red + other.red, 255)
        temp.blue = min(self.green + other.green, 255)
        temp.green == min(self.blue + other.blue, 255)
        return temp

    @staticmethod
    def brightness(color, c):
        cl = - 256 * (1 - c)
        f = (259 * (cl + 255)) / (255 * (259 - cl))
        lr = int(f * ((color) - 128) + 128)
        return lr

    def __mul__(self, c: float):
        return Color(Color.brightness(self.red, c),
                     Color.brightness(self.blue, c),
                     Color.brightness(self.green, c))

    __rmul__ = __mul__


orange1 = Color(255, 165, 0)
red = Color(255, 0, 0)
green = Color(0, 255, 0)
orange2 = Color(255, 165, 0)
color_list = [orange1, red, green, orange2]
print(red)
print(0.1 * red)
