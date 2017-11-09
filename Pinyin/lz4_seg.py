from pypinyin.contrib.mmseg import seg
text = '你好，我是中国人，我爱我的祖国'
text_cut = seg.cut(text)
print(text_cut)
text_cut_list = list(text_cut)
print(text_cut_list)
seg.train(['祖国','我是'])
text_cut_list_train = list(seg.cut(text))
print(text_cut_list_train)