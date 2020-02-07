#problem, take in 2 coords as tuples and return the distance of the line
class Line:
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
        print('variables are passed')

    def distance(self):
        print('passing through distance')
        distance_sum = ( ((self.coor2[0] - self.coor1[0]) ** 2) + ((self.coor2[1] - self.coor1[1] ) ** 2) ) ** (1/2)
        return distance_sum

    def slope(self):
        print('passing through slope')
        slope_sum = (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0] )
        return slope_sum

coordinate1 = (3,2) #x
coordinate2 = (8,10) #y

li = Line(coordinate1,coordinate2)

print(li.distance())
print(li.slope())

print("\n\n")

#problem 2, create the cylinder object
class Cylinder:
    def __init__(self,height = 1,radius = 1):
        self.height = height
        self.radius = radius

    def volume(self):
        volume_sum = 3.14 * (self.radius ** 2) * self.height
        return volume_sum

    def surface_area(self):
        top_base = 3.14 * ( self.radius ** 2)
        bottom_base = 3.14 * ( self.radius ** 2)
        side_area = 2 * 3.14 * self.radius * self.height

        sa_sum = side_area + bottom_base + top_base
        return sa_sum




c = Cylinder(2,3)

print(c.volume())
print(c.surface_area())