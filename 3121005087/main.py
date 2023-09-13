# 论文查重
import sys
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
sys.path.append("B:\\BaiduSyncdisk\\代码\\PY\\venv\\Lib\\site-packages") # 请根据环境修改,这里是我自己的环境
import jieba
from collections import Counter
from math import sqrt
jieba.setLogLevel(jieba.logging.INFO)

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


def find_duplicates(texts,sim):
    duplicates = []
    for i in range(len(texts)):
        for j in range(i + 1, len(texts)):
            similarity = calculate_similarity(texts[i], texts[j])
            sim.append(round(similarity,2))
            print("相似度为：", similarity)
            if similarity > 0.8:  # 可以根据需要调整相似度阈值
                duplicates.append((i, j))
    return duplicates


if __name__ == "__main__":
    # 读取命令行参数
    a=sys.argv[1]
    b=sys.argv[2]
    c=sys.argv[3]
    sim=[]#相似度(重复率)列表
    with open(a, 'r', encoding='gb18030', errors='ignore') as file1:
        text1 = file1.read()
    with open(b, 'r', encoding='gb18030', errors='ignore') as file2:
        text2 = file2.read()
    duplicates = find_duplicates([text1, text2],sim)
    with open(c, 'w', encoding='gb18030', errors='ignore') as file3:
        file3.write(str(sim))
