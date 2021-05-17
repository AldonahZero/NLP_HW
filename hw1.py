#训练语料
test_file = 'dataset/pku_training.utf8'
#测试语料
test_file2 = 'dataset/pku_test.utf8'
#生成结果
test_file3 = 'test/sc.txt'

#读取文本返回列表
def get_dic(test_file):
    with open(test_file,'r',encoding='utf-8',) as f:
        try:
            file_content = f.read().split()
        finally:
            f.close()
    chars = list(set(file_content))
    return chars

dic = get_dic(test_file)
def readfile(test_file2):
    max_length = 5

    h = open(test_file3,'w',encoding='utf-8',)
    with open(test_file2,'r',encoding='utf-8',) as f:
        lines = f.readlines()
    # 分别对每行进行正向最大匹配处理
    for line in lines:
        max_length = 5
        my_list = []
        len_hang = len(line)
        while len_hang>0 :
            tryWord = line[0:max_length]
            while tryWord not in dic:
                if len(tryWord)==1:
                    break
                tryWord=tryWord[0:len(tryWord)-1]
            my_list.append(tryWord)
            line = line[len(tryWord):]
            len_hang = len(line)
        # 将分词结果写入生成文件
        for t in my_list:
            if t == '\n' :
                h.write('\n')
            else:
                h.write(t + "  ")

    h.close()

readfile(test_file2)