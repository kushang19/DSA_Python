# =================  Word Ladder I ======================

from collections import deque

class Solution:
   
    # Function to determine number of steps
    # to reach from start ward to target word
    def wordLadderLength(self, startWord,
                        targetWord, wordList):
                           
        # Queue data structure to store pair:
        # {"word", steps to reach "word"}
        q = deque([(startWord, 1)])

        # Add all the words to a hashset
        st = set(wordList)
       
        # If target word is not there in word list,
        # return 0 as it is not possible to transform
        if targetWord not in st:
            return 0
       
        # Erase the starting word
        # from set (if it exists)
        st.discard(startWord)
       
        # Until the queue is empty
        while q:
           
            # Get the word from queue
            word, steps = q.popleft()

            # Return steps if target word is achieved
            if word == targetWord:
                return steps
           
            # Iterate on every character
            for i in range(len(word)):
                # Store the original letter
                original = word[i]
               
                # Replacing current character with
                # letters from 'a' to 'z' to match
                # any possible word from set
                for ch in range(ord('a'), ord('z') + 1):
                    word = word[:i] + chr(ch) + word[i+1:]
                   
                    # Check if it exists in the set
                    if word in st:
                       
                        # Erase the word from set
                        st.remove(word)
                       
                        # Add the transition to the queue
                        q.append((word, steps + 1))
               
                # Update the original letter back
                word = word[:i] + original + word[i+1:]
       
        # If no transformation sequence
        # is found, return 0
        return 0

if __name__ == "__main__":
   
    startWord = "der"
    targetWord = "dfs"
    wordList = ["des", "der", "dfr", "dgt", "dfs"]
   
    # Creating an instance of
    # Solution class
    sol = Solution()
   
    # Function call to determine number of
    # steps to reach from start ward to target word
    ans = sol.wordLadderLength(startWord, targetWord, wordList)
   
    # Output
    print("Word ladder length is:", ans)

















# # Word Ladder - Shortest Chain To Reach Target Word
# # https://www.youtube.com/watch?v=h9iTnkgv05E

# from collections import defaultdict, deque
# from typing import List

# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         if endWord not in wordList:
#             return 0
        
#         # Create adjacency map using patterns
#         nei = defaultdict(list)
#         wordList.append(beginWord)
#         for word in wordList:
#             for j in range(len(word)):
#                 pattern = word[:j] + "*" + word[j + 1:]
#                 nei[pattern].append(word)
        
#         # BFS initialization
#         visit = set([beginWord])
#         q = deque([beginWord])
#         res = 1
        
#         while q:
#             for i in range(len(q)):
#                 word = q.popleft()
#                 if word == endWord:
#                     return res
#                 for j in range(len(word)):
#                     pattern = word[:j] + "*" + word[j + 1:]
#                     for neiWord in nei[pattern]:
#                         if neiWord not in visit:
#                             visit.add(neiWord)
#                             q.append(neiWord)
#             res += 1
#         return 0