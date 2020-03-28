import sys
sys.path.append("../")
import Trie, unittest, ropes
from random import choice
from collections import Counter

prefix1 = ["interstate" ,"international" ,"intermission" ,"intermingle", "interface"]
prefix2 = ["foreshadow", "foresight", "foreseeable", "forecast" ,"foreground"]
prefix3 = ["incorrect", "insert", "inexpensive", "inability","inexperienced"]
prefix4 = ["uncover", "unlock", "unsafe", "unusual" , "unlikely", "unbearable", "undo", "unfair", "unreal", "unfit", "unbeatable"]
prefix5 = ["preview", "pretest", "prevent", "preplan"]
prefixes = ["inter", "fore", "in", "un", "pre"]
uppercase = ["HI","THERE","I","LOVE",'CODING',"IT","IS","AWESOME"]
mixedcase = ["Hi","thErE","i","LovE",'cODiNg',"It","iS","AwEsOMe"]

class TestTrie(unittest.TestCase):
    def testEmptyTrie(self):
        trie = Trie.Trie()
        self.assertEqual(len(trie.root.children), 0)

    def testInsertandSearch1(self):
        trie = Trie.Trie()
        for word in prefix1:
            trie.insert(word, trie.root)
            self.assertEqual(trie.find(word), True)

    def testInsertandSearch2(self):
        trie = Trie.Trie()
        for word in prefix2:
            trie.insert(word, trie.root)
            self.assertEqual(trie.find(word), True)

    def testInsertandSearch3(self):
        trie = Trie.Trie()
        for word in prefix3:
            trie.insert(word, trie.root)
            self.assertEqual(trie.find(word), True)

    def testInsertandSearch4(self):
        trie = Trie.Trie()
        for word in prefix4:
            trie.insert(word, trie.root)
            self.assertEqual(trie.find(word), True)

    def testInsertandSearch5(self):
        trie = Trie.Trie()
        for word in prefix5:
            trie.insert(word, trie.root)
            self.assertEqual(trie.find(word), True)

    def testUppercase(self):
        trie = Trie.Trie()
        for word in uppercase:
            trie.insert(word, trie.root)
            self.assertEqual(trie.find(word), True)

    def testMixedCase(self):
        trie = Trie.Trie()
        for word in mixedcase:
            trie.insert(word, trie.root)
            self.assertEqual(trie.find(word), True)

    def testAutocomplete_Prefix_Present_SuggestAll_1(self):
        trie = Trie.Trie()
        for word in prefix1:
            trie.insert(word, trie.root)
        self.assertCountEqual(Counter(trie.autocomplete("inter")), Counter(prefix1))

    def testAutocomplete_AlmostPrefix_Present_SuggestAll_1(self):
        trie = Trie.Trie()
        for word in prefix1:
            trie.insert(word, trie.root)
        self.assertCountEqual(Counter(trie.autocomplete("int")), Counter(prefix1))

    def testAutocomplete_AlmostPrefix_Present_SuggestPartial_1(self):
        trie = Trie.Trie()
        for word in prefix1:
            trie.insert(word, trie.root)
        self.assertCountEqual(Counter(trie.autocomplete("interm")), Counter(["intermission" ,"intermingle"]))

    def testAutocomplete_LongWord_NotPresent_1(self):
        trie = Trie.Trie()
        for word in prefix1:
            trie.insert(word, trie.root)
        longEnd = ""
        for _ in range(20):
            longEnd += chr(choice([i for i in range(65,123) if i not in list(range(91,97))]))
        self.assertEqual(trie.autocomplete("inter" + longEnd), None)

    def testAutocomplete_EmptyWord_1(self):
        trie = Trie.Trie()
        for word in prefix1:
            trie.insert(word, trie.root)
        self.assertEqual(trie.autocomplete(""), None)

    def testAutocomplete_AlmostPrefix_Not_Present_1(self):
        trie = Trie.Trie()
        for word in prefix1:
            trie.insert(word, trie.root)
        
        # generates a random letter (uppercase or lower) that is not that of the last letter in the prefix
        random_letter = choice([i for i in range(65,123) if i not in list(range(91,97)) + [ord(prefixes[0][-1].upper()),ord(prefixes[0][-1].lower())]])
        self.assertEqual(trie.autocomplete("inte" + chr(random_letter)), None)

    def testAutocomplete_NotPrefix_Not_Present_1(self):
        trie = Trie.Trie()
        for word in prefix1:
            trie.insert(word, trie.root)
        # generates a random letter (uppercase or lower) that is not that of the first letter in the prefix
        random_letter = choice([i for i in range(65,123) if i not in list(range(91,97)) + [ord(prefixes[0][0].upper()),ord(prefixes[0][0].lower())]])
        self.assertEqual(trie.autocomplete(chr(random_letter)), None)

    def testAutocomplete_Prefix_Present_SuggestAll_2(self):
        trie = Trie.Trie()
        for word in prefix2:
            trie.insert(word, trie.root)
        self.assertCountEqual(Counter(trie.autocomplete("fore")), Counter(prefix2))

    def testAutocomplete_AlmostPrefix_Present_SuggestAll_2(self):
        trie = Trie.Trie()
        for word in prefix2:
            trie.insert(word, trie.root)
        self.assertCountEqual(Counter(trie.autocomplete("fo")), Counter(prefix2))

    def testAutocomplete_AlmostPrefix_Present_SuggestPartial_2(self):
        trie = Trie.Trie()
        for word in prefix2:
            trie.insert(word, trie.root)
        self.assertCountEqual(Counter(trie.autocomplete("fores")), Counter(["foreshadow", "foresight", "foreseeable"]))

    def testAutocomplete_LongWord_NotPresent_2(self):
        trie = Trie.Trie()
        for word in prefix2:
            trie.insert(word, trie.root)
        longEnd = ""
        for _ in range(20):
            longEnd += chr(choice([i for i in range(65,123) if i not in list(range(91,97))]))
        self.assertEqual(trie.autocomplete("fore" + longEnd), None)

    def testAutocomplete_EmptyWord_2(self):
        trie = Trie.Trie()
        for word in prefix2:
            trie.insert(word, trie.root)
        self.assertEqual(trie.autocomplete(""), None)

    def testAutocomplete_AlmostPrefix_Not_Present_2(self):
        trie = Trie.Trie()
        for word in prefix2:
            trie.insert(word, trie.root)
        
        # generates a random letter (uppercase or lower) that is not that of the last letter in the prefix
        random_letter = choice([i for i in range(65,123) if i not in list(range(91,97)) + [ord(prefixes[1][-1].upper()),ord(prefixes[1][-1].lower())]])
        self.assertEqual(trie.autocomplete("for" + chr(random_letter)), None)

    def testAutocomplete_NotPrefix_Not_Present_2(self):
        trie = Trie.Trie()
        for word in prefix2:
            trie.insert(word, trie.root)
        # generates a random letter (uppercase or lower) that is not that of the first letter in the prefix
        random_letter = choice([i for i in range(65,123) if i not in list(range(91,97)) + [ord(prefixes[1][0].upper()),ord(prefixes[1][0].lower())]])
        self.assertEqual(trie.autocomplete(chr(random_letter)), None)

    def testAutocomplete_Prefix_Present_SuggestAll_3(self):
        trie = Trie.Trie()
        for word in prefix3:
            trie.insert(word, trie.root)
        self.assertCountEqual(Counter(trie.autocomplete("in")), Counter(prefix3))

    def testAutocomplete_AlmostPrefix_Present_SuggestAll_3(self):
        trie = Trie.Trie()
        for word in prefix3:
            trie.insert(word, trie.root)
        self.assertCountEqual(Counter(trie.autocomplete("i")), Counter(prefix3))

    def testAutocomplete_AlmostPrefix_Present_SuggestPartial_3(self):
        trie = Trie.Trie()
        for word in prefix3:
            trie.insert(word, trie.root)
        self.assertCountEqual(Counter(trie.autocomplete("ine")), Counter(["inexpensive","inexperienced"]))

    def testAutocomplete_LongWord_NotPresent_3(self):
        trie = Trie.Trie()
        for word in prefix3:
            trie.insert(word, trie.root)
        longEnd = ""
        for _ in range(20):
            longEnd += chr(choice([i for i in range(65,123) if i not in list(range(91,97))]))
        self.assertEqual(trie.autocomplete("in" + longEnd), None)

    def testAutocomplete_EmptyWord_3(self):
        trie = Trie.Trie()
        for word in prefix3:
            trie.insert(word, trie.root)
        self.assertEqual(trie.autocomplete(""), None)

    def testAutocomplete_AlmostPrefix_Not_Present_3(self):
        trie = Trie.Trie()
        for word in prefix3:
            trie.insert(word, trie.root)
        
        # generates a random letter (uppercase or lower) that is not that of the last letter in the prefix
        random_letter = choice([i for i in range(65,123) if i not in list(range(91,97)) + [ord(prefixes[2][-1].upper()),ord(prefixes[2][-1].lower())]])
        self.assertEqual(trie.autocomplete("i" + chr(random_letter)), None)

    def testAutocomplete_NotPrefix_Not_Present_3(self):
        trie = Trie.Trie()
        for word in prefix3:
            trie.insert(word, trie.root)
        # generates a random letter (uppercase or lower) that is not that of the first letter in the prefix
        random_letter = choice([i for i in range(65,123) if i not in list(range(91,97)) + [ord(prefixes[2][0].upper()),ord(prefixes[2][0].lower())]])
        self.assertEqual(trie.autocomplete(chr(random_letter)), None)

    def testAutocomplete_Prefix_Present_SuggestAll_4(self):
        trie = Trie.Trie()
        for word in prefix4:
            trie.insert(word, trie.root)
        self.assertCountEqual(Counter(trie.autocomplete("un")), Counter(prefix4))

    def testAutocomplete_AlmostPrefix_Present_SuggestAll_4(self):
        trie = Trie.Trie()
        for word in prefix4:
            trie.insert(word, trie.root)
        self.assertCountEqual(Counter(trie.autocomplete("u")), Counter(prefix4))

    def testAutocomplete_AlmostPrefix_Present_SuggestPartial_4(self):
        trie = Trie.Trie()
        for word in prefix4:
            trie.insert(word, trie.root)
        self.assertCountEqual(Counter(trie.autocomplete("unb")), Counter(["unbeatable","unbearable"]))

    def testAutocomplete_LongWord_NotPresent_4(self):
        trie = Trie.Trie()
        for word in prefix4:
            trie.insert(word, trie.root)
        longEnd = ""
        for _ in range(20):
            longEnd += chr(choice([i for i in range(65,123) if i not in list(range(91,97))]))
        self.assertEqual(trie.autocomplete("un" + longEnd), None)

    def testAutocomplete_EmptyWord_4(self):
        trie = Trie.Trie()
        for word in prefix4:
            trie.insert(word, trie.root)
        self.assertEqual(trie.autocomplete(""), None)

    def testAutocomplete_AlmostPrefix_Not_Present_4(self):
        trie = Trie.Trie()
        for word in prefix4:
            trie.insert(word, trie.root)
        
        # generates a random letter (uppercase or lower) that is not that of the last letter in the prefix
        random_letter = choice([i for i in range(65,123) if i not in list(range(91,97)) + [ord(prefixes[3][-1].upper()),ord(prefixes[3][-1].lower())]])
        self.assertEqual(trie.autocomplete("u" + chr(random_letter)), None)

    def testAutocomplete_NotPrefix_Not_Present_4(self):
        trie = Trie.Trie()
        for word in prefix4:
            trie.insert(word, trie.root)
        # generates a random letter (uppercase or lower) that is not that of the first letter in the prefix
        random_letter = choice([i for i in range(65,123) if i not in list(range(91,97)) + [ord(prefixes[3][0].upper()),ord(prefixes[3][0].lower())]])
        self.assertEqual(trie.autocomplete(chr(random_letter)), None)


    def testAutocomplete_Prefix_Present_SuggestAll_5(self):
        trie = Trie.Trie()
        for word in prefix5:
            trie.insert(word, trie.root)
        self.assertCountEqual(Counter(trie.autocomplete("pre")), Counter(prefix5))

    def testAutocomplete_AlmostPrefix_Present_SuggestAll_5(self):
        trie = Trie.Trie()
        for word in prefix5:
            trie.insert(word, trie.root)
        self.assertCountEqual(Counter(trie.autocomplete("pr")), Counter(prefix5))

    def testAutocomplete_AlmostPrefix_Present_SuggestPartial_5(self):
        trie = Trie.Trie()
        for word in prefix5:
            trie.insert(word, trie.root)
        self.assertCountEqual(Counter(trie.autocomplete("prev")), Counter(["preview","prevent"]))

    def testAutocomplete_LongWord_NotPresent_5(self):
        trie = Trie.Trie()
        for word in prefix5:
            trie.insert(word, trie.root)
        longEnd = ""
        for _ in range(20):
            longEnd += chr(choice([i for i in range(65,123) if i not in list(range(91,97))]))
        self.assertEqual(trie.autocomplete("pre" + longEnd), None)

    def testAutocomplete_EmptyWord_5(self):
        trie = Trie.Trie()
        for word in prefix5:
            trie.insert(word, trie.root)
        self.assertEqual(trie.autocomplete(""), None)

    def testAutocomplete_AlmostPrefix_Not_Present_5(self):
        trie = Trie.Trie()
        for word in prefix5:
            trie.insert(word, trie.root)
        
        # generates a random letter (uppercase or lower) that is not that of the last letter in the prefix
        random_letter = choice([i for i in range(65,123) if i not in list(range(91,97)) + [ord(prefixes[4][-1].upper()),ord(prefixes[4][-1].lower())]])
        self.assertEqual(trie.autocomplete("pr" + chr(random_letter)), None)

    def testAutocomplete_NotPrefix_Not_Present_5(self):
        trie = Trie.Trie()
        for word in prefix5:
            trie.insert(word, trie.root)
        # generates a random letter (uppercase or lower) that is not that of the first letter in the prefix
        random_letter = choice([i for i in range(65,123) if i not in list(range(91,97)) + [ord(prefixes[4][0].upper()),ord(prefixes[4][0].lower())]])
        self.assertEqual(trie.autocomplete(chr(random_letter)), None)
    

if __name__ == "__main__":
    unittest.main()