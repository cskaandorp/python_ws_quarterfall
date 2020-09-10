import json
import os.path
import answer


if __name__ == '__main__':

    # Quarterfall object containing the data
    qf = {}

    if os.path.exists('qf.json'):
        json_file = open('qf.json')
        qf = json.load(json_file)

        qf['test'] = 'LIJP'

        outfile = open('qf.json', 'w')
        json.dump(qf, outfile)



