import operator

"""
--- Part One ---

You've managed to sneak in to the prototype suit manufacturing lab. The Elves are making decent progress, but are still struggling with the suit's size reduction capabilities.

While the very latest in 1518 alchemical technology might have solved their problem eventually, you can do better. You scan the chemical composition of the suit's material and discover that it is formed by extremely long polymers (one of which is available as your puzzle input).

The polymer is formed by smaller units which, when triggered, react with each other such that two adjacent units of the same type and opposite polarity are destroyed. Units' types are represented by letters; units' polarity is represented by capitalization. For instance, r and R are units with the same type but opposite polarity, whereas r and s are entirely different types and do not react.

For example:

    In aA, a and A react, leaving nothing behind.
    In abBA, bB destroys itself, leaving aA. As above, this then destroys itself, leaving nothing.
    In abAB, no two adjacent units are of the same type, and so nothing happens.
    In aabAAB, even though aa and AA are of the same type, their polarities match, and so nothing happens.

Now, consider a larger example, dabAcCaCBAcCcaDA:

dabAcCaCBAcCcaDA  The first 'cC' is removed.
dabAaCBAcCcaDA    This creates 'Aa', which is removed.
dabCBAcCcaDA      Either 'cC' or 'Cc' are removed (the result is the same).
dabCBAcaDA        No further actions can be taken.

After all possible reactions, the resulting polymer contains 10 units.

How many units remain after fully reacting the polymer you scanned? (Note: in this puzzle and others, the input is large; if you copy/paste your input, make sure you get the whole thing.)

"""

text = open("input.txt").read().split()[0]

def reacted_polymer_length(text):
    new_text = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    while new_text != text:
        new_text = text

        for letter in alphabet:
            lower_first = f'{letter}{letter.upper()}'
            upper_first = f'{letter.upper()}{letter}'
            
            text = text.replace(lower_first,"")
            text = text.replace(upper_first,"")
    
    return len(new_text)


completely_reacted = reacted_polymer_length(text)
print(f"The length of the polymer after every unit has reacted is {completely_reacted}.")

"""
--- Part Two ---

Time to improve the polymer.

One of the unit types is causing problems; it's preventing the polymer from collapsing as much as it should. Your goal is to figure out which unit type is causing the most problems, remove all instances of it (regardless of polarity), fully react the remaining polymer, and measure its length.

For example, again using the polymer dabAcCaCBAcCcaDA from above:

    Removing all A/a units produces dbcCCBcCcD. Fully reacting this polymer produces dbCBcD, which has length 6.
    Removing all B/b units produces daAcCaCAcCcaDA. Fully reacting this polymer produces daCAcaDA, which has length 8.
    Removing all C/c units produces dabAaBAaDA. Fully reacting this polymer produces daDA, which has length 4.
    Removing all D/d units produces abAcCaCBAcCcaA. Fully reacting this polymer produces abCBAc, which has length 6.

In this example, removing all C/c units was best, producing the answer 4.

What is the length of the shortest polymer you can produce by removing all units of exactly one type and fully reacting the result?
"""

def find_most_problematic(text):
    freq = {}
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for letter in alphabet:    
        new_text = text

        new_text = new_text.replace(letter, '')
        new_text = new_text.replace(letter.upper(), '')

        new_polymer_length = reacted_polymer_length(new_text)

        freq[letter] = new_polymer_length

    most_problematic = sorted(freq.items(), key=operator.itemgetter(1))[0]

    return most_problematic

part_2 = find_most_problematic(text)
print(f'The most problematic unit in the polymer is {part_2[0]}. If we remove all instances of {part_2[0]}, we get a polymer {part_2[1]} units long.')
