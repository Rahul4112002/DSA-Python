# **Time Complexity of Common Python Operations & Methods**

# **List Operations**
# Indexing: O(1)
# Append: O(1)
# Pop (last): O(1)
# Pop (middle): O(n)
# Insert (middle): O(n)
# Delete (middle): O(n)
# Iteration: O(n)
# Sorting: O(n log n)
# Extend: O(k) (k = length of extending list)

# **Dictionary Operations**
# Get, Set, Delete (by key): O(1) (on average)
# Membership Check (`key in dict`): O(1)
# Iteration over keys/values/items: O(n)

# **Set Operations**
# Add: O(1)
# Remove/Discard: O(1)
# Membership Check (`x in set`): O(1)
# Iteration: O(n)
# Union/Intersection/Difference: O(min(len(set1), len(set2)))

# **String Operations**
# Indexing: O(1)
# Slicing: O(k) (k = slice length)
# Concatenation (`+` for small strings): O(n)
# String Join (`''.join(list)`): O(n)
# Membership Check (`x in string`): O(n)

# **Tuple Operations**
# Indexing: O(1)
# Iteration: O(n)
# Membership Check (`x in tuple`): O(n)

# **Queue (collections.deque) Operations**
# Append (left or right): O(1)
# Pop (left or right): O(1)
# Membership Check: O(n)
# Iteration: O(n)

# **Heap (heapq) Operations**
# Push: O(log n)
# Pop: O(log n)
# Heapify: O(n)

# **Counter (collections.Counter) Operations**
# Initialization: O(n)
# Access Count: O(1)
# Most Common Elements: O(n log k) (for top-k elements)

# **DefaultDict (collections.defaultdict) Operations**
# Get/Set Item: O(1)
# Membership Check (`key in defaultdict`): O(1)
