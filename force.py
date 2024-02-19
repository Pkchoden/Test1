print("Newton's second law of motion")
print("--------------------------------------------")
#determine the missing value
print("select the missing value")
print("1. mass(m)")
print("2. acceleration (a)")
print("3. force (f)")
missing_value_choice= input ("enter the option number for the missing value: ")
# prompt the user to enter the other two values
if missing_value_choice == "1":
    a = float(input("enter acceleration (a):"))
    f = float(input("enter force(f):"))
    m = f / a
    print(f"mass(m)={m}")
elif missing_value_choice == "2" :
    f = float(input("enter acceleration (a):"))
    m = float(input("enter mass(m):"))
    a = f / m
    print(f"acceleration(a)={a}")
elif missing_value_choice == "3" :
    m = float(input("enter acceleration (a):"))
    a = float(input("enter acceleration (a):"))
    f = m * a
    print(f"force(f)={f}")
else:
    print("invalid option selected for the missing value.")