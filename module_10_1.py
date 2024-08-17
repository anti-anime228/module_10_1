from time import sleep
from threading import Thread
from datetime import datetime

start_def = datetime.now()


def wite_words(word_count, file_name):
    with open(file_name, 'a') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)

    print(f"Завершилась запись в файл {file_name}")


res1 = wite_words(10, ' example1.txt')
res2 = wite_words(30, ' example2.txt')
res3 = wite_words(200, ' example3.txt')
res4 = wite_words(100, ' example4.txt')
fin_def = datetime.now()
res_def = fin_def - start_def
print(f"Время записи без потоков :{res_def}")

start_thr = datetime.now()
thr_first = Thread(target=wite_words, args=(10, 'example5.txt'))
thr_second = Thread(target=wite_words, args=(30, 'example6.txt'))
thr_third = Thread(target=wite_words, args=(200, 'example7.txt'))
thr_fourth = Thread(target=wite_words, args=(100, 'example8.txt'))

thr_first.start()
thr_second.start()
thr_third.start()
thr_fourth.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_fourth.join()

fin_thr = datetime.now()
res_thr = fin_thr - start_thr
print(f"Время записи с помошью потоков :{res_thr}")
