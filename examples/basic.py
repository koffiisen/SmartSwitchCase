from smartswitchcase import SmartSwitchCase, Case

var = 2


def first():
    print("I'm ... 1")


def two():
    print("I'm ... 2")


# Initialisation
swc = SmartSwitchCase(var)
# Add case
swc.case(Case(1, first))
swc.case(Case(2, two))
# Add default statement
swc.default(lambda: "I'm ... Default")
# Run
swc.exc()
