class Individual:
    def __init__(self) -> None:
        self.g = None
        self.x = None
        self.y = None
    def __str__(self) -> str:
        return f"G: {self.g}\nX: {self.x}\nY: {self.y}"