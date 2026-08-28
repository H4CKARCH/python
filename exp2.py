import math


class Polygon:
    def __init__(self, side_lengths, number_of_sides):
        if len(side_lengths) != number_of_sides:
            raise ValueError(
                f"A {number_of_sides}-sided polygon must have "
                f"{number_of_sides} side lengths."
            )

        self._side_lengths = side_lengths
        self._perimeter = self.perimeter()
        self._area = self.area()

    def perimeter(self):
        return sum(self._side_lengths)

    def area(self):
        raise NotImplementedError("Area calculation not defined for Polygon")


class Triangle(Polygon):
    def __init__(self, side_lengths):
        super().__init__(side_lengths, 3)

    def perimeter(self):
        return sum(self._side_lengths)

    def area(self):
        # Heron's formula
        semiperimeter = self._perimeter / 2

        product = semiperimeter

        for side in self._side_lengths:
            product *= (semiperimeter - side)

        return math.sqrt(product)


class Quadrilateral(Polygon):
    def __init__(self, side_lengths):
        super().__init__(side_lengths, 4)

    def perimeter(self):
        return sum(self._side_lengths)

    def area(self):
        # Brahmagupta's formula
        semiperimeter = self._perimeter / 2

        return math.sqrt(
            (semiperimeter - self._side_lengths[0]) *
            (semiperimeter - self._side_lengths[1]) *
            (semiperimeter - self._side_lengths[2]) *
            (semiperimeter - self._side_lengths[3])
        )


class Pentagon(Polygon):
    def __init__(self, side_lengths):
        super().__init__(side_lengths, 5)

    def perimeter(self):
        return sum(self._side_lengths)

    def area(self):
        # Area of a regular pentagon
        a = self._side_lengths[0]

        return (
            math.sqrt(5 * (5 + 2 * math.sqrt(5))) * a * a
        ) / 4


# Object of Triangle
t1 = Triangle([2, 1, 3])
print("Triangle:")
print("Perimeter =", t1.perimeter())
print("Area =", t1.area())


# Object of Quadrilateral
q1 = Quadrilateral([2, 2, 2, 2])
print("\nQuadrilateral:")
print("Perimeter =", q1.perimeter())
print("Area =", q1.area())


# Object of Pentagon
p1 = Pentagon([3, 3, 3, 3, 3])
print("\nPentagon:")
print("Perimeter =", p1.perimeter())
print("Area =", p1.area())
