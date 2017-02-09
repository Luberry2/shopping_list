Options = {}
Options = {
    "0": "Main Menu",
    "1": "Show all lists",
    "2": "show a specific list",
    "3": "add a new shopping  list",
    "4": "add an item to a shopping list",
    "5": "remove an item from a shopping list",
    "6": "remove a list by nickname",
    "7": "Exit when done",
}

shopping_dic = {
                "target": ["shampoo", "apples", "milk"],
                "safeway": ["milk", "butter", "cheese"],
                "birite": ["vanila", "icecream", "chocolate"],  }

answer = raw_input("Please choose 1-6")
if answer == "0":
   print Options

elif answer == "1":
    print shopping_dic

elif answer == "2":
    ask = raw_input ("which list?")
    print shopping_dic[ask]

elif answer == "3":
    ask = raw_input ("what do you want to call a new list?")
    shopping_dic[ask] = []




# shopping_dic = {}

# key_name = raw_input("What would you like to call your new list?: ")
# #key_name is the name of shopping list
# values = raw_input("What would you like to add?: ")
# #values are items for each list

# shopping_dic[key_name] = []
# some_list = ["target", "safeway", "birite"]
# shopping_dic = {
#                 "target": ["shampoo", "apples", "milk"],
#                 "safeway": ["milk", "butter", "cheese"],
#                 "birite": ["vanila", "icecream", "chocolate"],  }
# some_list.append({"walmart":"candy",})
# shopping_dict[some_list] = some_list.append(new_item)



# if answer == "1":
#     some_list = raw_input("What would you like to call your new list?: ")
#     new_items = raw_input("What do you want to add to %s?") %(some_list)
#     shopping_dic[some_list] = new_items

# elif answer == "2":
#     print some_list
