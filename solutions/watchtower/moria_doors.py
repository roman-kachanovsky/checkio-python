""" --- Moria Doors --- Simple

The Doors of Durin were opened by Gandalf and the Fellowship
entered in Moria. As they found, this underground kingdom
has gates on every passageway. Each gate has a written message
which contains the key word. Luckily, Gimli knows how
to recognize the key in these messages. It's the most "like" word,
which has the greatest average "likeness" coefficient with other
words in the message.

You are given a message. You need to pick out all words
(a consecutive sequence of letters or a single letter), calculate
the "likeness" coefficients with other words, take an average
of them and choose the greatest. Count "likeness" coefficient even
for the same words (of course it's 100). If several words have
the same resulting value, then choose the word closest to the end
of the message. Words in the message can be separated by whitespaces
and punctuation. There are no numbers.

"Likeness" coefficient for two words is measured in percentages using
the following rules:
    Letter case does not matter ("A" == "a");
    If the first letters of the words are equal, then add 10%;
    If the last letters of the words are equal, then add 10%;
    Add length comparison as (length_of_word1 / length_of_word2) * 30%,
        if length_of_word1 <= length_of_word2,
        else (length_of_word2 / length_of_word1) * 30%
    Take all unique letters from the both words in one set and count
        how many letters appear in the both words. Add to the coefficient
        (common_letter_number / unique_letters_numbers) * 50;

So the maximum coefficient of likeness is 100%.
For example: for the words "Bread" and "Beard".

The result should be given in the lower case.

Let's look at an example. The message "Friend Fred and friend Ted."
First, pick out words - ("friend", "fred", "and", "friend", "ted").
Next we calculate "likeness" for the first word with other. "friend"
and "fred" have the same first and last letters, so add 20. Then length
comparison: the length of "fred" is lesser than "friend",
so add (4/6)*30=20. The last rule: for these words unique letters are
"definr" and the intersected letters are "defr". So add (4/6)*50 ~ 33.333.
And the summary is 73.333.

This way we will count all other coefficients and get the following table
(results are rounded just for simplicity). The greatest average is 62.976
and the result is "friend".

        | friend  | fred    | and     | friend  | ted     |
--------|---------|---------|---------|---------|---------|
friend  | ------  | 73.333  | 39.286  | 100.0   | 39.286  |
fred    | 73.333  | ------  | 40.833  | 73.333  | 52.5    |
and     | 39.286  | 40.833  | ------  | 39.286  | 50.0    |
friend  | 100.0   | 73.333  | 39.286  | ------  | 39.286  |
ted     | 39.286  | 52.5    | 50.0    | 39.286  | ------  |
--------|---------|---------|---------|---------|---------|
sum     | 251.905 | 239.999 | 169.405 | 251.905 | 181.072 |
average | 62.976  | 60      | 42.351  | 62.976  | 45.268  |

Input:              A message as a string (unicode)
Output:             The keyword as a string.
How it is used:     This is a fabricated algorithm which can be modified
                    and be used for linguistic research and text pattern
                    recognition.
Precondition:       0 < len(message)
                    all(x in (string.ascii_letters + string.punctuation + " ")
                    for x in message)

"""


def my_solution(message):
    from string import ascii_lowercase

    def calculate_likeness(w1, w2):
        if len(w1) > len(w2):
            w1, w2 = w2, w1

        likeness = float(len(w1)) / len(w2) * 30

        if w1[0] == w2[0]:
            likeness += 10

        if w1[-1] == w2[-1]:
            likeness += 10

        likeness += float(len(set(w1) & set(w2))) / len(set(w1 + w2)) * 50
        return likeness

    words = filter(lambda c: c in ascii_lowercase + ' ', message.lower()).split()
    words_sum = {w: 0 for w in words}

    for w1 in words:
        for w2 in words:
            words_sum[w1] += calculate_likeness(w1, w2)

    words_avg = {k: (v - words.count(k) * 100) / words.count(k) / (len(words) - 1) for k, v in words_sum.items()}
    # max(words_avg, key=words_avg.get) looks better but can't pass the tests
    return filter(lambda x: words_avg[x] == max(words_avg.values()), words_avg)[-1]


def gyahun_dash_solution(message):
    import re

    def getscore(word1, word2):
        first = 10 if word1[0] == word2[0] else 0
        last = 10 if word1[-1] == word2[-1] else 0
        length = 30 * min(len(word1) / len(word2), len(word2) / len(word1))
        unique = 50 * len(set(word1) & set(word2)) / len(set(word1) | set(word2))
        return first + last + length + unique

    words = re.findall('[a-z]+', message.lower())[::-1]
    return max(words, key=lambda w: sum(getscore(w, x) for x in words))


def sim0000_solution(message):
    def f(s1, s2):
        point = 10 * ((s1[0] == s2[0]) + (s1[-1] == s2[-1]))
        point += 30 * min(len(s1), len(s2)) / max(len(s1), len(s2))
        point += 50 * len(set(s1) & set(s2)) / len(set(s1 + s2))
        return point

    m = ''.join(c if c.islower() else ' ' for c in message.lower()).split()
    score = {}
    for i, w1 in enumerate(m):
        score[i] = sum(f(w1, w2) for j, w2 in enumerate(m) if i != j)
    return m[max(reversed(range(len(m))), key=score.get)]
