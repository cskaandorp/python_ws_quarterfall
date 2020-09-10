import unittest
import json
import os.path
import answer



# Quarterfall object containing the data
qf = {}

class TestStringMethods(unittest.TestCase):

    def test_correct_hr(self):
        try:
            answ = answer.high_avg_hr
            self.assertEqual(answ.shape, (7, 8))
            qf['correctHighAvgHR'] = True
        except:
            qf['correctHighAvgHR'] = False

    @classmethod
    def setUpClass(cls):
        # read the data from QF json file if it exists
        if os.path.exists('qf.json'):
            json_file = open('qf.json')
            qf = json.load(json_file)
            json_file.close()

    @classmethod
    def tearDownClass(cls):
        # write the qf data to the json file
        outfile = open('qf.json', 'w')
        json.dump(qf, outfile)
        outfile.close()

if __name__ == '__main__':
    unittest.main()
