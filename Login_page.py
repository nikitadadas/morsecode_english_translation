from tkinter import *
import time
import subprocess

users = {
    'nikita': 'dadas',
    'sakshi': 'realme',
    'siddhi': 'realme1',
    'vidhya': 'realme2',
    'minal': 'realme3',
    'prathamesh': 'iphone',
}

def login():
    # check if the username and password are correct
    if username.get() in users and password.get() == users[username.get()]:
        # log the login event with the timestamp
        log_file.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")} User {username.get()} logged in successfully\n')
        
        # open the existing application
        # call your existing application
        subprocess.call(['python', 'main_page.py', '--username', username.get()])
        
    else:
        # log the login failure event with the timestamp
        log_file.write(f'{time.strftime("%Y-%m-%d %H:%M:%S")} Login failed for user {username.get()}\n')
        
        # show an error message
        error_label.config(text='Invalid username or password')

def on_closing():
    # close the log file
    log_file.close()
    
    # destroy the main window
    root.destroy()

# create the main window
root = Tk()
root.title('Login')
root.geometry('300x150')

# create the username and password labels and entry fields
username_label = Label(root, text='Username:')
username_label.grid(row=0, column=0, padx=10, pady=10)
username = Entry(root)
username.grid(row=0, column=1)

password_label = Label(root, text='Password:')
password_label.grid(row=1, column=0, padx=10, pady=10)
password = Entry(root, show='*')
password.grid(row=1, column=1)

# create the login button
login_button = Button(root, text='Login', command=login)
login_button.grid(row=2, column=0, columnspan=2)

# create the error label
error_label = Label(root, fg='red')
error_label.grid(row=3, column=0, columnspan=2)

# open the log file
log_file = open('db_add.log', 'a')

# bind the on_closing function to the "WM_DELETE_WINDOW" event
root.protocol("WM_DELETE_WINDOW", on_closing)

# start the main event loop
root.mainloop()
