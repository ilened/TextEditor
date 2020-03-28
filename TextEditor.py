import Trie, ropes, os, string, sys

class SimpleEditor:
    def __init__(self, documentPath , dictionaryFilePath):
        # Create Trie to store dictionary words
        self.dictionaryTrie = Trie.Trie()
        # Create rope structure for document
        self.document = None
        self.populateDocumentWithInputText(documentPath)
        # Insert dictionary words in Trie
        for word in self.yieldWords(dictionaryFilePath):
            self.dictionaryTrie.insert(word,self.dictionaryTrie.root)
        # Create an empty rope object to later store pasted text
        self.paste_text = ropes.Rope("")

    def yieldWords(self,filename):
        '''
        Given a filename, this function will yield words from the file that do not contain numbers
        and exclude punctuations from the word. 
        '''
        with open(filename, "r") as input_dictionary:
            for line in input_dictionary:
                words = line.split()
                for word in words:
                    if any(char.isdigit() for char in word):
                        continue
                    word = word.translate(str.maketrans('','',string.punctuation))
                    yield word

    def populateDocumentWithInputText(self,filename):
        '''
        A function to populate the self.document as a rope containing rope the input file's text.
        '''
        with open(filename, "r") as fi:
            data_text = fi.read()
            self.document = ropes.Rope(data_text)

    def cut(self, i, j):
        if i > j or j < i or i < 0 or j > len(str(self.document)):
            return "Range Error"

        self.paste_text = self.document[i:j]
        self.document = self.document[:i] + self.document[j:]

    def copy(self, i, j):
        if i > j or j < i or i < 0 or j > len(str(self.document)):
            return "Range Error"

        self.paste_text = self.document[i:j]

    def paste(self, i):
        if i < 0 or i > len(str(self.document)):
            return "Range Error"

        self.document = self.document[:i] + self.paste_text + self.document[i:]

    def get_text(self):
        return str(self.document)

    def misspellings(self):
        result = 0
        for word in str(self.document).split():
            word = word.translate(str.maketrans('','',string.punctuation))
            if not self.dictionaryTrie.find(word):
                result += 1
        return result

    def autocomplete(self, word):
        return self.dictionaryTrie.autocomplete(word)
