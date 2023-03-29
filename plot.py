import os
from tqdm import tqdm

####################
x=71.20           # 待测x坐标
y=71.20           # 待测y坐标
output_folder = 'K:/out'     #这个路径是前面文件转换后的输出路径，也是提取数据的输入路径
plot_folder = 'K:/plot'      #这是提取数据的输出路径
#####################

data = []
def extract_data(file_path, output_folder):
    with open(file_path, 'r') as f:
        lines = f.readlines()[-4290:]
        arr = []
        for line in lines:
            arr.append(line.split())
        global data
        for i in range(len(arr)):
            if float(arr[i][0]) == x and float(arr[i][1]) == y:   # location
                data.append([float(arr[i][2]), float(arr[i][3])])


        '''
        #this is write the corresponding data to a new file
        output_path = os.path.join(output_folder, os.path.basename(file_path) + '_output.dat')
        with open(output_path, 'w') as f2:
            for line in data:
                f2.write(" ".join(map(str,line)) + "\n")
        '''

print("Extracting the velocity...")
files = os.listdir(output_folder)
files = sorted(files, key=lambda x: int(x[-20:-16]))   # 按照照片编号后四位排序
if not os.path.exists(plot_folder):
    os.makedirs(plot_folder)
filename = os.listdir(output_folder)
total_files = len(filename)
for i, filename in tqdm(enumerate(filename), total=total_files,colour='blue'):
    if filename.endswith('.dat'):
    #    print(filename)
        #data.append(filename)                       #把文件名追加到data中，来看输出的文件顺序
        file_path = os.path.join(output_folder, filename)
        extract_data(file_path, plot_folder)
    plotname='plot_【'+str(x)+' '+str(y)+'】.dat'
    output_path = os.path.join(plot_folder, plotname)
with open(output_path, 'w') as f2:
    for line in data:
        f2.write("  ".join(map(str,line)) + "\n")



