import time


current_user = 'admin'

if current_user != "admin":
    raise Exception("Доступ Запрещен")
    print("Делаем что-то доступное только админу")
    print('Неверно')


"""Декоратор является ли входящий пользователь админом или нет(ПОДОБИЕ)"""


def admin(func):
        def wrap(*args, **kwargs):
            func(*args, **kwargs)
        log_admin = input('Логин\n')
        password_admin = str(input())

        if log_admin == "admin666" and password_admin == '4166':
            return wrap()
        else:
            print('Неверные данные\nПожалуйста попробуйте ещё')
            admin(func)

@admin
def x():
    if True:
        print('Молодец, Рассматриваем твое назначение на работе')
        current_user = 'admin'
        time.sleep(2)
    print(f"Твой Статус {current_user}\nДобро пожаловать\n")



zxc = [1231, 3214, 412, 12, 0 , 312, 31412, 5423342, 312123, 321]


"""sotring Bubble-Сортировка списка пузырьком
альтернатива "sort" """
def bubble_sorting(list):
    status = True

    while status:
        status = False
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                status = True





print(*zxc)
bubble_sorting(zxc)
print(*zxc)
zxc[0] , zxc[-1] = zxc[-1], zxc[0]
print(*zxc)






"""мини практика, вспоминаю чтобы не забыть"""

class User_reg:

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def len_pass(self):
        str(self.password)
        if len(self.password) < 7 and self.password != self.login:
            raise ValueError('Too short')

    def add_file(self):
        with open('users', 'w+') as file:
                file.write(f'{self.login, self.password}'+'\n')






us1 = User_reg('artur', '12332321')
us2 = User_reg('david', '423564765')
us3 = User_reg('quester', '7676876897')
us4 = User_reg('fench', '6546546456')
us1.add_file()
