import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='white')
sns.set(style='whitegrid', color_codes=True)
import statistics
import scipy
import re
import math

def acquire():
    data = pd.read_csv('C:/Users/irock/Documents/datamex_082020/module-1/pandas-project/your-code/data/attacks.csv', encoding = 'ISO-8859-1', sep=',')
    return data

def wrangle(df):
    #Cleaning column names
    col_names  = []
    col_names  = df.columns
    clean_col  = [i.replace('.',' ').upper() for i in col_names]
    clean_col  = [i.strip() for i in clean_col]
    df.columns = clean_col
    oredered_col = sorted(clean_col)
    df = df[oredered_col]
    print(oredered_col)
    #Droping duplicates
    df.drop_duplicates(keep = 'first', inplace = True)
    df.reset_index(drop=True, inplace = True)

    for i in range(df.shape[0]):
        lst = []
        for j in oredered_col:
            try:
                x = math.isnan(df[j][i])
                if x:
                    lst.append(str(x))
            except:
                x = False
        if len(lst) > 11:
            df.drop(i, axis = 0, inplace = True)
    df.tail()

    #for i in range(df.shape[0]):
        #try:
            #x=math.isnan(df['CASE NUMBER'][i]
        #except:
            #continue
        #if x == True:
            #df['CASE NUMBER'][i] = df['CASE NUMBER 1'][i]


    #Cleaning column AGE
    df['AGE'] = df['AGE'].fillna('Unknown')
    df['AGE'] = df['AGE'].str.strip()
    df['AGE'].unique()
    def age_clean(x):
        if re.search(r'[a-zA-Z½\s\D\W]',x) != None:
            return 'Unknown'
        else:
            return x
    df['AGE'] = df['AGE'].apply(age_clean)
    df['AGE'] = df['AGE'].fillna('Unknown')
    df['AGE'] = df['AGE'].str.replace(' ', 'Unknown')

    #Cleaning column SEX
    df['SEX'] = df['SEX'].fillna('Unknown')
    df['SEX'] = df['SEX'].str.replace('.', 'Unknown')
    df['SEX'] = df['SEX'].str.replace('lli', 'Unknown')
    df['SEX'] = df['SEX'].str.replace('N', 'M') # I will replace N with M because in the keyboard are toghether so it is probable that the user made a mistake
    df['SEX'] = df['SEX'].str.strip()

    #Cleaning column AREA
    df['AREA'] = df['AREA'].fillna('Unknown')
    df['AREA'] = df['AREA'].str.strip()
    df['AREA'] = df['AREA'].str.replace('','')
    df['AREA'] = df['AREA'].str.replace('?','')
    df['AREA'] = df['AREA'].str.replace('"','')
    df['AREA'] = df['AREA'].str.replace('º','')

    #Cleaning COUNTRY    
    df['COUNTRY'] = df['COUNTRY'].fillna('Unknown')
    df['COUNTRY'] = df['COUNTRY'].astype(str)
    df['COUNTRY'] = df['COUNTRY'].apply(lambda x: x.upper() if bool(x.lower()) else x.upper())
    df['COUNTRY'] = df['COUNTRY'].str.strip()
    df['COUNTRY'] = df['COUNTRY'].replace('?','')

    #Cleaning FATAL (Y/N)
    #def fatal_clean(x):
    #    if bool(re.search(r'\d', x)):
    #        return 'UNKNOWN'

    df['FATAL (Y/N)'] = df['FATAL (Y/N)'].fillna('UNKNOWN')
    df['FATAL (Y/N)'] = df['FATAL (Y/N)'].astype(str)
    df['FATAL (Y/N)'] = df['FATAL (Y/N)'].str.strip()
    df['FATAL (Y/N)'] = df['FATAL (Y/N)'].str.replace('M','N') #I will replace M with N as it is highly probable to be a typo because M and N are together in the keyboard
    df['FATAL (Y/N)'] = df['FATAL (Y/N)'].str.replace('2017','UNKNOWN')
    #df['FATAL (Y/N)'] = df['FATAL (Y/N)'].apply(fatal_clean)
    df['FATAL (Y/N)'] = df['FATAL (Y/N)'].apply(lambda x: x.upper() if bool(x.lower()) else x.upper())

    #Cleaning COUNTRY
    def clean_country_1(x):
        try:
            i = x.index('/')
            return x[:i]
        except:
            try:
                i = x.index('&')
                return x[:i]
            except:
                try:
                    i = x.index('(')
                    return x[:i]
                except:
                    return x

    df['COUNTRY'] = df['COUNTRY'].fillna('UNKNOWN')
    df['COUNTRY'] = df['COUNTRY'].str.replace('?','')
    df['COUNTRY'] = df['COUNTRY'].apply(lambda x: x.upper() if bool(x.lower()) else x.upper())
    df['COUNTRY'] = df['COUNTRY'].str.replace('BETWEEN','')
    df['COUNTRY'] = df['COUNTRY'].apply(clean_country_1)
    df['COUNTRY'] = df['COUNTRY'].str.strip()

    #Cleaning HREF FORMULA
    df['HREF'] = df['HREF'].str.strip()
    df['HREF FORMULA'] = df['HREF FORMULA'].str.strip()
    df['HREF FORMULA'] = df['HREF FORMULA'].str.replace('Q93', 'UNKNOWN')
    df['HREF'] = df['HREF'].str.replace('Q93', 'UNKNOWN')
    df['HREF FORMULA'] = df['HREF FORMULA'].str.replace('#VALUE!', 'UNKNOWN')

    for i in range(df.shape[0]):
        try:
            x = math.isnan(df['HREF FORMULA'][i])
        except:
            continue
        if x:
            df['HREF FORMULA'][i] = df['HREF'][i]

    #Cleaning INJURY
    df['INJURY'] = df['INJURY'].fillna('Unknown')
    df['INJURY'] = df['INJURY'].str.replace('"','')
    df['INJURY'] = df['INJURY'].str.strip()

    #Cleaning INVESTIGATOR OR SOURCE
    df['INVESTIGATOR OR SOURCE'] = df['INVESTIGATOR OR SOURCE'].fillna('Unknown')
    df['INVESTIGATOR OR SOURCE'] = df['INVESTIGATOR OR SOURCE'].str.strip()
    df['INVESTIGATOR OR SOURCE'] = df['INVESTIGATOR OR SOURCE'].str.lstrip('.')

    #Cleaning LOCATION
    df['LOCATION'] = df['LOCATION'].fillna('Unknown')
    df['LOCATION'] = df['LOCATION'].str.strip()
    df['LOCATION'] = df['LOCATION'].str.replace('','')
    df['LOCATION'] = df['LOCATION'].str.replace('"','')
    df['LOCATION'] = df['LOCATION'].str.replace('?','')
    df['LOCATION'] = df['LOCATION'].str.replace('(','')
    df['LOCATION'] = df['LOCATION'].str.replace(')','')

    #Cleaning NAME
    def name_cleaner(x):
        try:
            i = x.index[',']
            return x[:i]
        except:
            return x
    df['NAME'] = df['NAME'].fillna('Unknown')
    df['NAME'] = df['NAME'].str.strip()
    df['NAME'] = df['NAME'].str.replace('"','')
    df['NAME'] = df['NAME'].apply(lambda x: 'Unknown' if x[0].isdigit() else x)
    df['NAME'] = df['NAME'].str.replace('?','')
    df['NAME'] = df['NAME'].str.replace('',"'")
    df['NAME'] = df['NAME'].str.replace('k','')
    df['NAME'] = df['NAME'].apply(lambda x: 'Unknown' if x.startswith('a ') else x)
    df['NAME'] = df['NAME'].apply(lambda x: 'Unknown' if x.startswith('A ') else x)
    df['NAME'] = df['NAME'].apply(lambda x: 'Unknown' if x.startswith('B, ') else x)
    df['NAME'] = df['NAME'].apply(lambda x: 'Unknown' if bool(re.search('male',x)) else x)
    df['NAME'] = df['NAME'].apply(lambda x: 'Unknown' if bool(re.search('female',x)) else x)
    df['NAME'] = df['NAME'].apply(lambda x: 'Unknown' if bool(re.search('teen',x)) else x)
    df['NAME'] = df['NAME'].apply(lambda x: 'Unknown' if bool(re.search('child',x)) else x)
    df['NAME'] = df['NAME'].apply(lambda x: 'Unknown' if bool(re.search('girl',x)) else x)
    df['NAME'] = df['NAME'].apply(lambda x: 'Unknown' if bool(re.search('boy',x)) else x)
    df['NAME'] = df['NAME'].apply(lambda x: 'Unknown' if bool(re.search('Anonymous',x)) else x)
    df['NAME'] = df['NAME'].apply(lambda x: 'Unknown' if bool(re.search('boat',x)) else x)
    df['NAME'] = df['NAME'].apply(lambda x: 'Unknown' if bool(re.search('woman',x)) else x)
    df['NAME'] = df['NAME'].apply(lambda x: 'Unknown' if bool(re.search('sailor',x)) else x)
    df['NAME'] = df['NAME'].apply(lambda x: 'Unknown' if bool(re.search('native',x)) else x)
    df['NAME'] = df['NAME'].apply(lambda x: 'Unknown' if bool(re.search('fisherman',x)) else x)
    df['NAME'] = df['NAME'].apply(lambda x: 'Unknown' if bool(re.search('unknown',x)) else x)
    df['NAME'] = df['NAME'].apply(lambda x: 'Unknown' if bool(re.search('a youth',x)) else x)
    df['NAME'] = df['NAME'].apply(lambda x: 'Unknown' if bool(re.search('Unnown',x)) else x)
    df['NAME'] = df['NAME'].apply(lambda x: 'Unknown' if bool(re.search('unnown',x)) else x)
    df['NAME'] = df['NAME'].apply(lambda x: 'Unknown' if bool(re.search('unnown',x)) else x)
    df['NAME'] = df['NAME'].apply(lambda x: 'Unknown' if bool(re.search('crew',x)) else x)
    df['NAME'] = df['NAME'].apply(name_cleaner)
    df['NAME'] = df['NAME'].apply(lambda x: 'Unknown' if len(x)> 35 else x)


    df['PDF'] = df['PDF'].apply(lambda x: x[1:] if x.startswith('.') else x)

    #Cleaning SPECIES
    def shark_unknown(x):
        if x != 'Sand Shark' and x != 'Hammerhead Shark' and x != 'Spinner Shark' and x != 'Reef Shark' and x != 'Blacktip Shark' and x != 'Dusky Shark' and x != 'Grey Shark' and x != 'Whaler Shark' and x != 'White Shark' and x != 'Copper Shark' and x != 'Zambesi Shark' and x != 'Mako Shark' and x != 'Carpet Shark' and x != 'Cocktail Shark' and x != 'Dogfish Shark' and x != 'Silky Shark' and x != 'Tiger Shark' and x != 'Thresher Shark' and x != 'Bull Shark' and x != 'Blue Shark' and x != 'Cow Shark' and x != 'Banjo Shark' and x != 'Juvenile Shark' and x != 'Gaffed Shark' and x != 'Basking Shark' and x != 'Angel Shark' and x != 'Broadnose Shark' and x != 'Galapagos Shark' and x != 'Lemon Shark' and x != 'Nurse Shark' and x != 'Raggedtooth Shark' and x != 'Sevengill Shark' and x != 'Sevengill Shark' and x != 'Wobbegong Shark':
            return 'Unknown'
        else:
            return x

    df['SPECIES'] = df['SPECIES'].fillna('Unknown')
    df['SPECIES'] = df['SPECIES'].str.strip()
    df['SPECIES'] = df['SPECIES'].str.replace('"', '')
    df['SPECIES'] = df['SPECIES'].str.replace('+', '')
    df['SPECIES'] = df['SPECIES'].apply(lambda x: x[1:] if x.startswith('.') else x)
    df['SPECIES'] = df['SPECIES'].apply(lambda x: 'Unknown' if bool(re.search(r'or', x.lower())) else x)
    df['SPECIES'] = df['SPECIES'].apply(lambda x: 'Sand Shark' if bool(re.search(r'sand.+shark', x.lower())) else x)
    df['SPECIES'] = df['SPECIES'].apply(lambda x: 'Hammerhead Shark' if bool(re.search(r'hammer.+shark', x.lower())) else x)
    df['SPECIES'] = df['SPECIES'].apply(lambda x: 'Spinner Shark' if bool(re.search(r'spinner.+shark', x.lower())) else x)
    df['SPECIES'] = df['SPECIES'].apply(lambda x: 'Reef Shark' if bool(re.search(r'reef.+shark', x.lower())) else x)
    df['SPECIES'] = df['SPECIES'].apply(lambda x: 'Blacktip Shark' if bool(re.search(r'blacktip.+shark', x.lower())) else x)
    df['SPECIES'] = df['SPECIES'].apply(lambda x: 'Blacktip Shark' if bool(re.search(r'blacktip', x.lower())) else x)
    df['SPECIES'] = df['SPECIES'].apply(lambda x: 'Dusky Shark' if bool(re.search(r'dusky.+shark', x.lower())) else x)
    df['SPECIES'] = df['SPECIES'].apply(lambda x: 'Grey Shark' if bool(re.search(r'grey.+shark', x.lower())) else x)
    df['SPECIES'] = df['SPECIES'].apply(lambda x: 'Whaler Shark' if bool(re.search(r'whaler.+shark', x.lower())) else x)
    df['SPECIES'] = df['SPECIES'].apply(lambda x: 'Whaler Shark' if bool(re.search(r'whaler', x.lower())) else x)
    df['SPECIES'] = df['SPECIES'].apply(lambda x: 'White Shark' if bool(re.search(r'white.+shark', x.lower())) else x)
    df['SPECIES'] = df['SPECIES'].apply(lambda x: 'Copper Shark' if bool(re.search(r'copper.+shark', x.lower())) else x)
    df['SPECIES'] = df['SPECIES'].apply(lambda x: 'Zambesi Shark' if bool(re.search(r'zambesi.+shark', x.lower())) else x)
    df['SPECIES'] = df['SPECIES'].apply(lambda x: 'Mako Shark' if bool(re.search(r'mako.+shark', x.lower())) else x)
    df['SPECIES'] = df['SPECIES'].apply(lambda x: 'Carpet Shark' if bool(re.search(r'carpet.+shark', x.lower())) else x)
    df['SPECIES'] = df['SPECIES'].apply(lambda x: 'Cocktail Shark' if bool(re.search(r'cocktail.+shark', x.lower())) else x)
    df['SPECIES'] = df['SPECIES'].apply(lambda x: 'Dogfish Shark' if bool(re.search(r'dogfish.+shark', x.lower())) else x)
    df['SPECIES'] = df['SPECIES'].apply(lambda x: 'Dogfish Shark' if bool(re.search(r'dogfish', x.lower())) else x)
    df['SPECIES'] = df['SPECIES'].apply(lambda x: 'Silky Shark' if bool(re.search(r'silky.+shark', x.lower())) else x)
    df['SPECIES'] = df['SPECIES'].apply(lambda x: 'Tiger Shark' if bool(re.search(r'tiger.+shark', x.lower())) else x)
    df['SPECIES'] = df['SPECIES'].apply(lambda x: 'Thresher Shark' if bool(re.search(r'thresher.+shark', x.lower())) else x)
    df['SPECIES'] = df['SPECIES'].apply(lambda x: 'Bull Shark' if bool(re.search(r'bull.+shark', x.lower())) else x)
    df['SPECIES'] = df['SPECIES'].apply(lambda x: 'Blue Shark' if bool(re.search(r'blue.+shark', x.lower())) else x)
    df['SPECIES'] = df['SPECIES'].apply(lambda x: 'Dogfish Shark' if bool(re.search(r'dog', x.lower())) else x)
    df['SPECIES'] = df['SPECIES'].apply(lambda x: 'Cow Shark' if bool(re.search(r'cow.+shark', x.lower())) else x)
    df['SPECIES'] = df['SPECIES'].apply(lambda x: 'Banjo Shark' if bool(re.search(r'banjo.+shark', x.lower())) else x)
    df['SPECIES'] = df['SPECIES'].apply(lambda x: 'Juvenile Shark' if bool(re.search(r'juvenile.+shark', x.lower())) else x)
    df['SPECIES'] = df['SPECIES'].apply(lambda x: 'Gaffed Shark' if bool(re.search(r'gaffed.+shark', x.lower())) else x)
    df['SPECIES'] = df['SPECIES'].apply(lambda x: 'Basking Shark' if bool(re.search(r'basking.+shark', x.lower())) else x)
    df['SPECIES'] = df['SPECIES'].apply(lambda x: 'Angel Shark' if bool(re.search(r'angel.+shark', x.lower())) else x)
    df['SPECIES'] = df['SPECIES'].apply(lambda x: 'Broadnose Shark' if bool(re.search(r'broadnose.+shark', x.lower())) else x)
    df['SPECIES'] = df['SPECIES'].apply(lambda x: 'Galapagos Shark' if bool(re.search(r'galapagos.+shark', x.lower())) else x)
    df['SPECIES'] = df['SPECIES'].apply(lambda x: 'Lemon Shark' if bool(re.search(r'lemon.+shark', x.lower())) else x)
    df['SPECIES'] = df['SPECIES'].apply(lambda x: 'Nurse Shark' if bool(re.search(r'nurse.+shark', x.lower())) else x)
    df['SPECIES'] = df['SPECIES'].apply(lambda x: 'Raggedtooth Shark' if bool(re.search(r'raggedtooth.+shark', x.lower())) else x)
    df['SPECIES'] = df['SPECIES'].apply(lambda x: 'Sevengill Shark' if bool(re.search(r'sevengill.+shark', x.lower())) else x)
    df['SPECIES'] = df['SPECIES'].apply(lambda x: 'Sevengill Shark' if bool(re.search(r'seven-gill.+shark', x.lower())) else x)
    df['SPECIES'] = df['SPECIES'].apply(lambda x: 'Wobbegong Shark' if bool(re.search(r'wobbegong.+shark', x.lower())) else x)
    df['SPECIES'] = df['SPECIES'].apply(shark_unknown)

    #Cleaning TIME
    def time_cleaner(x):
        s = x.split(' ')
        x = s[0]
        return x

    df['TIME'] = df['TIME'].fillna('Unknown')
    df['TIME'] = df['TIME'].str.strip()
    df['TIME'] = df['TIME'].str.replace('>','Unknown')
    df['TIME'] = df['TIME'].str.replace('<','Unknown')
    df['TIME'] = df['TIME'].apply(lambda x: x.split(' ')[0])
    df['TIME'] = df['TIME'].apply(lambda x: 'Unknown' if bool(re.search(r'or',x.lower())) else x)
    df['TIME'] = df['TIME'].apply(lambda x: 'Unknown' if bool(re.search(r'/',x.lower())) else x)
    df['TIME'] = df['TIME'].apply(lambda x: 'Unknown' if bool(re.search(r'to',x.lower())) else x)
    df['TIME'] = df['TIME'].apply(lambda x: x if bool(re.search(r'^\d\dh\d\d$',x)) else 'Unknown')
    df['TIME'] = df['TIME'].str.strip()

    #Cleaning TYPE
    df['TYPE'] = df['TYPE'].fillna('Unknown')
    df['TYPE'] = df['TYPE'].str.replace('Questionable','Unknown')
    df['TYPE'] = df['TYPE'].str.replace('Boatomg','Boating') # I will replace Boatomg to Boating because the 'o' and 'i' are next to each other on the keyboard
    df['TYPE'] = df['TYPE'].str.replace('Boat','Boating')

    #Clenaing YEAR
    df['YEAR'] = df['YEAR'].fillna(0)
    df['YEAR'] = df['YEAR'].apply(lambda x: 0 if x < 999 else x)

    #Fillin UNNAMED: 22 and UNNAMED: 23
    df['UNNAMED: 22'].fillna('Unknown', inplace = True)
    df['UNNAMED: 23'].fillna('Unknown', inplace = True)

    #Cleaning DATE
    df['DATE'].fillna('Unknown', inplace = True)
    df['DATE'] = df['DATE'].str.strip()
    df['DATE'] = df['DATE'].str.replace('Reported','')
    df['DATE'] = df['DATE'].apply(lambda x: x if bool(re.search(r'^\d\d-\w\w\w-\d\d\d\d$',x.lower())) else 'Unknown')

    #Cleaning ACTIVITY
    def activity_unknown(x):
        if (x != 'Diving' and x != 'Adrift' and x != 'Air Disaster' and x != 'Sea Disaster' and x != 'Aircraft Accident' and 
            x != 'American Cruiser' and x != 'American Freighter' and x != 'Air Minesweeper' and x != 'American Schooner' and 
            x != 'Anesthetize Shark' and x != 'Attempting to Rescue' and x != 'Air Disaster' and x != 'Accident' and 
            x != 'Surfing' and x != 'Snorkel' and x != 'Scuba Diving' and x != 'Boogie boarding' and x != 'Windsurfing' and 
            x != 'Surf skiing' and x != 'Fishing' and x != 'Floating' and x != 'Surfing' and x != 'Bathing' and x != 'Wading' and 
            x != 'Standing' and x != 'Kayaking' and x != 'Canoeing' and x != 'Sailing' and x != 'Accident' and x != 'Boarding' and 
            x != 'Playing' and x != 'Floating' and x != 'Accident' and x != 'Murder' and x != 'Diving' and 
            x != 'Feeding Sharks' and x != 'Lifesaving' and x != 'Suicide' and x != 'Rowing' and x != 'Swimming'):
            return 'Other'
        else:
            return x

    df['ACTIVITY'].fillna('Unknown', inplace = True)
    df['ACTIVITY'] = df['ACTIVITY'].str.strip()
    df['ACTIVITY'] = df['ACTIVITY'].str.replace('"','')
    df['ACTIVITY'] = df['ACTIVITY'].str.replace('.','')
    df['ACTIVITY'] = df['ACTIVITY'].apply(lambda x: 'Diving' if bool(re.search(r'div',x.lower())) else x)
    df['ACTIVITY'] = df['ACTIVITY'].apply(lambda x: 'Adrift' if bool(re.search(r'adrift',x.lower())) else x)
    df['ACTIVITY'] = df['ACTIVITY'].apply(lambda x: 'Air Disaster' if bool(re.search(r'air.+disaster',x.lower())) else x)
    df['ACTIVITY'] = df['ACTIVITY'].apply(lambda x: 'Sea Disaster' if bool(re.search(r'sea.+disaster',x.lower())) else x)
    df['ACTIVITY'] = df['ACTIVITY'].apply(lambda x: 'Aircraft Accident' if bool(re.search(r'Aircraft',x.lower())) else x)
    df['ACTIVITY'] = df['ACTIVITY'].apply(lambda x: 'American Cruiser' if bool(re.search(r'american.+cruiser',x.lower())) else x)
    df['ACTIVITY'] = df['ACTIVITY'].apply(lambda x: 'American Freighter' if bool(re.search(r'american.+freighter',x.lower())) else x)
    df['ACTIVITY'] = df['ACTIVITY'].apply(lambda x: 'Air Minesweeper' if bool(re.search(r'air.+minesweeper',x.lower())) else x)
    df['ACTIVITY'] = df['ACTIVITY'].apply(lambda x: 'American Schooner' if bool(re.search(r'american.+schooner',x.lower())) else x)
    df['ACTIVITY'] = df['ACTIVITY'].apply(lambda x: 'Anesthetize Shark' if bool(re.search(r'anesthetize.+shark',x.lower())) else x)
    df['ACTIVITY'] = df['ACTIVITY'].apply(lambda x: 'Attempting to Rescue' if bool(re.search(r'rescue',x.lower())) else x)
    df['ACTIVITY'] = df['ACTIVITY'].apply(lambda x: 'Air Disaster' if bool(re.search(r'air.+disaster',x.lower())) else x)
    df['ACTIVITY'] = df['ACTIVITY'].apply(lambda x: 'Accident' if bool(re.search(r'f[ea]ll',x.lower())) else x)
    df['ACTIVITY'] = df['ACTIVITY'].apply(lambda x: 'Surfing' if bool(re.search(r'surf',x.lower())) else x)
    df['ACTIVITY'] = df['ACTIVITY'].apply(lambda x: 'Snorkel' if bool(re.search(r'snork',x.lower())) else x)
    df['ACTIVITY'] = df['ACTIVITY'].apply(lambda x: 'Scuba Diving' if bool(re.search(r'scuba',x.lower())) else x)
    df['ACTIVITY'] = df['ACTIVITY'].apply(lambda x: 'Boogie boarding' if bool(re.search(r'boog',x.lower())) else x)
    df['ACTIVITY'] = df['ACTIVITY'].apply(lambda x: 'Windsurfing' if bool(re.search(r'wind',x.lower())) else x)
    df['ACTIVITY'] = df['ACTIVITY'].apply(lambda x: 'Surf skiing' if bool(re.search(r'ski',x.lower())) else x)
    df['ACTIVITY'] = df['ACTIVITY'].apply(lambda x: 'Fishing' if bool(re.search(r'fish',x.lower())) else x)
    df['ACTIVITY'] = df['ACTIVITY'].apply(lambda x: 'Floating' if bool(re.search(r'floa',x.lower())) else x)
    df['ACTIVITY'] = df['ACTIVITY'].apply(lambda x: 'Surfing' if bool(re.search(r'surfing',x.lower())) else x)
    df['ACTIVITY'] = df['ACTIVITY'].apply(lambda x: 'Bathing' if bool(re.search(r'bath',x.lower())) else x)
    df['ACTIVITY'] = df['ACTIVITY'].apply(lambda x: 'Wading' if bool(re.search(r'wad',x.lower())) else x)
    df['ACTIVITY'] = df['ACTIVITY'].apply(lambda x: 'Standing' if bool(re.search(r'stand',x.lower())) else x)
    df['ACTIVITY'] = df['ACTIVITY'].apply(lambda x: 'Kayaking' if bool(re.search(r'kayak',x.lower())) else x)
    df['ACTIVITY'] = df['ACTIVITY'].apply(lambda x: 'Canoeing' if bool(re.search(r'cano',x.lower())) else x)
    df['ACTIVITY'] = df['ACTIVITY'].apply(lambda x: 'Sailing' if bool(re.search(r'sail',x.lower())) else x)
    df['ACTIVITY'] = df['ACTIVITY'].apply(lambda x: 'Accident' if bool(re.search(r'disas',x.lower())) else x)
    df['ACTIVITY'] = df['ACTIVITY'].apply(lambda x: 'Boarding' if bool(re.search(r'board',x.lower())) else x)
    df['ACTIVITY'] = df['ACTIVITY'].apply(lambda x: 'Playing' if bool(re.search(r'play',x.lower())) else x)
    df['ACTIVITY'] = df['ACTIVITY'].apply(lambda x: 'Floating' if bool(re.search(r'flo',x.lower())) else x)
    df['ACTIVITY'] = df['ACTIVITY'].apply(lambda x: 'Accident' if bool(re.search(r'jump',x.lower())) else x)
    df['ACTIVITY'] = df['ACTIVITY'].apply(lambda x: 'Murder' if bool(re.search(r'murd',x.lower())) else x)
    df['ACTIVITY'] = df['ACTIVITY'].apply(lambda x: 'Diving' if bool(re.search(r'splash',x.lower())) else x)
    df['ACTIVITY'] = df['ACTIVITY'].apply(lambda x: 'Feeding Sharks' if bool(re.search(r'Feed',x.lower())) else x)
    df['ACTIVITY'] = df['ACTIVITY'].apply(lambda x: 'Lifesaving' if bool(re.search(r'lifes',x.lower())) else x)
    df['ACTIVITY'] = df['ACTIVITY'].apply(lambda x: 'Suicide' if bool(re.search(r'suicide',x.lower())) else x)
    df['ACTIVITY'] = df['ACTIVITY'].apply(lambda x: 'Rowing' if bool(re.search(r'row',x.lower())) else x)
    df['ACTIVITY'] = df['ACTIVITY'].apply(lambda x: 'Swimming' if bool(re.search(r'swim',x.lower())) else x)
    df['ACTIVITY'] = df['ACTIVITY'].apply(activity_unknown)

    #CSV CLEAN
    df.to_csv('C:/Users/irock/Documents/datamex_082020/module-1/pandas-project/your-code/data/Attacks Clean.csv', index = False, sep =',')

    return df


def analyze_visualize(df):
    df.describe()
    days = 365

    means = pd.DataFrame(df.tail(days).mean())
    std = pd.DataFrame(df.tail(days).std())
    ratios = pd.concat([means, std], axis = 1).reset_index()
    ratios.columns = ['Description','Mean','Std']
    ratios['Ratio'] = ratios['Mean']/ratios['Std']
    ratios

    df['YEAR'] = df['YEAR'].replace(0, np.nan)
    fig, ax = plt.subplots()
    ax = df['YEAR'].hist(bins=50, density=True, stacked=True, color='navajowhite', alpha=0.8)
    ax = df['YEAR'].plot(kind='density', color='orange')
    ax.set(title='Shark Attack Data')
    ax.set(xlabel='Years')
    plt.xlim(1800,2021)
    plt.savefig('plots/Years Hist.png', dpi =100)
    plt.show()
    df['YEAR'] = df['YEAR'].replace(np.nan, 0)

    df['YEAR_GRAPH'] = df[df['YEAR']>1950]['YEAR']
    year_counter = df['YEAR_GRAPH'].value_counts().sort_index()

    year_counter.plot(title='Shark Attacks Per Year 1950 - 2018',color = 'crimson')
    plt.savefig('C:/Users/irock/Documents/datamex_082020/module-1/pandas-project/your-code/plots/Attacks Per Year.png')
    

    df['AGE_GRAPH'] = df['AGE'].str.extract('([0-9]+)', expand = False).dropna().astype(int)
    age_counter = df['AGE_GRAPH'].value_counts()
    age_counter.plot(title = 'Ages of Attacked People',style='.', color = 'k')
    plt.xlim(0,100)
    plt.savefig('C:/Users/irock/Documents/datamex_082020/module-1/pandas-project/your-code/plots/Ages of Attacked People.png')


    p = sns.countplot(x='ACTIVITY', data=df, palette='BuGn_r', order = df.ACTIVITY.value_counts().iloc[:7].index)
    p.axes.xaxis.label.set_text('Activity')
    p.axes.yaxis.label.set_text('Count')
    p.set_title('Most Accidented Activities')
    plt.savefig('C:/Users/irock/Documents/datamex_082020/module-1/pandas-project/your-code/plots/Most Accidented Activities.png')
    plt.show()

    df1 = df.copy()
    df1['SPECIES'] = df1[df1.SPECIES != 'Unknown']['SPECIES']
    print(df1['SPECIES'].value_counts()[0:5])
    p = sns.countplot(x='SPECIES', data=df1, palette='GnBu_d', order = df1.SPECIES.value_counts().iloc[0:5].index)
    p.set_xticklabels(p.get_xticklabels(),rotation=45)
    p.axes.xaxis.label.set_text('Species')
    p.axes.yaxis.label.set_text('Count')
    p.set_title('Most Dangerous Species')
    plt.tight_layout()
    plt.savefig('C:/Users/irock/Documents/datamex_082020/module-1/pandas-project/your-code/plots/Most Dangerous Species.png',dpi = 100)
    plt.show()

    df['SEX'].value_counts().plot(kind='pie', rot = 45, autopct = '%1.1f%%', figsize=(5,5), title='Attacks by Gender', colors = ['lightblue','lightpink','gainsboro'], table = True)
    plt.tight_layout()
    plt.savefig('C:/Users/irock/Documents/datamex_082020/module-1/pandas-project/your-code/plots/Attacks by Gender.png',dpi=100)
    plt.show()

    df['FATAL (Y/N)'].value_counts().plot(kind='pie', rot = 45, autopct = '%1.1f%%', figsize=(5,5), title='Fatatlity of the Attack', colors = ['darkseagreen','tomato','gainsboro'], table = True)
    plt.tight_layout()
    plt.savefig('C:/Users/irock/Documents/datamex_082020/module-1/pandas-project/your-code/plots/Fatality.png',dpi=100)
    plt.show()

    df1 = df.copy()
    df1['COUNTRY'] = df1[df1.SPECIES != 'Unknown']['COUNTRY']
    print(df1['COUNTRY'].value_counts()[0:7])
    p = sns.countplot(x='COUNTRY', data=df1, palette='coolwarm', order = df1.COUNTRY.value_counts().iloc[0:7].index)
    p.set_xticklabels(p.get_xticklabels(),rotation=45)
    p.axes.xaxis.label.set_text('Countries')
    p.axes.yaxis.label.set_text('Count')
    p.set_title('Attacks per Country')
    plt.tight_layout()
    plt.savefig('C:/Users/irock/Documents/datamex_082020/module-1/pandas-project/your-code/plots/Attacks per Country.png',dpi = 100)
    plt.show()

    #if __name__ == '__main__':
data = acquire()
filtered = wrangle(data)
results = analyze_visualize(filtered)
