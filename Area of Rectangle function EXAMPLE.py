#function to get Area of the Rectangle
import math
#Defining the function
#def AreaofRectangle():
    #length=int(input("Enter length:\n"))
    #width=int(input("Enter width:\n"))
    #area = length*width
    #print("Area of the Rectangle is: ", area , "cm squared")

#outside of the function
# Here, we CALL the function
#AreaofRectangle()

#function to get Area of a circle
#Defining the function
def AreaofCircle():
    #pie=int(3.14)
    radius=int(input("Enter radius:\n"))
    area=math.pi*radius*radius
    print("Area of a Circle:", area, "cm squared")

#outside of the function
#Here, we CALL the function
AreaofCircle()