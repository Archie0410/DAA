class Solution(object):
    def sortSentence(self, s):
        words = s.split()
        sorted_words = [''] * len(words)
        for word in words:
            index = int(''.join(filter(str.isdigit, word))) - 1
            sorted_words[index] = ''.join(filter(str.isalpha, word))
        return ' '.join(sorted_words)