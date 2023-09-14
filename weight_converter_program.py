weight= input("Enter the weight: ")
word=input("Weight is given on :"
           "(L) for lbs, (K) for kg: ")
if word=='L' or 'l' :
    kg=int(weight)/2.204623
    print("The weight on KG is: ", kg)
elif word=='K' or 'k':
    lbs=int(weight)*2.204623
    print("The weight on Pounds is: ", lbs)
else:
    print("Invalid Choice: ")
