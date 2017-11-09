from pypinyin import lazy_pinyin
from pypinyin.style import register
@register('kiss')
def kiss(pinyin,**kwargs):
    return '😘 {0}'.format(pinyin)
meme = lazy_pinyin('么么', style='kiss')
print(meme)