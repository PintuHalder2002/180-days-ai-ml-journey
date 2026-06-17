def find_cylinder_volume(r, h=7):
    print("radius: ",r)
    print("height: ",h)
    volume = 3.14*(r**2)*h
    print(volume)
    return volume


print("Total cylinder volume: ",find_cylinder_volume(5,8))
print("Total cylinder volume: ",find_cylinder_volume(5))
