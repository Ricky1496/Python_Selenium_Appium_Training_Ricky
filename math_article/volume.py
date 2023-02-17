import math


def volume_of_sphere(radius):
    volume = (4 / 3) * math.pi * radius ** 3
    return volume


def volume_of_cylinder(radius, height):
    volume = math.pi * radius ** 2 * height
    return volume


def volume_of_pyramid(base_length, base_width, height):
    volume = (1 / 3) * base_length * base_width * height
    return volume


def volume_of_cone(radius, height):
    volume = (1/3) * math.pi * radius**2 * height
    return volume


def volume_of_cuboid(length, width, height):
    volume = length * width * height
    return volume


def volume_of_hemisphere(radius):
    volume = (2/3) * math.pi * radius**3
    return volume
