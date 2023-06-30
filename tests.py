import unittest
from translator.translator import english_to_french, french_to_english

class TranslationTests(unittest.TestCase):
    def test_french_to_english(self):
        result = french_to_english("Bonjour")
        self.assertEqual(result, "Good morning")

    def test_english_to_french(self):
        result = english_to_french("Good morning")
        self.assertEqual(result, "Bonjour")

    def test_french_to_english_not_equal(self):
        result = french_to_english("Bonjour")
        self.assertNotEqual(result, "Bonjour")

    def test_english_to_french_not_equal(self):
        result = english_to_french("Good morning")
        self.assertNotEqual(result, "Good morning")

if __name__ == '__main__':
    unittest.main()
