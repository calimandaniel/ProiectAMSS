import os
from tkinter import *
import tkinter.messagebox
from PIL import Image
import customtkinter
import mysql.connector
import main_page
import register
from connected_user import ConnectedUser

connectiondb = mysql.connector.connect(host='localhost',
                                       database='logindb',
                                       user='root',
                                       password='1q2w3e')
cursordb = connectiondb.cursor()

curr_user = None


DARK_GREY = '#121212'
MEDIUM_GREY = '#1F1B24'
OCEAN_BLUE = '#464EB8'
WHITE = "white"
FONT = ("Helvetica", 17)
BUTTON_FONT = ("Helvetica", 15)
SMALL_FONT = ("Helvetica", 13)



def login():
    global root2
    root2 = Toplevel(root)
    root2.title("Account Login")
    root2.geometry("440x500")
    root2.config(bg=MEDIUM_GREY)
    root2.grid_rowconfigure(0, weight=3)
    root2.grid_rowconfigure(1, weight=1)
    root2.grid_rowconfigure(2, weight=2)
    root2.grid_rowconfigure(3, weight=1)
    root2.grid_rowconfigure(4, weight=2)
    root2.grid_rowconfigure(5, weight=2)

    global username_verification
    global password_verification

    app_name_label = customtkinter.CTkLabel(root2, text="  Please Enter your Account Details",
                                            compound="left",
                                            font=customtkinter.CTkFont(size=25, weight="bold"))
    app_name_label.grid(row=0)

    username_verification = StringVar()
    password_verification = StringVar()

    user_name_label = customtkinter.CTkLabel(root2, text="Username:",
                                            compound="left",
                                            font=customtkinter.CTkFont(size=15))
    user_name_label.grid(row=1, sticky="s")

    user_name_textbox = customtkinter.CTkEntry(root2, height=30, textvariable=username_verification)
    user_name_textbox.grid(row=2, sticky="n")

    password_label = customtkinter.CTkLabel(root2, text="Password:",
                                             compound="left",
                                             font=customtkinter.CTkFont(size=15))
    password_label.grid(row=3, sticky="s")

    password_textbox = customtkinter.CTkEntry(root2, height=30, textvariable=password_verification, show="*")
    password_textbox.grid(row=4, sticky="n")

    login_button = customtkinter.CTkButton(root2, corner_radius=0, height=40, border_spacing=10,
                                          text="   Login",
                                          font=customtkinter.CTkFont(size=25, weight="bold"),
                                          fg_color="transparent", text_color=("gray10", "gray90"),
                                          hover_color=("gray70", "gray30"),
                                          anchor="w", command=login_verification)
    login_button.grid(row=5)


def logged_destroy():
    root2.destroy()
    root.destroy()
    global curr_user
    app = main_page.App(curr_user)
    app.mainloop()


def register_function():
    register.register_page(root)


def failed_destroy():
    failed_message.destroy()

def failed():
    global failed_message
    failed_message = Toplevel(root2)
    failed_message.title("Invalid Message")
    failed_message.geometry("500x100")
    Label(failed_message, text="Invalid Username or Password", fg="red", font="bold").pack()
    Label(failed_message, text="").pack()
    Button(failed_message, text="Ok", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'),
           command=failed_destroy).pack()


def login_verification():
    user_verification = username_verification.get()
    pass_verification = password_verification.get()
    sql = "select * from person where username = %s and user_password = %s"
    cursordb.execute(sql, [(user_verification), (pass_verification)])
    results = cursordb.fetchall()

    if results:
        for i in results:
            global curr_user
            curr_user = ConnectedUser(results[0][3], results[0][4], results[0][5], results[0][6], results[0][7],
                                      results[0][8], results[0][9])
            logged_destroy()
            break
    else:
        failed()


def Exit():
    wayOut = tkinter.messagebox.askyesno("Login System", "Do you want to exit the system")
    if wayOut > 0:
        root.destroy()
        return


def main_display():
    global root
    root = Tk()
    root.config(bg=MEDIUM_GREY)
    root.title("Login System")
    root.geometry("440x500")

    root.grid_rowconfigure(0, weight=2)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_rowconfigure(3, weight=1)

    app_name_label = customtkinter.CTkLabel(root, text="  Home management platform",
                                                         compound="left",
                                                         font=customtkinter.CTkFont(size=30, weight="bold"))
    app_name_label.grid(row=0)
    image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "theme_images")
    login_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "login1.png")),
                                             dark_image=Image.open(os.path.join(image_path, "login1.png")),
                                             size=(30, 30))

    login_button = customtkinter.CTkButton(root, corner_radius=0, height=40, border_spacing=10,
                                               text="Log in",
                                               font=customtkinter.CTkFont(size=25, weight="bold"),
                                               fg_color="transparent", text_color=("gray10", "gray90"),
                                               hover_color=("gray70", "gray30"),
                                               image=login_image, anchor="w", command=login)
    login_button.grid(row=1)

    register_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "register.png")),
                                        dark_image=Image.open(os.path.join(image_path, "register.png")),
                                        size=(30, 30))

    register_button = customtkinter.CTkButton(root, corner_radius=0, height=40, border_spacing=10,
                                          text="Register",
                                          font=customtkinter.CTkFont(size=25, weight="bold"),
                                          fg_color="transparent", text_color=("gray10", "gray90"),
                                          hover_color=("gray70", "gray30"),
                                          image=register_image, anchor="w", command=register_function)
    register_button.grid(row=2)

    exit_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "register.png")),
                                            dark_image=Image.open(os.path.join(image_path, "register.png")),
                                            size=(30, 30))

    exit_button = customtkinter.CTkButton(root, corner_radius=0, height=40, border_spacing=10,
                                              text="Exit",
                                              font=customtkinter.CTkFont(size=25, weight="bold"),
                                              fg_color="transparent", text_color=("gray10", "gray90"),
                                              hover_color=("gray70", "gray30"),
                                              image=exit_image, anchor="w", command=Exit)
    exit_button.grid(row=3)


if __name__ == "__main__":
    main_display()
    root.mainloop()
