f=open('../include/ordinal_numbers.wordlist','w+')
ordinal_numbers=['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']
for ordinal_number in ordinal_numbers:
    f.write(ordinal_number + '\n')
f.close()
