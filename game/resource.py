from game.exception import NoPointsError


# class Resource:
#     def __init__(self, value, min_value=0):
#         self._value = value
#         self._min_value = min_value
#         self._max_value = value
#
#     @property
#     def value(self):
#         return self._value
#
#     def has_points_left(self):
#         return self._value > self._min_value
#
#     def _subtract(self, points):
#         self._value -= points
#         if self._value < self._min_value:
#             self._value = 0
#             raise NoPointsError
#
#     def __str__(self):
#         return str(self.value)
#
# class HP(Resource):
#     def subtract(self, points):
#         super(HP, self)._subtract(points=points)
#
#
# class Mana(Resource):
#     def subtract(self, points):
#         try:
#             super(Mana, self)._subtract(points=points)
#         except NoPointsError:
#             pass
#
#     def restore(self):
#         self._value = self._max_value

class Resource:
    def __init__(self, value, min, max):
        self.value = value
        self.min = min
        self.max = max

class HP(Resource):
    def __init__(self, value):
        super(HP, self).__init__(self, value, min=1, max=10)
        self.value = max([value, self.max])

class Mana(Resource):
    def __init__(self, value):
        super(Mana, self).__init__(self, value, min=0, max=20)