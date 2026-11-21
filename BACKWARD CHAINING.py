# Backward Chaining

facts = ["rain", "cloudy"]

rules = {
    "wet_ground": ["rain"],
    "slippery": ["wet_ground"],
    "take_umbrella": ["cloudy", "rain"]
}

def backward_chaining(goal):
    if goal in facts:
        return True

    if goal in rules:
        for condition in rules[goal]:
            if not backward_chaining(condition):
                return False
        return True

    return False

goal = "slippery"

if backward_chaining(goal):
    print(goal, "can be proved")
else:
    print(goal, "cannot be proved")
