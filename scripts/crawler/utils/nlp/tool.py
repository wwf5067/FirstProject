import re
import jiagu

# text = '东京奥运会纸板床的标价上万元（人民币），实际成本真有那么高吗？'

# words = jiagu.seg(text) # 分词
# print(words)

# # pos = jiagu.pos(words) # 词性标注
# # filter(lambda x: x!='n' or x!='v', pos)
# pos = jiagu.pos(words)
# kws = [words[idx] for idx, val in enumerate(pos) if val == 'n' or val == 'v' or val == 'nr' or val == 'ns' or val == 'nt' or val == 'nz']
# print(kws)
# print(pos)
# ner = jiagu.ner(words) # 命名实体识别
# print(ner)

def getKW(text):
    words = jiagu.seg(text)

    ner = jiagu.ner(words)
    ke = [words[idx] for idx,val in enumerate(ner) if val != 'O']

    pos = jiagu.pos(words)
    kw_t = [words[idx] for idx, val in enumerate(pos) if val == 'n' or val == 'v' 
        or val == 'nr' or val == 'ns' or val == 'nt' or val == 'nz']
    kw = list(set(kw_t).difference(set(ke)))
    
    return ke, kw

# print(getKW(text))