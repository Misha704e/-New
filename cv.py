import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark")  # або "light"
ctk.set_default_color_theme("blue")

# Головне вікно
app = ctk.CTk()
app.title("Логін")
app.geometry("400x300")

# Функція для збереження даних
def sav_log():
    username = entry_usern.get()
    password = entry_passw.get()

    if username and password:
        with open("user_d.txt", "a") as file:
            file.write(f"Username: {username}, Password: {password}\n")
        messagebox.showinfo("Успіх", "Дані збережено!")
        entry_usern.delete(0, ctk.END)
        entry_passw.delete(0, ctk.END)
    else:
        messagebox.showwarning("Помилка", "Будь ласка, введіть логін та пароль")

# Віджети
label_title = ctk.CTkLabel(app, text="Вхід у систему", font=("Arial", 20))
label_title.pack(pady=20)

entry_usern = ctk.CTkEntry(app, placeholder_text="Логін")
entry_usern.pack(pady=10)

entry_passw = ctk.CTkEntry(app, placeholder_text="Пароль", show="*")
entry_passw.pack(pady=10)

btn_login = ctk.CTkButton(app, text="Увійти", command=sav_log)
btn_login.pack(pady=20)

app.mainloop()
