my_mod= 33 % 4
# print(my_mod)
my_quote = 33 // 4
# print(my_quote)

a_num = 32
b_num = 5
check = (a_num == b_num)
# print(check)



#######comparison operators
First_num = 67
Second_num = 21
Quick_check = First_num == Second_num
# print(Quick_check)

first_num = 67
secons_num = 67.00000000001
Quick_check = First_num != Second_num
# print(Quick_check)


######Logical Operations

first_num = 67
second_num = 40
feedback = (first_num % 2 != 0) or (second_num > first_num) and not((second_num == 40) or (second_num // 2!=0))
# print(feedback)

a_num = 60
b_num = 55
result = not (a_num != 78 and b_num == 30)
# print(result)


Career = "she is a model!"
output = "she i" in Career
# print(output)

scores = (62, 55, 72, 89)
check = "62" in scores
# print(check)

####Concatenation
first_phrase = "Hello"
second_phrase = "there, welcome1"
full_sent = first_phrase + " " + second_phrase
# print(full_sent)


Career = "she is a model who lives in california!"
desired_char = Career[7]
# print(desired_char)

new_word = "24", "35", "46", "58", "100"
# print(new_word[3])

new_name = "Blue Sky"
# print(new_name[2:8:4])

age_limit = 10
report_template = "you can't gain access until you are {} years old.". format(age_limit)
# print(report_template)

church_items = "bible"
check = "you need your {} in church". format(church_items)
# print(check)

mood_swings = 'It is john\'s pen'
# print(mood_swings)


Career = "she is a model who lives in california!"
trans_list = Career.split(" ")
# print(trans_list)

career = "He is a medical doctor"
result = career.endswith("doctor")
# print(result)


Career = "she is a model who lives in california!"
desired_career = Career.title()
# print(desired_career)

Career = "she is a model who lives in california!"
trans_list = Career.split(" who ")
# print(trans_list)

new_Career = Career.replace("california", "Texas")
# print(new_Career)

trimmed = Career.strip("ia!")
# print(trimmed)


#########LIST
random_stuffs = ["pawn", "phone", "pen", False, 99.90, 2021, 4+2j]
# print(random_stuffs)

random_stuffs = ["20", "49", "13", "45"]
random_stuffs.remove("13")
# print(random_stuffs)

random_stuffs[1] = "water"
# print(random_stuffs)

random_stuffs[2 : 3: 1] = ["bike", True]
# print(random_stuffs)

first = [34, 58, 55]
second = [2, 13, 47]
first.extend(second)
# print(first)

first_list = ["2", "4", "20",]
second_list = ["5", "12", "30"]
full_list = first_list + second_list
# print(full_list)

random_stuffs.append("file")
# print(random_stuffs)

backup_list = random_stuffs.copy()
# print(backup_list)

random_stuffs.insert(0, "awesome")
# print(random_stuffs)

scores = [12, 38, 29, 15, 40]
scores.sort()
# print(scores)

scores.reverse()
# print(scores)

# print(random_stuffs)
# print("\n")
random_stuffs.reverse()
# print(random_stuffs)

my_pen = 600
cost = 0.5 * my_pen
# print(cost)

#####Set
my_set = {"chair", "34", "67", True, 2021}
my_set.discard("67")
# print(my_set)

my_set.add('39')
# print(my_set)

my_second_set = {"Table", "45", "18", "pen", 2020, "65", "90"}
my_second_set.update(my_set)
# print(my_second_set)

grocery_cart1 = {"Bread", "oranges", " jam", "fruit juice", "eggs", "butter", "cookies"}
grocery_cart2 = {"eggs", "yam", "grapes", "cookies", "apples", "carrot","Bread", "ice cream"}

grocery_cart2.discard("yam")
# print(grocery_cart2)

merge_cart = grocery_cart1.union(grocery_cart2)
# print(merge_cart)

# grocery_cart1.update(grocery_cart2)
# print(grocery_cart1)

backup_cart1 = grocery_cart1.copy()
backup_cart2 = grocery_cart2.copy()
# print(backup_cart1)

cart1_only = grocery_cart1.difference(grocery_cart2)
# print(cart1_only)
cart2_only = grocery_cart2.difference(grocery_cart1)
# print(cart2_only)

grocery_cart2.difference_update(grocery_cart1)
# print(grocery_cart2)

common_groceries = grocery_cart1.intersection(grocery_cart2)
# print(common_groceries)

backup_cart1.intersection_update(backup_cart2)
# print(backup_cart1)

cart2_only = grocery_cart1.isdisjoint(grocery_cart2)
# print(cart2_only)

taking_out_duplicates = grocery_cart1.symmetric_difference(grocery_cart2)
# print(taking_out_duplicates)

cart_3 = grocery_cart1.symmetric_difference_update(grocery_cart2)
# print(cart_3)

cart_4 = grocery_cart1.pop()
# print(cart_4)


####DICTIONARIES
Customer_info = {
    "name" : ["Mike Aubentraut", "Uzo Chuks", "Tom Whiteside", "Mary Jane"],  
"gender" : ["Male", "Male", "Male", "Female"], 
"age" : [23, 29, 34, 18],
"nationality" : ["American", "Nigerian", "Canadian", "Jamaican"]
}

# print(Customer_info)

all_names = Customer_info ["name"]
# print(all_names)

all_nationalities = Customer_info.get("nationality") 
# print(all_nationalities)

all_keys = Customer_info.keys()
# print(all_keys)

all_values = Customer_info.values()
# print(all_values)

all_items = Customer_info.items()
# print(all_items)

Customer_info.update({"Occupation" : ["Actor", "Banker", "Footballer", "Experienced Engineer"]})
# print(Customer_info)

Customer_info.pop("age")
# print(Customer_info)

#####BUILT-IN FUNCTIONS
# get_data = input("Enter data here: ")
# print(get_data)

sports = {"swimming", "football", "boxing", "cricket", "Tenis"}
# sports_count = len(sports)
# print(sports_count)

scores = [20, 40, 50, 4 ]
# print(sum(scores))

# print(min(scores))
# print(max(scores))

# get_data = input ("Enter data here: ")
# # To have access to the integers
# con_list = get_data.split(" ")
# # To change/convert the entries to integers
# con_list[0] = int(con_list[0])
# con_list[1] = int(con_list[1])
# con_list[2] = int(con_list[2])
# con_list[3] = int(con_list[3])
# con_list[4] = int(con_list[4])

# new_list = list(set(con_list))
# new_list.sort()

# output_list = new_list[-2]
# print(output_list)

# con_list.sort()
# print(con_list[3])
# smallest_integer = min(con_list)
# print(smallest_integer)

first_list = ["high", "low", "middle"]
second_list =[1, 2, 3]

# Zipped_object = zip(first_list, second_list)
# print(list(Zipped_object))

first_list = ["high", "low", "middle", "high-lows", "dark space"]
second_list =[1, 2, 3]
# Zipped_object = zip(first_list, second_list)
# print(list(Zipped_object))

Players = ["Ronaldo", "Messi", "Diego", "Okocha"]
output = enumerate(Players)
# print(list(output))

my_adder = lambda x:x + 100
# print(my_adder(1))

double = lambda n:n**2
# print(double(10))

modifier = lambda x : x.upper()
output = modifier ("voice")
# print(output)

modifier = lambda x : x.startswith("voi")
output = modifier ("voice")
# print(output)

my_math = lambda x, y, z : x **2 + y + z
# print(my_math(5, 6, 7))

add = lambda p1, p2: p1 > p2
# print(add(10, 5))

names = ["Jonathan", "John", "Michael", "Nicholas", "Paul"]
# names.sort(key = lambda n: len(n))
# print(names)

mapped_obj = map(lambda x : x + 70, [20, 40, 60])
# print(list(mapped_obj))

words = ["new", "old", "used"]
upgraded = map(lambda a : a + "", words)
# print(list(upgraded))

###Filter
num = [20,31,45,60,10,77]
# my_filter = filter(lambda x : x % 2, num)
# print(list(my_filter))

rand_words = ["Emmanuel", "Pizza", " Coarse", " Smooth", "Laptop", 'Screen']
# my_filter1 = filter(lambda a: "e" in a, rand_words)
# output1 = list(my_filter1)
# print(output1)

####Range
my_num = range(1,8)
# print(list(my_num))

numbers = range(0,10,2)
# print(list(numbers))

####BUILT-IN MODULES
import time
# print("This is line 334")
# time.sleep(5)
# print("done")

##random
import random as rd
# rd.seed(99)
rand_words = ["Emmanuel", "Pizza", "Coarse", "Smooth", "Laptop", 'Screen']
# rd.shuffle(rand_words)
# print(rand_words)

# rand_words_filter = filter(lambda a: len(a) >=7, rand_words)
# print(list(rand_words_filter))
# if len(rand_words_filter) >=1:
#     print("yes")
# else:
#     print("no")


# random_pick = rd.choice(rand_words)
# print(random_pick)

# selected_items = rd.sample(rand_words, k = 3)
# print(selected_items)

# feedback = rd.randrange(14, 44, 2)
# print(feedback)

####DATETIME
from datetime import datetime as dt
current_date_and_time = dt.now()
# print(current_date_and_time)

# current_year = dt.now().year
# print(current_year)

output = current_date_and_time.strftime("%B")
# print(output)

# output = current_date_and_time.strftime("%A%d")
# print(output)

###strptime
ch_day = "25/12/2021"
# converted_data = dt.strptime(ch_day, "%d/%m/%Y")
# print(converted_data.date())


notable_days = ["15/1/2021", "14/2/2021", "1/4/2021", "12/6/2021", "1/10/2021", "25/12/2021"]
new_notable_days = map(lambda a: dt.strptime(a, "%d/%m/%Y").date(), notable_days)
# print(list(new_notable_days))

####CONDITIONAL
# if 100 > 101:
#  print ("Are you sure")  
# else:
#  print("it is less than")

# if 5 > 8 or dt.now().minute % 2 == 0:
#      print("definitely")
# else:
#     pass



# if "e" in "Emmanuel":
#     print("spelt correctly")
# elif 59 > 58.9:
#     print("mathematically correct")
# else:
#     pass


# get_data = input("Enter data here: ")
# print(get_data)
# if len(set(get_data)) != len(get_data):
#     print("duplicates are present")
# else:
#     print("There are no duplicates")

# get_data = input("Enter data here: ")
# print(get_data)
# if "family" in (get_data):
#     print("present")
# else:
#     print("Not present")


####LOOPS
##While loops
# cracker = 1
# while (cracker < 5):
#     if cracker == 3:
#         print("Here is my ride outta the loop!")
#         break
#     else:
#         print("I am in the loop") 
#         # cracker +1


#####Guess Game
# import random as rd
# get_data = input("Enter two integers here: ")
# con_list = get_data.split (" ")
# #Converting to integer
# con_list[0] = int(con_list[0])
# con_list[1] = int(con_list[1])

# #Randomly select an integer within the given range
# random_integer = rd.randrange(con_list[0], con_list[1])

# ##Time to guess
# while True:
#     user_guess = input("Enter your guess here: ")
#     if random_integer == int(user_guess):
#         print("you guessed right!")
#         break
#     elif int(user_guess) < random_integer:
#         print("Guess too low...try again")
#     elif int(user_guess) > random_integer:
#         print("Guee too high... try again")
#     else:
#         pass

# ####For loop
# entry_data = "Universe"
# for letter in entry_data:
#     print("Home for all")

# new_list = ("pop", "rock", "country")
# for items in new_list:
#     print(items)

# scores = [68, 90, 78, 71, 83]
# for num in scores:
    # if num % 2 == 0:
    #     print(f"{num} is an even number")
    # elif num % 2 != 0 :
    #     print("{} is an odd number".format(num))
    # else:
    #     pass

Customer_info = {
    "name" : ["Mike Aubentraut", "Uzo Chuks", "Tom Whiteside", "Mary Jane"],  
"gender" : ["Male", "Male", "Male", "Female"], 
"age" : [23, 29, 34, 18],
"nationality" : ["American", "Nigerian", "Canadian", "Jamaican"]
}

# for entry in Customer_info:
#     print(entry)

# for entry in Customer_info.items():
#     print(entry[1][0])
#     print("\n")

# continents = ["Africa", "Asia", "North America", "South America", "Europe", "Antartica", "Australia"]
# countries = ["Morocco", "China", "USA", "Argentina", "Croatia", "Eskimo", "New Zealand"]

# Zipped_object = zip(countries, continents)
# for entry in Zipped_object:
#     print(entry)

# for country_name, continent_name in Zipped_object:
#     print(country_name)


# get_data = input ("Enter integers here:")
# con_list = get_data.split(" ")
# ###converting to integers
# for num in range(len(con_list)):
#     con_list[num] = int(con_list[num])

# for x in range(len(con_list)):
#     con_list[x] *= 1.1
#     con_list[x] = round(con_list[x], 2)
#     print(con_list)

# get_data = input("Enter any integer here:")
# con_list = get_data.split(" ")
# #converting to integers
# new_list = map(lambda a : int(a), con_list)
#to increment

# output= list(map(lambda a: a * 1.1, new_list))
# print(output)


# output= list(map(lambda a: round( a * 1.1, 2), new_list))
# print(output)

####2-LEVEL NESTED LOOP
# nouns = ["car", "country", "lady"]
# adjectives = ["fast", "beautiful", "awesome"]

# for qualifier in adjectives:
#     for word in nouns:
#         print(qualifier, word)
#         print("\n")


# starters = ["Its", "They are", "They all are"]
# nouns = ["car", "country", "lady"]
# adjectives = ["fast", "beautiful", "awesome"]

# for beginner in starters:
#     for qualifier in adjectives:
#         for word in nouns:
#             print(beginner, qualifier, word)
#     print("\n")

#####LIST COMPREHENSION
scores = [60, 62, 64, 66]
upgraded_scores = [num + 3 for num in scores]
# print(upgraded_scores)

# weird_strutures = [print(num + 3) for num in scores]

new_upgrade = [num + 3 for num in scores if num % 2 == 0]
# print(new_upgrade)





























    




























