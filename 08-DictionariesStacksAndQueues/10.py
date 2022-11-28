array=[
    {
        'Population': 38000000,
        'Name': 'Poland'
    },
    {
        'Population': 1400000000,
        'Name': 'India'
    },
    {
        'Population': 1400000000,
        'Name': 'China'
    },
    {
        'Population': 83000000,
        'Name': 'germany'
    },
    {
        'Population': 10000000,
        'Name': 'Sweden'
    }
]

a=0
while a<len(array):
    for x,y in array[a].items():
        print(y, end=':')
    a+=1
    print()