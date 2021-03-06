# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 09:27:12 2020

@author: Philippine
"""

import script_get_data as data
import pandas as pd

#Nettoyage aéroport

liste_indice=[7031,7032,7137,7138,7158,7160,7161,7164,7165,7184,7191,7221,7233,7236,7237,7238,7249,7250,7251,7252,7253,
              7254,7255,7256,7257,7259,7260,7262,7263,7264,7265,7266,7267,7269,7270,7271,7272,7273,7274,7275,7276,7277,
              7278,7279,7280,7283,7288,7641,7680]
liste_ville=["Minsk Mazowiecki","Powidz","nan","nan","Asahikawa","Utsunomiya","Chungju","Bislig","Mati","Metropolitano",
             "Belaya Gora","Volgodonsk","Ratnagiri","Ambala","Sirsa","Udhampur","Ararat","Benalla","Balranald","Brewarrina",
             "Cleve","Corowa","Corryong","Cootamundra","Dirranbandi","Dysart","Echuca","Gunnedah","Hay","Hopeton","Kerang",
             "Kempsey","Kingaroy","Mareeba","Ngukurr","Narromine","Port Pirie","Smithton","Snake Bay","Stawell","Tibooburra",
             "Tumut","Wangaratta","Warracknabeal","Warren","Young","Baruun Urt","Hard Bargain","Xingcheng"]

incidents_data=pd.read_excel('C:/Users/Philippine/Documents/GitHub/project_planes/données/incidents_data.xlsx', encoding='UTF-8')


def cleaning_airports(liste_indice,liste_ville):
    airports=data.airport_data.iloc[:,[1,2,3,5,6,7]]
    for i in range(len(liste_indice)):
        airports.loc[liste_indice[i],'City']=liste_ville[i]
    return(airports)
    
airports=cleaning_airports(liste_indice,liste_ville)
airports.drop(5860,inplace=True)
airports.loc[7698]=["Unknown","Unknown","Unknown","0000","NONE","NONE"]

#Nettoyage incidents
incidents_data['airp_dep_ICAO'].fillna("0000", inplace=True)
incidents_data['airp_arr_ICAO'].fillna("0000", inplace=True)

#Nettoyage routes

#liste_ligne_supp=[38,54,1163,2113,2114,2249,2250,2251,2252,2253,2254,2255,2256,2257,2258,2259,2260,2261,2262,2867,3394,
#                 3777,3778,3779,3780,4126,4127,4128,4129,4130,4131,4132,4133,4468,4469,4567,4635,5541,8741,8742,9725,
#                 10139,10158,10199,10212,10496,10497,10498,10499,10500,10501,10502,10503,10504,10505,10506,10507,10508,
#                 14552,17960,18801,22823,22824,22825,22826,23257,23408,23426,23448,23456,23457,23458,24185,28478,29437,
#                 29984,29996,29997,29998,29999,30000,30001,30002,30034,30035,30036,30047,30048,30049,30050,30055,30061,
#                 30062,30063,30065,30066,30067,30068,30069,30070,30071,30072,30073,30082,30083,30084,30087,30088,30089,
#                 30102,30103,30104,30551,32133,33066,33267,35513,35526,37843,39950,39951,39952,40582,40846,41131,42633,
#                 42634,45208,45332,45333,45720,45721,45722,45992,45995,46421,46584,46658,46659,46696,46697,46706,47163,
#                 47476,47645,47800,47802,47803,47804,47805,47806,48016,48043,48289,48290,48291,48292,48293,48294,49466,
#                 49467,49468,49469,49470,49471,49472,49473,49474,49475,49476,49477,49478,49479,49480,49481,50473,51358,
#                 51359,51360,51602,51603,51808,52142,52680,52755,52763,53855,58020,58560,60722,61869,61871,61918,62497,
#                 62498,62534,62578,62883,62884,62885,63026,63027,63028,63371,63372,63381,63382,63383,63384,65092,65963,
#                 65964,66249,66304,66352,66353,67468,67469,67470,67471,46680,63369,58071,45210,37834,30095,30096,30098,
#                 30099,30100,30101,3740,63386,2108,29979,29981,29982,29983,35515,46587,30549,35528,62891,42625,62805,46678,
#                 67502,3786,33271,46647,63360,45326,63356,45323,63354,30037,30038,30040,30041,30043,30044,30045,30059,30028,
#                 30025,30026,30019,30020,30021,5845,14717,17356,65928,65929,3775,42643,4474,66361,39954,39955,22829,61900,
#                 33051,7,22821,52056,3379,66302,41130,18160,46822,40882,50565,53888,4168,40645,10645,49545,4204,48343,49536,
#                 2301,4183,10584,48329,49518,49497,2199,49418,49411,10655,49550,2142,3968,10304,48194,49376,66256,47671,
#                 2287,2215,4079,10419,48260,49433,17911,2340,10663,49553,2181,10367,49405,2128,2326,2321,4201,10613,48340,
#                 49533,49483,2248,49461,2161,3999,10327,48214,49393,2120,10282,49362,22830,58531,47822,22831,22827,48,47772,
#                 32143,15393,47778,47779,45727,45728,45729,47836,47837,60727,62584,62544,8841,62500,62505,48450,8638,39948,
#                 67483,10149,67455,10594,65127,10627,29493,2234,23175,23413,28439,3949,24076,23453,47956,48038,23512,46709,
#                 23535,23537,23540,10069,10088,67443,51545,51575,10552,51450,51311,63380,3752,45987,45990,46657,2873,1136,
#                 62634,62963,52605,52613,52380,9852,10204,51811,4556,4633,47391,30086]
#
#routes=data.routes_data.iloc[:,[1,3,5,7]].drop(liste_ligne_supp,0)


#suppression des codes ICAO non présent dans le jeu de données 'incidents'

liste_ind_dep=[]
(n,m)=incidents_data.shape
for i in range(n):
    if incidents_data['airp_dep_ICAO'][i] not in list(airports['ICAO']):
        liste_ind_dep.append(i)
        
incidents_data.drop(liste_ind_dep, inplace=True)
incidents_data.reset_index(inplace=True)

liste_ind_arr=[]
(p,q)=incidents_data.shape

for i in range(p):
    if incidents_data['airp_arr_ICAO'][i] not in list(airports['ICAO']):
        liste_ind_arr.append(i)

incidents_data.drop(liste_ind_arr, inplace=True)
incidents_data.reset_index(inplace=True)

#Création de fichiers csv
airports.to_csv('airports_data.csv', encoding='UTF-8')
incidents_data.to_csv('incidents_data.csv', encoding='UTF-8')

#test=pd.read_csv('incidents_data.csv',encoding='UTF-8')
