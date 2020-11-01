from smartswitchcase import SmartSwitchCase, Case

mydict = {
    "data": {
        "1": {"name": "Joel"},
        "2": {"name": "Github & Python"}
    }
}

# Initialisation
swc = SmartSwitchCase(mydict)
# Add case
swc.case(Case({"data": {"1": {"name": "Hi"}}}, lambda: "Maybe 1"))
swc.case(Case({"data": {"1": {"name": "Git"}, "2": {"name": "Github & Python"}, }}, lambda: "Maybe 2"))
swc.case(Case({"data": {"1": {"name": "Joel"}, "2": {"name": "Github & Python"}, }}, lambda: "Maybe 3"))
swc.case(Case({"data": {"1": {"name": "PyPi"}, "2": {"name": "Github & Python"}, }}, lambda: "Maybe 4"))
swc.case(Case({"data": {"1": {"name": "Dict"}, "2": {"name": "Github & Python"}, }}, lambda: "Maybe 5"))
# Run
swc.exc()
# If you statement return a result you can get her after execution
result = swc.result()
# Show the result
print(result)
