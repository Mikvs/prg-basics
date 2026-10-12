###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
surface_area = a*b*c
volume = a*b*2+a*c*2+b*c*2
print(f'The volume is {volume}')
print(f'The surface area is {surface_area}')