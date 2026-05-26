import psutil
import os

data = []

for i in range(50000):
    data.append(bytearray("love you" * 1024 * 1024, 'utf-8'))

    ram = psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024
    print(f"{ram:.2f} MB")