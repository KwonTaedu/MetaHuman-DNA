class LinearUnit:
    cm = 0
    m = 1

class AngleUnit:
    degree = 0
    radian = 1


class Unit:
    def __init__(self,linear_unit=None,angle_unit=None):
        self.linear_unit = linear_unit
        self.angle_unit = angle_unit