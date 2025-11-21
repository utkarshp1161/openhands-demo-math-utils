def moving_average(values, window_size):
    """Return a moving average over a list of floats.
    """
    if len(values) < window_size:
        return []
    
    moving_averages = []
    for i in range(len(values) - window_size + 1):
        window = values[i:i + window_size]
        avg = sum(window) / window_size
        moving_averages.append(avg)
    
    return moving_averages
    

def is_prime(n: int) -> bool:
    """Return True if n is prime, otherwise False.
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Only check odd divisors up to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
