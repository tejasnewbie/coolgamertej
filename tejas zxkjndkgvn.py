# # # variables
# # var1 = "56"
# # var2 = "87"
# # var3 = 89
# # var = "78"
# # var5 = "tejas"
# # var6 = "joshi"
# # enternumber = 786549065
# # print(enternumber)
# # #type casting
# # print(100 * str(int(var) + (var3)) )
# # print(100 * "helloworld\t")
# # print(10 * "helloworld\n")
# # '''
# # types of variables
# # int()
# # str()
# # float()
# # '''
# #
# # # print(100 * str(int(var)))
# # # print(100 * str(var3))
# # #
# #
# #  print("enter your number")
# #  inpnum = input()
# #  print('you entered', int(inpnum) +10)
# #  addtion calculator
# # print('enter your forst number')
# #  n1 = input()
# #  print('enter your second number')
# #  n2 = input()
# #  print("your sum is", int(n1) + int(n2))
# #  #MULTIPLICATION CALCULATOR
# #  print("enter your number")
# #  n3 = input()
# #  print("enter your second number")
# #  n4 = input()
# #  print("your answer is", int(n3) * int(n4))
# # #
# #
# #
# # # string sliciing
# # # mystr = 'tejas is a good boy '
# # # mystr2  = '23456'
# # # print(mystr)
# # # print(mystr[0:5])
# # # print(mystr[0:])
# # # print(mystr[:19])
# # # print(mystr[0:19:1])
# # # print(mystr[0:19:3])
# # # print(mystr[::-1])
# # # #how to find length
# # # print(len(mystr))
# # # print(mystr.isalpha())
# # # print(mystr2.isalnum())
# # # print(mystr2.endswith("6"))
# # # # count how many times letter\word has arrived
# # # print(mystr.count('boy'))
# # # print(mystr.capitalize())
# # # print(mystr.find('is'))
# # # print(mystr.upper())
# # # print(mystr.lower())
# # # print(mystr.replace('good', 'are'))
# #
# # # list data structure---- mutable
# # # print('tejas')
# # grocery = ['harpic', 'vimbar', 'deo', 'bhindi', 'lolypop', 56]
# # #print(grocery)
# # # print(grocery[4])
# # numbers = [2, 7, 9, 11,3 ]
# # # print(numbers[2])
# # # numbers.sort()
# # # numbers.reverse()
# # # print(numbers[::-1])
# # # print(len(numbers))
# # # print(max(numbers))
# # # print(min(numbers))
# # # numbers.append(78)
# # # numbers.append(56)
# # # numbers.insert(4,67)
# # # numbers.remove(7)
# # # /
# # # print(numbers)
# # #tuple ----- immutable
# # # numbers[1] = 34
# # # print(numbers)
# # #mutable - can be change
# # #immutable - canoot be changed
# # tp = (1, 2, 3)
# # tp2 = (1,)
# # print(tp)
# # print(tp2)
# # a = 1
# # b = 2
# # # temp = a
# # # a = b
# # # b = temp
# # #OR
# # a,b = b,a
# # # print(a)
# # # print(b)
# # print(a, b)
# # #dictonary is nothing but key value pairs
# # d1 = {}
# # # print(type(d1))
# # d2 = {'harry':'burger', 'rohan':'fish', 'tejas':'roti', 'shubham':{'B':'MAGGIE', 'L':'chicken'} }
# # d2['ankit'] = 'junk food'
# # # del d2['ankit']
# # # print(d2['shubham']['B'] )
# # d3 = d2.copy()
# # # print(d2.copy())
# # del d3['tejas']
# # print(d2)
# # print(d2.copy())
# #
# # print(d3)
# # # print(d2)
# # d2.update({'leena':'tofee'})
# # print(d2.items())
# # #if and else statements
# # num = 45
# # num2 = 56
# # num3 = int(input())
# # if num3 > num:
# #     print('greater')
# # elif num3==num:
# #     print('equal')
# # else:
#     print('lesser')
# # print('welcome to my game')
# # score = 0
# # q = 'what is your name'
# # q = input()
# # if q == 'bharathi(indian)':
# #     print('correct')
# #     score+= 1
# # else:
# #     print('incorrect')
# list1 = [5, 7, 8 ]
# # if 5  in list1:
# #     print('its in the list')
# # else:
# #     print('no its not in the list')
# #
# #
# # if 15 not in list1:
# #     print('no its not in the list')
# # else:
# #     print('its in the list')
# # print(5 in list1)
# # print(52 in list1)
# #
# # # quiz
# # age = int(input())
# # # if age>18:
# # #      print('you can drive')
# # if age<18:
# #     print('shakal dehk apni,ghar betho')
# # elif age==18:
# #     print('itna wait kiya hai tho ek saal aur shai')
# # elif  age>60:
# #     print('mazak chodo chacha ghar jao')
# # else:
# #     print('lets go for long dirve')
# #
# #
# #
# # print('.\n')
# #
# #
# #
# # # dictonary= {'harry': 'burger', 'rohan': 'fish', 'tejas': 'roti', 'shubham': {'B': 'MAGGIE', 'L': 'chicken'}}
# # # print('what do you want to search')
# # # print('avalible options are ---harry,rohan,tejas,shubham ')
# # # print('your answer is', dictonary[input()])
# # #
# #
# # #faulty calculator
# # print('enter your first number')
# # t1 = int(input())
# # print('enter your secondnumber')
# # t2 = int(input())
# # print('select operator'+ '+, -, *, /' )
# # t3 = input()
# # if t1==455 and t2==5 and t3=='*':
# #     print('987')
# # elif t1==900 and t2==3 and t3=='+':
# #     print('5437')
# # elif t3=='*':
# #     mulp = t1*t2
# #     print(mulp)
# # elif t3=='+':
# #     plus = t1+t2
# #     print(plus)
# # elif t3=='-':
# #     sub = t1-t2
# #     print(sub)
# # elif t3=='/':
# #     div = t1/t2
# #     print(div)
# #
# # # list2 = [ ['harry', 1], ['tejas', 10] ]
# # # for items, lollypop in list2:
# # #     print(items,'eats', lollypop, 'lollypop')
# #
# tejasj = [int,4,6,8,10,11,23]
#
# for item in tejasj:
#     if str(item).isnumeric() and item>=6:
#         print(item)
#
#
i = 0
# while(True):
#     if i+1<5:
#         i = i + 1
#         continue
#     print(i+1, end=' ')
#     if (i==44):
#         break
#         i = i = 1

 #
 # print('wite a number')
 # tj = 300

# print('guess a number')
# tj = 456
# tj = int(input())
# while(True):
#     tj = int(input())
#     if tj==456:
#         print('you are correct')
#     elif tj<350:
#         print('guess is too low')
#     elif tj<500:
#         print('your guess is too high')

# while(True):
#     inp = int(input("enter a number"))
#     if inp>100:
#         print('congo u gussed it crercr')
#         break
#     else:
#         print('try again')
#         continue
# inp = 56
# print('guess the number')
# numbers_of_guess = 0
# while(numbers_of_guess<=6):
#     numbers_of_guess = numbers_of_guess + 1
#     inp = int(input())
#     if inp<56:
#         print('too low')
#     elif inp>56:
#         print('too high')
#     else:
#         print('you won')
#         print(numbers_of_guess, 'he took oto finish')
#         if numbers_of_guess>10:
#             break
# print('you have reached maxiumum nuber of guesses')
# print('game over')


number_of_guesse = 0
print('only 9 guesses')
while(number_of_guesse<=9):
    number_of_guesse = number_of_guesse + 1
    joshi = int(input('enter your number\n'))
    if joshi < 18:
        print('this number is low,please try gai')
    elif joshi > 18:
        print('this number is high,please try gai')
    elif joshi==18:
        print('YOU WON THIS GAME')
        print('your results are as follows:-')
        print('no of guesses used:', number_of_guesse)
        print( "no. of guesses left:", 9 - number_of_guesse)
        print('thnx for playing this game')
        break

if number_of_guesse>9:
    print('maximum no.of gusss reached')
    print('GAME OVER')

quit("GAME FINISHED")




