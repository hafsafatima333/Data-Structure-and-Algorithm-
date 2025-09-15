# d = {1:"Hafsa",
#      2:"Ayesha",
# }


#============================Dictionary=======================

#mai yaha lib ka use kuch iss trh krhi hu kay 1,2,3,4 waly part ko mainy'k' kha ha 
# and  'coco,lemon,juice' waly part ko mainy 'v' kha hai tw lehaza yha 
# loop chala ha or dono ko apni values milgai han +++++++++++++++++


# yha 1,2,3,4 (keys) hen 
# and coco, lemon (values) hen 


#----------------------------------------------------------------------------------

#(Yahan 1 aur 2 ne address ka kaam kiya → jaise 
# ghar ka number hota hai jahan se cheez milti hai.)
# d = {
#     1:"coco",
#     2:"lemon",
#     3:"nuts",
#     4:"juice"
# }


# for k, v in d.items():
#     print(k, v)



#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
#+++++++++++++++++++++++++++=Tuple+++++++++++++++===
#Easy samjho:
#Tuple ek dabba hai jisme values fixed hoti hain.
#list me tum values change kar sakti ho, tuple me nahi.


# t = ("coco", "lemon", "mango")
# for item in t:
#     print(item)

    #+++++++++++++++++++++=  for item in t:
#iska matlab hota hai:
#Tuple t = ("coco", "lemon", "mango") lo
#Usme jo jo elements hain unhe ek-ek karke item me daalo
#Aur loop ke andar jo likha hai wo chalao






#::::::::::::::::::Another Example:::::::::::::::
# f =("Sara" , "Junaid" , "Irtiza")
# for data in f:
#     print(data)








   # ________________________tuple padhne ki zaroorat kyu hai?_____________________________
#         Answer==>           Data ko safe rakhne ke liye (Immutable)


# days = ("Monday" , "Tuesday")

#Structured Data store karne ke liye
#Tuple ko use karke multiple values ek sath store kar sakte ho.
#Jaise student ka record:
#student = ("Hafsa", 18, "BSCS")



#/////////////////////////////////////////Lists----------------------------------
#             🔹 List → flexible data structure (mutable)
#                     Bana liya → elements add/remove/update kar sakte ho
# d= {1: "Ela",
#     2: 2}
# list (d.keys()) 
# print (d.keys())


#//////////////////////////////[    "ZIP" -----> the builtin function (pairs bnata ha💀💀)     ]------++++++++===========+++++++++++
#in below given example::::::{{{{{{{{{{{}}}}}}}}}}}
#Now here hamye list ka keyword use krna essential ha wrna tw error ayega 
#cuzz list mutable data ha bd ma change houskta hai isky zariye zip mai data 
a = [1,2,3,4,5]
b = [6,7,8,9,10]
new_data = list(zip(a,b))
print (new_data)






#+++++++++++++++ANOTHER EXAMPLE
# Real World usecase of ZIP:-----> combining column headers with row values

value1 = ["Name" , "id" , "email" , "Depart"]
value2 = ["Ali" , "101" , "alirights@gmail.com" , "BSIT"]
value3= ["Zamal" , "121" , "hehe44" , "BBA"]
new = dict(zip(value1 , value2))
#=...........another syntax ||
print (new)