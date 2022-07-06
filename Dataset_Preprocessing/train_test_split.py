import random
import os
#This code can just create two files as 'train.txt' and 'test.txt' remember when testing your algorithm you need another validation set so actually three files are needed 

def data_split(full_list, ratio, shuffle=False):
    n_total = len(full_list)
    offset = int(n_total * ratio)
    if n_total == 0 or offset < 1:
        return [], full_list
    if shuffle:
        random.shuffle(full_list)
    sublist_1 = full_list[:offset]
    sublist_2 = full_list[offset:]
    return sublist_1, sublist_2
    
if __name__ == "__main__":
    filenumber = 1500 # change with your file number(from 0000 to x)
    data = list(range(filenumber)) 
    sub_data1, sub_data2 = data_split(data, ratio=0, shuffle=False) # shuffle number or not
    file_split = "G:\\paper\\Falling_Things\\Fat\\test1\\left" #target file
    with open(os.path.join(file_split,"train.txt"),"w") as tr:
        for line in sub_data2:
            trainnum = str(line)
            trainnumfill=trainnum.zfill(4)
            tr.write(trainnumfill+'\n')
        
    tr.close()
    with open(os.path.join(file_split,"test.txt"),"w") as te:
        for line in sub_data1:
            testnum = str(line)
            testnumfill=testnum.zfill(4)
            te.write(testnumfill+'\n')
    te.close()
    print(sub_data1)
    print(sub_data2)
