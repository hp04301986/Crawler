import numpy as np
import snownlp
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

comment = []
with open("test.txt", mode='r', encoding='utf-8') as f:
    rows = f.readlines()
    for row in rows:
        if row not in comment:
            comment.append(row.strip('\n'))
    f.close()

def wordsence(self):
    sentimentslist = []
    for li in self:
        #print(li)
        s = snownlp.SnowNLP(li)
        #print(s.sentiments)
        sentimentslist.append(s.sentiments)
    myfont = fm.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')

    plt.title('琅琊榜之风起长林豆瓣评论情感分析', fontproperties=myfont)
    plt.hist(sentimentslist, bins=np.arange(0, 1, 0.01))
    plt.show()

wordsence(comment)
#print(matplotlib.matplotlib_fname())