import os
from tqdm import tqdm
from tqdm.notebook import trange
def process_file(file_path, output_folder):
    with open(file_path, 'r') as f:
        lines = f.readlines()[-4290:]   #从倒数4290行开始读取
        arr = []
        for line in lines:
            arr.append(line.split())
        for i in range(len(arr)):
            arr[i][2] = round(float(arr[i][2])/1000, 4)
            arr[i][3] = round(float(arr[i][3]) / 1000, 4)
            del arr[i][4]
        output_path = os.path.join(output_folder, os.path.basename(file_path) + '_output.dat')
        with open(output_path, 'w') as f2:
            f2.write('variables="x","y","u","v"\n')
            f2.write('zone i=55,j=78,f=point\n')
            for line in arr:
                f2.write(" ".join(map(str,line)) + "\n")

input_folder = 'K:/tmp/test1/0323/PIVdata'
output_folder = 'K:/tmp/test1/0323/out1'
print("Look! File conversion in progress...")
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
filename = os.listdir(input_folder)
total_files = len(filename)
for i, filename in tqdm(enumerate(filename), total=total_files,colour='blue'):
    if filename.endswith('.dat'):
        file_path = os.path.join(input_folder, filename)
        process_file(file_path, output_folder)




