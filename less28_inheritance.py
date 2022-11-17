# Inheritance - inheriting attributes or functions for one class from another one

class Chef:
    def make_chicken(self):
        print("The chef makes a chicken")

    def make_salad(self):
        print("The chef makes a salad")

    def make_special_dish(self):
        print("The chef makes a bbq ribs")


class ChineseChef(Chef):
    def make_kupa(self):
        print("The chinese makes a kupa dish")

    def make_siuiu(self):
        print("The chinese makes a siuiu dish")

    """If it has a similar function to inherited class, it will use its own"""
    def make_special_dish(self):
        print("The chef makes an orange chicken")


chef1 = Chef()
chinechef = ChineseChef()
chef1.make_chicken()  # --> The chef makes a chicken
chinechef.make_kupa()  # --> The chinese makes a kupa dish
chinechef.make_special_dish()  # --> The chef makes an orange chicken
chef1.make_special_dish()  # --> The chef makes a bbq ribs