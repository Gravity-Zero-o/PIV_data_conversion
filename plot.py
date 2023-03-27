import os

data = []
def extract_data(file_path, output_folder):
    with open(file_path, 'r') as f:
        lines = f.readlines()[-4290:]
        arr = []
        for line in lines:
            arr.append(line.split())
        global data
        for i in range(len(arr)):
            if float(arr[i][0]) == 73.15 and float(arr[i][1]) == 51.20:   # location 73.15 51.20
                data.append([float(arr[i][2]), float(arr[i][3])])

        '''#this is write the corresponding data to a new file
        output_path = os.path.join(output_folder, os.path.basename(file_path) + '_output.dat')
        with open(output_path, 'w') as f2:
            for line in data:
                f2.write(" ".join(map(str,line)) + "\n")
        '''


input_folder = 'K:/tmp/test1/0323/PIVdata'
output_folder = 'K:/tmp/test1/0323/out'
plot_folder='K:/tmp/test1/0323/plot'
files = os.listdir(output_folder)
files = sorted(files, key=lambda x: int(x[-8:-4]))   # 按照照片编号后四位排序
for filename in os.listdir(output_folder):
    if filename.endswith('.dat'):
    #    print(filename)
        #data.append(filename)                       #把文件名追加到data中，来看输出的文件顺序
        file_path = os.path.join(output_folder, filename)
        extract_data(file_path, plot_folder)
    output_path = os.path.join(plot_folder, 'plot2.dat')
with open(output_path, 'w') as f2:
    for line in data:
        f2.write("  ".join(map(str,line)) + "\n")



