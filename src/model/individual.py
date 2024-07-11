class Individual:
    def __init__(self) -> None:
        self.g = None # g is the chromosome value
        self.x = None # x is the solution that derived from g using gpm function
        self.y = None # y is the fitness value
    def __str__(self) -> str:
        return f"G: {self.g}\nX: {self.x}\nY: {self.y}"