class Text:
    # def __init__(self, text_string):
    def __init__(self, sentences):
        # pass
        # self.text_string = text_string
        self.sentences = sentences

    def __str__(self):
        # return self.sentences
        return ''.join(map(str, self.sentences))


class Sentence:
    # def __init__(self, word_string="", letters=[]):
    def __init__(self, sentence_elements):
        # pass
        # self.text_string = word_string
        self.sentence_elements = sentence_elements

    def __str__(self):
        # return self.text_string + self.letters
        # return self.text_string + ' ' + ''.join(map(str, self.letters))
        sentence_string = "" + str(self.sentence_elements[0]);
        for index in range(1, len(self.sentence_elements)):
            if isinstance(self.sentence_elements[index], Word):
                sentence_string += ' ' + str(self.sentence_elements[index])
            else:
                sentence_string += '' + str(self.sentence_elements[index])

        # return ' '.join(map(str, self.sentence_elements))
        return sentence_string


class Word:
    # def __init__(self, word_string="", letters=[]):
    def __init__(self, letters):
        # pass
        # self.text_string = word_string
        self.letters = letters

    def __str__(self):
        # return self.text_string + self.letters
        # return self.text_string + ' ' + ''.join(map(str, self.letters))
        return ''.join(map(str, self.letters))


class Punctuation:
    def __init__(self, symbols):
        # pass
        self.symbols = symbols

    def __str__(self):
        return self.symbols


class Letter:
    def __init__(self, symbol):
        # pass
        self.symbol = symbol

    def __str__(self):
        return self.symbol


if __name__ == '__main__':
    pass

# text = Text("Hello world")
# Hello, world! I am Program?


letter = Letter('a')
letter2 = Letter('b')
# word = Word("ab", [letter, letter2])
word = Word([letter, letter2])
# myText.myCustomField = "1";

print(Text([
    Sentence([
        Word([
            Letter('H'),
            Letter('e'),
            Letter('l'),
            Letter('l'),
            Letter('o'),
        ]),
        Punctuation(','),
        Word([
            Letter('w'),
            Letter('o'),
            Letter('r'),
            Letter('l'),
            Letter('d'),
        ]),
        Punctuation('!'),
    ]),
    # Sentence(),
]))
print(letter)
print(word)
# print(myText.myCustomField)
