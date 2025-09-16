class Rectangle:

    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def calc_area(self):
        area = self.__height * self.__width
        return area

    def calc_parameter(self):
        parameter = 2 * (self.__width + self.__height)
        return parameter

    def calc_diagonal(self):
        diagonal = 0.5 ** ((self.__width ** 2) + (self.__height ** 2))
        return diagonal


rectangle_height = int(input("Enter height: "))
rectangle_width = int(input("Enter width: "))
rectangle_1 = Rectangle(rectangle_height, rectangle_width)

print(rectangle_1.calc_area())
print(rectangle_1.calc_parameter())
print(rectangle_1.calc_diagonal())