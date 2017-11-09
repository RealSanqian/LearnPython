from pypinyin import lazy_pinyin, load_phrases_dict, Style, load_single_dict
hans = '桔子'
hans1 = lazy_pinyin(hans, style=Style.TONE2)
print(hans1)
load_phrases_dict({'桔子': [['jié'], ['zǐ']]})  # 增加 "桔子" 词组,故意使用一个错误的拼音
hans2 = lazy_pinyin(hans, style=Style.TONE2)
print(hans2)
hanm = '还没'
hanm1 = lazy_pinyin(hanm, style=Style.TONE2)
print(hanm1)
load_single_dict({ord('还'): 'hái,huán'})  # 调整 "还" 字的拼音顺序
hanm2 = lazy_pinyin('还没', style=Style.TONE2)
print(hanm2)
