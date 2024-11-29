"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты
"""
def check_str(s1, s2):
    if type(s1) is not str or type(s2) is not str:
        return 0
    elif s1==s2:
        return 1
    elif s1!=s2 and len(s1)>len(s2):
        return 2
    elif s2=='learn':
        return 3

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    s1=100
    s2="word"
    result = check_str(s1,s2)
    print(result)
    s1="equal"
    s2="equal"
    result = check_str(s1,s2)
    print(result) 
    s1="test10"
    s2="test"
    result = check_str(s1,s2)
    print(result)
    s1="test"
    s2="learn"
    result = check_str(s1,s2)
    print(result)
    
if __name__ == "__main__":
    main()
