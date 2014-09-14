.. image:: https://travis-ci.org/Kesin11/JpTokenPreprocessing.svg?branch=master
    :target: https://travis-ci.org/Kesin11/JpTokenPreprocessing


====================================================
JpTokenPreprocessing -- Japanese Token Preprocessing
====================================================

JpTokenPreprocessing is a Python library for token preprocessing. It supports filtering noize (e.g. too short token, only number or only symbol token) and normalizing (support alphabet case and unicode normalize).
There are common preprocessing for natural language processing (NLP).

Usage
====================================

.. code-block :: python

    #coding: utf-8
    # Python3
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

Installation
====================================

.. code-block :: bash

    pip install JpTokenPreprocessing

MeCab for python3
-----------------------------------

Please apply below patch for installing and using MeCab module with python3. (2014/09/07 MeCab 0.996)

https://code.google.com/p/mecab/issues/detail?id=7

METHODS
====================================

JpTokenPreprocessing(args)
-----------------------------------

- number = BOOL (default: False)

    Allow only number token.

- symbol = BOOL (default: False)

    Allow only symbol token.

- case = 'lower' or 'upper' or 'capitalize'

    Normalize alphabet case.

- unicode = 'NFC' or 'NFKC' or 'NFD' or 'NFKD'a (default: 'NFKC')

    Normalize unicode string with unicodedata.normalize().

- min_len = int (default: 2)

    Filter out few character token. If min_len = 2 filter out token that has only 1 or 0 character.

- stopwords = list (default: [])

    Filter out any token that are contained in stopword list.

- JpTokenPreprocessing.preprocessing(iterable)

    Return preprocessed tokens iterator.

Future work
====================================

- Add some hook point for extending own preprocess.

Authors
====================================
Kenta kase kesin1202000@gmail.com

License
====================================
MIT License
