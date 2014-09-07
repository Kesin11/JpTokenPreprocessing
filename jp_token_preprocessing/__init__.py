#coding: utf-8
"""
JpTokenPreprocessing

トークナイズされた日本語の前処理のためのモジュール

- Unicode正規化
- 記号除去
- 数字除去
- 小文字化、大文字化、キャピタライズ化
- N文字以下のトークンを除去

あたりをオプション制御で選択できるようにしたい

入力はリストかイテレーター
出力はイテレーターにしたい

オプションとして数字とか記号の判定は引数で渡した関数で判定できるようにしたい
ex: 独自正規表現でフィルタリングを行う関数
"""
import unicodedata
import re

class JpTokenPreprocessing(object):
    """JpWorkPreprocessing

    トークナイズされた日本語の前処理
    """
    def __init__(self, number=False, symbol=False, case='lower', unicode='NFKC', min_len=2, stopwords=[]):
        """初期化"""
        self.number = number
        self.symbol = symbol
        self.case = case
        self.unicode_normalize = unicode
        self.min_len = min_len
        self.stopwords = stopwords
        self.re_symbol = re.compile('^\W+$')

    def preprocessing(self, tokens):
        for token in tokens:
            if len(token) < self.min_len:
                continue

            token = self._transform(token)

            if not self._filter_out(token):
                continue

            if token in self.stopwords:
                continue

            yield token

    def _filter_out(self, token):
        if not self.number and self._is_number(token):
            return None
        if not self.symbol and self._is_symbol(token):
            return None

        return token

    def _transform(self, token):
        if self.unicode_normalize:
            token = unicodedata.normalize(self.unicode_normalize, token)

        if self.case:
            if self.case == 'lower':
                token = token.lower()
            elif self.case == 'upper':
                token = token.upper()
            elif self.case == 'capitalize':
                token = token.capitalize()

        return token

    def _is_number(self, token):
        if token.isdigit():
            return True

    def _is_symbol(self, token):
        if self.re_symbol.findall(token):
            return True
