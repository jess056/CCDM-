import math
class perimeter:
    def __init__(self,l,w,r,s):
        self.length=l
        self.width=w
        self.radius=r
        self.side=s
        
    
    def PeriRect(self):
        perimeter = self.length+self.width+self.length+self.width
        print("perimeter of Rectangle",perimeter,"cm")

    def circumf(self):
        perimeter = math.pi * self.radius * 2
        print("primeter of circumfernce",perimeter,"cm")

    def periTri(self):
        perimeter = self.side + self.side + self.side
        print("primeter of Triangle",perimeter,"cm")


    


 
 
    
    
    



    
        







