## Q850. Rectangle Area II
_re-visit_ https://leetcode.com/problems/rectangle-area-ii/submissions/

## Q930. Binary Subarrays With Sum
__must re-visit; spent long time to figure out__  
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

## Q391. Perfect Rectangle
__must re-vist__
https://leetcode.com/problems/perfect-rectangle/submissions/

## Q103. Binary Tree Zigzag Level Order Traversal
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/submissions/

## Q725. Split Linked List in Parts  
https://leetcode.com/problems/split-linked-list-in-parts/submissions/

## Q130. Surrounded Regions  
__must re-visit__
https://leetcode.com/problems/surrounded-regions/submissions/

## Q341. Flatten Nested List Iterator  
https://leetcode.com/problems/flatten-nested-list-iterator/submissions/

## Q945. Minimum Increment to Make Array Unique
__must re-visit__  
https://leetcode.com/problems/minimum-increment-to-make-array-unique/

## Q1218. Longest Arithmetic Subsequence of Given Difference
_re-visit_  
https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/submissions/

## Q388. Longest Absolute File Path ***
https://leetcode.com/problems/longest-absolute-file-path/submissions/

## Q554. Brick Wall ****
https://leetcode.com/problems/brick-wall/submissions/

## Q22. Generate Parentheses
https://leetcode.com/problems/generate-parentheses/submissions/

## Q19. Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/

## Q756. Pyramid Transition Matrix
https://leetcode.com/problems/pyramid-transition-matrix/  
We are stacking blocks to form a pyramid. Each block has a color which is a one letter string.  We are allowed to place any color block C on top of two adjacent blocks of colors A and B, if and only if ABC is an allowed triple.  
__Sol:__
```python
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        
        # scan throught the allowed combinations
        # so that the we only look at the allowed upper blocks in constant time
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

## Q1145. Binary Tree Coloring Game
https://leetcode.com/problems/binary-tree-coloring-game/

## Q12. Integer to Roman
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

## Q11. Container With Most Water
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

## Q5. Longest Palindromic Substring
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

## Q3. Longest Substring Without Repeating Characters
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
