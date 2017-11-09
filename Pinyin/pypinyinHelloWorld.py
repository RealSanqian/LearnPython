from pypinyin import pinyin, lazy_pinyin, Style
zhongxin1 = pinyin("中心")
print(zhongxin1)
zhongxin2 = pinyin('中心', heteronym=True)  # 启用多音字模式
print(zhongxin2)
zhongxin3 = pinyin('中心', style=Style.FIRST_LETTER)  # 设置拼音风格
print(zhongxin3)
zhongxin4 = pinyin('中心', style=Style.TONE2, heteronym=True)
print(zhongxin4)
zhongxin5 = lazy_pinyin('中心')  # 不考虑多音字的情况
print(zhongxin5)