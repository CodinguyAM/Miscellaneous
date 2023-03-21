import re


tests = ["From: A", "Firm; B", "B; Firm", "FxYM", "Fxym", "Fbabm", "Fym5", "Fm"]
r = "^F.?m"
for t in tests:
    if re.search(r, t):
        print( t)
