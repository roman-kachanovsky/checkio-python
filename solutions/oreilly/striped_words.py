""" 04. --- Striped Words ---  Simple

The alphabet contains both vowel and consonant letters
(yes, we divide the letters).

Vowels -- A E I O U Y
Consonants -- B C D F G H J K L M N P Q R S T V W X Z

You are given a block of text with different words. These words are
separated by white-spaces and punctuation marks.
Numbers are not considered words in this mission (a mix of letters
and digits is not a word either). You should count the number
of words (striped words) where the vowels with consonants are
alternating, that is; words that you count cannot have
two consecutive vowels or consonants. The words consisting of
a single letter are not striped -- do not count those. C
asing is not significant for this mission.

Input:              A text as a string (unicode)
Output:             A quantity of striped words as an integer.
How it is used:     This idea in this task is a useful exercise
                    for linguistic research and analysis. Text processing
                    is one of the main tools used in the analysis
                    of various books and languages and can help
                    translate print text to a digital format.
Precondition:       The text contains only ASCII symbols.
                    0 < len(text) < 10**5

"""


VOWELS = 'AEIOUY'
CONSONANTS = 'BCDFGHJKLMNPQRSTVWXZ'


def my_solution(text):
    def _is_stripped(w):
        previous = None
        for l in w:
            if l == previous:
                return 0
            else:
                previous = l
        return 1

    words = ''.join([ch.upper() if ch.isalpha() or ch.isdigit() else ' ' for ch in text]).split()

    result = [_is_stripped(
        ''.join(['1' if ch in VOWELS else '0' for ch in word])
    ) for word in words if len(word) > 1 and not any(ch.isdigit() for ch in word)]

    return sum(result)


# TODO: Investigate most clear solution here
# https://py.checkio.org/mission/striped-words/publications/review/clear/
