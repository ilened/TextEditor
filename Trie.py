from typing import List, Set, Tuple, NewType
from nltk.corpus import words
from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.endOfWord = False
        self.children = {}

class Trie:
    # Note : Trie is not case sensitive as I convert letters to lowercase.
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word : str, node : TrieNode):
        word = word.lower()
        currentNode = node
        for i in range(len(word)):
            if word[i] not in currentNode.children:
                currentNode.children[word[i]] = TrieNode()
            currentNode = currentNode.children[word[i]]

        currentNode.endOfWord = True


    def find(self, word : str):
        '''
        Checks if a word is in the Trie
        '''
        # Start at the root of the Trie
        node = self.root
        # Check if the word is valid one letter at a time down each level of the Trie
        for level in range(len(word)):
            letter = word[level].lower()
            if letter not in node.children:
                return False
            node = node.children[letter]
        return node.endOfWord

    def autocomplete(self, word : str):
        suggestions = []

        #Helper function to recursively discover autocomplete words
        def helper(node, word):
            if node.endOfWord:
                suggestions.append(word)

            for letter, letter_node in node.children.items():
                helper(letter_node, word + letter)

        node = self.root
        unfound = False
        temp = ""

        # For each letter in the word
        for letter in word:
            letter = letter.lower()
            # If the next letter cannot be found in the trie, break and return None
            if letter not in node.children or not node.children[letter]:
                unfound = True
                break
            # Otherwise, continue traversing down the tree
            temp += letter
            node = node.children[letter]

        # If the word is empty or the prefix is not found, return None
        if unfound or (node.endOfWord and not node.children) or not len(word):
            return None

        helper(node, temp)
        return suggestions
