import unittest
from translator import englishToFrench,frenchToEnglish

class TestEnglishToFrench(unittest.TestCase):
     def test1(self):
        firstValue = None
        # error message in case if test case got failed
        message = "Test value is not none."
        # assertIsNone() to check that if input value is none
        self.assertIsNone(firstValue, message)
        # assertEqual() to check function englishToFrench
        self.assertEqual(englishToFrench("Hello"),"Bonjour")


class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        firstValue = None
        # error message in case if test case got failed
        message = "Test value is not none."
        # assertIsNone() to check that if input value is none
        self.assertIsNone(firstValue, message)
        # assertEqual() to check function efrenchToEnglish
        self.assertEqual(frenchToEnglish("Bonjour"),"Hello")

unittest.main()
