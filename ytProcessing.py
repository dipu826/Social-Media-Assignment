"""
COSC2671 Social Media and Network Analytics
@author Jeffrey Chan, RMIT University, 2023
"""

import re
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords

class TextProcessing:
    def __init__(self, tokenizer, stopwords):
        self.tokenizer = tokenizer
        self.stopwords = stopwords

    def process(self, text):
        text = text.lower()
        tokens = self.tokenizer.tokenize(text)  # Fixed typo here
        tokensStripped = [tok.strip() for tok in tokens]

        regexDigit = re.compile("\d")  # Adjusted to match any digit
        regexHttp = re.compile(r"http[s]?://")  # Adjusted to match any URL
        regexEmoji = re.compile("[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F700-\U0001F77F\U0001F900-\U0001F9FF\U0001F1E0-\U0001F1FF]", re.UNICODE)


        return [
            tok for tok in tokensStripped
            if tok not in self.stopwords and not regexDigit.search(tok) and not regexHttp.search(tok)
        ]
