def fibonacci(n):
    """
    Вычисляет n-ное число Фибоначчи
    """
    if n < 0: raise ValueError("n должно быть неотрицательным")
    
    if n > 1000000: raise ValueError("Максимально допустимое число для расчета Фибоначи - fib(n_max) == 1000000")
    
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibonacci_sequence(count):
    """
    Возвращает последовательность чисел Фибоначчи
    """
    if count <= 0:
        return []
    elif count == 1:
        return [0]
    elif count == 2:
        return [0, 1]
    
    sequence = [0, 1]
    for i in range(2, count):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence
