#对论文查重的测试
import unittest
import main
class MyTestCase(unittest.TestCase):
    def test_readfile(self):
        p1='orig.txt'
        p2='orig_0.8_add.txt'
        self.assertTrue(main.readfile(p1))
        self.assertTrue(main.readfile(p2))

    def test_calculate_similarity(self):
        text1 = main.readfile('orig.txt')
        text2 = main.readfile('orig_0.8_add.txt')
        self.assertTrue(main.calculate_similarity(text1,text2))

    def test_find_duplicates(self):
        texts=[]
        texts.append(main.readfile('orig.txt'))
        texts.append(main.readfile('orig_0.8_add.txt'))
        sim=[]
        self.assertTrue(main.find_duplicates(texts,sim))

    def test_text_to_vector(self):
        text = main.readfile('orig.txt')
        self.assertTrue(main.text_to_vector(text))

    def test_cosine_similarity(self):
        text1 = main.readfile('orig.txt')
        text2 = main.readfile('orig_0.8_add.txt')
        vector1 = main.text_to_vector(text1)
        vector2 = main.text_to_vector(text2)
        self.assertTrue(main.cosine_similarity(vector1,vector2))

    def test_writefile(self):
        p3 = 'temp.txt'
        self.assertTrue(main.writefile(p3,'test'))


if __name__ == '__main__':
    unittest.main()

