"""
用Spyder運行，命令行參數在 Run-Configuration per file-Command line options 設置
e.g. do.txt doc.txt
"""
import sys
import os
import re
def get_file_name(c):
    res = []
    prefix = input_filename.split(c)[0]
    dirPath = os.getcwd()           # 獲取當前工作路徑
    for root, dirs, files in os.walk(dirPath):
        for file in files:
            # 用正則表達式匹配文件名 *和？會按要求重複匹配[0-9a-zA-Z]
            res += re.findall('^('+prefix+'[0-9a-zA-Z]'+c+'\.txt)',file)
    print(res)
    return res

input_filename = sys.argv[1]    # 獲取命令行輸入的參數，0是當前文件路徑
output_filename = sys.argv[2]

if '*' in input_filename:
    file_list = get_file_name('*')
    flag = True
elif '?' in input_filename:
    file_list = get_file_name('?')
    flag = True
else:
    file_list = [input_filename]
    flag = False
if len(file_list) == 0:
    print("No matching!")
else:    
    try:
        res = ''
        for file in file_list:
            with open(file, 'r') as f1:
                article = f1.read()
                if flag:
                    res += "Name of file: " + file + '.\n'
                # 統計字母的數量
                res += "Number of characters: "+str(len([x for x in article if x.isalpha()]))+'.\n'
                res += "Number of words: "+str(len(article.split()))+'.\n'
                res += "Number of lines: "+str(len(article.split('\n')))+'.\n'
        with open(output_filename, 'w') as f2:
            f2.write(res)            
    except:
        print('Opening file ' + input_filename + ' failed!')
