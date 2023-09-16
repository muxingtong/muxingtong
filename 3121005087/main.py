# 论文查重
import sys
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append("B:\\BaiduSyncdisk\\代码\\PY\\venv\\Lib\\site-packages") # 请根据环境修改,这里是我自己的环境
import jieba
import time
from collections import Counter
from math import sqrt
jieba.setLogLevel(jieba.logging.INFO)
starttime= time.time()

#计算计算余弦相似度
def cosine_similarity(vec1, vec2):
    dot_product = sum(vec1[key] * vec2.get(key, 0) for key in vec1)
    magnitude1 = sqrt(sum(val ** 2 for val in vec1.values()))
    magnitude2 = sqrt(sum(val ** 2 for val in vec2.values()))
    return dot_product / (magnitude1 * magnitude2)

#使用Counter对象计算每个词语在文本中出现的频率
def text_to_vector(text):
    words = jieba.lcut(text)
    return Counter(words)


def calculate_similarity(text1, text2):
    #将文本转换为向量表示
    vector1 = text_to_vector(text1)
    vector2 = text_to_vector(text2)
    return cosine_similarity(vector1, vector2)

#此函数还可以寻找相似的文本对，当输入文件为2个以上时，可以输出相似度大于0.8的文本对
def find_duplicates(texts,sim):
    duplicates = []
    #for i in range(len(texts)):
        #for j in range(i + 1, len(texts)):
    similarity = calculate_similarity(texts[0], texts[1])
    sim.append(round(similarity,2))
    print("相似度为：", similarity)

            #下为扩展功能，可以输出相似度大于0.8的文本对，需要读取多个文件
            #if similarity > 0.8:  # 可以根据需要调整相似度阈值
                #duplicates.append((i, j))
    return 1

def readfile(path):
    try:
        with open(path, 'r', encoding='gb18030', errors='ignore') as file:
            text = file.read()
    except:
        print("文件读取错误,请检查文件路径是否正确")
        return False
    return text

def writefile(path,text):
    try:
        with open(path, 'w', encoding='gb18030', errors='ignore') as file:
            file.write(text)
    except:
        print("文件写入错误,请检查文件路径是否正确")
        return False
    return True
if __name__ == "__main__":
    # 读取命令行参数
    try:
        a=sys.argv[1]
        b=sys.argv[2]
        c=sys.argv[3]
    except:
        print("参数输入错误,请检查参数是否输入正确")
    sim=[]#相似度(重复率)列表
    text1 = readfile(a)
    text2 = readfile(b)
    duplicates = find_duplicates([text1, text2],sim)
    if(writefile(c,str(sim))):
        print("相似度列表已写入文件")
endtime = time.time()
print("程序运行时间为：",endtime-starttime)