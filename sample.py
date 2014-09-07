#coding: utf-8
from jp_token_preprocessing import JpTokenPreprocessing
import MeCab

# Return japanese word tokens using morphological analyzer MeCab.
# And select only noun.
def tokenize(text):
    tagger = MeCab.Tagger()
    node = tagger.parseToNode(text)
    while node:
        if '名詞' in node.feature:
            surface = node.surface
            yield surface
        node = node.next

if __name__=='__main__':
    text = """
    これは自然言語処理に必須な前処理のためのモジュールです。
    形態素解析や、n-gramでトークン化した後のフィルタリング、正規化を補助します。
    一語だけのトークンや'1234'のような数字だけのトークン、'!!'のような記号だけのトークンのフィルタリング、
    全角文字'ＰＹＴＨＯＮ'の半角化、英単語'Word'の小文字化といった正規化も行えます。
    さらに必ず除外したいトークンをストップワードに設定することもできます。
    """
    stopwords = ['これ', 'こと']

    tokens = tokenize(text)
    """
    >>> print(list(tokens))

    ['', '', '言語', '処理', '必須', '前', '処理', 'ため', 'モジュール', '形態素',
    '解析', 'n', '-', 'gram', 'トー', 'クン', '化', '後', 'フィルタ', 'リング', '正規',
    '化', '補助', '一語', 'トーク', 'ン', "'", '1234', "'", 'よう', '数字','トー',
    'クン', "'!!'", 'よう', '記号', 'トー', 'クン', 'フィルタ', 'リング', '全角',
    '文字', "'", 'ＰＹＴＨＯＮ', "'", '半角', '化', '英単語', "'", 'Word',"'", '小文字',
    '化', '正規', '化', '除外', 'トーク', 'ン', 'ストップ', 'ワード', '設定', 'こと']
    """

    tokens = tokenize(text)
    preprocessor = JpTokenPreprocessing(number=False,
                                        symbol=False,
                                        case='lower',
                                        unicode='NFKC',
                                        min_len=2,
                                        stopwords=stopwords)
    tokens = preprocessor.preprocessing(tokens)
    # Return iterator of tokens. Using list() for print sample.
    """
    >>> print(list(tokens))
    ['言語', '処理', '必須', '処理', 'ため', 'モジュール', '形態素', '解析', 'gram',
    'トー', 'クン', 'フィルタ', 'リング', '正規', '補助', '一語', 'トーク', 'よう',
    '数字', 'トー', 'クン', 'よう', '記号', 'トー', 'クン', 'フィルタ', 'リング',
    '全角', '文字', 'python', '半角', '英単語', 'word', '小文字', '正規', '除外',
    'トーク', 'ストップ', 'ワード', '設定']
    """
