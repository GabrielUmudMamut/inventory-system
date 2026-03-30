# ============================================================
# SCHOOL CANTEEN TRACKER
# Helps the canteen know what to cook tomorrow
# ============================================================

import json   # json lets us save and load data from a file
import os     # os lets us check if a file already exists

# ------ SETTINGS ------
SAVE_FILE = "canteen_data.json"   # the file where we store all our data

def load_data():
    if os.path.exists(SAVE_FILE):          # check if the save file is there
        with open(SAVE_FILE, "r") as f:    # open it in read mode
            return json.load(f)            # turn the file contents into a Python list
    return []                              # no file yet? return an empty list

def del_data():
    if os.path.exists(SAVE_FILE):
        os.remove(SAVE_FILE)
    else:
        print("File not found or unsufficient premissions to delete file.")

def clear_screen():
    _ = os.system('cls')

def save_data(data):
    with open(SAVE_FILE, "w") as f:        # open file in write mode (overwrites old content)
        json.dump(data, f, indent=2)       # write the data in a neat, readable format
    print("The data was saved!")

def add_item(data):
    print("\n Add 1 Item")

    name = input("Item name: ").strip().lower()   # get item name, remove spaces, make lowercase

    # keep asking until we get a valid number for 'prepared'
    while True:
        try:
            prepared = int(input(f"How many {name} did you prepare today? "))   # convert to integer
            if prepared < 0:                                            # can't prepare a negative amount of items
                print("Must be 0 or more.")
                continue                                                 # ask again by going back up to the while true:
            break                                                        # number is valid, stop asking                                             # number is valid, stop asking
        except ValueError:                                               # user typed letters instead of a number
            print("Please type a whole number.")

    # keep asking until we get a valid number for 'sold'
    while True:
        try:
            sold = int(input(f"How many {name} did you SELL today? "))
            if sold < 0:
                print("Must be 0 or more.")
                continue                                                 # ask again by going back up to the while true:
            if sold > prepared:                                          # you can't sell more than you made!
                print(f"You can't sell more {name} than you prepared ({prepared}).")
                continue                                                 # ask again by going back up to the while true:
            break                                                        # number is valid, stop asking            
        except ValueError:
            print("Please type a whole number.")

    leftover = prepared - sold   # simple math: what's left over

    # build a dictionary (mini record in other words) for this item
    item = {
        "name": name,
        "prepared": prepared,
        "sold": sold,
        "leftover": leftover
    }

    data.append(item)   # add the record to our main list
    
    print(f"'{name}' added! Leftover: {leftover}")

def view_summary(data):
    print("\n Summary of the items")

    if len(data) == 0:               # no data yet? tell the user
        print("No items recorded yet.")
        return

    total_waste = 0                  # we'll add up all leftovers here

    for item in data:                # loop through every item in the list
        print(f"  {item['name']:15} | Prepared: {item['prepared']:3} | Sold: {item['sold']:3} | Leftover: {item['leftover']:3}")
        total_waste += item['leftover']   # add this item's leftover to the total
        if total_waste > 100:
            print("You are wasting a bunch of stuff!!")

    print(f"\nTotal waste today is {total_waste} items")

def top_wasted(data):
    print("\n Top 3 wasted items.")

    if len(data) == 0:
        print("No data yet.")
        return
    
    # sort the list by the leftover amount, highest first because its top 3. idk how this works too well. ai did this one
    sorted_items = sorted(data, key=lambda x: x['leftover'], reverse=True)   

    # show only the top 3 (or fewer if we have less than 3 items)
    top3 = sorted_items[:3]

    for i, item in enumerate(top3):   # enumerate gives us a counter (0, 1, 2...)
        print(f"  #{i+1} {item['name']} — {item['leftover']} leftover") # the {i+1} is just to number it like in a list. 

def main():
    clear_screen()
    data = load_data()   # load any saved data before showing the menu

    print("=====================================")
    print("Simple School Canteen Item Tracker")
    print("Simple as in it only tracks 1 day's items")
    print("=====================================")

    while True:   # keep showing the menu until the user quits
        print("") # could also add /n to to the string below but i didnt cuz i am tuff
        print("What do you want to do?")
        print("  1 - Add 1 item")
        print("  2 - View summary of all items")
        print("  3 - Top 3 wasted items")
        print("  4 - Delete old save files")
        print("  5 - Save")
        print("  6 - Quit")

        choice = input("\nEnter 1-6: ").strip()   # get user input as a number

        if choice == "1":
            add_item(data)
            save_data(data)
        elif choice == "2":
            view_summary(data)
        elif choice == "3":
            top_wasted(data)
        elif choice == "4":
            del_data()
        elif choice == "5":
            save_data(data)
        elif choice == "6":
            print("Bye bye!")
            break             # exit the while loop, ending the program
        elif choice == "7":
            print("super secret easter egg made by Gabriel.")
        else:
            print("You typed smth invalid, try again. Choose a choice between 1 and 6.")

# only run if being run directly. not imported or smth like that.
if __name__ == "__main__":
    main()