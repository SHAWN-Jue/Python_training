
f = open("shopping_items","r+")    #已可读写的方式打开商品目录清单，指针放在文件开头
sc = open("shoppingcart","r+")     #已可读写的方式打开购物车清单，指针放在文件开头，主要目的是查余额
identity = ["用户入口","商家入口"]  #建立用户选择菜单
shopping_cart = {}                 #建立存放购物车商品的字典
shopping_list = {}                 #建立存放商品目录的字典
while True:
    for i in identity:
        print(identity.index(i),i)    #生成用户身份选择
    identity_choice = input("Please choose your identity:")
    if identity_choice.isdigit():     #如果身份输入是数字
        if int(identity_choice) == 0:  #判断数字是否为0，如果为0，则是用户
            while True:
                                                #此处缺少一段代码，用于读取shoppingcart.txt中的工资余额，如果大于0，则不要求输入工资
                salary = input("Please input your salary and prepare for shopping:") #如果上段代码发现工资为0，则输入工资
                if salary.isdigit():                                    #判断工资是否为数字
                    salary = int(salary)                                #将字符串转换为整数型

                    for line in f:
                        key, value = line.strip().split(",")
                        shopping_list[key] = int(value)                  #将文件f中商品逐行打印存入字典shopping_list
                    while salary > 0:                                    #进入while循环，只要工资>0，则为真
                        print("Items list".center(20, "-"))
                        for key in shopping_list:
                            print(key, shopping_list[key])               #将shopping_list中的内容逐行打印输出
                        shopping_choice = input("Please input the item you want to buy:")  #让用户输入想购买的商品名称
                        if shopping_choice.isdigit():                       #判断如果是数字，打印出错
                            print("Sorry,you input is a number, not a name, please try it again.")
                        elif shopping_choice in shopping_list:             #如果输入商品在目录中
                            if salary > int(shopping_list[shopping_choice]):   #判断工资余额是否能买。如果能则为真
                                salary -= int(shopping_list[shopping_choice])   #扣去所买商品，所剩余额
                                sc = open("shoppingcart","a+")                  #打开购物车文件，存放已购商品
                                sc.writelines(shopping_choice+","+str(salary)+"\n")   # 写入已购商品，和余额
                                sc.close()
                                #print("Items bought".center(20,"-"),"\n",shopping_cart,"The ballance is:",salary)
                                print("The ballance is:", salary)
                            else:
                                print("Sorry, your money is not enough to buy this item, please try the other ones.")
                        elif shopping_choice in ["Q","q"]:
                            print("Thanks for your shopping\n", "Your balance is:",salary,"\nItems you've bought are:",shopping_cart)
                            break
                        else:
                            print("Sorry, you've just input a invalid content,please input it again.")
                else:
                    print("Sorry, you've just input is not a number,please input it again.")

        elif int(identity_choice) == 1:          #如果输入1，则是商户入口
            print("Hi,my boss, you can add new items or change the prices of the existed items.")
            while True:
                for line in f:                   #同样将文件内容存入shopping_list
                    key, value = line.strip().split(",")
                    shopping_list[key] = int(value)
                for key in shopping_list:           #将字典内容逐行打印
                    print(key, shopping_list[key])
                change_item = input("Please input items your want to add or change:")   #输入要修改商品名称
                if change_item.isdigit():
                    print("Sorry,you input is a number, not a name, please try it again.")
                elif change_item in shopping_list:
                        choice = input("You want to delete it or change the price, please input d for delete, or c for change the price:")
                        if choice in ["D","d"]:
                            del shopping_list[change_item]
                        elif choice in ["C","c"]:
                            price = input("Please input the updated price:")
                            shopping_list[change_item] = price
                        elif choice in ["Q","q"]:
                            print("Goodbye, Boss")
                        else:
                            print("Sorry, you've just input a invalid content,please input it again.")
                else:
                    while True:
                        new_item_price = input("Please input the price of the item you've just input:")
                        if new_item_price.isdigit() and int(new_item_price) >= 0:
                            shopping_list[change_item] = new_item_price
                        elif new_item_price in ["Q", "q"]:
                            break

                        elif print("Sorry,your input is a number, not a name, please try it again."):
                            pass

        else:
            print("Sorry, what you've just input is a invalid number,if you want quit,please input Q or q.")

    elif identity_choice in ["Q","q"]:
        print("Thanks for your shopping, Goodbye")
        break
    else:
        print("Sorry, what you've just input is not a number,if you want quit,please input Q or q.")
