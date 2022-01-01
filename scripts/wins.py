import json
import os
from os import path

def get_ascension_20_heart_wins(dir):
    '''Counts wins in a given folder'''
    wins = 0
    for infile in os.listdir(dir):
        filename = dir + '/' + infile
        try:
            run = read_run(filename)
            if is_win(run):
                wins += 1
        except:
            print('File {} could not be analyzed.'.format(infile))
            continue
    return wins

def read_run(file):
    '''Reads data from a run'''
    with open(file) as json_file:
        data = json.load(json_file)
        return data

def is_win(run):
    '''Determines if a run was a win or not'''
    return run['victory'] and run['is_ascension_mode'] and run['ascension_level'] == 20 and run['floor_reached'] == 57 

def main():
    print('Ironclad wins: {}'.format(get_ascension_20_heart_wins('../runs/IRONCLAD')))
    print('Silent wins: {}'.format(get_ascension_20_heart_wins('../runs/THE_SILENT')))
    print('Defect wins: {}'.format(get_ascension_20_heart_wins('../runs/DEFECT')))
    print('Watcher wins: {}'.format(get_ascension_20_heart_wins('../runs/WATCHER')))

if __name__ == '__main__':
    main()

