import os
from tqdm import tqdm

##################
input_folder = 'K:/Velocity'
output_folder = 'K:/out'
read_line = 4290  #设置倒数的行数，这里是倒数第4290行，值为xy之积
x_line = 55       #每个x对应的y数量
y_line = 78       #x的总数
##################


def process_file(file_path, output_folder):
    with open(file_path, 'r') as f:
        lines = f.readlines()[-read_line:]   #从倒数read_line行开始读取
        arr = []
        for line in lines:
            arr.append(line.split())
        for i in range(len(arr)):
            arr[i][2] = round(float(arr[i][2])/1000, 4)
            arr[i][3] = round(float(arr[i][3])/1000, 4)
            del arr[i][4]
        output_path = os.path.join(output_folder, os.path.basename(file_path) + '_output.dat')
        with open(output_path, 'w') as f2:
            f2.write('variables="x","y","u","v"\n')
            f2.write('zone i='+str(x_line)+',j='+str(y_line)+',f=point\n')
            for line in arr:
                f2.write(" ".join(map(str,line)) + "\n")


print("Look! File conversion in progress...")
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
filename = os.listdir(input_folder)
total_files = len(filename)
for i, filename in tqdm(enumerate(filename), total=total_files,colour='blue'):
    if filename.endswith('.dat'):
        file_path = os.path.join(input_folder, filename)
        process_file(file_path, output_folder)




