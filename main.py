from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
import mysql.connector

from kivy.core.window import Window

Window.size = (320, 680)

myDb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='user_account'
)

myCursor = myDb.cursor()


# Define different screens
class MainWindow(Screen):
    Config.set("graphics", "width", "320")
    Config.set("graphics", "height", "680")
    Config.set("graphics", "borderless", "0")
    Config.set("graphics", "resizable", "0")

    def verify_credentials(self):
        myCursor.execute("SELECT * FROM account")
        records = myCursor.fetchall()
        for row in records:
            try:
                if row[1] == self.ids.login.text:
                    if row[2] == self.ids.passw.text:
                        self.ids.err_lbl.text = ""
                        self.manager.current = "menu"
                        self.manager.screens[1].ids.user_nickname.text = "Hi " + row[6] + "!"
                        self.manager.screens[2].ids.info_a.text = row[1]
                        self.manager.screens[2].ids.info_c.text = row[3]
                        self.manager.screens[2].ids.info_d.text = row[4]
                        self.manager.screens[2].ids.info_e.text = row[5]
                        self.manager.screens[2].ids.info_f.text = row[6]
                        self.manager.screens[2].ids.info_g.text = row[7]
                        self.manager.screens[2].ids.info_h.text = row[8]
                        self.manager.screens[2].ids.info_i.text = str(row[9])
                        self.manager.screens[2].ids.info_j.text = row[10]
                        self.manager.screens[2].ids.info_k.text = row[11]
                        self.manager.screens[2].ids.info_l.text = row[12]
                        self.ids.login.text = ""
                        self.ids.passw.text = ""
                    elif row[2] != self.ids.passw.text:
                        self.ids.err_lbl.text = ""
                        self.ids.err_lbl.text = "Account doesn't exist!"
                        self.ids.login.text = ""
                        self.ids.passw.text = ""
            finally:
                pass


class UserWindow(Screen):
    pass


class MenuWindow(Screen):
    def show_info(self):
        self.manager.current = "info_page"
        myCursor.execute("SELECT * FROM account")
        records = myCursor.fetchall()

    def logout(self):
        if self.manager.screens[0].ids.err_lbl.text != "":
            self.manager.screens[0].ids.err_lbl.text = ""
        self.manager.current = "home"


class SignupWindow(Screen):
    def save_signup(self):
        query = "INSERT INTO account (username, password, last_name, first_name, middle_name, nickname, gender," \
                "birthday, contact, email, barangay, complete_address) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (self.ids.sut1.text, self.ids.sut2.text, self.ids.sut3.text, self.ids.sut4.text, self.ids.sut5.text,
               self.ids.sut6.text, self.ids.sut7.text, self.ids.sut8.text, self.ids.sut9.text, self.ids.sut10.text,
               self.ids.sut11.text, self.ids.sut12.text)
        myCursor.execute("SELECT * FROM account")
        records = myCursor.fetchall()
        for row in records:
            if row[1] != self.ids.sut1.text:
                if self.ids.sut1.text != "":
                    myCursor.execute(query, val)
                    myDb.commit()
                    self.manager.current = "home"
                    self.ids.sut1.text = ""
                    self.ids.sut2.text = ""
                    self.ids.sut3.text = ""
                    self.ids.sut4.text = ""
                    self.ids.sut5.text = ""
                    self.ids.sut6.text = ""
                    self.ids.sut7.text = ""
                    self.ids.sut8.text = ""
                    self.ids.sut9.text = ""
                    self.ids.sut10.text = ""
                    self.ids.sut11.text = ""
                    self.ids.sut12.text = ""
                else:
                    continue
            elif row[1] == self.ids.sut1.text:
                self.ids.sut1.text = ""


class WindowManager(ScreenManager):
    pass


# Designate Our .kv file
kv = Builder.load_file('mobile_app.kv')


class BalayanihanApp(MDApp):
    def build(self):
        return kv


if __name__ == "__main__":
    BalayanihanApp().run()
