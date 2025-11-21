import numpy as np
from src.math_utils import moving_average, is_prime

numbers = np.array(range(0, 10))

print("numbers", numbers)

moving_average_of_numbers = moving_average(values=numbers, window_size=1)

print("moving average of numbers is", moving_average_of_numbers)
