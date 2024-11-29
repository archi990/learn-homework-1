"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""
def whose_age(age):
    if age<=6:
        result="To you in kindergarten"
        return result
    elif age>6 and age<19:
        result="To your school"
        return result
    elif age>18 and age< 24:
        result="To you at the university"
        return result
    else:
        result="you to work"
        return result 
    

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    age=int(input('Please enter your age: '))
    who_i_am=whose_age(age)
    print(who_i_am)

if __name__ == "__main__":
    main()
