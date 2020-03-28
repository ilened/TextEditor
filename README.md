# TextEditor

A TextEditor that can cut text, copy text, paste text, get text, and count misspelled words. I also added in an additional autocomplete feature.

# External Libraries
``` bash
$ pip install pyrope
```

# Rope
A rope, also known as a cord, is a binary tree composed of smaller strings that is used to efficiently store and manipulate a very long string, which is definitely useful for our purposes.

| Operation    | Time          |
| ------------ | ------------- |
| cut(i,j)     | O(j + log N)  |
| copy(i,j)    | O(j + log N)  |
| paste(i)     | O(log N)      |
| get_text     | O(N)          |

where N represented the number of nodes in the Rope.

### Pros
- Fast insertion and deletion of text compared to arrays
- Rope operations do not require O(n) extra memory
- Ropes do not need large continguous memory areas like arrays
- Stable performance regardless of size

### Cons
- Occupies greater overall storage space in comparison to a simple string
- Increased complexity of structure can create a greater risk of bugs
- Slower on small strings

### Which data structure is better an array or rope?
The answer as always is: it depends.

If we are only dealing with small and simple strings then we would want to use an array.

However since we are building a text editor, I am assuming that the document string will be relatively large and continue to grow therefore a rope is better suited. For fast operations we pay for the price in overall storage but this trade-off reduces as our string grows.

Performance wise, I noticed that the rope implementation improved in performance drastically for the cut, paste, and 
copy operations. However, the performance did not drastically improve for the get_text operation, which is due to the fact that we must build the string from the rope in order to return in. This is a trade-off for the faster
cut,past, and copy operations.

# Trie
A Trie is a tree  data strcuture where the nodes contain a character and strings/words can be reTRIEved by traversing down a branch path.

| Operation    | Time          | 
| ------------ | ------------- |
| misspellings | O(wk)         |
| autocomplete | O(k)          |

where w represents the number of words in the document, k represents the number of characters in the longest word.

### Pros 
- Fast and consistent insertion and search time 
    - Lookup is a predictable O(k) time operation and can take less time if the word is not in the trie
- Can efficiently do prefix search or sutocomplete with Trie
- No need for a hash function
- Supports ordered traversals


### Cons
- Requires a lot of memory 

### Hashing vs Trie

In order to serve the user a fast and consistent response, a trie is desirable because it will always perform these operations in O(k) time. Hash tables must rebuild their index when it becomes full, which is an expensive operation. Hashtables also must deal with collisions.

Another perk of using a trie is that it allows us to implement other features. For example, a trie can efficiently implement an autocomplete features, which users would enjoy having in a text editor.

I chose to use a Trie because I believe that it is important to satify users by delivering consistently fast speed. In addition, the trie introduces other utilities and features that can enhance the TextEditor experience.

Let's talk about the major disadvantage of a trie, which is not easy to ignore. A trie takes up a lot of memory. Depending on how large our Trie grows, we can consider the idea of compressing the Trie. There are several ways you can do this including a bitwise tree.

Additionally, imagine that your dictionary grows. It is fast to insert in a Trie. Often times as your dictionary of words grows, you will notice that the words often contain the same prefix. In the case or a large dictionary or growing dictionary with common prefixes, you would be saving memory as opposed to hashing.

# Create SimpleEditor Object
The Simple Editor takes in two arguments: 
1) An absolute file path to the text to edit as a text file
2) An absolute file path to the dictionary text file


# Testing
To test files, navigate to Project/Test

To test the Trie data structure
```bash
$ python TestTrie.py
```

To test the TextEditor
```bash
$ python TestEditor.py
```

To test the performance
```bash
$ python performanceTest.py
```# TextEditor
