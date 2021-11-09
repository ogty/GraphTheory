from matching import Player
from matching.games import StableMarriage


# Data definition
suitors = [
    Player(name="Bingley"),
    Player(name="Collins"),
    Player(name="Darcy"),
    Player(name="Wickham"),
]

reviewers = [
    Player(name="Charlotte"),
    Player(name="Elizabeth"),
    Player(name="Jane"),
    Player(name="Lydia"),
]

# Data unpacking
bingley, collins, darcy, wickham = suitors
charlotte, elizabeth, jane, lydia = reviewers

# Suitors
bingley.set_prefs([jane, elizabeth, lydia, charlotte])
collins.set_prefs([jane, elizabeth, lydia, charlotte])
darcy.set_prefs([elizabeth, jane, charlotte, lydia])
wickham.set_prefs([lydia, jane, elizabeth, charlotte])

# Reviewers
charlotte.set_prefs([bingley, darcy, collins, wickham])
elizabeth.set_prefs([wickham, darcy, bingley, collins])
jane.set_prefs([bingley, wickham, darcy, collins])
lydia.set_prefs([bingley, wickham, darcy, collins])

# Solve and result
game = StableMarriage(suitors, reviewers)
result = game.solve()

print(result)

# - Result -
# {Bingley: Jane, Collins: Charlotte, Darcy: Elizabeth, Wickham: Lydia}