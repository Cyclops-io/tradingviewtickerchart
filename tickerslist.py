#!/usr/bin/env python

import pandas as pd
import sys

var = "s"
table = pd.read_csv("SWTSX_FundHoldings_2020-12-31.csv")

text = []

#fstring format:
# var + index + " = input('" + ticker + "', type=input.symbol)

if __name__ == "__main__":
    for index, row in table.iterrows():
        ticker = row['Symbol']
        if ticker != 'nan':
            text.append(str(f'{var}{index} = input(\'{ticker}\', type=input.symbol)'))
#            text.append(("\n   "))
    with open('output.txt', 'w') as f:
        for t in text:
            f.write(t + '\n')
        print(' wrote output.txt')