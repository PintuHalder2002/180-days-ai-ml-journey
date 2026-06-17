import datetime


class CricketPlayer:
    def __init__(self, f_name, l_name, birth_year, team):
        self.first_name = f_name
        self.last_name = l_name
        self.birth_year = birth_year
        self.team = team
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def get_average_score(self):
        return sum(self.scores)/len(self.scores)

    def get_age(self):
        now = datetime.datetime.now()
        return now.year - self.birth_year

    def __str__(self):
        return f"{self.first_name} {self.last_name}, the cricket player from {self.team}"

    def __lt__(self, other):
        self.avg_score = self.get_average_score()
        other.avg_score = self.get_average_score()
        return self.avg_score < other.avg_score

    def __eq__(self, other):
        self_age = self.get_age()
        other_age = other.get_age()
        print(self_age, other_age)
        return self_age == other_age

virat = CricketPlayer('virat', 'kohli', 1988, "India")
virat.add_score(37)
virat.add_score(100)
virat.add_score(23)

david = CricketPlayer('david', 'warner', 1988, "australia")
david. add_score(37)
david.add_score(23)
david.add_score(85)


# print(f'''{virat.first_name},
# {virat.last_name},
# {virat.birth_year},
# {virat.team},
# {virat.scores},
# {round(virat.get_average_score())}''')

print(virat)
print(david)

print(virat.get_average_score())
print(david.get_average_score())

print(david < virat)
print(virat == david)




