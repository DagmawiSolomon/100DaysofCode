import math


def paint_calc(height,width,coverage):
    area = height*width
    number_of_cans = math.ceil(area / coverage)
    print(number_of_cans)


paint_calc(height=7, width=13, coverage=5)