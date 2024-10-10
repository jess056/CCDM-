from PermeterClass import perimeter
choice = int(input("Enter1,2,3 to calculate the following:\n1 for Rectangle\n2 for circumference\n3 for Triangle\n"))
if choice==1:
    l=int(input("Enter length:\n"))
    w=int(input("Enter width:\n"))
    Robj=perimeter(l,w,0,0)
    Robj.PeriRect()
   
elif choice==2:
    r=int(input("Enter radius:\n"))
    Cobj=perimeter(0,0,r,0)
    Cobj.circumf()

elif choice==3:
    side=int(input("Enter side:\n"))
    Tobj=perimeter(0,0,0,side)
    Tobj.periTri()

else:
    print("Invalid choice")      

    





 