import networkx as nx
import numpy as np
import pandas as pd

buildings = pd.read_csv("Buildings.csv", index_col=0)

mail_code_dict={}
for each in buildings.index:
    mail_codes = buildings.loc[each]['Campus Mail Code']
    if len(mail_codes)>3:
        mail_code_list = mail_codes.split(', ')
        for code in mail_code_list:
            mail_code_dict[code]=each
    else:
        mail_code_dict[mail_codes] = each

print(mail_code_dict)
