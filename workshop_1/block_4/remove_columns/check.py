import unittest
import json
import os.path
import answer


# Quarterfall object containing the data
qf = {}

class TestStringMethods(unittest.TestCase):

    # test to check whether the power is correctly computed
    def test_existance(self):
        try:
            self.assertNotEqual(answer.training != None)
            qf['trainingExists'] = True
        except:
            qf['trainingExists'] = False
            raise
    
    @classmethod
    def setUpClass(cls):
        # read the data from QF json file if it exists
        if os.path.exists('qf.json'):
            json_file = open('qf.json')
            qf = json.load(json_file)

    @classmethod
    def tearDownClass(cls):
        # write the qf data to the json file
        outfile = open('qf.json', 'w')
        json.dump(qf, outfile)

if __name__ == '__main__':
    unittest.main()
