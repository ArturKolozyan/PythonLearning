class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

    def get_length(self):
        length = self._x2 - self._x1
        return length

    def get_width(self):
        width = self._y1 - self._y2
        return width

    def get_area(self):
        area = self.get_length() * self.get_width()
        return area

    def get_perimeter(self):
        perimeter = 2 * (self.get_length() + self.get_width())
        return perimeter

    def is_square(self):
        if self.get_length() == self.get_width():
            return True
        return False