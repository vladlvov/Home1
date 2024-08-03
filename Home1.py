grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]  # Cписок
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}  # Множество
students = sorted(list(students))  # Множество меняем на список (list) (Помните, что множество не является упорядоченной последовательностью. (нужен перевод в другой тип).
                                   # sorted-в Python возвращает новый отсортированный список из переданной ей итерируемой коллекции.
grades_average = [(sum(grades[0]) / len(grades[0])), (sum(grades[1]) / len(grades[1])),
                  (sum(grades[2]) / len(grades[2])), (sum(grades[3]) / len(grades[3])), (sum(grades[4]) / len(grades[4]))]
average_score = dict(zip(students,grades_average))  # dict— неупорядоченная коллекция произвольных объектов с доступом по ключу, zip - которая позволяет объединить в кортежи элементы нескольких списков, Для решения задачи нужно вспомнить функции sum, len и др. (подумать самому).
print(average_score)
