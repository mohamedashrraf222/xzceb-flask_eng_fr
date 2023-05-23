import unittest
import sys
sys.path.append("..")  # Add parent directory to sys.path
import translator

class TestOne(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(translator.english_to_french(text=""), "please enter text to be translated") 
        self.assertEqual(translator.english_to_french("Hello"), "Bonjour")  

        
class TestTwo(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(translator.french_to_english(text=""), "please enter text to be translated")
        self.assertEqual(translator.french_to_english("Bonjour"), "Hello") 


unittest.main()
