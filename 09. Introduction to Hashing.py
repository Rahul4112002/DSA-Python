# ========================================
# HASHING IMPLEMENTATION IN PYTHON
# ========================================

"""
Definition of Hashing:
----------------------
Hashing is a technique used to efficiently store and retrieve elements by mapping 
them to an index using a hash function. It helps achieve O(1) average time complexity 
for search and retrieval, making it useful for large-scale data processing.
"""

# ========================================
# INTEGER HASHING
# ========================================

# Given Arrays
n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]

# ---- 1. Brute Force Approach (O(n * m)) ----
def brute_force_integer_hash(n, m):
    """ Brute force approach for integer hashing (Slow) """
    print("Brute Force Integer Hashing:")
    for query in m:
        count = 0
        for num in n:
            if num == query:
                count += 1
        print(f"{query}: {count}")

# ---- 2. Hash List Approach (Optimal O(n + m)) ----
def hash_list_integer(n, m):
    """ Hash List approach for integer hashing (Efficient) """
    print("\nHash List Integer Hashing:")
    hash_list = [0] * 11  # Fixed size for 1 to 10

    for num in n:
        hash_list[num] += 1  # Store frequency

    for query in m:
        if 1 <= query <= 10:
            print(f"{query}: {hash_list[query]}")
        else:
            print(f"{query}: 0")  # Out of range case

# ---- 3. Dictionary Approach (Alternative O(n + m)) ----
def dictionary_integer_hash(n, m):
    """ Dictionary-based approach for integer hashing """
    print("\nDictionary-Based Integer Hashing:")
    hash_dict = {}  # Dynamic storage

    for num in n:
        hash_dict[num] = hash_dict.get(num, 0) + 1  # Increment frequency

    for query in m:
        print(f"{query}: {hash_dict.get(query, 0)}")  # Default to 0 if not found

# ========================================
# CHARACTER HASHING
# ========================================

# Given String and Queries
s = "azyxyyzaaaa"
q = ['d', 'a', 'y', 'x']

# ---- 1. Brute Force Approach (O(n * q)) ----
def brute_force_character_hash(s, q):
    """ Brute force approach for character hashing (Slow) """
    print("\nBrute Force Character Hashing:")
    for char in q:
        count = sum(1 for c in s if c == char)
        print(f"{char}: {count}")

# ---- 2. Hash List Approach (Optimal O(n + q)) ----
def hash_list_character(s, q):
    """ Hash List approach for character hashing (Efficient) """
    print("\nHash List Character Hashing:")
    char_hash = [0] * 26  # 26 letters in a-z

    for ch in s:
        char_hash[ord(ch) - ord('a')] += 1  # Store frequency

    for ch in q:
        print(f"{ch}: {char_hash[ord(ch) - ord('a')]}")  # Fetch count

# ---- 3. Dictionary Approach (Alternative O(n + q)) ----
def dictionary_character_hash(s, q):
    """ Dictionary-based approach for character hashing """
    print("\nDictionary-Based Character Hashing:")
    char_dict = {}  # Dynamic storage

    for ch in s:
        char_dict[ch] = char_dict.get(ch, 0) + 1  # Increment frequency

    for ch in q:
        print(f"{ch}: {char_dict.get(ch, 0)}")  # Default to 0 if not found

# ========================================
# RUNNING ALL APPROACHES
# ========================================

if __name__ == "__main__":
    # Running Integer Hashing Methods
    brute_force_integer_hash(n, m)
    hash_list_integer(n, m)
    dictionary_integer_hash(n, m)

    # Running Character Hashing Methods
    brute_force_character_hash(s, q)
    hash_list_character(s, q)
    dictionary_character_hash(s, q)
