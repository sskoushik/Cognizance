import pandas as pd
sam = pd.Series(['amrita', 'vishwa', 'vidyapeetham'])
comp = sam.map(lambda x: x[0].upper() + x[1:])
print("\nfirst character of each element in a series to uppercase:")
print(comp)