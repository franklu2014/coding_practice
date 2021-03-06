## Binary Tree

- Q144. Binary Tree Preorder Traversal
https://leetcode.com/problems/binary-tree-preorder-traversal/submissions/

- Swap Nodes [Algo]  
_re-visit_; 2 versions of solutions
https://www.hackerrank.com/challenges/swap-nodes-algo/problem  

- Is This a Binary Search Tree?  
_re-visit_; 2 versions of solutions
https://www.hackerrank.com/challenges/is-binary-search-tree/problem

---
## String manipulation (sliding window)

- Q3. Longest Substring Without Repeating Characters (Python & Scala)  
https://leetcode.com/problems/longest-substring-without-repeating-characters/

- Q438. Find All Anagrams in a String  
https://leetcode.com/problems/find-all-anagrams-in-a-string/

- Q30. Substring with Concatenation of All Words (sliding window)  
https://leetcode.com/problems/substring-with-concatenation-of-all-words/

- Q76. Minimum Window Substring (doubly sliding window)  
_re-visit_  
https://leetcode.com/problems/minimum-window-substring/

- Q438. Find All Anagrams in a String  
https://leetcode.com/problems/find-all-anagrams-in-a-string/

- Q424. Longest Repeating Character Replacement (Python & Scala; doubly sliding window)  
https://leetcode.com/problems/longest-repeating-character-replacement/

- Q567. Permutation in String  
https://leetcode.com/problems/permutation-in-string/

---
## Back-trace

- Q90. Subsets II  
https://leetcode.com/problems/subsets-ii/

- Q78. Subsets  
https://leetcode.com/submissions/detail/401935231/

- Q39. Combination Sum  
https://leetcode.com/submissions/detail/401989806/

- Q40. Combination Sum II
https://leetcode.com/submissions/detail/402096397/
---

- Q55. Jump Game  
https://leetcode.com/problems/jump-game/submissions/

- Q1306. Jump Game III  
https://leetcode.com/problems/jump-game-iii/submissions/

- Q45. Jump Game II  
<span style="color:red">__must re-visit__</span>  
_tripped again on 2020-07-30 & 2020-08-04_  
https://leetcode.com/problems/jump-game-ii/submissions/

---
## overlapping segments

- Q850. Rectangle Area II  
_re-visit_; keep max of overlapping values  
https://leetcode.com/problems/rectangle-area-ii/submissions/

- Q732. My Calendar III  
https://leetcode.com/problems/my-calendar-iii/submissions/

- Q729. My Calendar I  
https://leetcode.com/problems/my-calendar-i/submissions/  

- Q731. My Calendar II  
https://leetcode.com/problems/my-calendar-ii/submissions/  

- Q855. Exam Room
https://leetcode.com/problems/exam-room/submissions/  

- __coordinate compression__  
    - Q699. Falling Squares  
    _re-visit_  
    https://leetcode.com/problems/falling-squares/submissions/

    - Q218. The Skyline Problem  
    __must re-visit__
    https://leetcode.com/problems/the-skyline-problem/submissions/

---
## binary search for minimizing maximum or maximizing minimum
The LeetCode page for similar questions: https://leetcode.com/problems/magnetic-force-between-two-balls/discuss/794070/Python-Binary-search-solution-with-explanation-and-similar-questions  

- Q1552. Magnetic Force Between Two Balls
https://leetcode.com/problems/magnetic-force-between-two-balls/

- Q410. Split Array Largest Sum
https://leetcode.com/problems/split-array-largest-sum/  

- Q875. Koko Eating Bananas
https://leetcode.com/problems/koko-eating-bananas/submissions/

- Q215. Kth Largest Element in an Array  
_the 1036ms solution uses a supposedly $O(n)$ algo_  
_the 64ms solution uses $O(\log n)$ algo_
https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/

---
## DP questions

- The Minion Game
https://www.hackerrank.com/challenges/the-minion-game/problem

- Q843. Guess the Word  
_very interesting_  
https://leetcode.com/problems/guess-the-word/submissions/

- Q746. Min Cost Climbing Stairs
https://leetcode.com/problems/min-cost-climbing-stairs/submissions/

- Q72. Edit Distance  
_re-visit_; DP, lru_cache  
https://leetcode.com/problems/edit-distance/submissions/

- Q44. Wildcard Matching  
__should re-visit with Q10__; DP  
https://leetcode.com/problems/wildcard-matching/submissions/


- Q930. Binary Subarrays With Sum
__must re-visit__; *spent long time to figure out*  
In an array A of 0s and 1s, how many non-empty subarrays have sum S?
https://leetcode.com/problems/binary-subarrays-with-sum/submissions/  
```python
def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        ret = subtot = 0
        cnt = {0: 1}
        for n in A:
            subtot += n
            if subtot - S in cnt:
                ret += cnt[subtot - S]
            cnt[subtot] = 1 + cnt[subtot] if subtot in cnt else 1
        return ret
```

---
## Don't have category yet but interesting

- Dynamic Array  
https://www.hackerrank.com/challenges/dynamic-array/submissions/code/179647633

- Bigger is Greater  
https://www.hackerrank.com/challenges/bigger-is-greater/submissions/code/181147729

- Word Order  
https://www.hackerrank.com/challenges/word-order/submissions/code/182869636

- Maximize It!  
_re-visit; my implementation of itertools.product_  
https://www.hackerrank.com/challenges/maximize-it/submissions/code/182912139

- Q678. Valid Parenthesis String  
_2-stack solution; __TODO: DP solution___  
https://leetcode.com/problems/valid-parenthesis-string/

- Q785. Is Graph Bipartite?  
  - my solution: https://leetcode.com/problems/is-graph-bipartite/submissions/
  - elegant solution: https://leetcode.com/problems/is-graph-bipartite/discuss/119514/python-3-bfs-dfs-solutions

- Q316. Remove Duplicate Letters  
_re-visit; 2 sols: 36ms and 56ms_  
https://leetcode.com/problems/remove-duplicate-letters/

- Q52. N-Queens II  
_very similar to N-Queens below_  
https://leetcode.com/problems/n-queens-ii/

- Q51. N-Queens  
_more of an implementation test; not hard really_  
https://leetcode.com/submissions/detail/402379417/

- Organizing Containers of Balls (Python & Scala)  
_interesting line of thought but not hard_
https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem

- Queen's Attack (Python & Scala)  
https://www.hackerrank.com/challenges/queens-attack-2/problem  

- Non-Divisible Subset (evenly divisible)  
https://www.hackerrank.com/challenges/non-divisible-subset/problem?isFullScreen=false

- Between Two Sets (GCF & LCM)
__must re-visit; tripped several times__
https://www.hackerrank.com/challenges/between-two-sets/problem

- Forming a Magic Square (implement beautiful 3x3 matrix)
https://www.hackerrank.com/challenges/magic-square-forming/problem

- Lily's Homework (sort bidirectionally)  
_re-visit_  
https://www.hackerrank.com/challenges/lilys-homework/problem

- Q391. Perfect Rectangle
__must re-vist__  
https://leetcode.com/problems/perfect-rectangle/submissions/

- Q103. Binary Tree Zigzag Level Order Traversal
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/submissions/

- Q725. Split Linked List in Parts  
https://leetcode.com/problems/split-linked-list-in-parts/submissions/

- Q130. Surrounded Regions  
__must re-visit__  
https://leetcode.com/problems/surrounded-regions/submissions/

- Q341. Flatten Nested List Iterator  
https://leetcode.com/problems/flatten-nested-list-iterator/submissions/

- Q945. Minimum Increment to Make Array Unique
__must re-visit__  
https://leetcode.com/problems/minimum-increment-to-make-array-unique/

- Q1218. Longest Arithmetic Subsequence of Given Difference
_re-visit_  
https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/submissions/

- Q388. Longest Absolute File Path ***
https://leetcode.com/problems/longest-absolute-file-path/submissions/

- Q554. Brick Wall ****
https://leetcode.com/problems/brick-wall/submissions/

- Q22. Generate Parentheses
https://leetcode.com/problems/generate-parentheses/submissions/

- Q19. Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/

- Q756. Pyramid Transition Matrix
https://leetcode.com/problems/pyramid-transition-matrix/  
We are stacking blocks to form a pyramid. Each block has a color which is a one letter string.  We are allowed to place any color block C on top of two adjacent blocks of colors A and B, if and only if ABC is an allowed triple.  
__Sol:__
```python
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:

        # scan through the allowed combinations
        # so that we only look at the allowed upper blocks in constant time
        dic = dict()
        for s in allowed:
            dic.setdefault(s[0 : 2], []).append(s[2])

        def dfs(i, old, new):
            for c in dic.setdefault(old[i : i+2], []):
                res = False
                if len(old) == 2 and len(new + c) == 1:
                    return True
                elif i >= len(old) - 2:
                    res = dfs(0, new + c, '')
                else:
                    res = dfs(i + 1, old, new + c)
                if res:
                    return True
            return False

        return dfs(0, bottom, '')

```

- Q1145. Binary Tree Coloring Game
https://leetcode.com/problems/binary-tree-coloring-game/

- Q12. Integer to Roman
Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.  
__Sol:__
```python
class Solution:
    def intToRoman(self, num: int) -> str:
        denom = 1000
        mp = {
            1000: 'M',
            500: 'D',
            100: 'C',
            50: 'L',
            10: 'X',
            5: 'V',
            1: 'I'
        }
        res = ''

        while num > 0:
            curr = num // denom
            if curr <= 3:
                res = res + mp[denom] * curr
            elif curr == 4:
                res = res + mp[denom] + mp[denom * 5]
            elif curr <= 8:
                dup = curr - 5
                res = res + mp[denom * 5] + mp[denom]*dup
            else:
                dup = 10 - curr
                res = res + mp[denom] * dup + mp[denom * 10]
            num = num - curr * denom
            denom = denom // 10

        return res
```

- Q11. Container With Most Water
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.  
__Sol:__
```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        maxarea = 0
        # im, jm = i, j

        while i < j:
            x, y = height[i], height[j]
            area = (j - i) * min(x, y)
            if area > maxarea:
                maxarea = area
                # im, jm = i, j
            if x < y:
                i += 1
            else:
                j -= 1

        return maxarea

```

- Q5. Longest Palindromic Substring
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

__Sol 1:__ This has the best time and space complexity
```python
class Solution:
    def bfs(self, s, l, r):
        while(l >= 0 and r < len(s) and s[l]==s[r]):
            l -= 1
            r += 1
        return l+1, r-1

    def longestPalindrome(self, s: str) -> str:
        # self.s = s
        left = 0
        right = 1
        mx = 0
        for i in range(1, len(s), 1):
            l, r = self.bfs(s, i-1, i+1)
            if(r - l + 1 > mx):
                mx = r - l + 1
                left = l
                right = r
            l, r = self.bfs(s, i-1, i)
            if(r - l + 1 > mx):
                mx = r - l + 1
                left = l
                right = r
        return s[left : right + 1]
```
__Sol 2:__ This is the slowest but supposed to have similar performance as Sol_1
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while(i < j):
            if(s[i] != s[j]):
                return False
            i += 1
            j -= 1
        return True

    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        size = len(s)
        res = ''
        ifFind = False

        while(size > 0 and not ifFind):
            i = 0
            while(i + size <= length):
                if(self.isPalindrome(s[i : i+size])):
                    res = s[i : i+size]
                    ifFind = True
                    break
                i += 1
            size -= 1

        return res
```
__Sol 3:__ Dynamic programming technique; works but slow
```python
class Solution:

    def longestPalindrome(self, s: str) -> str:
        ll = len(s)
        mp = [[True]*ll for i in range(ll)]
        mx = (0, (0, 0))

        for i in range(1, ll, 1):
            c = s[i]
            for row in range(i-1, -1, -1):
                if not (mp[row+1][i-1] and c == s[row]):
                    mp[row][i] = False
                else:
                    mx = (i - row, (row, i)) if i-row > mx[0] else mx
        return s[mx[1][0] : mx[1][1]+1]
```

- Q3. Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.

__Sol:__
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        prev = ''
        res = list()
        # temp = dict()
        n_max = 0
        # idx = 0
        for c in s:
            if c not in res:
                # temp[c] = idx
                res.append(c)
            else:
                curr_len = len(res)
                n_max = curr_len if curr_len > n_max else n_max
                if c != prev:
                    res = res[res.index(c) + 1:]
                    res.append(c)
                else:
                    res = list(c)
            prev = c

        return len(res) if len(res) > n_max else n_max
```
