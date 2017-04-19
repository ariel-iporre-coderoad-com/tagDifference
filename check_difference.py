import pandas as pd
import starflex
import json
import numpy


python_tags2 = {u'E200329D1317FC713188CFF1': 2, u'E200329D1317F9313188CFE4': 1, u'E201329D13833DF131905CF7': 1, u'E200329D131782713188CE09': 1, u'AE1000000000000000373951': 5, u'E201329D1382DE3131905B78': 1, u'BABE11112222333344445555': 5, u'E201329D13834B7131905D2D': 1, u'7777777777777777777777777777777777778D63': 1, u'E200329D131764313188CD90': 2, u'AE1000000000000000376918': 4, u'E201329D1383537131905D4D': 1, u'E201329D13834FB131905D3E': 1, u'E201329D1382F3F131905BCF': 1, u'AE1000000000000000376913': 3, u'AE1000000000000000376912': 4, u'AE1000000000000000376911': 3, u'AE1000000000000000376910': 7, u'E201329D1382EBB131905BAE': 1, u'E201329D13832D7131905CB5': 3, u'E200329D1317CAB13188CF2A': 1, u'AE1000000000000000376914': 4, u'E201329D138349F131905D27': 1, u'E201329D1383457131905D15': 1, u'E200329D13175DF13188CD77': 2, u'E201329D1382F17131905BC5': 1, u'AE1000000000000000373054': 3, u'E201329D1382E1F131905B87': 3, u'E201329D13832FB131905CBE': 1, u'E200329D131788713188CE21': 3, u'E201329D1382EBF131905BAF': 3, u'E201329D1382F3B131905BCE': 1, u'E200329D1317EE713188CFB9': 1, u'E200329D13179CB13188CE72': 3, u'E200329D1317A0F13188CE83': 2, u'E200329D131792F13188CE4B': 7, u'E201329D13833A3131905CE8': 1, u'E200329D131759713188CD65': 3, u'E200329D1317A3313188CE8C': 4, u'E200329D1317B0B13188CEC2': 3, u'E200329D131798F13188CE63': 1, u'E200329D131799313188CE64': 1, u'E200329D13178A713188CE29': 1, u'E200329D13178CB13188CE32': 1, u'AE1000000000000000367040': 8, u'E200329D13177F313188CDFC': 3, u'E201329D1382D9B131905B66': 1, u'E200329D131801313188D004': 1, u'E200329D131794B13188CE52': 7, u'E200329D13175F713188CD7D': 1, u'E201329D1382EB7131905BAD': 1, u'E201329D1383337131905CCD': 1, u'E200329D131769713188CDA5': 1, u'E201329D13842BF1319060AF': 8, u'E200329D131788B13188CE22': 2, u'E201329D1382D9F131905B67': 1, u'E200329D131761F13188CD87': 1, u'E201329D1382F1B131905BC6': 1, u'E201329D1382EDB131905BB6': 6, u'E201329D1382DA3131905B68': 3, u'AE1000000000000000376920': 3, u'E200329D13179D313188CE74': 1, u'E201329D1382ED7131905BB5': 5, u'E200329D131792B13188CE4A': 6, u'AE1000000000000000376565': 4, u'E201329D1382FDF131905BF7': 1, u'E200329D1317CA713188CF29': 3, u'E201329D1383317131905CC5': 1, u'E200329D13177EF13188CDFB': 1, u'E201329D13832DB131905CB6': 3, u'E200329D131780B13188CE02': 1, u'E200329D131796B13188CE5A': 1, u'E201329D13834BF131905D2F': 1, u'E200329D131795313188CE54': 1, u'E201329D13834A3131905D28': 2, u'E201329D1383377131905CDD': 1, u'E201329D1382F03131905BC0': 1, u'E200329D13179EF13188CE7B': 1, u'E201329D1382FBF131905BEF': 1, u'E201329D138335F131905CD7': 3, u'E200329D13179AB13188CE6A': 3, u'E201329D138430B1319060C2': 7, u'E200329D13175FF13188CD7F': 1, u'E200329D131790F13188CE43': 1, u'9999999999999999': 1, u'E201329D13833FB131905CFE': 1, u'E200329D13179CF13188CE73': 8, u'E201329D1383483131905D20': 3, u'E201329D1382E3B131905B8E': 1, u'E201329D138337B131905CDE': 7, u'E201329D138429F1319060A7': 3, u'E201329D13842EB1319060BA': 3, u'E200329D1317F8B13188CFE2': 1, u'E200329D1317F8713188CFE1': 5, u'E200329D131791313188CE44': 7, u'E201329D1382E5B131905B96': 1, u'E201329D1382EDF131905BB7': 1, u'E200329D131786B13188CE1A': 3, u'E200329D131802713188D009': 1, u'E200329D131757F13188CD5F': 1, u'E201329D1382DBB131905B6E': 1, u'E201329D1382EE3131905BB8': 1, u'E200329D1317B3713188CECD': 7, u'E201329D1382E03131905B80': 1, u'E200329D13175B713188CD6D': 3, u'E201329D1382FFB131905BFE': 2, u'E200329D131760313188CD80': 1, u'E201329D138331F131905CC7': 1, u'E200329D1317A4B13188CE92': 1, u'E200329D131797313188CE5C': 1, u'E200329D1317F6B13188CFDA': 3, u'E200329D131798B13188CE62': 1, u'123123123AEAEAEAEEAEAEAE': 8, u'E201329D13833FF131905CFF': 1, u'E200329D131898F13188D263': 8, u'E201329D1382E7F131905B9F': 1, u'AE1000000000000000376564': 3, u'E201329D1382F7B131905BDE': 3, u'E200329D1317F0F13188CFC3': 2, u'AE1000000000000000376563': 3, u'E201329D1383503131905D40': 2, u'E200329D13179E713188CE79': 1, u'E200329D131783313188CE0C': 1, u'E200329D13178F313188CE3C': 1, u'E201329D1382F9F131905BE7': 2, u'E201329D1382E5F131905B97': 1, u'E201329D1383343131905CD0': 1, u'ABABABABABABABABABABA123': 6, u'E200329D131897313188D25C': 3, u'1414141414AFAFAFAFFFAAFF': 6, u'E201329D1382DFB131905B7E': 3, u'E200329D131759F13188CD67': 1, u'E200329D1317AF713188CEBD': 8, u'E201329D1382E77131905B9D': 1, u'E200329D1317F5313188CFD4': 1, u'E201329D138337F131905CDF': 1, u'E201329D13832F7131905CBD': 3, u'E201329D1382F77131905BDD': 3, u'E201329D13834BB131905D2E': 7, u'AE1000000000000000376579': 4, u'E200329D131804713188D011': 1, u'CBA000000000000000000293': 3, u'AE1000000000000000376909': 4, u'E200329D131757B13188CD5E': 3, u'E200329D13179AF13188CE6B': 3, u'E200329D131796713188CE59': 1, u'E201329D1382F37131905BCD': 1, u'CEACEACEACEACEACAECAECACACEACACC1234C9E9': 5, u'E2003412DC030119521133240000000000000000000000000000000000000000': 7, u'E200329D13178EB13188CE3A': 1, u'E200329D13178D313188CE34': 1, u'E201329D138353F131905D4F': 1, u'E201329D1382EFF131905BBF': 1, u'E201329D1382DBF131905B6F': 3, u'E200329D131762313188CD88': 1, u'E200329D13178EF13188CE3B': 3, u'E200329D1317FD313188CFF4': 1, u'E201329D1382F43131905BD0': 1, u'E200329D1317EB313188CFAC': 1, u'E200329D1317A2F13188CE8B': 4, u'E201329D1382F57131905BD5': 3, u'E200329D131790713188CE41': 1, u'E200329D131785313188CE14': 1, u'E201329D1383383131905CE0': 1, u'E200329D1317A4F13188CE93': 1, u'E201329D1382F23131905BC8': 1, u'E201329D1382F5B131905BD6': 3, u'AE1000000000000000376584': 1, u'E201329D1382E3F131905B8F': 3, u'E200329D1317A8713188CEA1': 3, u'AE1000000000000000376581': 1, u'AE1000000000000000376582': 1, u'E200329D1317F4713188CFD1': 1, u'E200329D1317ECF13188CFB3': 1, u'E200329D13175FB13188CD7E': 2, u'E201329D1382E37131905B8D': 3, u'E201329D138335B131905CD6': 1, u'E200329D131798713188CE61': 1, u'E200329D131782F13188CE0B': 3, u'E201329D1382FDB131905BF6': 2, u'E200329D131789313188CE24': 3, u'E200329D131786F13188CE1B': 3, u'AE1000000000000000376915': 3, u'E201329D1382E23131905B88': 3, u'E201329D138351B131905D46': 1, u'E200329D1317CC713188CF31': 3, u'E201329D1382E9B131905BA6': 2, u'E200329D131793313188CE4C': 1, u'E201329D1382FF7131905BFD': 1, u'E201329D1382E1B131905B86': 3, u'E200329D131784F13188CE13': 1, u'E201329D1383397131905CE5': 1, u'E201329D1382DD7131905B75': 2, u'E201329D1382F9B131905BE6': 1, u'E201329D13833DB131905CF6': 1, u'E200329D131896F13188D25B': 8, u'E200329D1317FE713188CFF9': 1, u'E201329D1382DB7131905B6D': 4, u'E201329D1383497131905D25': 1, u'E200329D131800F13188D003': 1, u'ABC778899112233445566777': 3, u'E200329D13175BB13188CD6E': 1, u'AE1000000000000000376599': 3, u'AE1000000000000000376598': 4, u'AE1000000000000000376597': 3, u'AE1000000000000000376596': 1, u'E201329D138345B131905D16': 1, u'E200329D1317FA713188CFE9': 1, u'E201329D13832DF131905CB7': 1, u'E200329D131796F13188CE5B': 1, u'E201329D1383323131905CC8': 1, u'E201329D1383357131905CD5': 3, u'E200329D13178AF13188CE2B': 1, u'E201329D1382E83131905BA0': 1, u'E201329D1382DDF131905B77': 3, u'E201329D13830B7131905C2D': 3, u'E201329D1382EFB131905BBE': 6, u'E200329D13178C713188CE31': 1, u'E200329D1317AEF13188CEBB': 3, u'E201329D138347F131905D1F': 1, u'E201329D138375B131905DD6': 3, u'AE1000000000000000376899': 3, u'E201329D13832FF131905CBF': 3, u'E201329D13832E3131905CB8': 1, u'E200329D131781313188CE04': 3, u'AE1000000000000000367036': 6, u'E201329D1382F1F131905BC7': 2, u'E201329D1382DDB131905B76': 1, u'E200329D1317A5313188CE94': 1, u'E200329D131758313188CD60': 1, u'E201329D1382EA3131905BA8': 1, u'E200329D1317F8F13188CFE3': 3, u'AE1000000000000000367032': 11, u'AE1000000000000000367033': 9, u'E201329D138341F131905D07': 1, u'E201329D138377B131905DDE': 3, u'E201329D1382F7F131905BDF': 4, u'AE1000000000000000367037': 8, u'AE1000000000000000367034': 9, u'AE1000000000000000367035': 9, u'E201329D1382E97131905BA5': 1, u'AE1000000000000000367038': 7, u'AE1000000000000000367039': 5, u'E200329D1317A2B13188CE8A': 1, u'E201329D1382DF7131905B7D': 1, u'E200329D13179C713188CE71': 3, u'E201329D1382DFF131905B7F': 2, u'E200329D1317FAB13188CFEA': 1, u'E200329D131765B13188CD96': 1, u'AE1000000000000000376907': 2, u'E201329D1382E43131905B90': 1, u'E201329D1382FBB131905BEE': 1, u'E200329D13178B313188CE2C': 1, u'E200329D131784B13188CE12': 1, u'E200329D13178AB13188CE2A': 1, u'E201329D1382FFF131905BFF': 1, u'E201329D1382F63131905BD8': 1, u'E201329D13842A31319060A8': 3, u'E201329D13833E3131905CF8': 1, u'E201329D138339F131905CE7': 1, u'E200329D131784713188CE11': 1, u'E201329D1383463131905D18': 3, u'E200329D1317F7313188CFDC': 1, u'E201329D138345F131905D17': 1, u'E200329D131782B13188CE0A': 1, u'E200329D1317F6713188CFD9': 5, u'E201329D1383477131905D1D': 1, u'E201329D1382DC3131905B70': 3, u'E200329D13179A713188CE69': 2, u'E201329D138347B131905D1E': 2, u'E200329D1317F3313188CFCC': 1, u'E200329D13175A313188CD68': 1, u'35E017010900000000925E12': 3, u'E200329D131790B13188CE42': 3, u'E200329D131794F13188CE53': 1, u'E200329D131761713188CD85': 1, u'E201329D1382E9F131905BA7': 1, u'AE1000000000000000376901': 1, u'AE1000000000000000376921': 7, u'E201329D1382EF7131905BBD': 8, u'AE1000000000000000376904': 3, u'AE1000000000000000376905': 3, u'AE1000000000000000376906': 1, u'E200329D131757713188CD5D': 4, u'E200329D13178E713188CE39': 1, u'E200329D131780F13188CE03': 1, u'E200329D13175C313188CD70': 1, u'E200329D131761B13188CD86': 3, u'E201329D1382FB7131905BED': 1, u'E201329D1382E17131905B85': 1, u'E201329D1382FD7131905BF5': 1, u'E200329D131787313188CE1C': 1, u'E201329D1383363131905CD8': 2, u'E201329D1382E57131905B95': 1, u'E200329D13177EB13188CDFA': 1, u'E200329D13178CF13188CE33': 1}


tags_py = python_tags2.keys()
counts_py = python_tags2.values()

df1 = pd.DataFrame({'tags' : tags_py, 'counts' : counts_py})


client = starflex.star_client('10.100.1.71')

message = client.get_msg('/apps/inventory',verbose=True)
x = json.loads(message)
print x.keys()
tags_inv = map(lambda y: str(y), x.keys())
counts_inv = numpy.ones(322)
df2 = pd.DataFrame({'tags' : tags_inv, 'counts' : counts_inv})
print 'in python '
print df1.head(10)
print 'in inventory'
print df2.head(10)

df1.to_pickle('df1_pickle.pickle')
df2.to_pickle('df2_pickle.pickle')
# df2 = pd.read_pickle('pickle.pickle')
# print(HPI_data2)
