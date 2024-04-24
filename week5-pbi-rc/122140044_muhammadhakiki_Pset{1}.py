import tkinter as tk
from tkinter import messagebox

class Login:
    def __init__(self):
        self.kotak_masuk = tk.Tk()
        self.kotak_masuk.title('Login')
        self.kotak_masuk.geometry('300x200')
        self.username = tk.StringVar()
        self.password = tk.StringVar()

        tk.Label(self.kotak_masuk, text='username:').pack()
        tk.Entry(self.kotak_masuk, textvariable=self.username).pack()
        tk.Label(self.kotak_masuk, text='password:').pack()
        tk.Entry(self.kotak_masuk, textvariable=self.password, show='*').pack()
        tk.Button(self.kotak_masuk, text='Login', command=self.checking).pack()
        tk.Button(self.kotak_masuk, text='Register', command=self.open_reg).pack()

        self.users = {'Hakiki12': 'tiocell2', 'lopek': 'baliindah'}

    def open_reg(self):
        self.kotak_masuk.withdraw()  # Hide login window
        self.kotak_register = Register(self.kotak_masuk, self.users)
        self.kotak_register.jendela.protocol("WM_DELETE_WINDOW", lambda: self.on_register_close())
        self.kotak_register.jendela.mainloop()

    def on_register_close(self):
        self.kotak_masuk.deiconify()  # Show login window when register window closes

    def checking(self):
        if self.username.get() in self.users and self.password.get() == self.users[self.username.get()]:
            messagebox.showinfo('Successful', 'Anjay berhasil login bos')
        else:
            messagebox.showerror('Error', 'Salah pw/usename nya cs')

    def run(self):
        self.kotak_masuk.mainloop()

class Register:
    def __init__(self, master, users):
        self.master = master
        self.jendela = tk.Toplevel()
        self.jendela.title('Register')
        self.jendela.geometry('300x300')

        self.users = users
        self.register_nama = tk.StringVar()
        self.register_pw = tk.StringVar()
        self.confirm = tk.StringVar()

        tk.Label(self.jendela, text='Username:').pack()
        tk.Entry(self.jendela, textvariable=self.register_nama).pack()
        tk.Label(self.jendela, text='Password:').pack()
        tk.Entry(self.jendela, textvariable=self.register_pw).pack()
        tk.Label(self.jendela, text='Confirm Password:').pack()
        tk.Entry(self.jendela, textvariable=self.confirm).pack()

        tk.Button(self.jendela, text='Register', command=self.tombol_register).pack()

    def tombol_register(self):
        if self.register_pw.get() == self.confirm.get():
            if not self.ada_username(self.register_nama.get()):
                self.users[self.register_nama.get()] = self.register_pw.get()
                messagebox.showinfo(' ANJAY Registrasi Berhasil', 'BOS berhasil registrasi akun')

                 # Close register window after successful registration
            else:
                messagebox.showerror('Register Gagal', 'Username anda sudah digunakan')
        else:
            messagebox.showerror('Error', 'Tidak Sesuai')

    def ada_username(self, username):
        return username in self.users


login = Login()
login.run()
