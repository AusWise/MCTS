from src.exception import NoPointsError


class Resource:
    def __init__(self, value, min_value=0):
        self._value = value
        self._min_value = min_value
        self._max_value = value

    @property
    def value(self):
        return self._value

    def has_points_left(self):
        return self._value > self._min_value

    def subtract(self, points):
        self._value -= points
        if self._value < self._min_value:
            self._value = self._min_value
            raise NoPointsError
