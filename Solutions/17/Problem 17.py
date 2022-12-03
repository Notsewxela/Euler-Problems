'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''

def base_characters(number):
    # takes an integert betwween 1 and 1000
    str_number = str(number)
    if str_number == "0":
        return ""
    elif str_number == "1":
        return "one"
    elif str_number == "2":
        return "two"
    elif str_number == "3":
        return "three"
    elif str_number == "4":
        return "four"
    elif str_number == "5":
        return "five"
    elif str_number == "6":
        return "six"
    elif str_number == "7":
        return "seven"
    elif str_number == "8":
        return "eight"
    elif str_number == "9":
        return "nine"
    elif str_number == "10":
        return "ten"
    elif str_number == "11":
        return "eleven"
    elif str_number == "12":
        return "twelve"
    elif str_number == "13":
        return "thirteen"
    elif str_number == "14":
        return "fourteen"
    elif str_number == "15":
        return "fifteen"
    elif str_number == "16":
        return "sixteen"
    elif str_number == "17":
        return "seventeen"
    elif str_number == "18":
        return "eighteen"
    elif str_number == "19":
        return "nineteen"
    elif str_number == "20":
        return "twenty"
    elif str_number == "30":
        return "thirty"
    elif str_number == "40":
        return "fourty"
    elif str_number == "50":
        return "fifty"
    elif str_number == "60":
        return "sixty"
    elif str_number == "70":
        return "seventy"
    elif str_number == "80":
        return "eighty"
    elif str_number == "90":
        return "ninety"

def num_to_str(number):
    # assumes an integer n: 1 <= n <= 9999
    if number <= 20:
        return base_characters(number)
    elif number <= 99:
        tens, ones = divmod(number, 10)
        if ones == 0:
            return base_characters(10 * tens)
        else:
            return base_characters(10 * tens) + "-" + num_to_str(ones)
    elif number <= 999:
        hundreds, rest = divmod(number, 100)
        string = base_characters(hundreds) + " hundred"
        if rest == 0:
            return string
        else:
            return string + " and " + num_to_str(rest)
    elif number <= 9999:
        thousands, rest = divmod(number, 1000)
        string = base_characters(thousands) + " thousand"
        if rest == 0:
            return string
        elif rest < 100:
            return string + " and " + num_to_str(rest)
        else:
            return string + ", " + num_to_str(rest)

def number_length(str_number):
    return len(str_number.replace(" ", "").replace("-", "").replace(",", ""))

numbers = {x : number_length(num_to_str(x)) for x in range(1, 10000)}
tot = 0
for i, (num, length) in enumerate(numbers.items()):
    tot += length
print(tot)