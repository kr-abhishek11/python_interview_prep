numbers =[1,2,3,4,5]
while(n:= len(numbers)) > 0: print(numbers.pop())

a = True
print(a:=False)

names =["Abhishek","Harsh","Rishabh"]
if (name:= input("Enter a name")) in names: 
    print(f"The entered name is {name}")
else:
    print("Name not found")