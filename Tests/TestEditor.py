import sys
sys.path.append("../")
import Trie, unittest, os, TextEditor, ropes
from random import choice, randint
from collections import Counter

fileDir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))

commonPrefix = fileDir + '/TestTextFiles/commonPrefix.txt'
commonPrefix_WordsWithoutPunctuation = ['interstate', 'international', 'intermission', 'intermingle', 'interface', 'foreshadow', 'foresight', 'foreseeable',
 'forecast', 'foreground', 'incorrect', 'insert', 'inexpensive', 'illegal', 'irregular', 'inability', 'uncover', 'unlock', 'unsafe', 'preview', 'pretest', 'prevent', 'preplan', 'unusual', 'unlikely', 'unbearable', 'undo', 'unfair', 'unreal', 'unfit']  
commonPrefix_as_str = "interstate international intermission intermingle, interface\nforeshadow foresight foreseeable forecast foreground\nincorrect insert inexpensive illegal irregular inability\nuncover unlock unsafe\npreview pretest prevent preplan\nunusual unlikely unbearable undo unfair unreal unfit"

empty = fileDir + '/TestTextFiles/empty.txt'
empty_WordsWithoutPunctuation = []
empty_as_str = ""

manySpaces = fileDir +  '/TestTextFiles/manySpaces.txt'
manySpaces_WordsWithoutPunctuation = ['about', 'above', 'abroad', 'absence', 'absolute', 'absolutely', 'absorb', 'abuse', 'cheek', 'cheese', 'chef', 'chemical', 'dirt', 'dirty', 'earn', 'earnings', 'earth', 'ease', 'flame', 'flat', 'flavor', 'flee', 'flesh', 'flight', 'float', 'floor', 'gesture', 'get', 'ghost', 'giant', 'gift', 'gifted', 'girl'] 
manySpaces_as_str = "about above abroad\n          absence absolute\n\n\nabsolutely          absorb         abuse\ncheek\n               cheese\n        chef\nchemical\n       dirt\ndirty\n\nearn                   earnings\nearth\n                     ease\nflame flat flavor flee flesh flight float floor\ngesture get ghost giant gift gifted\ngirl"


numbersAndWords = fileDir +  '/TestTextFiles/numbersAndWords.txt'
numbersAndWords_WordsWithoutPunctuation = ['lemon', 'length', 'less', 'lesson', 'let', 'letter', 'level', 'liberal', 'library', 'license', 'lie', 'neighborhood', 'neither', 'nerve', 'nervous', 'net', 'network', 'never', 'panel',  'pant', 'paper', 'parent', 
'park', 'parking'] 
numbersAndWords_as_str = "lemon length less lesson let letter level\nliberal library license lie 67868 neighborhood\nneither nerve nervous net network never panel 8980890\npant paper parent park 123\npar987k char897t parking"

commonText1 = fileDir +  '/TestTextFiles/commonText1.txt'
commonText1_WordsWithoutPunctuation = ['The', 'opposite', 'wall', 'of', 'this', 'entry', 'was', 'hung', 'all', 'over', 'with', 'a', 'heathenish', 'array', 'of', 'monstrous', 'clubs', 'and', 'spears', 'Some', 'were', 'thickly', 'set', 'with', 'glittering', 'teeth', 'resembling', 'ivory', 'saws', 'others', 'were', 'tufted', 'with', 'knots', 'of', 'human', 'hair', 'and', 'one', 'was', 'sickleshaped', 'with', 'a', 'vast', 'handle', 'sweeping', 'round', 'like', 'the', 'segment', 'made', 'in', 'the', 'newmown', 'grass', 'by', 'a', 'longarmed', 'mower', 'You', 'shuddered', 'as', 'you', 'gazed', 'and', 'wondered', 'what', 'monstrous', 'cannibal', 'and', 'savage', 'could', 'ever', 'have', 'gone', 'a', 'deathharvesting', 'with', 'such', 'a', 'hacking', 'horrifying', 'implement', 'Mixed', 'with', 'these', 'were', 'rusty', 'old', 'whaling', 'lances', 'and', 'harpoons', 'all', 'broken', 'and', 'deformed', 'Some', 'were', 'storied', 'weapons', 'With', 'this', 'once', 'long', 'lance', 'now', 'wildly', 'elbowed', 'fifty', 'years', 'ago', 'did', 'Nathan', 'Swain', 'kill', 'fifteen', 'whales', 'between', 'a', 'sunrise', 'and', 'a', 'sunset', 'And', 'that', 'harpoon—so', 'like', 'a', 'corkscrew', 'now—was', 'flung', 'in', 'Javan', 'seas', 'and', 'run', 'away', 'with', 'by', 'a', 'whale', 'years', 'afterwards', 'slain', 'off', 'the', 'Cape', 'of', 'Blanco', 'The', 'original', 'iron', 'entered', 'nigh', 'the', 'tail', 'and', 'like', 'a', 'restless', 'needle', 'sojourning', 'in', 'the', 'body', 'of', 'a', 'man', 'travelled', 'full', 'forty', 'feet', 'and', 'at', 'last', 'was', 'found', 'imbedded', 'in', 'the', 'hump']
commonText1_as_str = "The opposite wall of this entry was hung all over with a heathenish array of monstrous clubs and spears. Some were thickly set with glittering teeth resembling ivory saws; others were tufted with knots of human hair; and one was sickle-shaped, with a vast handle sweeping round like the segment made in the new-mown grass by a long-armed mower. You shuddered as you gazed, and wondered what monstrous cannibal and savage could ever have gone a death-harvesting with such a hacking, horrifying implement. Mixed with these were rusty old whaling lances and harpoons all broken and deformed. Some were storied weapons. With this once long lance, now wildly elbowed, fifty years ago did Nathan Swain kill fifteen whales between a sunrise and a sunset. And that harpoon—so like a corkscrew now—was flung in Javan seas, and run away with by a whale, years afterwards slain off the Cape of Blanco. The original iron entered nigh the tail, and, like a restless needle sojourning in the body of a man, travelled full forty feet, and at last was found imbedded in the hump."
commonText1AllMisspelled = fileDir + '/TestTextFiles/commonText1AllMisspelled.txt'
commonText1WithMisspelling = fileDir + '/TestTextFiles/commonText1WithMisspelling.txt'



class TestEditor(unittest.TestCase):

    def testEditorCreation_On_CommonText(self):
        editor = TextEditor.SimpleEditor(commonText1,commonText1)
        self.assertEqual(editor.paste_text, ropes.Rope(""))
        for word in commonText1_WordsWithoutPunctuation:
            self.assertEqual(editor.dictionaryTrie.find(word),True)
        self.assertEqual(editor.document,ropes.Rope(commonText1_as_str))

    def testEditorCreation_On_CommonPrefix(self):
        editor = TextEditor.SimpleEditor(commonPrefix,commonPrefix)
        self.assertEqual(editor.paste_text, ropes.Rope(""))
        for word in commonPrefix_WordsWithoutPunctuation:
            self.assertEqual(editor.dictionaryTrie.find(word),True)
        self.assertEqual(editor.document,ropes.Rope(commonPrefix_as_str))

    def testEditorCreation_On_Empty(self):
        editor = TextEditor.SimpleEditor(empty,empty)
        self.assertEqual(editor.paste_text, ropes.Rope(""))
        self.assertEqual(len(editor.dictionaryTrie.root.children),0)
        self.assertEqual(editor.document,ropes.Rope(empty_as_str))

    def testEditorCreation_On_manySpaces(self):
        editor = TextEditor.SimpleEditor(manySpaces,manySpaces)
        self.assertEqual(editor.paste_text, ropes.Rope(""))
        for word in manySpaces_WordsWithoutPunctuation:
            self.assertEqual(editor.dictionaryTrie.find(word),True)
        self.assertEqual(editor.document,ropes.Rope(manySpaces_as_str))

    def testEditorCreation_On_numbersAndWords(self):
        editor = TextEditor.SimpleEditor(numbersAndWords,numbersAndWords)
        self.assertEqual(editor.paste_text, ropes.Rope(""))
        for word in numbersAndWords_WordsWithoutPunctuation:
            self.assertEqual(editor.dictionaryTrie.find(word),True)
        self.assertEqual(editor.document,ropes.Rope(numbersAndWords_as_str))

    def testWithMisspelling(self):
        editor = TextEditor.SimpleEditor(commonText1WithMisspelling,commonText1)
        self.assertEqual(editor.misspellings(),12)

    def testWithAllMisspelled(self):
        editor = TextEditor.SimpleEditor(commonText1AllMisspelled ,commonText1)
        self.assertEqual(editor.misspellings(),50)

    def testAutocomplete(self):
        editor = TextEditor.SimpleEditor(commonPrefix,commonPrefix)
        self.assertCountEqual(Counter(editor.autocomplete("interm")), Counter(["intermission" ,"intermingle"]))

    def testAutocomplete_On_EmptyStr(self):
        editor = TextEditor.SimpleEditor(commonPrefix,commonPrefix)
        self.assertEqual(editor.autocomplete(""), None)

    def testAutocomplete_On_NotPresentPrefix(self):
        editor = TextEditor.SimpleEditor(commonPrefix,commonPrefix)
        self.assertEqual(editor.autocomplete("zib"), None)

    def testCopy_On_empty(self):
        editor = TextEditor.SimpleEditor(empty,empty)
        editor.copy(0,0)
        self.assertEqual(editor.paste_text, ropes.Rope(""))

    def testCopy_On_commonText(self):
        editor = TextEditor.SimpleEditor(commonText1,commonText1)
        length = len(commonPrefix_as_str)
        random_i = randint(0,length - 1)
        random_j = randint(random_i,length)
        editor.copy(random_i,random_j)
        self.assertEqual(editor.paste_text, ropes.Rope(commonText1_as_str[random_i:random_j]))

    def testCopy_On_commonPrefix(self):
        editor = TextEditor.SimpleEditor(commonPrefix,commonPrefix)
        length = len(commonPrefix_as_str)
        random_i = randint(0,length - 1)
        random_j = randint(random_i,length)
        editor.copy(random_i,random_j)
        self.assertEqual(editor.paste_text, ropes.Rope(commonPrefix_as_str[random_i:random_j]))
    
    def testCopy_On_manySpaces(self):
        editor = TextEditor.SimpleEditor(manySpaces,manySpaces)
        length = len(manySpaces_as_str)
        random_i = randint(0,length - 1)
        random_j = randint(random_i,length)
        editor.copy(random_i,random_j)
        self.assertEqual(editor.paste_text, ropes.Rope(manySpaces_as_str[random_i:random_j]))

    def testCopy_On_numbersAndWords(self):
        editor = TextEditor.SimpleEditor(numbersAndWords,numbersAndWords)
        length = len(numbersAndWords_as_str)
        random_i = randint(0,length - 1)
        random_j = randint(random_i,length)
        editor.copy(random_i,random_j)
        self.assertEqual(editor.paste_text, ropes.Rope(numbersAndWords_as_str[random_i:random_j]))

    def testCopyPaste_On_empty(self):
        editor = TextEditor.SimpleEditor(empty,empty)
        editor.copy(0,0)
        random_paste_index = randint(0,0)
        editor.paste(random_paste_index)
        self.assertEqual(editor.document, ropes.Rope("") )
    
    def testCopyPaste_On_commonText(self):
        editor = TextEditor.SimpleEditor(commonText1,commonText1)
        length = len(commonText1_as_str)
        random_i = randint(0,length - 1)
        random_j = randint(random_i,length)
        editor.copy(random_i,random_j)
        random_paste_index = randint(0,length)
        editor.paste(random_paste_index)
        self.assertEqual(editor.document, ropes.Rope(commonText1_as_str[:random_paste_index ]) + ropes.Rope(commonText1_as_str[random_i:random_j]) + ropes.Rope(commonText1_as_str[random_paste_index :]) )
    
    def testCopyPaste_On_commonPrefix(self):
        editor = TextEditor.SimpleEditor(commonPrefix,commonPrefix)
        length = len(commonPrefix_as_str)
        random_i = randint(0,length - 1)
        random_j = randint(random_i,length)
        editor.copy(random_i,random_j)
        random_paste_index = randint(0,length)
        editor.paste(random_paste_index)
        self.assertEqual(editor.document, ropes.Rope(commonPrefix_as_str[:random_paste_index ]) + ropes.Rope(commonPrefix_as_str[random_i:random_j]) + ropes.Rope(commonPrefix_as_str[random_paste_index :]) )
    
    def testCopyPaste_On_manySpaces(self):
        editor = TextEditor.SimpleEditor(manySpaces,manySpaces)
        length = len(manySpaces_as_str)
        random_i = randint(0,length - 1)
        random_j = randint(random_i,length)
        editor.copy(random_i,random_j)
        random_paste_index = randint(0,length)
        editor.paste(random_paste_index)
        self.assertEqual(editor.document, ropes.Rope(manySpaces_as_str[:random_paste_index ]) + ropes.Rope(manySpaces_as_str[random_i:random_j]) + ropes.Rope(manySpaces_as_str[random_paste_index :]) )
    
    def testCopyPaste_On_numbersAndWords(self):
        editor = TextEditor.SimpleEditor(numbersAndWords,numbersAndWords)
        length = len(numbersAndWords_as_str)
        random_i = randint(0,length - 1)
        random_j = randint(random_i,length)
        editor.copy(random_i,random_j)
        random_paste_index = randint(0,length)
        editor.paste(random_paste_index)
        self.assertEqual(editor.document, ropes.Rope(numbersAndWords_as_str[:random_paste_index ]) + ropes.Rope(numbersAndWords_as_str[random_i:random_j]) + ropes.Rope(numbersAndWords_as_str[random_paste_index :]) )
    
    def testCut_On_empty(self):
        editor = TextEditor.SimpleEditor(empty,empty)
        editor.cut(0,0)
        self.assertEqual(editor.paste_text, ropes.Rope(""))
        self.assertEqual(editor.document, ropes.Rope(""))
       
    def testCut_On_commonText(self):
        editor = TextEditor.SimpleEditor(commonText1,commonText1)
        length = len(commonText1_as_str)
        random_i = randint(0,length - 1)
        random_j = randint(random_i,length)
        editor.cut(random_i,random_j)
        self.assertEqual(editor.paste_text, ropes.Rope(commonText1_as_str[random_i:random_j]))
        self.assertEqual(editor.document, ropes.Rope(commonText1_as_str[:random_i]) + ropes.Rope(commonText1_as_str[random_j:]))
       
    def testCut_On_commonPrefix(self):
        editor = TextEditor.SimpleEditor(commonPrefix,commonPrefix)
        length = len(commonPrefix_as_str)
        random_i = randint(0,length - 1)
        random_j = randint(random_i,length)
        editor.cut(random_i,random_j)
        self.assertEqual(editor.paste_text, ropes.Rope(commonPrefix_as_str[random_i:random_j]))
        self.assertEqual(editor.document, ropes.Rope(commonPrefix_as_str[:random_i]) + ropes.Rope(commonPrefix_as_str[random_j:]))
       
    def testCut_On_manySpaces(self):
        editor = TextEditor.SimpleEditor(manySpaces,manySpaces)
        length = len(manySpaces_as_str)
        random_i = randint(0,length - 1)
        random_j = randint(random_i,length)
        editor.cut(random_i,random_j)
        self.assertEqual(editor.paste_text, ropes.Rope(manySpaces_as_str[random_i:random_j]))
        self.assertEqual(editor.document, ropes.Rope(manySpaces_as_str[:random_i]) + ropes.Rope(manySpaces_as_str[random_j:]))
       
    def testCut_On_numbersAndWords(self):
        editor = TextEditor.SimpleEditor(numbersAndWords,numbersAndWords)
        length = len(numbersAndWords_as_str)
        random_i = randint(0,length - 1)
        random_j = randint(random_i,length)
        editor.cut(random_i,random_j)
        self.assertEqual(editor.paste_text, ropes.Rope(numbersAndWords_as_str[random_i:random_j]))
        self.assertEqual(editor.document, ropes.Rope(numbersAndWords_as_str[:random_i]) + ropes.Rope(numbersAndWords_as_str[random_j:]))
       
if __name__ == "__main__":
    unittest.main()