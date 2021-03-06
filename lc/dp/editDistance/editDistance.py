
'''
Leetcode 72: Edit Distance
Posted on August 15, 2018 · 4 minute read
Question
Given two words word1 and word2, find the minimum
 number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
'''

class Solution:
    def minDistance(self,word1,word2):
        def dp(word1,word2,i,j):
            if i >= len(word1) or j >= len(word2):
                return 0
            if word1[i] == word2[j]:
                return dp(word1,word2,i+1,j+1)
            else:

                insertion = 1+dp(word1,word2,i,j+1)
                replace = 1+dp(word1,word2,i+1,j+1)
                delete = 1+dp(word1,word2,i+1,j)
                return min(insertion,replace,delete)
            pass
        return dp(word1,word2,0,0)

    # Levenhstein distance
    def levMinDistance(self,word1,word2):
        rs,cs = len(word1),len(word2)
        matrix = [[0]*(cs) for i in range(rs)]
        for r in range(rs):
            for c in range(cs):
                if min(r,c) == 0:
                    matrix[r][c] = max(r,c)+1
                else: 
                    insert = matrix[r-1][c]+1
                    delete = matrix[r][c-1]+1
                    if (word1[r] != word2[c]):
                        replace = matrix[r-1][c-1]+1
                    else:
                        replace = matrix[r-1][c-1]
                    matrix[r][c] = min(insert,replace,delete)

            pass
        for r in matrix:
            print(r)
        return matrix[rs-1][cs-1]
    pass

s = Solution()
print("")
print(s.levMinDistance("cat","cap"))

