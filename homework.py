Age = int(input ("Enter your age:"))
student = input ("Are you a student?(yes/no):")
if (Age <= 12) or ( Age>= 13 and Age<=18 and student == 'yes') :
    print ("you are eligible for a discount on a movie ticket ")
else:
    print ("you are not eligible for a discount on the movie ticket")
