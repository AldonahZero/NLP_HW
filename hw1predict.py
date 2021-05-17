test_file = 'test/sc.txt'
test_file2 = 'dataset/gold/pku_test_gold.utf8'
def get_word(fname):

    f = open(fname,'r',encoding='utf-8',)
    lines = f.readlines()

    return lines


def calc():
    lines_list_sc = get_word(test_file)
    lines_list_gold = get_word(test_file2)

    lines_list_num = len(lines_list_gold)

    right_num = 0
    m = 0#m存逆向结果文本词的总数
    n = 0#n存gold文本词的总数

    for i in range(lines_list_num):

        line_list_sc = list(lines_list_sc[i].split())#line_list_sc为生成结果每行通过空格切分后的词汇表
        line_list_gold = list(lines_list_gold[i].split())#line_list_gold为正确结果每行通过空格切分后的词汇表

        m += len(line_list_sc)
        n += len(line_list_gold)

        str_sc = ''#存结果文本每行无空格连接起来的字符串
        str_gold = ''#存gold文本每行无空格连接起来的字符串

        s = 0#表示结果文本每行列表的下标
        g = 0#表示gold文本每行列表的下标

        while s < len(line_list_sc) and g < len(line_list_gold):
            str_word_sc = line_list_sc[s]
            str_word_gold = line_list_gold[g]

            str_sc += str_word_sc
            str_gold += str_word_gold

            if str_word_sc == str_word_gold:#如果当前词汇相同，表明结果正确，且之前的词汇拼成的字符串长度相等
                s += 1
                g += 1
                right_num += 1

            else:#如果当前词汇不同，结果错误，不断取词汇拼字符串直到两个字符串长度相同

                while len(str_sc) > len(str_gold):
                    g += 1
                    str_gold += line_list_gold[g]


                while len(str_sc) < len(str_gold):
                    s += 1
                    str_sc += line_list_sc[s]

                g += 1
                s += 1

    print("生成结果词的个数：", m)
    print("gold文本词的个数：", n)
    print("正确词的个数：", right_num)
    p = right_num/m
    r = right_num/n
    f = 2*p*r/(p+r)
    print("Precision ：", p)
    print("Recall ：", r)
    print("F measure：", f)
calc()