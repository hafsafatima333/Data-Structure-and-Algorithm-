# x = 25
# if (x < 0):
#     print ("25 is less than 0")

# elif(x == 25):
#     print("x is equal to 25")

# else:
#     print("25 is greater than 0")


# p = 0
# while (p < 10):
#    print(p)
#    p += 1


# p= 0
# while(p <= 10):
#     print("p = " , p)
#     p += 2


#for loop 
# for i in range (20):
#     print(i)



#++++++++++++++++++++++++++++++++++++++++++++++++++++Maths library++++++++++++++++++++++++++++++++++++++++++++++++++++

# import math
# k=5
# for k in [2,4,6,8,10]:
#     print("Square root of" + str(k) + ":" , end="")
#     print(math.sqrt(k))




#+++++++++++++++++++++++++++++++++++++++++++++++++++=Dictionary concept+++++++++++++++++++++++++++++++++++++++++++++++

d = {
     1:"one",
     2:"two"
     } 
#single single element ko show krwata ha  
#jysy 1 py one rkha ha
#2 py two rkha ha----->
print(d[1])
print(d[2])



#pair ki form mai dekhata hai dictionary ko 
print(d.items())











#Another example i made:++++++++++++++++++>>>>>>>>
d = {1:"Zoya",
     2:"Sara",
     3:"Alishba",
     4:"Hiba",
     5:"Areeba",
     5:"Maryam"
     }

print(d[1])
print(d[2])
print(d[3])
print(d[4])
print(d[5])
print(d[6])

print(d.items())

#++++++++++++++++++++++++++++++++++++++++++++++++++++++=



for k, v in d.items():
    print(k, v)
 


