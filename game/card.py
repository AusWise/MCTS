class Card:
    def __init__(self, name, text=None):
        self.name = name
        self.text = text

    def __str__(self):
        return self.name

class CardFactory:
    def __call__(self, *args, **kwargs):
        cards = [Card("Card 1"), Card("Card 2"),
                 Card("Card 3"), Card("Card 4"),
                 Card("Card 5"), Card("Card 6"),
                 Card("Card 7"), Card("Card 8"),
                 Card("Card 9"), Card("Card 10")]

        return cards
