total = 0.0
count = 0
choice = "Yes"

while choice[0] == "Y" or choice[0] == "y":
    number = int(input("enter a number :"))
    total=total + number
    count=count+1
    choice = input("Do you want to continue? - type 'Yes' or 'No' :")
    average= total/count
    print('Average = ',average)