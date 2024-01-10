from typing import List


class TrieNode:

    def __init__(self, char: str) -> None:
        # the character stored in this node
        self.char = char

        # indicates that this is the end of the word
        self.is_end = False

        # how many times this word is used
        self.counter = 0

        # a dictionary of child nodes
        self.children = {}

        # top 5 searches
        self.top_searches = []

    # def new(self, char:str) -> 'TrieNode':
    #     if char in self.children:
    #         return self.children[char]
    #     else:
    #         new_node = TrieNode(char)
    #         self.children[char] = new_node
    #         return new_node


class Trie(object):
    """The Trie object itself"""

    def __init__(self) -> None:
        """
        The trie has at least the root node.
        The root node does not store any character
        """
        self.root = TrieNode("")

    def insert(self, word: str):
        node = self.root

        # Loop through each character in the word
        # Check if there is no child containing the character, create a new child for the current node
        for char in word:
            if char in node.children:
                # character is found, return the reference
                node = node.children[char]
            else:
                # If a character is not found,
                # create a new node in the trie
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        # Mark the end of a word
        node.is_end = True

        # Increment the counter to indicate that we see this word once more
        node.counter += 1

    def track(self, query: str, word: str):
        """Store the top word(s) under the query """
        node = self.root

        for char in query:
            if char in node.children:
                # character is found, return the reference
                node = node.children[char]
            else:
                raise Exception()

        # store top searches
        node.top_searches.append(word)

        # it's not the word itself, update counter
        if node.is_end:
            node.counter += 1

        pass

    def query(self, q: str, limit=5) -> str:
        """Given an input (a prefix), retrieve all words stored in
        the trie with that prefix, sort the words by the number of 
        times they have been inserted
        """
        # Use a variable within the class to keep all possible outputs
        # As there can be more than one word with such prefix
        self.output = []
        node = self.root

        # Check if the prefix is in the trie
        for char in q:
            if char in node.children:
                node = node.children[char]
            else:
                # cannot found the prefix, return empty list
                return []
        # Traverse the trie to get all candidates
        self.dfs(node, q[:-1])

        # rank with top searches
        ranked = {}
        for item in self.output:
            if item[0] in ranked:
                ranked[item[0]] += item[1]
            else:
                ranked[item[0]] = item[1]

        self.output = list(ranked.items())

        # Sort the results in reverse order and return
        return sorted(self.output, key=lambda x: x[1], reverse=True)[:limit]

    def dfs(self, node: TrieNode, prefix):
        """Depth-first traversal of the trie

        Args:
            - node: the node to start with
            - prefix: the current prefix, for tracing a
                word while traversing the trie
        """
        if node.is_end:
            self.output.append((prefix + node.char, node.counter))

        if len(node.top_searches) > 0:
            for ts in node.top_searches:
                self.output.append((ts, 1))

        for child in node.children.values():
            self.dfs(child, prefix + node.char)


t = Trie()

t.insert("was")
t.insert("word")
t.insert("war")
t.insert("wax")
t.insert("what")
t.insert("whack")
t.insert("whacka")
t.insert("which")
t.insert("where")
t.insert("wash")
t.insert("washing")
t.insert("washington")

print(t.query("wash", 5))

# user has clicked the search, update the counter
t.track("wa", "war")
t.track("war", "war")
t.track("was", "washington")
t.track("wash", "washington")

print(t.query("wa", 5))
