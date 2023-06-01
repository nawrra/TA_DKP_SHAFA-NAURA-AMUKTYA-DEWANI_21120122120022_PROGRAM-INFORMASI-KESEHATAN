import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta


class LoginPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("LOGIN")
        self.geometry("300x200")
        self.stack = []

        label_username = tk.Label(self, text="Username:")
        label_username.pack()

        self.entry_username = tk.Entry(self)
        self.entry_username.pack()

        label_password = tk.Label(self, text="Password:")
        label_password.pack()

        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack()

        button_login = tk.Button(self, text="LOGIN", command=self.login)
        button_login.pack(pady=10)

        button_register = tk.Button(self, text="REGISTER", command=self.register)
        button_register.pack()

    def login(self):
        username = self.get_username()
        password = self.get_password()
        if username == "nau" and password == "022":
            self.destroy()
            registration_form_login = RegistrationFormLogin(previous_ui=LoginPage)
            registration_form_login.show_form()
        else:
            messagebox.showerror("LOGIN GAGAL", "Terjadi kesalahan saat memasukkan username atau password!")

    def register(self):
        self.destroy()
        registration_form = RegistrationForm(self)
        registration_form.show_form()

    def set_username(self, username):
        self.entry_username.delete(0, tk.END)
        self.entry_username.insert(tk.END, username)

    def get_username(self):
        return self.entry_username.get()

    def set_password(self, password):
        self.entry_password.delete(0, tk.END)
        self.entry_password.insert(tk.END, password)

    def get_password(self):
        return self.entry_password.get()


class RegistrationFormLogin(tk.Tk):
    def __init__(self, previous_ui):
        super().__init__()
        self.title("PROFILE")
        self.geometry("300x350")
        self.stack = []
        self.previous_ui = previous_ui

        label_nama = tk.Label(self, text="Nama:")
        label_nama.pack()

        self.entry_nama = tk.Entry(self)
        self.entry_nama.pack()

        label_umur = tk.Label(self, text="Umur:")
        label_umur.pack()

        self.entry_umur = tk.Entry(self)
        self.entry_umur.pack()

        label_jk = tk.Label(self, text="Jenis Kelamin:")
        label_jk.pack()

        self.jenis_kelamin = tk.StringVar()
        self.jenis_kelamin.set("str")

        rb_pria = tk.Radiobutton(self, text="Pria", variable=self.jenis_kelamin, value="Pria")
        rb_pria.pack()

        rb_wanita = tk.Radiobutton(self, text="Wanita", variable=self.jenis_kelamin, value="Wanita")
        rb_wanita.pack()

        label_berat_badan = tk.Label(self, text="Berat Badan (kg):")
        label_berat_badan.pack()

        self.entry_berat_badan = tk.Entry(self)
        self.entry_berat_badan.pack()

        label_tinggi_badan = tk.Label(self, text="Tinggi Badan (cm):")
        label_tinggi_badan.pack()

        self.entry_tinggi_badan = tk.Entry(self)
        self.entry_tinggi_badan.pack()

        button_back = tk.Button(self, text="Back", command=self.go_back)
        button_back.pack(pady=10)
        
        button_register = tk.Button(self, text="SUBMIT", command=self.register)
        button_register.pack()

    def go_back(self):
        self.destroy()
        self.previous_ui().show_form()    
    
    def register(self):
        nama = self.get_nama()
        umur = self.get_umur()
        jenis_kelamin = self.get_jenis_kelamin()
        berat_badan = self.get_berat_badan()
        tinggi_badan = self.get_tinggi_badan()

        if not all([nama, umur, jenis_kelamin, berat_badan, tinggi_badan]):
            messagebox.showerror("REGISTER GAGAL", "Harap isi semua kolom!")
            return

        if not self.is_numeric(umur) or not self.is_numeric(berat_badan) or not self.is_numeric(tinggi_badan):
            messagebox.showerror("REGISTER GAGAL", "Umur, berat badan, dan tinggi badan harus berupa angka!")
            return

        umur = int(umur)
        berat_badan = float(berat_badan)
        tinggi_badan = float(tinggi_badan)
        self.destroy()
        health_options = HealthOptions()
        health_options.show_options()

    def set_nama(self, nama):
        self.entry_nama.delete(0, tk.END)
        self.entry_nama.insert(tk.END, nama)

    def get_nama(self):
        return self.entry_nama.get()

    def set_umur(self, umur):
        self.entry_umur.delete(0, tk.END)
        self.entry_umur.insert(tk.END, umur)

    def get_umur(self):
        return self.entry_umur.get()

    def set_jenis_kelamin(self, jenis_kelamin):
        self.jenis_kelamin.set(jenis_kelamin)

    def get_jenis_kelamin(self):
        return self.jenis_kelamin.get()

    def set_berat_badan(self, berat_badan):
        self.entry_berat_badan.delete(0, tk.END)
        self.entry_berat_badan.insert(tk.END, berat_badan)

    def get_berat_badan(self):
        return self.entry_berat_badan.get()

    def set_tinggi_badan(self, tinggi_badan):
        self.entry_tinggi_badan.delete(0, tk.END)
        self.entry_tinggi_badan.insert(tk.END, tinggi_badan)

    def get_tinggi_badan(self):
        return self.entry_tinggi_badan.get()
    
    def is_numeric(self,value):
        try:
            float(value)
            return True
        except ValueError:
            return False


class RegistrationForm(tk.Tk):
    def __init__(self, previous_ui):
        super().__init__()
        self.title("REGISTER")
        self.geometry("300x400")
        self.stack = []
        self.previous_ui = previous_ui

        label_username = tk.Label(self, text="Username:")
        label_username.pack()

        self.entry_username = tk.Entry(self)
        self.entry_username.pack()

        label_password = tk.Label(self, text="Password:")
        label_password.pack()

        self.entry_password = tk.Entry(self, show="*")
        self.entry_password.pack()       

        label_nama = tk.Label(self, text="Nama:")
        label_nama.pack()

        self.entry_nama = tk.Entry(self)
        self.entry_nama.pack()

        label_umur = tk.Label(self, text="Umur:")
        label_umur.pack()

        self.entry_umur = tk.Entry(self)
        self.entry_umur.pack()

        label_jk = tk.Label(self, text="Jenis Kelamin:")
        label_jk.pack()

        self.jenis_kelamin = tk.StringVar()
        self.jenis_kelamin.set(str)

        rb_pria = tk.Radiobutton(self, text="Pria", variable=self.jenis_kelamin, value="Pria")
        rb_pria.pack()

        rb_wanita = tk.Radiobutton(self, text="Wanita", variable=self.jenis_kelamin, value="Wanita")
        rb_wanita.pack()

        label_berat_badan = tk.Label(self, text="Berat Badan (kg):")
        label_berat_badan.pack()

        self.entry_berat_badan = tk.Entry(self)
        self.entry_berat_badan.pack()

        label_tinggi_badan = tk.Label(self, text="Tinggi Badan (cm):")
        label_tinggi_badan.pack()

        self.entry_tinggi_badan = tk.Entry(self)
        self.entry_tinggi_badan.pack()

        button_register = tk.Button(self, text="REGISTER", command=self.register)
        button_register.pack(pady=10)

    def register(self):
        nama = self.get_nama()
        umur = self.get_umur()
        jenis_kelamin = self.get_jenis_kelamin()
        berat_badan = self.get_berat_badan()
        tinggi_badan = self.get_tinggi_badan()

        if not all([nama, umur, jenis_kelamin, berat_badan, tinggi_badan]):
            messagebox.showerror("REGISTER GAGAL", "Harap isi semua kolom!")
            return

        if not self.is_numeric(umur) or not self.is_numeric(berat_badan) or not self.is_numeric(tinggi_badan):
            messagebox.showerror("REGISTER GAGAL", "Umur, berat badan, dan tinggi badan harus berupa angka!")
            return

        umur = int(umur)
        berat_badan = float(berat_badan)
        tinggi_badan = float(tinggi_badan)
        self.destroy()
        health_options = HealthOptions()
        health_options.show_options()

    def set_nama(self, nama):
        self.entry_nama.delete(0, tk.END)
        self.entry_nama.insert(tk.END, nama)

    def get_nama(self):
        return self.entry_nama.get()

    def set_umur(self, umur):
        self.entry_umur.delete(0, tk.END)
        self.entry_umur.insert(tk.END, umur)

    def get_umur(self):
        return self.entry_umur.get()

    def set_jenis_kelamin(self, jenis_kelamin):
        self.jenis_kelamin.set(jenis_kelamin)

    def get_jenis_kelamin(self):
        return self.jenis_kelamin.get()

    def set_berat_badan(self, berat_badan):
        self.entry_berat_badan.delete(0, tk.END)
        self.entry_berat_badan.insert(tk.END, berat_badan)

    def get_berat_badan(self):
        return self.entry_berat_badan.get()

    def set_tinggi_badan(self, tinggi_badan):
        self.entry_tinggi_badan.delete(0, tk.END)
        self.entry_tinggi_badan.insert(tk.END, tinggi_badan)

    def get_tinggi_badan(self):
        return self.entry_tinggi_badan.get()
    
    def is_numeric(self,value):
        try:
            float(value)
            return True
        except ValueError:
            return False


class HealthOptions(tk.Tk):
    def __init__(self,previous_ui=None):
        super().__init__()
        self.title("INFORMASI KESEHATAN")
        self.geometry("300x200")
        self.stack = []
        self.previous_ui = previous_ui

        label_pilihan = tk.Label(self, text="PILIH INFORMASI!", font=("Arial", 14))
        label_pilihan.pack(pady=20)

        button_prediksi_menstruasi = tk.Button(self, text="PREDIKSI MENSTRUASI", width=20, command=self.show_hari_terakhir_menstruasi_form)
        button_prediksi_menstruasi.pack(pady=5)

        button_kalkulator_bmi = tk.Button(self, text="KALKULATOR BMI", width=20, command=self.show_bmi_calculator)
        button_kalkulator_bmi.pack(pady=5)

        button_informasi_kalori = tk.Button(self, text="AKTIVITAS-GOALS", width=20, command=self.show_calorie_info_form)
        button_informasi_kalori.pack(pady=5)

    def show_hari_terakhir_menstruasi_form(self):
        self.destroy()
        menstruasi = MenstruasiForm(previous_ui=self)
        menstruasi.show_form()

    def show_bmi_calculator(self):
        self.destroy()
        bmi_calculator = BMICalculator(previous_ui=self)
        bmi_calculator.show_calculator()

    def show_calorie_info_form(self):
        self.destroy()
        calorie_info_form = CalorieInfoForm(previous_ui=self)
        calorie_info_form.show_form()


class MenstruasiForm(tk.Tk):
    def __init__(self, previous_ui=None):
        super().__init__()
        self.title("PREDIKSI MENSTRUASI")
        self.geometry("300x150")
        self.stack = []
        self.previous_ui = previous_ui

        label_terakhir = tk.Label(self, text="Tanggal Terakhir Menstruasi")
        label_terakhir.pack()

        self.entry_terakhir = tk.Entry(self)
        self.entry_terakhir.pack()

        button_submit = tk.Button(self, text="Submit", command=self.predict_menstruation)
        button_submit.pack(pady=10)

        button_back = tk.Button(self, text="Back", command=self.go_back)
        button_back.pack(pady=5)

    def predict_menstruation(self):
        last_period = self.entry_terakhir.get()
        try:
            last_period_date = datetime.strptime(last_period, "%d/%m/%Y")
            next_period_date = last_period_date + timedelta(days=28)
            messagebox.showinfo("PREDIKSI MENSTRUASI", f"Menstruasi Anda berikutnya diperkirakan pada {next_period_date.strftime('%d/%m/%Y')}")
        except ValueError:
            messagebox.showerror("ERRORRR", "Kesalahan Memasukkan Tanggal!")

    def go_back(self):
        if self.previous_ui:
            self.destroy()
            menstruasi_form = HealthOptions()
            menstruasi_form.show_options

    
class BMICalculator(tk.Tk):
    def __init__(self, previous_ui):
        super().__init__()
        self.title("KALKULATOR BMI")
        self.geometry("300x250")
        self.stack = []
        self.previous_ui = previous_ui
        
        label_berat = tk.Label(self, text="Berat (kg):")
        label_berat.pack()

        self.entry_berat = tk.Entry(self)
        self.entry_berat.pack()

        label_tinggi = tk.Label(self, text="Tinggi (cm):")
        label_tinggi.pack()

        self.entry_tinggi = tk.Entry(self)
        self.entry_tinggi.pack()

        button_submit = tk.Button(self, text="Hitung", command=self.calculate_bmi)
        button_submit.pack(pady=10)

        self.label_bmi = tk.Label(self, text="BMI:")
        self.label_bmi.pack()

        self.label_kategori = tk.Label(self, text="Kategori:")
        self.label_kategori.pack()

        button_back = tk.Button(self, text="Back", command=self.go_back)
        button_back.pack(pady=5)
        
    def calculate_bmi(self):
        berat = float(self.entry_berat.get())
        tinggi = float(self.entry_tinggi.get())

        bmi = berat / ((tinggi/100) ** 2)

        self.label_bmi.config(text="BMI: {:.2f}".format(bmi))

        if bmi < 18.5:
            self.label_kategori.config(text="Kategori: Berat Badan Kurang")
        elif bmi < 24.9:
            self.label_kategori.config(text="Kategori: Berat Badan Normal")
        elif bmi < 29.9:
            self.label_kategori.config(text="Kategori: Berat Badan Berlebih")
        else:
            self.label_kategori.config(text="Kategori: Obesitas")

    def go_back(self):
        if self.previous_ui:
            self.destroy()
            bmi_calculator = HealthOptions()
            bmi_calculator.show_options


class CalorieInfoForm(tk.Tk):
    def __init__(self, previous_ui):
        super().__init__()
        self.title("AKTIVITAS-GOALS")
        self.geometry("300x400")
        self.stack = []
        self.previous_ui = previous_ui

        label_aktivitas = tk.Label(self, text="Pilih Aktivitas Anda:")
        label_aktivitas.pack(pady=10)

        self.var_aktivitas = tk.StringVar()
        self.var_aktivitas.set(str)
        rb_aktivitas1 = tk.Radiobutton(self, text="Tidak Aktif", variable=self.var_aktivitas, value="Menetap")
        rb_aktivitas1.pack()
        rb_aktivitas2 = tk.Radiobutton(self, text="Sedikit Aktif", variable=self.var_aktivitas, value="Sedikit Aktif")
        rb_aktivitas2.pack()
        rb_aktivitas3 = tk.Radiobutton(self, text="Cukup Aktif", variable=self.var_aktivitas, value="Cukup Aktif")
        rb_aktivitas3.pack()
        rb_aktivitas4 = tk.Radiobutton(self, text="Sangat Aktif", variable=self.var_aktivitas, value="Sangat Aktif")
        rb_aktivitas4.pack()

        label_goal = tk.Label(self, text="Pilih Keinginan Anda:")
        label_goal.pack()

        self.var_goal = tk.StringVar()
        self.var_goal.set(str)
        rb_goal1 = tk.Radiobutton(self, text="Menurunkan Berat Badan", variable=self.var_goal, value="Menurunkan Berat Badan")
        rb_goal1.pack()
        rb_goal2 = tk.Radiobutton(self, text="Menjaga Berat Badan", variable=self.var_goal, value="Menjaga Berat Badan")
        rb_goal2.pack()
        rb_goal3 = tk.Radiobutton(self, text="Menambah Berat Badan", variable=self.var_goal, value="Menambah Berat Badan")
        rb_goal3.pack()

        button_submit = tk.Button(self, text="Submit", command=self.calculate_calorie)
        button_submit.pack(pady=10)

        self.label_calorie = tk.Label(self, text="Total Kalori:")
        self.label_calorie.pack()

        button_back = tk.Button(self, text="Back", command=self.go_back)
        button_back.pack(pady=5)

    def calculate_calorie(self):
        aktivitas = self.var_aktivitas.get()
        goal = self.var_goal.get()

        if aktivitas == "Sedentary":
            activity_factor = 1.2
        elif aktivitas == "Lightly Active":
            activity_factor = 1.375
        elif aktivitas == "Moderately Active":
            activity_factor = 1.55
        else:
            activity_factor = 1.725

        if goal == "Lose Weight":
            calorie_factor = 0.8
        elif goal == "Maintain Weight":
            calorie_factor = 1.0
        else:
            calorie_factor = 1.2

        calorie_intake = 2000 * activity_factor * calorie_factor
        self.label_calorie.config(text="Total Kalori: {:.0f}".format(calorie_intake))

    def show_options(self):
        self.mainloop()

    def go_back(self):
        if self.previous_ui:
            self.destroy()
            calorie_info = HealthOptions()
            calorie_info.show_options


if __name__ == "__main__":
    login_page = LoginPage()
    login_page.mainloop()
