base = (1,5,10,50,100,500,1000)
roman = ('I','V','X','L','C','D','M')

class InvalidRomanNumeralError(Exception):
    pass

def roman(numeral):
    if numeral.isalpha() and numeral == numeral.upper():
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
                raise InvalidRomanNumeralError
            if len(numeral) > 1:
                lower_count = 0
                repeat_count = 0
                for i in range(1,len(index)):
                    if index[i] > index[i-1]:
                        lower_count+=1
                        if lower_count > 1 or (lower_count == 1 and repeat_count > 0):
                            raise InvalidRomanNumeralError
                        repeat_count=0
                        if (index[i]%2 == 0 and index[i]-index[i-1] > 2) or (index[i]%2 == 1 and index[i]-index[i-1] > 1):
                            raise InvalidRomanNumeralError
                        value[i] = value[i] - value[i-1]
                        value[i-1] = 0
                    elif index[i] == index[i-1]:
                        lower_count=0
                        repeat_count+=1
                        if (index[i]%2 == 0 and repeat_count >= 3) or (index[i]%2 == 1 and repeat_count >= 2):
                            raise InvalidRomanNumeralError
                    else:
                        lower_count=0
                        repeat_count=0
                if sum(value) in base:
                    raise InvalidRomanNumeralError
            value = sum(value)
        else:
            raise InvalidRomanNumeralError
    else:
        raise InvalidRomanNumeralError
    return value
