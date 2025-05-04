'''
Test.py is only for testing the functions imported from HelperFunctions.py
HelperFunctions.py will be exposing its functions for TagChecker.py
'''

from HelperFunctions import *
import unittest

class TestMathUtils(unittest.TestCase):


    def test_remove_slash(self):
        self.assertEqual(remove_slash("</A>"), "<A>")
        self.assertEqual(remove_slash("</B>"), "<B>")

    def test_add_slash(self):
        self.assertEqual(add_slash("<A>"), "</A>")
        self.assertEqual(add_slash("<B>"), "</B>")

    def test_regex_sort_correct(self):
        words = ['<A>', 'Hello', '</A>']
        op_stack = []
        result = regex_sort(words, op_stack)
        self.assertEqual(result, 'Correctly tagged paragraph",')

    def test_regex_sort_mismatched_tags(self):
        words = ['<A>', 'Hello', '</B>']
        op_stack = []
        result = regex_sort(words, op_stack)
        self.assertEqual(result, '"Expected </A> found </B>",')

    def test_regex_sort_no_closing_tag(self):
        words = ['<A>', 'Hello']
        op_stack = []
        result = regex_sort(words, op_stack)
        self.assertEqual(result, '"Expected </A> found #",')

    def test_regex_sort_no_opening_tag(self):
        words = ['Hello', '</A>']
        op_stack = []
        result = regex_sort(words, op_stack)
        self.assertEqual(result, '"Expected # found </A>",')


if __name__ == '__main__':
    unittest.main()

# sentences = get_sentences("Paragraph.txt")

# print(sentences)
# print(remove_quotation(sentences[0]))

# word1 = "<B>"
# word2 = "<B>"
# stack1 = []
# stack2 = []

# regex_sort(word1, stack1, stack2)
# regex_sort(word2, stack1, stack2)

# print("stack1 ",stack1)
# print("stack2 ",stack2)

# B = "</B>"
# print(remove_slash(B)=="<B>")

# A = "<A>"
# print(add_slash(A)=="</A>")

