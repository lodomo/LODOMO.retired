class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def Get_Vector2(data):
    return Vector2(data[0], data[1])
