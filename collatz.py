import matplotlib.pyplot as plt
import numpy as np
import time


def collatz_conjecture(number, verbose=False):
    """Run the Collatz sequence for ``number`` and plot the results."""
    travelled_nums = [number]
    steps = 0
    start = time.time()

    while number != 1:
        if verbose:
            print(number)
        if number % 2 == 0:
            number //= 2
        else:
            number = 3 * number + 1
        travelled_nums.append(number)
        steps += 1

    end = time.time()

    print(f"Total steps taken: {steps}")
    print(f"Total time: {end - start}s")

    plt.plot(np.array(travelled_nums, dtype=np.int64))
    plt.xlabel("Numbers travelled")
    plt.show()


if __name__ == "__main__":
    num = int(input("Enter number for collatz conjecture: "))
    collatz_conjecture(num)
