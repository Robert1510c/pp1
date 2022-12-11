ICAO= {
        "A": 'Alfa',
    'B': 'Bravo',
    'C': 'Charlie',
    'D': 'Delta',
    'E': 'Echo',
    'F': 'Foxtrot',
    'G': 'Golf',
    'H': 'Hotel',
    'I': 'India',
    'J': 'JUliett',
    'K': 'KIlo',
    'L': 'Lima',
    'M': 'MIke',
    'N': 'November',
    'O': 'Oscar',
    'P': 'Papa',
    'Q': 'Quebec',
    'R': 'Romeo',
    'S': 'Sierra',
    'T': 'Tango',
    'U': 'UNiform',
    'V': 'Victor',
    'W': 'Whiskey',
    'X': 'X-ray',
    'Y': 'Yankee',
    'Z': 'Zulu',
}

with open('ICAO.txt','w',encoding='utf-8') as file:
    for key,value in ICAO.items():
        file.write(key)
        file.write('\t')
        file.write(value)
        file.write('\n')
    