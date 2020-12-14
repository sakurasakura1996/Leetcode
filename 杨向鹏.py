# 批量处理xvg，读取其中的 一个 浮点数

import os
def main(read_path, write_path):
    files = os.listdir(read_path)  # 读取到path路径下的所有文件
    ans = {}
    for file in files:
        file_path = os.path.join(read_path, file)  # 目录下某一个文件的具体路径
        index = int(file.split('.')[0][3:])  # 数字索引
        # 然后读取该文件
        number_str = ""
        with open(file_path, mode='r') as f:
            lines = f.readlines()
            # print(len(lines))
            line = lines[19].strip()
            line_len = len(line)
            left = 0
            right = 0
            for i in range(line_len):
                if line[i] == '=':
                    left = i+1
                if line[i] == '(':
                    right = i
                    break
            number_str = line[left:right].strip()
            ans[index] = round(float(number_str),4)
        f.close()
    # 全部结果存储在ans字典中了，然后排序
    output = sorted(ans.items(), key= lambda x:x[1], reverse=True)
    with open(write_path, 'w') as f:
        for value in enumerate(output):
            print(value)
            tmp = str(value[1][0]) + "   " + str(value[1][1]) + "\n"
            f.write(tmp)
    f.close()



def generateTxt(path):
    # 用于生成bat脚本文件的txt文件
    command = "gmx msd -f C510V1ns.pdb -s md-c510v.gro -n awater.ndx -o msd"
    with open(path, mode='w') as f:
        f.write("@echo off\n")
        for i in range(1001):  # 在这里改动数字就行了，
            tmp = "echo "+str(i)+"|"+command + str(i)+".vxg\n"
            f.write(tmp)
    f.close()


if __name__ == '__main__':
    read_path = "D:/QQFile/2470375551/FileRecv/yxp/xvg"
    write_path = "D:/QQFile/2470375551/FileRecv/yxp/txt/ans.txt"
    main(read_path, write_path)
    txt_path = "C:/Users/Administrator/Desktop/cmd2.txt"
    # generateTxt(txt_path)