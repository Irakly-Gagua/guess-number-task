# Проект 0 (SkillFactory, DS, Модуль PY 9). Угадай число

## Описание проекта    
Программа загадывает натуральное число от 1 до 100 и сама пытается его угадать за наименьшее число попыток. Одна попытка - это узнать, правда ли, что загаданное число больше (меньше) того или иного числа.

## Метод решения
Функция binary_search, производящая угадывание, использует метод двоичного поиска.

## Результат
Полученное среднее значение числа попыток составляет около 6.72, что несколько больше теоретического значения log_2 (100) = 6.64...

## Выводы
Раскождение со значением 6.64 связано с тем, что данное теоретическое значение предполагает снижение количества подозреваемых чисел в два раза на каждом шаге. Но После двух делений на два получается нечетное количество чисел (25), из-за чего точное деление на два невозможно.

Если изменить значение константы MAX_NUMBER со 100 на 128, получаемое значение числа попыток в точности совпатает с теоретическим - 7.0.