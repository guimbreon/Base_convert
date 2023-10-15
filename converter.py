def getData(file_link):
    values = []
    with open(file_link,"r") as file:
        for item in file:
            item = item.replace("\n","")
            values.append((item.split("|")))
    return values

def getValues():
    quote = "6712AF16.12414AFCD|16"
#    quote = input("")
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


values = getData("/home/guimbreon/Desktop/git/Tests/Base_transformer/Keys")
quote,base = getValues()
quoteConvert = fromXTo10(quote,base)
baseConvert = 10
print(f"The value {quote} that is in the base {base}, converted to {baseConvert} is equal to {quoteConvert}")