from game.exception import NoPointsError


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

    def _subtract(self, points):
        self._value -= points
        if self._value < self._min_value:
            self._value = 0
            raise NoPointsError


class HP(Resource):
    def subtract(self, points):
        super(HP, self)._subtract(points=points)


class Mana(Resource):
    def subtract(self, points):
        try:
            super(Mana, self)._subtract(points=points)
        except NoPointsError:
            pass

    def restore(self):
        self._value = self._max_value
