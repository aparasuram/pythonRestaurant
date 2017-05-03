# Python Restaurant
# Author : Anand Parasuram
# Date : 5/3/2017

fooditems = ""
totalcharge=0
timetaken=0

var1 = "1. Vegetable Pasta in red sauce\t\tRs.230"
t1=10
p1=230
var2 = "2. Macaroni and Cheese in a white sauce\tRs.210"
t2=10
p2=210
var3 = "3. Veggie Delight Pizza\t\t\tRs.200"
t3=15
p3=200
var4 = "4. Chicken, Corn and Cabbage Pizza \t\tRs.290"
t4=18
p4=290
var5 = "5. Mixed Vegetable and corn salad\t\tRs.150"
t5=12
p5=150
var6 = "6. Red Mexican Rice with Tacos\t\tRs.230"
t6=18
p6=230
var7 = "7. Burrito Grande with rice and capsicum\tRs.210"
t7=16
p7=210
var8 = "8. Vegetable steamed momos.4 in number\t Rs.250"
t8=15
p8=250
var9 = "9. Salad in Thai peanut sauce\t\t\tRs.190"
t9=10
p9=190
var10= "10. Big bowl Noodles in manchow soup\t\tRs.170"
t10=16
p10=170
while(True):
    print("\n"*30)
    print("*"*90)
    print("\t\t\t\t\tPython Restaurant")
    print("\t\t\t\t\t*****Italian*****")
    print("\t\t\t"+var1)
    print("\t\t\t"+var2)
    print("\t\t\t" + var3)
    print("\t\t\t" + var4)
    print("\t\t\t\t\t*****Mexican*****")
    print("\t\t\t"+var5)
    print("\t\t\t" + var6)
    print("\t\t\t" + var7)
    print("\t\t\t\t\t*****Chinese*****")
    print("\t\t\t" + var8)
    print("\t\t\t" + var9)
    print("\t\t\t" + var10)
    print("*"*90)
    print("S. Show cart")
    print("X. Checkout")
    print("E. Exit")
    opt=input("Please enter an option :")
    if opt=="1":
        fooditems=fooditems + "\n"+var1
        totalcharge=totalcharge+p1
        if t1 > timetaken:
            timetaken=t1
    elif opt=="2":
        fooditems=fooditems + "\n"+var2
        totalcharge=totalcharge+p2
        if t2 > timetaken:
            timetaken=t2
    elif opt=="3":
        fooditems=fooditems + "\n"+var3
        totalcharge=totalcharge+p3
        if t3 > timetaken:
            timetaken=t3
    elif opt=="4":
        fooditems=fooditems + "\n"+var4
        totalcharge=totalcharge+p4
        if t4 > timetaken:
            timetaken=t4
    elif opt=="5":
        fooditems=fooditems + "\n"+var5
        totalcharge=totalcharge+p5
        if t5 > timetaken:
            timetaken=t5
    elif opt=="6":
        fooditems=fooditems + "\n"+var6
        totalcharge=totalcharge+p6
        if t6 > timetaken:
            timetaken=t6
    elif opt=="7":
        fooditems=fooditems + "\n"+var7
        totalcharge=totalcharge+p7
        if t7 > timetaken:
            timetaken=t7
    elif opt=="8":
        fooditems=fooditems + "\n"+var8
        totalcharge=totalcharge+p8
        if t8 > timetaken:
            timetaken=t8
    elif opt=="9":
        fooditems=fooditems + "\n"+var9
        totalcharge=totalcharge+p9
        if t9 > timetaken:
            timetaken=t9
    elif opt=="10":
        fooditems=fooditems + "\n"+var10
        totalcharge=totalcharge+p10
        if t10 > timetaken:
            timetaken=t10
    elif opt=="e":
        break
    elif opt=="s":
        print(fooditems)
        print("-"*90)
        print("\t\t\t\t\tRs."+str(totalcharge))
        input()
    elif opt=="x":
        print(fooditems)
        print("-"*90)
        print("\t\t\t\t\tRs."+str(totalcharge))
        if totalcharge > 0:
            print("Your food will arrive in a maximum of ",timetaken, "minutes")
            print("You can pay using PayPal if you wish...")
            input()
        else:
            print("Nothing in your cart. Please select the food items you would like to order")
            input()
    else:
        print("Invalid food choice/option selection")
        input()
        
print("*"*90)
print("Thank you for visiting the Python Restaurant")
print("Hope you enjoy your food")
print("*"*90)
    

          
