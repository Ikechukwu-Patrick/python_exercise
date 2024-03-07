from MyDiaryApp.Diary import Diary


class TheMainDiaryApp:
    def __init__(self):
        self.diary = Diary('Omi Ewa', 'my_password')

    def main_app(self):
        self.display_page()

    def display_page(self):
        print('''Welcome to Omi Ewa's Diary App
        1-> Create Diary
        2-> Find Diary
        3-> Unlock Diary
        4-> Add Entry
        5-> Lock Diary
        6-> Delete Entry
        7-> Find Entry
        8-> Update Entry
        9-> Exit App
        ''')


diary = TheMainDiaryApp()
diary.main_app()
