import time
import multiprocessing

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())
    return all_data

if __name__ == '__main__':

    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    start_time = time.time()
    for filename in filenames:
        data = read_info(filename)
    linear_time = time.time() - start_time
    print(f"Время выполнения линейного подхода: {linear_time:.4f} секунд")

    start_time = time.time()
    with multiprocessing.Pool() as pool:
        results = pool.map(read_info, filenames)
    parallel_time = time.time() - start_time
    print(f"Время выполнения многопроцессного подхода: {parallel_time:.4f} секунд")

