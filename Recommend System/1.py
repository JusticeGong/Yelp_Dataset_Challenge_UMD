
import random
with open('D:/Workplace/BigData/network.txt', 'w', encoding="utf8") as f:
    for i in range(1,11):
        for j in random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], random.randint(1,10)):
            f.write("page" + str(i) + "\t" + "page" + str(j) + "\n")
    f.close()
