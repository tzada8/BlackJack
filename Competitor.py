class Competitor:

    def __init__(self, money, cards):
        self.money = money  # Int of how much money they have
        self.cards = cards  # List of all their cards


# Creating user and dealer as Competitor objects
user = Competitor(1000, [])  # User automatically starts with $1000
dealer = Competitor("Inf", [])
