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
        'space': space,
    }
# Read csv
data = pd.read_csv("accounts.csv")
df = pd.DataFrame(columns=['length', 'lower', 'upper', 'numeric', 'special', 'space'])
i = 0
for password in data['Password']:
    result = repass(password)
    df.loc[i] = result
    i += 1

print(df)
print('Average Length:\t' + str(df['length'].mean().round(2)))
print('Average Lower:\t' + str(df['lower'].mean().round(2)))
print('Average Upper:\t' + str(df['upper'].mean().round(2)))
print('Average Numeric:' + str(df['numeric'].mean().round(2)))
print('Average Special:' + str(df['special'].mean().round(2)))
print('Average Space:\t' + str(df['space'].mean().round(2)) + '\n')
"""print(df['length'].describe())
print(df['lower'].describe())
print(df['upper'].describe())
print(df['numeric'].describe())
print(df['special'].describe())
print(str(df['space'].describe()) + "\n")
"""
