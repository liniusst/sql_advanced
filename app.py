from main import Users
from session import session
import tkinter as tk

window = tk.Tk()

selection = tk.Label(
    text="Select action: \n1 - Add new user \n2 - View all users \n3 - Update user \n4 - Remove user \n5 - Exit",
    fg="white",
    width=25,
    height=10,
)
selection.pack()

first_button = tk.Button(window, text="Add new user", width=25)
first_button.pack()
second_button = tk.Button(window, text="Add new user", width=25)
second_button.pack()
third_button = tk.Button(window, text="Update user", width=25)
third_button.pack()
fourth_button = tk.Button(window, text="Remove user", width=25)
fourth_button.pack()

window.mainloop()

while True:
    # print(
    #     "Select action: \n1 - Add new user \n2 - View all users \n3 - Update user \n4 - Remove user \n5 - Exit"
    # )
    choice = int(input("Your selection: "))
    if choice == 1:
        name = input("Enter user name: ")
        surname = input("Enter user surname: ")
        date_of_birth = input("Enter date of birth: ")
        salary = int(input("Enter user salary: "))
        user_data = Users(name, surname, date_of_birth, salary)
        session.add(user_data)
        session.commit()

    if choice == 2:
        users = session.query(Users).all()
        print("-------------------")
        for user in users:
            print(user)
        print("-------------------")

    if choice == 3:
        users = session.query(Users).all()
        print("-------------------")
        for user in users:
            print(users)
        print("-------------------")
        user_id = int(input("Select user ID for update: "))
        updating_user = session.query(Users).get(user_id)
        print(
            "What you want to update \n1 - name \n2 - surname \n3 - date of birth \n4 - salary"
        )
        update_choice = int(input("Your selection: "))
        if update_choice == 1:
            updating_user.name = input("Enter new value: ")
        if update_choice == 2:
            updating_user.surname = input("Enter new value: ")
        if update_choice == 3:
            updating_user.date_of_birth = input("Enter new value: ")
        if update_choice == 4:
            updating_user.salary = input("Enter new value: ")
        session.commit()

    if choice == 4:
        users = session.query(Users).all()
        print("-------------------")
        for user in users:
            print(user)
        print("-------------------")
        selected_user_id = int(input("Select user by ID: "))
        select_to_delete = session.query(Users).get(selected_user_id)
        session.delete(select_to_delete)
        session.commit()

    if choice == 5:
        break
