#...................................import....................................
import json
import os
#..................................path.................................
path = "/storage/emulated/0/Python learning/things made by Siddharth/habits.txt"
#................................data handling.............................
def load_data():
    if os.path.exists(path):
        with open(path, "r") as file:
            return json.load(file)
    else:
        return {}
def save_data(data):
    with open(path, "w") as file:
        json.dump(data, file, indent = 4)
#.................................core features................................
def add_habit():
        habit_name = input("Add habit: ")
        data = load_data()
        if habit_name in data:
            print("This habit already exists")
        else:
            data[habit_name] = {"streak": 0}
            save_data(data)
def mark_done():
        habit_mark = input("Enter name of the habit: ")
        data = load_data()
        data[habit_mark]["streak"] += 1
        save_data(data)
        print("Streak updated: ", data[habit_mark]["streak"])
def view_habits():
        print("Showing habits.........")
        data = load_data()
        print(data)
def delete_habit():
        delete_mark = input("Enter habit name: ")
        data = load_data()
        del data[delete_mark]
        print("Habit deleted")
        save_data(data)
def exit():
        print("Bye")
#................................menu.............................
def menu():
        print("\n1) Add habit")
        print("2) Mark done")
        print("3) View habits")
        print("4) Delete habit")
        print("5) Exit")
        while True:
            user = input("Enter your choice")
            if(user in ["1", "2", "3", "4", "5"]):
                return user
            else:
                print("Invalid")
#..................................main...........................
def main():
        while True:
            user = menu()
            
            if(user == "1"):
                add_habit()
            elif(user == "2"):
                mark_done()
            elif(user == "3"):
                view_habits()
            elif(user == "4"):
                delete_habit()
            elif(user == "5"):
                exit()
                break
main()
        
        
        