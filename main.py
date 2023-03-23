import os
import shutil

'''
def delete_first_lines(filename,count,filename1): # write the header file format of tecplot
    fin = open(filename,'r') # read a file
    a = fin.readlines()
    fout = open(filename1,'w') # write a file
    fout.write('variables="x","y","u","v","flag"\n')
    fout.write('zone t="Frame 0" i=55,j=79,f=point\n')
    b=''.join(a[count:])
    fout.write(b)
    print(b)# write lines begin with index count, I think it maybe require much internal storage

def read_numbers_from_file(file_path):   # read data from file into an array s[]
    data = []
    with open(file_path, 'r') as f:
        for line in f:
            row = []
            for word in line.split():
                    row.append(word)
            data.append(row)
'''
# 读取文件夹下所有文本文件
path = 'K://tmp/test1/gy'
files = os.listdir(path)
txt_files = [f for f in files if f.endswith('.dat')]

def renames():
    # 按顺序重命名文件
    txt_files.sort()
    for i, f in enumerate(txt_files):
        new_name = f'u10f4_Frame{i+1}.dat'
        os.rename(os.path.join(path, f), os.path.join(path, new_name))
# 输出到新的文本文件
def rewrite():
    for i, f in enumerate(txt_files):
        with open(os.path.join(path, f), 'r') as file:
            content = file.readlines()
        new_name = f'u10f4_Frame{i+1}.dat'  # t is the name of the file, and i is the index of it
        with open(os.path.join(path, new_name), 'w') as file:
            #file.write(content) # write all origin data
            file.write('variables="x","y","u","v","flag"\n')
            file.write('zone i=55,j=78,f=point\n')
            b = ''.join(content[-4290:])
            file.write(b)  # write lines begin with index count, I think it maybe require much internal storage

''' 
    i=0
    for i in range(10):              # from this we know that the array s is 2D, though it has only one []
        for j in range(5):
            print(data[i][j],end=" ")# the end and a space means the output data is in one line with a space
        print('\n')                  # change the next line after 5 loops
'''
'''
def write_numbers_to_file(data, file_path):
    with open(file_path, 'w') as f:
        for row in data:
            for number in row:
                f.write(str(number) + ' ')
            f.write('\n')
    print(f"Data written to {file_path}")

# Example usage
data = read_numbers_from_file('K://tmp/test1/test01.txt')
#write_numbers_to_file(data, 'K://tmp/test1/test_out.txt')

def find_indices_of_value(data, value):
    indices = []
    for i, row in enumerate(data):
        for j, number in enumerate(row):
            if number == value:
                indices.append((i, j))
    return indices


path="K://tmp/test1"
files=os.listdir(path)
s=[]
for file in files:
    if not os.path.isdir(file): # whether it is a floder
        f=open(path+"/"+file);
        iter_f = iter(f);
        str = ""
        for line in iter_f:
            str=str+line
        s.append(str)
for i in range(4):
    print(i,s[i])
    print('\n')
'''



# ***************************** zone to call funs
#read_numbers_from_file("K://tmp/test1/test02.txt")
#t = 'k://tmp/test1/test3.txt' # old_file location
#t1= 'k://tmp/test1/test3out.txt' # new_file location
#delete_first_lines(t,4,t1) #we could use  all files fun to call delete fun
#renames()
rewrite()