from smartswitchcase import SmartSwitchCase, Case

# Initialisation
swc = SmartSwitchCase([1, 2, 3, 4, 5])
# Add case
swc.case(Case([6, 7, 8], lambda: "[6, 7, 8] Match with [1, 2, 3, 4, 5]"))
swc.case(Case([9, 10, 11], lambda: "[6, 7, 8] Match with [1, 2, 3, 4, 5]"))
swc.case(Case([1, 2, 3, 4, 5], lambda: "[1, 2, 3, 4, 5] Match with [1, 2, 3, 4, 5]"))
swc.case(Case([78, 17, 98], lambda: "[78, 17, 98] Match with [1, 2, 3, 4, 5]"))
# Add default statement
swc.default(lambda: "I'm ... Default [1, 2, 3, 4, 5]")
# Run
swc.exc()
# If you statement return a result you can get her after execution
result = swc.result()
# Show the result
print(result)
