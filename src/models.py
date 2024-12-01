class MP:
    def __init__(self, name, party, constituency, votes):
        self.name = name
        self.party = party
        self.constituency = constituency
        self.votes = votes

class Party:
    def __init__(self, name):
        self.name = name
        self.total_votes = 0
        self.mps = []

    def add_mp(self, mp):
        self.mps.append(mp)
        self.total_votes += mp.votes

class Constituency:
    def __init__(self, name, total_voters, votes_cast):
        self.name = name
        self.total_voters = total_voters
        self.votes_cast = votes_cast
