    # This is a class that represents a football club with attributes for its name, league, and whether it is qualified for the UEFA competition.
class Club :
    # Constructor method to initialize the club's attributes
    def __init__(self, name, league, qualified_to_uefa):
        self.name = name 
        self.league = league
        self.qualified_to_uefa = qualified_to_uefa

    # This method returns information about the club
    def get_name(self):
        return self.name
    
    def get_league(self):
        return self.league

    def get_qualified_to_uefa(self):
        return self.qualified_to_uefa

    # This method sets the club's attributes
    def set_name(self, name):
        self.name = name

    def set_league(self, league):
        self.league = league

    def set_qualified_to_uefa(self, qualified_to_uefa):
        if not isinstance(qualified_to_uefa, bool):
            print("Value must be True or False")
            return
        self.qualified_to_uefa = qualified_to_uefa


c1 = Club("Real Madrid", "La Liga", True)
c2 = Club("Manchester United", "Premier League", True)
c3 = Club("Bayern Munich", "Bundesliga", True)
c4 = Club("Juventus", "Serie A", False)
c5 = Club("Paris Saint-Germain", "Ligue 1", True)
c6 = Club("Barcelona", "La Liga", True)
c7 = Club("Ac Milan", "Serie A", True)

c4.set_qualified_to_uefa(True)
c7.set_qualified_to_uefa(False)

print(f"The club {c1.get_name()} is in the {c1.get_league()} and is qualified for the UEFA competition: {c1.get_qualified_to_uefa()}")
print(f"The club {c2.get_name()} is in the {c2.get_league()} and is qualified for the UEFA competition: {c2.get_qualified_to_uefa()}")
print(f"The club {c3.get_name()} is in the {c3.get_league()} and is qualified for the UEFA competition: {c3.get_qualified_to_uefa()}")
print(f"The club {c4.get_name()} is in the {c4.get_league()} and is qualified for the UEFA competition: {c4.get_qualified_to_uefa()}")
print(f"The club {c5.get_name()} is in the {c5.get_league()} and is qualified for the UEFA competition: {c5.get_qualified_to_uefa()}")
print(f"The club {c6.get_name()} is in the {c6.get_league()} and is qualified for the UEFA competition: {c6.get_qualified_to_uefa()}")
print(f"The club {c7.get_name()} is in the {c7.get_league()} and is qualified for the UEFA competition: {c7.get_qualified_to_uefa()}")


# output:
# The club Real Madrid is in the La Liga and is qualified for the UEFA competition: True
# The club Manchester United is in the Premier League and is qualified for the UEFA competition: True
# The club Bayern Munich is in the Bundesliga and is qualified for the UEFA competition: True
# The club Juventus is in the Serie A and is qualified for the UEFA competition: True
# The club Paris Saint-Germain is in the Ligue 1 and is qualified for the UEFA competition: True
# The club Barcelona is in the La Liga and is qualified for the UEFA competition: True
# The club Ac Milan is in the Serie A and is qualified for the UEFA competition: False