def getData(file_link):
    values = []
    with open(file_link,"r") as file:
        for item in file:
            item = item.replace("\n","")
            values.append((item.split("|")))
    return values

def getValues():
    quote = "429128.12312369|10"
    #quote = input("What values do you want to work with?\n(value|base)\n>>>")
    quote = quote.split("|")
    return quote[0],int(quote[1])


def hexaToNums(quote):
    i = 1
    new_quote = []
    for item in quote:
        if item == "A":
            item = "10"
        elif item == "B":
            item = "11"
        elif item == "C":
            item = "12"
        elif item == "D":
            item = "13"
        elif item == "E":
            item = "14"
        elif item == "F":
            item = "15"
        new_quote.append(item)
        i += 1
    quote = new_quote

    return quote


def convertTo10Whole(quote,base):
    total = 0
    if base == 16:
        quote = hexaToNums(quote)
    i = 1
    for item in quote:
        total += int(quote[-i]) * base**(i-1)
        i += 1
    return total


def convertTo10Frac(quote,base):
    value = 0
    i = -1
    
    if base == 16:
        quote = hexaToNums(quote)
    for item in quote:
        value += int(item) * (base ** i)
        i -= 1
        print(value,i,base ** i)
    return (str(value).split("."))[1]


def fromXTo10(quote,base):
    new_quote = ""
    
    if len(quote.split(".")) != 1:
        part1 = convertTo10Whole((quote.split("."))[0],base)
        part2 = convertTo10Frac((quote.split("."))[1],base)
        new_quote = str(part1) + "." + str(part2)
    else:
        new_quote = convertTo10Whole(quote,base)
    return new_quote



def fromXTo2Frac10(quote, base):
    quote = float("0." + quote)

    new_quote = ""
    precision = 20  # You can adjust the precision as needed

    for _ in range(precision):
        quote *= 2
        new_quote += str(int(quote))
        quote = quote - int(quote)


    return new_quote


def fromXTo2All(quote,base):
    new_quote = ""
    if base == 10:
        quote = int(quote)
        while quote > 0:
            new_quote += str(quote%2)
            quote = quote//2
        return new_quote[::-1]
    elif base == 16:
        for item in quote:
            for hexa in values:
                if item == hexa[2]:
                    new_quote += hexa[0]
        return new_quote
    elif base == 8:
        for item in quote:
            for octa in values:
                if item == octa[1]:
                    new_quote += octa[3]
        return new_quote
    

    


def fromXTo2(quote,base):
    quote = quote.split(".")
    print(quote)
    new_quote = ""
    if len(quote) != 1:
        part1 = fromXTo2All(quote[0],base)
        if base == 16:
            part2 = fromXTo2Frac10(quote[1],base)
        else:
            part2 = fromXTo2All(quote[1],base)
        new_quote = part1 + "." + part2
    else:
        new_quote = fromXTo2All(quote[0],base)
    return new_quote


values = getData("/home/guimbreon/Desktop/git/Base_transformer/Keys")
quote,base = getValues()
#baseConvert = input("What base do you want to transform it too?\n>>>")
baseConvert = "2"
if baseConvert == "10":
    quoteConvert = fromXTo10(quote,base)
elif baseConvert == "8":
    quoteConvert = fromXTo8(quote,base)
elif baseConvert == "2":
    quoteConvert = fromXTo2(quote,base)
else:
    print("The value you inserted is not a possible value to transform to.")
print(f"The value {quote} that is in the base {base}, converted to {baseConvert} is equal to {quoteConvert}")