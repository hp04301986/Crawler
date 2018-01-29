from os import path
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

def mk_wordcloud():
    text_content = open('test.txt', 'r', encoding = 'utf-8').read()
    wordlist_cut_by_jieba = jieba.cut(text_content, cut_all=False)
    wordlist_space = ' '.join(wordlist_cut_by_jieba)
    #print(wordlist_space)
    background_image = plt.imread('xpj.jpg')
    print('加载图片')
    #屏蔽词
    stopwords = STOPWORDS.copy()
    stopwords.add("还是")
    stopwords.add("但是")
    stopwords.add("不是")
    stopwords.add("就是")
    stopwords.add("没有")
    stopwords.add("知道")
    stopwords.add("因为")
    stopwords.add("看到")
    stopwords.add("还有")
    stopwords.add("觉得")
    stopwords.add("有点")
    stopwords.add("这么")
    stopwords.add("其实")
    stopwords.add("一个")
    stopwords.add("为什么")
    stopwords.add("开始")
    stopwords.add("不要")
    stopwords.add("本来")
    stopwords.add("虽然")
    stopwords.add("出来")
    wc = WordCloud(
        width = 750,
        height = 1335,
        background_color = 'white',
        mask = background_image,
        font_path = 'C:\Windows\Fonts\simsun.ttc',
        max_words = 400,#最多字数
        stopwords = stopwords,
        max_font_size=400,#字体最大值
        random_state = 50, #随机生成状态，即多少种配色方案
    )
    wc.generate_from_text(wordlist_space)
    img_color = ImageColorGenerator(background_image)#背景色
    wc.recolor(color_func=img_color) #字体颜色为背景图片的颜色
    plt.imshow(wc) #显示词云图
    plt.axis('off')#不显示下标
    plt.show()

mk_wordcloud()
