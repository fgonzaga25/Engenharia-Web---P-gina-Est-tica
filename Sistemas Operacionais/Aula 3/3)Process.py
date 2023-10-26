from multiprocessing import Process

def print_numbers():
    for i in range(1, 6):
        print(f"Processo 1: {i}")

def print_letters():
    for letter in "abcde":
        print(f"Processo 2: {letter}")

if __name__ == "__main__":
    process1 = Process(target=print_numbers)
    process2 = Process(target=print_letters)

    process1.start()
    process2.start()

    process1.join()
    process2.join()