# print("hhhh!/><  12891\t12")

###################
## EXAMPLE: strings 
###################

# hi = "hi"
# name = "ana"
# greet = hi + name
# space = " "  
# print(hi + " " + name)
# print("hello there" + " " + "ana")
# print(greet)
# greeting = hi + " " + name
# print(greeting)
# silly = (hi + (" " + name)) * 3 + hi * 4 + hi
# print(silly)
# anaanaana
#  ana ana ana
# hi ana ana ana

####################
## EXAMPLE: output 
####################
# x = 1
# print(x)
# x_str = str(x)
# print("my fav number is", x, ".", "x=", x)
# print("my fav number is", x_str + "." + "x=" + x_str)
# print("my fav number is" + x_str + "." + "x=" + x_str)

# printt = 1
# print(printt)

###################
# EXAMPLE: input
##################
# text = input("Type anything... ")
# print(5*text)
# num = int(input("Type a number... "))
# print(5*num)


###################
# EXAMPLE: conditionals/branching 
###################
# x = int(input("Enter a number for x: "))
# y = int(input("Enter a number for y: "))

# if x == y:
#    print("x and y are equal")
#    if y != 0:
#        print("therefore, x / y is", x/y)
# elif x < y:
#    print("x is smaller")
# elif x > y:
#    print("y is smaller")
# print("thanks!")

# x: 1.0
# y: 1.0

# x and y are equal
# therefore, x / y is 1
# thanks!

# x: 1.0
# y: 2.0

# therefore, x / y is 0.5
# x is smaller
# # thanks!

# x 2.0
# y 1.0

# y is smaller
# thanks!


# if 判断条件1:
#     执行语句1……
# elif 判断条件2:
#     执行语句2……
# elif 判断条件3:
#     执行语句3……
# else:
#     执行语句4……


######################################
# flag = 0

# 随机抽奖 ==> 好 或者 垃圾
# 池子中越来越少
# 固定概率

# 100个皮肤

# 99个垃圾皮肤
# 1个好皮肤

# 99%
# 98/99 < 99%
# 1垃圾1好的
# 50%

# 99%
# 1%

# if(flag == 100 or 抽到最好的皮肤 == true){
#     flag = 0;
#     给玩家一个好皮肤
# }
# else{
#     flag++;
#     给玩家一个垃圾皮肤
# }

# flag = 100
####################################

# 法律 ==> 
# 计算机网络 ==> id
# 游客登录

# 设备 序列号 

# 网络安全 密码学

# print(1)

####################
## EXAMPLE: remainder 
####################
#num = int(input("Enter a number: "))
#if num % 2 == 0:
#    print("number is even")
#else:
#    print("number is odd")


####################
## EXAMPLE: while loops 
## Try expanding this code to show a sad face if you go right
## twice and flip the table any more times than that. 
## Hint: use a counter
####################
# n = input("You are in the Lost Forest\n****************\n****************\n :)\n****************\n****************\nGo left or right? ")
# while n == "right" or n == "Right":
#    n = input("You are in the Lost Forest\n****************\n******       ***\n  (╯°□°）╯︵ ┻━┻\n****************\n****************\nGo left or right? ")
# # print("\nYou got out of the Lost Forest!\n\o/")

# n = 0
# while n < 5:
#    print(n)
#    n = n+1

# ####################
# ## EXAMPLE: for loops
# ####################
# for n in range(5):
#    print(n + 1)
# 人编译器
# mysum = 0
# for i in range(3):
#    mysum = mysum + i
# print(mysum)

# mysum = 0
# for i in range(7, 10, 2):
#    mysum += i
# print(mysum)
# print(7 + 9)

# 步长
# mysum = 0
# for i in range(5, 11, 2):
#    mysum += i
#    if mysum == 5:
#        break
#        mysum += 1
# print(mysum)
# print(5 + 7 + 9)



###################
# EXAMPLE: perfect squares
###################
ans = 0
neg_flag = False
x = int(input("Enter an integer: "))
if x < 0:
   neg_flag = True
while ans**2 < x:
   ans = ans + 1
if ans**2 == x:
   print("Square root of", x, "is", ans)
else:
   print(x, "is not a perfect square")
   if neg_flag:
       print("Just checking... did you mean", -x, "?")




####################
## TEST YOURSELF!
## Modify the perfect squares example to print 
## imaginary perfect sqrts if given a negative num.
####################

# {}