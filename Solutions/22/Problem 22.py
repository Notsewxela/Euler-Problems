"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

def main():
    f = open("p022_names.txt")
    unsorted_names = f.read()
    f.close()
    
    # Assuming every name is already capitalised
    names = sorted(unsorted_names.replace('"', '').split(','))
    
    total = 0
    for i, name in enumerate(names):
        sub_tot = 0
        for c in name:
            # "A" is 65
            sub_tot += ord(c) - 64
        total += sub_tot * (i + 1)
    
    print(total)

main()