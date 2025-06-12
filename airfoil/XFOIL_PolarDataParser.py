# -*- coding: utf-8 -*-
"""
Created on Mon May 19 00:53:51 2025

@author: Sam Cutmore
"""
import pandas as pd
import matplotlib.pyplot as plt
import re

def parse_xfoil_polar(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # Use RegExp to find start of data table and then skip dashed line.
    data_start = None
    for i, line in enumerate(lines):
        if re.match(r'\s*alpha\s+CL\s+CD\s+CDp\s+CM\s+Top_Xtr\s+Bot_Xtr', line):    # find RegExp for "alpha CL CD CDp CM Top_Xtr Bot_Xtr"
            data_start = i + 2                                                      # skip dashed lines
            break

    # Load columns containing the data
    data = []
    for line in lines[data_start:]:
        if line.strip() == '':
            continue
        values = list(map(float, line.strip().split()))
        data.append(values)

    columns = ['alpha', 'CL', 'CD', 'CDp', 'CM', 'Top_Xtr', 'Bot_Xtr']
    return pd.DataFrame(data, columns=columns)

# Parse both polar files
df_s1223 = parse_xfoil_polar(r"C:\Users\SamC2\Downloads\XFOIL6.99\s1223polar.dat")
df_ag26 = parse_xfoil_polar(r"C:\Users\SamC2\Downloads\XFOIL6.99\ag26polar.dat")

# Plot Lift-to-Drag ratio vs Angle of Attack for comparison. Add a division by zero check when you flesh this out.
plt.figure(figsize=(10, 6))
plt.plot(df_s1223['alpha'], df_s1223['CL'] / df_s1223['CD'], label='S1223', marker='o')
plt.plot(df_ag26['alpha'], df_ag26['CL'] / df_ag26['CD'], label='AG26', marker='s')
plt.xlabel('Angle of Attack (degrees)')
plt.ylabel('Lift-to-Drag Ratio (CL/CD)')
plt.title('Lift-to-Drag Ratio vs Angle of Attack')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
