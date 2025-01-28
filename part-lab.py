class Solution:
    def partitionLabels(self, s: str) -> List[int]:
            already = {}
            already_word = []
            for c in s:
                if c in already:
                    word_tot = ""
                    while not (c in word_tot):
                        word_tot = already_word[-1] + word_tot 
                        already_word.pop()
                    already_word.append(word_tot + c)
                else:
                    already[c] = 1
                    already_word.append(c)
            for i, el in enumerate(already_word):
                already_word[i] = len(already_word[i])
            return already_word