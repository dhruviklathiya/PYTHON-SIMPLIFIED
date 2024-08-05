# DSA Questions

# 1. Arrays
# Q1: Write a Python function to find the maximum sum of a contiguous subarray using Kadane's Algorithm.
# A1:
def max_subarray_sum(arr):
    max_so_far = arr[0]
    max_ending_here = arr[0]
    
    for i in range(1, len(arr)):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far

# 2. Linked Lists
# Q2: Write a Python function to reverse a singly linked list.
# A2:
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):
    prev = None
    current = head
    
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    
    return prev

# 3. Stacks
# Q3: Write a Python function to evaluate a postfix expression using a stack.
# A3:
def evaluate_postfix(expression):
    stack = []
    
    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        else:
            val1 = stack.pop()
            val2 = stack.pop()
            if char == '+':
                stack.append(val2 + val1)
            elif char == '-':
                stack.append(val2 - val1)
            elif char == '*':
                stack.append(val2 * val1)
            elif char == '/':
                stack.append(val2 / val1)
    
    return stack.pop()

# 4. Queues
# Q4: Write a Python function to implement a queue using two stacks.
# A4:
class QueueWithStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop() if self.stack2 else None

# 5. Trees
# Q5: Write a Python function to perform an inorder traversal of a binary tree.
# A5:
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=' ')
        inorder_traversal(root.right)

# 6. Graphs
# Q6: Write a Python function to perform a depth-first search (DFS) on a graph.
# A6:
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# 7. Heaps
# Q7: Write a Python function to implement a min-heap and insert an element into it.
# A7:
import heapq
def insert_into_min_heap(heap, item):
    heapq.heappush(heap, item)

# 8. Hashing
# Q8: Write a Python function to find the first non-repeating character in a string using a hash map.
# A8:
def first_non_repeating_char(s):
    char_count = {}
    
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    for char in s:
        if char_count[char] == 1:
            return char
    
    return None

# 9. Sorting Algorithms
# Q9: Write a Python function to implement the quicksort algorithm.
# A9:
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# 10. Searching Algorithms
# Q10: Write a Python function to implement binary search on a sorted array.
# A10:
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# 11. Dynamic Programming
# Q11: Write a Python function to solve the 0/1 Knapsack problem using dynamic programming.
# A11:
def knapsack(weights, values, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]

# 12. Greedy Algorithms
# Q12: Write a Python function to solve the fractional knapsack problem using a greedy approach.
# A12:
def fractional_knapsack(weights, values, capacity):
    index = list(range(len(values)))
    ratio = [v/w for v, w in zip(values, weights)]
    index.sort(key=lambda i: ratio[i], reverse=True)
    
    max_value = 0
    for i in index:
        if weights[i] <= capacity:
            capacity -= weights[i]
            max_value += values[i]
        else:
            max_value += values[i] * (capacity / weights[i])
            break
    
    return max_value

# 13. Backtracking
# Q13: Write a Python function to solve the N-Queens problem using backtracking.
# A13:
def solve_n_queens(n):
    def is_safe(board, row, col):
        for i in range(col):
            if board[row][i] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        return True

    def solve(board, col):
        if col >= n:
            return True
        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 1
                if solve(board, col + 1):
                    return True
                board[i][col] = 0
        return False

    board = [[0 for _ in range(n)] for _ in range(n)]
    if not solve(board, 0):
        return []
    return board

# 14. Divide and Conquer
# Q14: Write a Python function to find the closest pair of points using the divide and conquer approach.
# A14:
def closest_pair_of_points(points):
    def distance(p1, p2):
        return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

    def closest_pair_rec(points_sorted_x, points_sorted_y):
        if len(points_sorted_x) <= 3:
            return min((distance(points_sorted_x[i], points_sorted_x[j]), (points_sorted_x[i], points_sorted_x[j]))
                       for i in range(len(points_sorted_x)) for j in range(i + 1, len(points_sorted_x)))

        mid = len(points_sorted_x) // 2
        Qx = points_sorted_x[:mid]
        Rx = points_sorted_x[mid:]
        midpoint = points_sorted_x[mid][0]
        Qy = list(filter(lambda x: x[0] <= midpoint, points_sorted_y))
        Ry = list(filter(lambda x: x[0] > midpoint, points_sorted_y))

        (dist1, pair1) = closest_pair_rec(Qx, Qy)
        (dist2, pair2) = closest_pair_rec(Rx, Ry)

        (min_dist, closest_pair) = (dist1, pair1) if dist1 < dist2 else (dist2, pair2)

        in_strip = [p for p in points_sorted_y if abs(p[0] - midpoint) < min_dist]
        for i in range(len(in_strip)):
            for j in range(i + 1, len(in_strip)):
                if (in_strip[j][1] - in_strip[i][1]) >= min_dist:
                    break
                d = distance(in_strip[i], in_strip[j])
                if d < min_dist:
                    min_dist = d
                    closest_pair = (in_strip[i], in_strip[j])
        return min_dist, closest_pair

    points_sorted_x = sorted(points, key=lambda x: x[0])
    points_sorted_y = sorted(points, key=lambda x: x[1])
    return closest_pair_rec(points_sorted_x, points_sorted_y)

# 15. Bit Manipulation
# Q15: Write a Python function to find the single number in a list where every other number appears twice.
# A15:
def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# 16. Sliding Window
# Q16: Write a Python function to find the maximum sum of a subarray of size k.
# A16:
def max_sum_subarray_k(nums, k):
    max_sum = current_sum = sum(nums[:k])
    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, current_sum)
    return max_sum

# 17. String Algorithms
# Q17: Write a Python function to find the longest palindromic substring in a given string.
# A17:
def longest_palindromic_substring(s):
    def expand_around_center(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest = ""
    for i in range(len(s)):
        odd_palindrome = expand_around_center(s, i, i)
        even_palindrome = expand_around_center(s, i, i + 1)
        longest = max(longest, odd_palindrome, even_palindrome, key=len)
    return longest

# 18. Trie
# Q18: Write a Python class to implement a Trie (prefix tree).
# A18:
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# 19. Segment Tree
# Q19: Write a Python class to implement a segment tree for range sum queries.
# A19:
class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        self.build_tree(data)

    def build_tree(self, data):
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index, value):
        pos = self.n + index
        self.tree[pos] = value
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]

    def range_sum(self, left, right):
        left += self.n
        right += self.n
        sum_ = 0
        while left < right:
            if left % 2:
                sum_ += self.tree[left]
                left += 1
            if right % 2:
                right -= 1
                sum_ += self.tree[right]
            left //= 2
            right //= 2
        return sum_

# 20. Graph Algorithms
# Q20: Write a Python function to find the shortest path in an unweighted graph using BFS.
# A20:
def bfs_shortest_path(graph, start, goal):
    queue = [(start, [start])]
    visited = set()
    while queue:
        vertex, path = queue.pop(0)
        if vertex in visited:
            continue
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor == goal:
                return path + [neighbor]
            else:
                queue.append((neighbor, path + [neighbor]))
    return None

