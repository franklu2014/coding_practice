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
