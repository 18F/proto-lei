from pandas import DataFrame, merge

preLEI = DataFrame.from_csv(open('../results/protoLEI_preLEI_mapping.csv'), index_col=False)

duns = DataFrame.from_csv(open('../results/protoLEI_DUNS_mapping.csv'), index_col=False)

matches = merge(preLEI, duns, left_on='ProtoLEI', right_on='ProtoLEI')

print matches[:2]

print "%d matches found." % len(matches['Vendor Name_x'])