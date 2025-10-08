import time
import sys
from fibonacci import fibonacci, fibonacci_sequence
from figurate import square_number

sys.set_int_max_str_digits(1000000)

def main():
    while True:
        print("\n=== Вычислитель математических последовательностей ===")
        print("1. Вычислить число Фибоначчи")
        print("2. Вычислитель последовательности Фибоначчи")
        print("3. Вычислитель 16-угольное числа")
        print("0. Выход из программы")
        
        choice = input("\nВведите номер (0-3): ").strip()
        
        if choice == "1":
            while True:
                print("\n=== Вычислитель числа Фибоначчи ===")
                print("1. Расчитать число Фибоначчи")
                print("2. Выйти в главное меню")
                
                enter = input("\nВведите номер (1-2): ").strip()
                
                if enter == "1":
                    try:
                        n = int(input("\nВведите n для рассчета числа Фибоначчи: "))
                        start_time = time.time()
                        result = fibonacci(n)
                        end_time = time.time()
                        print(f"Фибоначчи({n}) = {result}")
                        print(f"Время вычисления: {end_time - start_time:.6f} секунд")
                    except ValueError as e:
                        print(f"Ошибка: {e}")
                elif enter == "2":
                    print("Выход в главное меню.")
                    break
                else:
                    print("Неверный ввод! Попробуйте снова (1,2).")
                    
                
        elif choice == "2":
            while True:
                print("\n=== Вычислитель последовательности Фибоначчи ===")
                print("1. Вывести последовательность Фибоначчи")
                print("2. Выйти в главное меню")
                
                enter = input("\nВведите номер (1-2): ").strip()
                
                if enter == "1":
                    try:
                        count = int(input("\nВведите количество чисел Фибоначчи: "))
                        start_time = time.time()
                        sequence = fibonacci_sequence(count)
                        end_time = time.time()
                        print(f"Последовательность чисел Фибоначчи: {sequence}")
                        print(f"Время вычисления: {end_time - start_time:.6f} секунд")
                    except ValueError as e:
                        print(f"Ошибка: {e}")
                elif enter == "2":
                    print("Выход в главное меню.")
                    break
                else:
                    print("Неверный ввод! Попробуйте снова (1,2).")
                
        elif choice == "3":
            while True:
                print("\n=== Вычислитель 16-угольное числа ===")
                print("1. Рассчитать 16-угольное число")
                print("2. Выйти в главное меню")
                
                enter = input("\nВведите номер (1-2): ").strip()
                
                if enter == "1":
                    try:
                        n = int(input("\nВведите n для 16-угольное: "))
                        start_time = time.time()
                        result = square_number(n)
                        end_time = time.time()
                        print(f"16-e число({n}) = {result}")
                        print(f"Время вычисления: {end_time - start_time:.6f} секунд")
                    except ValueError as e:
                        print(f"Ошибка: {e}")
                elif enter == "2":
                    print("Выход в главное меню.")
                    break
                else:
                    print("Неверный ввод! Попробуйте снова (1,2).")
                
        elif choice == "0":
            print("Выход из программы...")
            break
            
        else:
            print("Неверный ввод! Попробуйте снова (0,1,2,3).")

if __name__ == "__main__":
    main()


