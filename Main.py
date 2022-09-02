import Goods
import sys

print("1. Assign the goods to the Cargo")
print("2. Return - Update the goods when returned by the cargo")
print("3. Exit")

ch = int(input("Enter your choice:\n"))
goods = Goods.Goods()

if ch == 1:
    user = input("Enter username:\n")
    passwrd = input("Enter password:\n")
    s = goods.validateUsernamePassword('user.xml', user, passwrd)
    if s:
        goodsType = input("Enter goods type:\n")
        s = goods.checkGoodsType('goods.xml', user, goodsType)
        if s:
            pass
        else:
            print("Invalid goods type")
            sys.exit()
    else :
        print("Invalid Username")
        sys.exit()
        
elif ch == 2:
    user = input("Enter username:\n")
    passwrd = input("Enter password:\n")
    s1 = goods.validateUsernamePassword('user.xml', user, passwrd)
    if s1:
        goodsNo = int(input("Enter goods number:\n"))
        s1 = goods.updateOnReturn("goods.xml", goodsNo)
        if s1:
            pass
        else :
            print("Invalid goods number")
    else :
        print("Invalid Username")
        
elif ch == 3:
    sys.exit()