import pandas as pd
import re
def repass(password):
    length = len(password)
    lower = 0
    upper = 0
    numeric = 0
    special = 0
    space = 0
    for c in password:
        if re.search(r"[a-z]", c):
            lower += 1
        if re.search(r"[A-Z]", c):
            upper += 1
        if re.search(r"[0-9]", c):
            numeric += 1
        if re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', c):
            special += 1
        if re.search(r' ', c):
            space += 1

    return {
        'length': length,
        'lower': lower,
        'upper': upper,
        'numeric': numeric,
        'special': special,
        'password': password,
        'space': space,
    }
# Read csv
data = pd.read_csv("accounts.csv")
for password in data['Password']:
    result = repass(password)
    print(result)