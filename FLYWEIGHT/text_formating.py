class FormattedText:
    def __init__(self, plain_text) -> None:
        self.plaint_text = plain_text
        #Fuerza bruta
        self.caps = [False] * len(plain_text)

    def capitalize(self, start, end):
        for i in range(start, end):
            self.caps[i] = True
    
    def __str__(self) -> str:
        result = []
        for i in range(len(self.plaint_text)):
            c = self.plaint_text[i]
            result.append(
                c.upper() if self.caps[i] else c
            )
        return "".join(result)

class BetterFormattedText:
    def __init__(self, plain_text) -> None:
        self.plain_text = plain_text
        self.formatting = []

    class TextRange:
        def __init__(self, start, end, capitalize=False) -> None:
            self.end = end
            self.start = start
            self.capitalize = capitalize

        def covers(self, position):
            return self.start <= position <= self.end
    
    def get_range(self, start, end):
        range = self.TextRange(start, end)
        self.formatting.append(range)
        return range
    
    def __str__(self) -> str:
        result = []
        for i in range(len(self.plain_text)):
            c = self.plain_text[i]
            for r in self.formatting:
                if r.covers(i) and r.capitalize:
                    c = c.upper()
            result.append(c)
        return ''.join(result)



if __name__ == "__main__":
    text = "esto es una prueba"
    f = FormattedText(text)
    f.capitalize(5, 10)
    print(f)

    bft = BetterFormattedText(text)
    bft.get_range(12,14).capitalize = True
    print(bft)