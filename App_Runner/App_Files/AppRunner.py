from tkinter import *
from tkinter import filedialog
import os

app_list = []
path_list = []
delete = 0


# Adds apps on to the screen
def add_apps():
    for app in app_list:
        label = Label(frame, text=app, bg='#cce5ed', fg='black', font='Arial, 12')
        label.pack(anchor='center')


# Allows user to open file explorer to select files
def open_file():
    filename = filedialog.askopenfilename(initialdir='C:/', title='Select File',
                                          filetypes=(('Executables', '*.exe'), ('All Files', '*.*')))
    tail = os.path.split(filename)  # splits the path
    new_filename = tail[1]  # Assigns the final part of the path to this variable
    app_list.append(new_filename)
    path_list.append(filename)

    for widget in frame.winfo_children():
        widget.destroy()

    add_apps()


# Runs all the apps that are stored in path_list
def run_apps():
    for app in path_list:
        os.startfile(app)


# Deletes all apps on the frame
def delete_apps():
    for widget in frame.winfo_children():
        widget.destroy()
    label = Label(frame, text="Restart App For Full Deletion", bg='#cce5ed', fg='red', font='Arial, 12')
    label.pack(anchor='center')
    global delete
    delete += 1


# Opens a new file and saves all the files that are stored in the app_list
def file_saver():
    with open('save.txt', 'w') as f:
        for app in app_list:
            f.write(app + ',')


if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        app_list = [x for x in tempApps if x.strip()]
# ================================================================
# GUI
root = Tk()
root.geometry('500x600')
root.title("App Runner")
# root.iconbitmap('C:/Python_Projects/App_Runner/App_Files/App_Icon.ico')

main_color = '#1e5a8f'

canvas = Canvas(root, bg=main_color)
canvas.place(relwidth=1, relheight=0.9)

frame = Frame(canvas, bg='#cce5ed')
frame.place(relwidth=0.8, relheight=0.8, rely=0.1, relx=0.1)

buttons = ["Open File", "Run Apps", "Delete Apps"]
relx = 0.2

for i in buttons:
    if i == "Open File":
        x = open_file
    elif i == "Run Apps":
        x = run_apps
    else:
        x = delete_apps

    button = Button(root, text=i, bg=main_color, fg='white', font='Arial,20', command=x)
    button.place(relwidth=0.2, relheight=0.1, rely=0.9, relx=relx)
    relx += 0.2

add_apps()

root.mainloop()

if delete == 0:
    file_saver()
else:
    if os.path.isfile('save.txt'):
        os.remove('save.txt')
