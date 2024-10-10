student={"SID":111,"Sname":"Tom","course":"CFCDB","Age":25}
print(student)
# Output {"SID":111,"Sname"}
print(student.keys())
print(student.values())
print(student.items())
#print(type(student.items))
student["Sname"]= "Jessia"
print(student)
