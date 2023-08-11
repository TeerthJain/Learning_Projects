



files = open('./Project_2_MadLibs/testing.txt', 'r+')
reads = files.read()
readings= reads.split(' ')
def counts():
    string = "" 
    for i in readings:
        wrd = i.lower()
        if 'adjective' in wrd or 'noun' in wrd or 'adverb' in wrd or 'verb' in wrd:
            wrd = inputs(wrd)
            string += str(wrd) 
            string += ". " if '.' in i else " "
        else: 
            string += str(i) + " "
    return string
#     adj_count = readings.count('ADJECTIVE')
#     verb_count = readings.count('VERB')
#     adverb = readings.count('ADVERB')
#     noun_count = readings.count('NOUN')
#     inputs(adj_count, verb_count, adverb, noun_count)


def inputs(item): 
    return input(f'Enter an {item}:')
    
if __name__ == '__main__': 
    print(counts())
    