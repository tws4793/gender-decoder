import unittest
import genderdecoder

class TestPackage(unittest.TestCase):
  def test_assess(self):
        assert genderdecoder.assess('test') == {
            'explanation': "This job ad doesn't use any words that are stereotypically masculine and stereotypically feminine. It probably won't be off-putting to men or women applicants.", 
            'masculine_coded_words': [], 
            'result': 'neutral', 
            'feminine_coded_words': []
        }

if __name__ == '__main__':
    unittest.main()