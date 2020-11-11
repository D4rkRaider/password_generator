from tkinter import *
from tkinter import ttk
import random
import string


class App(object):

    def __init__(self):
        self.root = Tk()  # create window
        self.root.iconbitmap("./icon.ico")
        self.root.title("Password Generator")  # set window title
        self.root.geometry("276x120")  # set window geometry
        self.root.resizable(width=False, height=False)  # set window resizable to False
        self.style = ttk.Style()  # create style
        self.style.theme_use("vista")  # set theme

        self.frm = ttk.Frame(self.root)
        self.frm.pack(expand=True, fill="both")

        self.PasswordLength, self.Strength, self.RandomPassword = IntVar(), StringVar(), StringVar()

        # Create ComboBox For Password Length
        self.PwdLength = ttk.Combobox(self.frm, values=list(num for num in range(8, 257)), state="readonly",
                                      textvariable=self.PasswordLength,
                                      width=15)
        self.PwdLength.set("Length")
        self.PwdLength.place(x=19, y=15)

        # Create ComboBox For Password Strength
        self.PwdStrength = ttk.Combobox(self.frm, values=["weak", "common", "strong"], state="readonly",
                                        textvariable=self.Strength, width=15)
        self.PwdStrength.set("Strength")
        self.PwdStrength.place(x=141, y=15)

        # Create Button
        self.btn = ttk.Button(self.frm, text="Generate", command=self.Generate, width=38)
        self.btn.place(x=19, y=45)

        # Create Entry
        self.password = ttk.Entry(self.frm, textvariable=self.RandomPassword, width=38)
        self.password.place(x=19, y=85)

    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation

    def Generate(self):
        length = self.PasswordLength.get()  # get password length
        strength = self.Strength.get()  # get password strength

        if strength == "weak":
            self.RandomPassword.set(self.GenerateWeak(length=length))

        elif strength == "common":
            self.RandomPassword.set(self.GenerateCommon(length=length))

        elif strength == "strong":
            self.RandomPassword.set(self.GenerateStrong(length=length))

    # Weak Password Generator
    def GenerateWeak(self, length):
        chars = self.letters
        pwd = "".join(random.choices(chars, k=length))
        return pwd

    # Common Password Generator
    def GenerateCommon(self, length):
        chars = self.letters + self.digits
        pwd = "".join(random.choices(chars, k=length))
        return pwd

    # Strong Password Generator
    def GenerateStrong(self, length):
        chars = self.letters + self.digits + self.punctuation
        pwd = "".join(random.choices(chars, k=length))
        return pwd


app = App()
app.root.mainloop()
