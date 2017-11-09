from pypinyin import pinyin, lazy_pinyin, Style
#default (默认行为): 不做任何处理，原样返回:
nihao_default = lazy_pinyin('你好☆☆')
print("default")
print(nihao_default)
#ignore : 忽略该字符
nihao_ingore = lazy_pinyin('你好☆☆', errors='ignore')
print("ingore")
print(nihao_ingore)
#replace : 替换为去掉 \u 的 unicode 编码:
nihao_replace = lazy_pinyin('你好☆☆', errors='replace')
print("replace")
print(nihao_replace)
#callable 对象 : 提供一个回调函数，接受无拼音字符(串)作为参数, 支持的返回值类型: unicode 或 list ([unicode, ...]) 或 None
nihao_callable = lazy_pinyin('你好☆☆', errors=lambda x: 'star')
print("callable")
print(nihao_callable)