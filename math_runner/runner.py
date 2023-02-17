from math_article import volume


def volume_of_all() -> object:
    sphere = volume.volume_of_sphere(40)
    print(f"Volume of Sphere: {sphere}")

    cylinder = volume.volume_of_cylinder(20, 55)
    print(f"Volume of Cylinder: {cylinder}")

    pyramid = volume.volume_of_pyramid(30, 15, 45)
    print(f"Volume of Sphere: {pyramid}")

    cone = volume.volume_of_cone(30, 60)
    print(f"Volume of Sphere: {cone}")

    cuboid = volume.volume_of_cuboid(20, 25, 54)
    print(f"Volume of Sphere: {cuboid}")

    hemisphere = volume.volume_of_hemisphere(40)
    print(f"Volume of Sphere: {hemisphere}")


