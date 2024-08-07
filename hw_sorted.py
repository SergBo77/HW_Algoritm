def min_sort(arr):
   # Проходим по всему списку
   for i in range(len(arr)):
       # Предполагаем, что первый элемент в неотсортированной части - это минимальный
       min_index = i
       # Ищем минимальный элемент в оставшейся части списка
       for j in range(i+1, len(arr)):
           if arr[j] < arr[min_index]:
               min_index = j
       # Меняем местами найденный минимальный элемент с первым элементом в неотсортированной части
       arr[i], arr[min_index] = arr[min_index], arr[i]

def max_sort(arr):
   # Проходим по всему списку
   for i in range(len(arr)):
       # Предполагаем, что первый элемент в неотсортированной части - это максимальный
       max_index = i
       # Ищем максимальный элемент в оставшейся части списка
       for j in range(i+1, len(arr)):
           if arr[j] > arr[max_index]:
               max_index = j
       # Меняем местами найденный максимальный элемент с первым элементом в неотсортированной части
       arr[i], arr[max_index] = arr[max_index], arr[i]


# Пример использования
numbers = []

while True:
    number = input("Введите числа для сортировки. Введите 'нет' для завершения работы: ")

    if number.lower() == 'нет':  # Проверка на "нет", регистронезависимо
        break

    try:
        number = int(number)  # Пытаемся преобразовать ввод в целое число
        numbers.append(number)  # Добавляем число в список
    except ValueError:  # Обрабатываем ошибку, если ввод не является числом
        print("Ошибка ввода! Пожалуйста, введите корректное число.")


choice = input("Для сортировки по возрастанию нажмите 1, по убыванию нажмите 2: ")

if choice == "1":
    print("Отсортированный список по возрастанию:")
    min_sort(numbers)
    print(numbers)
else:
    print("Отсортированный список по убыванию:")
    max_sort(numbers)
    print(numbers)