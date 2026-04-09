from tkinter import *
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@sql.01",  
    database="login_credentials"
)
cursor = db.cursor()

root = Tk()
root.title("Login Screen")



username_Label = Label(root, text="Username" )
username_entry = Entry(root)
password_Label =  Label(root, text="Password") 
password_entry = Entry(root, show="*")
username_Label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
password_Label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
username_entry.grid(row=0, column=1, padx=10, pady=10)
password_entry.grid(row=1, column=1, padx=10, pady=10)

def login():
    Username = username_entry.get()
    Password = password_entry.get()
    print("Username:", Username)
    print("Password:", Password)
    query = "SELECT * FROM users WHERE username=%s"
    cursor.execute(query, (Username,))
    existing_user = cursor.fetchone()
    if existing_user:
        if Password == existing_user[2]:
            print("Login sucessful!")
            user_id = existing_user[0]
            tasks = Toplevel(root)
            tasks.title("Your Tasks")
            tasks.geometry("500x400")
            
            task_listbox = Listbox(tasks, width=50)
            task_listbox.pack(pady = 20)
            cursor.execute("Select task_text from tasks where user_id=%s", (user_id,))
            tasks_data = cursor.fetchall()

            for task in tasks_data:
                task_listbox.insert(END, task[0])

            task_entry = Entry(tasks, width=40)
            task_entry.pack()
            def add_task():
                task = task_entry.get()
                print("Tasks are:", task)
                if task != "":
                    query = "Insert into tasks (user_id, task_text) values (%s, %s)"
                    cursor.execute(query, (user_id, task))
                    db.commit()

                    task_listbox.insert(END, task)

                    task_entry.delete(0, END)


            add_button = Button(tasks, text = "Add Task", command=add_task)
            add_button.pack(pady=5)

            def delete_task():

                selected_task = task_listbox.get(ACTIVE)
                query = "Delete from tasks where user_id=%s AND task_text=%s"
                cursor.execute(query, (user_id, selected_task))
                db.commit()

                task_listbox.delete(ACTIVE)
            delete_button = Button(tasks, text="Delete Task", command=delete_task)
            delete_button.pack(pady=5)

            def edit_task():
                old_task = task_listbox.get(ACTIVE)

                new_task = task_entry.get()
                if new_task != "":
                    query = "Update tasks Set task_text=%s where user_id = %s and task_text = %s"
                    cursor.execute(query, (new_task, user_id, old_task))
                    db.commit()

                    task_listbox.delete(ACTIVE)
                    task_listbox.insert(END, new_task)
            edit_button = Button(tasks, text="Edit TASK", command=edit_task)
            edit_button.pack(pady=5)

        else:
            print("Invalid Password!")

    else:
        insert_query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor.execute(insert_query, (Username, Password))
        db.commit()
        print("User registered sucessfully")

login_button = Button(root, text="Login", command=login)
login_button.grid(row=2, column=1, pady=10)


root.mainloop()