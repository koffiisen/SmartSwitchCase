from smartswitchcase import SmartSwitchCase, Case
import random

obj = random.randint(1, 11)


def first():
    return "I'm ... 1"


def two():
    return "I'm ... 2"


# Initialisation
swc = SmartSwitchCase(obj)
# Add case
swc.case(Case(1, first))
swc.case(Case(2, two))
swc.case(Case(3, lambda: "I'm ... 3"))
swc.case(Case(4, lambda: "I'm ... 4"))
swc.case(Case(5, lambda: "I'm ... 5"))
swc.case(Case(6, lambda: "I'm ... 6"))
swc.case(Case(7, lambda: obj * 7))
swc.case(Case(8, lambda: 888))
swc.case(Case(9, lambda: 999))
# Add default statement
swc.default(lambda: "I'm ... Default")
# Run
swc.exc()
# If you statement return a result you can get her after execution
result = swc.result()
# Show the result
print(result)
