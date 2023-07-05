import unittest
from machinetranslation import translator


class TestEnlgishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(translator.englishToFrench("Hello"), "Bonjour")


class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(translator.frenchToEnglish("Bonjour"), "Hi")


unittest.main()