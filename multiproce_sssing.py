import multiprocessing


def write_to_file(filename, data):
    with open(filename, 'w') as f:
        f.write(f"{data}\n")
        print(f'data written to {filename}')


def append_to_file(filename, data):
    with open(filename, 'a') as file:
        file.write(f"{data}\n")
        print(f'appended to {filename}')


def main():
    filename1 = 'mult1.txt'
    filename2 = 'mult2.txt'
    data1 = "Hello from Process 1!"
    data2 = "very wonderful from process 2 !"
    data3 = "Hello world I am a software developer."
    # create processing
    process1 = multiprocessing.Process(target=write_to_file, args=(filename1, data1))
    process2 = multiprocessing.Process(target=write_to_file, args=(filename2, data2))
    process3 = multiprocessing.Process(target=append_to_file, args=(filename1, data3))
    process4 = multiprocessing.Process(target=append_to_file, args=(filename2, data3))

    # start processing
    process1.start()
    process2.start()
    process3.start()
    process4.start()

    process1.join()
    process2.join()
    process3.join()
    process4.join()


if __name__ == '__main__':
    main()

