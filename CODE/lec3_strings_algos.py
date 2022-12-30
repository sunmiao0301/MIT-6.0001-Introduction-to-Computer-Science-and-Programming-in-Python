from codecs import charmap_build
from traceback import print_tb
from xml.etree.ElementPath import prepare_child


s = "abc"
# print(s[0])
# print(s[1])
# print(s[2])
# print(s[3])

# print(s[-1])
# print(s[-2])
# 内置
# print(s[-0 == 0])

# s = "abcdefgh"
# print(s[3:6])
# print(s[3:6:2]) #df
# print(s[::])
# print(s[::-1])

# s = "hello"
# print(s[0])
# # s[0] = 'j'
# # print(s[0])

# s = "jello"
# print(s[0])

####################
## EXAMPLE: for loops over strings
# ###################

# s = "jello"
# i = 0
# print(s[i])

# s = "demoouuuuu"
# for i in range(10):
#    if s[i] == 'i' or s[i] == 'u':
#        print("There is an i or u")
#    else:
#        print("当前i位置的字母不是i或者u")

# char # 字符
# string = "abc"# 字符串

# s = "demoouuuuu"
# for char in s:
#    if char == 'i' or char == 'u':
#        print("There is an i or u")
#    else:
#        print("当前i位置的字母不是i或者u")

####################################
# print('num_guesses =', num_guesses)

####################
## EXAMPLE: while loops and strings
## CHALLENGE: rewrite while loop with a for loop
###################

# an_letters = "aeiou"
# word = input("I will cheer for you! Enter a word: ")
# times = int(input("Enthusiasm level (1-10): "))

# for char in word:
#    if char in an_letters:#恰
#        print("Give me an " + char + "! " + char)
#    else:
#        print("Give me a  " + char + "! " + char)

# print("What does that spell?")
# for i in range(times):
#    print(word, "!!!")

# s1 = "mit u rock"
# s2 = "i rule mit"
# if len(s1) == len(s2):
#     for char1 in s1:
#         for char2 in s2:
#             if char1 == char2:
#                 print("common letter")
#                 break

####################
## EXAMPLE: perfect cube 
####################
# cube = -27
# # cube = 8120601
# for guess in range(cube+1):# 0~27
#    if guess**3 == cube:
#        print("Cube root of", cube, "is", guess)
#        break
#    else:
#        print(guess)
    #    loops keeps going even after found the cube root
    

####################
## EXAMPLE: guess and check cube root 
####################
# cube = -27
# #cube = 8120601
# for guess in range(abs(cube)+1):
#    # passed all potential cube roots
#    if guess**3 >= abs(cube):
#        # no need to keep searching
#        break
# if guess**3 != abs(cube):
#    print(cube, 'is not a perfect cube')
# else:
#    if cube < 0:
#        guess = -guess
#    print('Cube root of ' + str(cube) + ' is ' + str(guess))


####################
## EXAMPLE: approximate cube root 
####################
cube = 27
#cube = 8120601
#cube = 10000
epsilon = 0.1
guess = 0.0
increment = 0.01
num_guesses = 0
# look for close enough answer and make sure
# didn't accidentally skip the close enough bound
while abs(guess**3 - cube) >= epsilon and guess <= cube:
   guess += increment
   num_guesses += 1
print('num_guesses =', num_guesses)
# if abs(guess**3 - cube) >= epsilon:
#    print('Failed on cube root of', cube, "with these parameters.")
# else:
print(guess, 'is close to the cube root of', cube)


###################
# EXAMPLE: bisection cube root (only positive cubes!)
####################
cube = 27
#cube = 8120601
# won't work with x < 1 because initial upper bound is less than ans
#cube = 0.25
epsilon = 0.01
num_guesses = 0

low = 0
high = cube

guess = (high + low)/2.0
while abs(guess**3 - cube) >= epsilon:
   if guess**3 < cube:
       # look only in upper half search space
       low = guess
   else:
       # look only in lower half search space
       high = guess
   # next guess is halfway in search space
   guess = (high + low)/2.0
   num_guesses += 1
print('num_guesses =', num_guesses)
print(guess, 'is close to the cube root of', cube)

# print(int(3/2))