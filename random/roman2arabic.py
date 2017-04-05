base = (1,5,10,50,100,500,1000)
roman = ('I','V','X','L','C','D','M')

print(' ----- ROMAN NUMERAL TO ARABIC NUMBER CONVERTER ----- ')

class InvalidInputError(Exception):
    pass
class NonStandardInputError(Exception):
    pass
class NoInputError(Exception):
    pass

while True:
    try:
        numeral = input('\nEnter a roman numeral: ')
        if numeral == '':
            raise NoInputError
        if numeral.isalpha():
            numeral = numeral.upper()
            test = numeral
            for Letter in roman:
                test = test.replace(Letter,'')
            if len(test) == 0:
                value = []
                index = []
                for i in range(len(numeral)):
                    value.append(base[roman.index(numeral[i])])
                    index.append(roman.index(numeral[i]))
                if not (index[0] == max(index) or index[1] == max(index)):
                    raise NonStandardInputError
                if len(numeral) > 1:
                    lower_count = 0
                    repeat_count = 0
                    for i in range(1,len(index)):
                        if index[i] > index[i-1]:
                            lower_count+=1
                            if lower_count > 1 or (lower_count == 1 and repeat_count > 0):
                                raise NonStandardInputError
                            repeat_count=0
                            if (index[i]%2 == 0 and index[i]-index[i-1] > 2) or (index[i]%2 == 1 and index[i]-index[i-1] > 1):
                                raise NonStandardInputError
                            value[i] = value[i] - value[i-1]
                            value[i-1] = 0
                        elif index[i] == index[i-1]:
                            lower_count=0
                            repeat_count+=1
                            if (index[i]%2 == 0 and repeat_count >= 3) or (index[i]%2 == 1 and repeat_count >= 2):
                                raise NonStandardInputError
                        else:
                            lower_count=0
                            repeat_count=0
                    if sum(value) in base:
                        raise NonStandardInputError
                value = sum(value)
                print(value)
            else:
                raise InvalidInputError
        else:
            raise InvalidInputError
    except InvalidInputError:
        print('Not a roman numeral!')
    except NonStandardInputError:
        print('Roman numeral in non-standard form; unable to convert.')
    except NoInputError:
        print('No input. Try again.')
