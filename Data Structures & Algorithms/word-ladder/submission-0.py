import string

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)


        queue = []
        queue.append([beginWord, 1])

        while queue:
            word, count = queue.pop(0)

            if word == endWord:
                return count
        
            for i in range(len(word)):
                # instead of --> for c in 'abcdefgi.....' use below does the same thing.
                for c in string.ascii_lowercase[:26]:
                    next_word = word[:i] + c + word[i + 1 :]

                    if next_word in wordList:
                        queue.append([next_word, count + 1])
                        wordList.remove(next_word)
        return 0