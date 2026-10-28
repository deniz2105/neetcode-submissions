import bisect

class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.words = {}
        for i in range(len(wordsDict)):
            if wordsDict[i] in self.words:
                self.words[wordsDict[i]].append(i)
            else:
                self.words[wordsDict[i]] = [i] 
        
            

        

    def shortest(self, word1: str, word2: str) -> int:
        idxs1 = self.words[word1]
        shortest = float('inf')
        idxs2 = self.words[word2]
        for idx in idxs1:
            idx2 = bisect.bisect_right(idxs2, idx)
            currMin = float('inf')
            if idx2-1 >= 0 and idx2 < len(idxs2):
                currMin = min(abs(idx - (idxs2[idx2-1])), abs(idx - idxs2[idx2]))
            elif idx2-1 >= 0:
                currMin = abs(idx - (idxs2[idx2-1]))
            else:
                currMin = abs(idx - idxs2[idx2])
             
            shortest = min(currMin, shortest)
        return shortest



        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
