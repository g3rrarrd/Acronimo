class acronimo:

    def __init__(self, text):
        self.__text = text

    def convert_text_acro(self):
        acron = self.__text
        words = acron.split()
        acronimo = ''.join(word[0].upper() for word in words)
        return acronimo