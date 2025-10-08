def square_number(n):
    if n <= 0:
        raise ValueError("n должно быть положительным")
    return (14*n*n-12*n)/2
