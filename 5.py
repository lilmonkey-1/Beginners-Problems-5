#Biggest, Smallest and Average
numsList = [7, 6, 23, 8.18, 18, 8, 7.2, 85, 915, 12]

max_value = max(numsList)
max_position = numsList.index(max_value)

min_value = min(numsList)
min_position = numsList.index(min_value)

average = sum(numsList) / len(numsList)

print(f"The biggest number is {max_value} at position {max_position}.")
print(f"The smallest number is {min_value} at position {min_position}.")
print(f"The average of all the numbers is {average:.2f}.")

#Same Start and End 
#HI CAN I PLEASE GET SOME HELP ON THIS ONE PLEASE I DONT UNDERSTAND IT!!!
#HELP
#HELP
#HELP
stringsList = ["abc", "123", "2332", "aBBA", "heelloo", "1212", "DcEfD"]

for string in stringsList:
    first_char = string[0]
    last_char = string[-1]
    if first_char== last_char:
        print(string)

#I Like Pesto (a lot)
otherFoods=[]
iLikePesto=[]

for food in range(8):
    food=input("What's your favourite food?")
    if food=="pesto":
        iLikePesto.append(food)
    else:
        otherFoods.append(food)
    
print(f"Pesto is loved by {len(iLikePesto)} people!")
for pesto in range(len(iLikePesto)):
    print("I like pesto")
print("Other Foods:")
print(otherFoods)

#List of (good) Cereals
cerealList=[]

badCereal=False
while not badCereal:
    cereal=input("Name a cereal:")
    cerealList.append(cereal)
    if cereal=="sultana and bran":
        badCereal=True
    elif cereal=="weetbix":
        badCereal=True

print(cerealList)

