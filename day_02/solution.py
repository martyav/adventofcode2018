import re
from input import strings

"""
--- Part One ---

You stop falling through time, catch your breath, and check the screen on the device. "Destination reached. Current Year: 1518. 
Current Location: North Pole Utility Closet 83N10." You made it! Now, to find those anomalies.

Outside the utility closet, you hear footsteps and a voice. "...I'm not sure either. But now that so many people have chimneys, 
maybe he could sneak in that way?" Another voice responds, "Actually, we've been working on a new kind of suit that would let 
him fit through tight spaces like that. But, I heard that a few days ago, they lost the prototype fabric, the design plans, 
everything! Nobody on the team can even seem to remember important details of the project!"

"Wouldn't they have had enough fabric to fill several boxes in the warehouse? They'd be stored together, so the box IDs should be 
similar. Too bad it would take forever to search the warehouse for two similar box IDs..." They walk too far away to hear any more.

Late at night, you sneak to the warehouse - who knows what kinds of paradoxes you could cause if you were discovered - and use 
your fancy wrist device to quickly scan every box and produce a list of the likely candidates (your puzzle input).

To make sure you didn't miss any, you scan the likely candidate boxes again, counting the number that have an ID containing 
exactly two of any letter and then separately counting those with exactly three of any letter. You can multiply those two counts 
together to get a rudimentary checksum and compare it to what your device predicts.

For example, if you see the following box IDs:

    abcdef contains no letters that appear exactly two or three times.
    bababc contains two a and three b, so it counts for both.
    abbcde contains two b, but no letter appears exactly three times.
    abcccd contains three c, but no letter appears exactly two times.
    aabcdd contains two a and two d, but it only counts once.
    abcdee contains two e.
    ababab contains three a and three b, but it only counts once.

Of these box IDs, four of them contain a letter which appears exactly twice, and three of them contain a letter which appears exactly
three times. Multiplying these together produces a checksum of 4 * 3 = 12.

What is the checksum for your list of box IDs?
"""

arr = strings.split('\n')

def freq_counter(text):
    alphabet = dict()

    for i in range(0, len(text)):
        char = text[i]

        if char in alphabet:
            alphabet[char] += 1
        else:
            alphabet[char] = 1

    return alphabet

def check_values(text):
    counter = freq_counter(text)

    twos = 0
    threes = 0

    for value in counter.values():
        if value == 2 and twos == 0:
            twos += 1
        if value == 3 and threes == 0:
            threes += 1
    
    return {'twos': twos, 'threes': threes}
    
def calculate_checksum(arr):
    twos = 0
    threes = 0

    for value in arr:
        checked = check_values(value)

        twos += checked['twos']
        threes += checked['threes']

    return twos * threes

check_sum = calculate_checksum(arr)

print(f'The checksum is { check_sum }')

"""
--- Part Two ---

Confident that your list of box IDs is complete, you're ready to find the boxes full of prototype fabric.

The boxes will have IDs which differ by exactly one character at the same position in both strings. For example, given the
following box IDs:

abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz

The IDs abcde and axcye are close, but they differ by two characters (the second and fourth). However, the IDs fghij and fguij
differ by exactly one character, the third (h and u). Those must be the correct boxes.

What letters are common between the two correct box IDs? (In the example above, this is found by removing the differing character
from either ID, producing fgij.)
"""

def star_out_letters(text):
    words = []

    for i in range(0, len(text)):
        if i == len(text) - 1:
            new_word = text[:i] + '*'
        else:
            new_word = text[:i] + '*' + text[i + 1:]
        
        words.append(new_word)

    return words

def find_prototype(arr):
    starred_out = []
    dupe = ''

    for value in arr:
        starred_out.extend(star_out_letters(value))

    for i in range(0, len(starred_out) - 1):
        look_ahead = starred_out[i + 1:]
        current = starred_out[i]

        if current in look_ahead:
            dupe = current

    id = dupe.replace('*', '')

    return id

prototype_id = find_prototype(arr)

print(f'The prototype ID is { prototype_id.upper() }')
