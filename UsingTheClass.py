#as a user
from CLASSES import Area

l = int(input("Enter length:\n"))
w = int(input("Enter width:\n"))
r = int(input("Enter radius:\n"))

# Create object and assign values
Robj=Area(l,w,0)

#use object to access the AreaofRectangle function
#Robj.AreaofRectangle()

Cobj=Area(0,0,r)
Cobj.AreaofCircle()

#as a user
#choice 1 2 or3

l = int(input("Enter:\n"))  
w = int(input("Enter width:\n"))
r = int(input("Enter radius:\n"))
b = int(input("Enter base:\n"))
h = int(input("Enter height:\n"))

#user1
#create object and assign values
Robj=Area(l,w,0)
Robj.AreaofRectangle()

#user2
#create object and assign valuea
Cobj=Area(0,0,r)
Cobj.Areaofcircle()

#user3
#create object and assign values
Tobj=Area(0,0,0,b,h)
Tobj.AreaofTriangle()







