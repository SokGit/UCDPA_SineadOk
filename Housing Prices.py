#Import Pandas as Pd/Import numpy as np
import pandas as pd
import numpy as np
#HP=HousePrice/Second Hand House Price=SecondHP
NewHP=pd.read_csv(r'C:\Users\soksi\OneDrive\Desktop\Annual New Property Price.csv')
SecondHP=pd.read_csv(r'C:\Users\soksi\OneDrive\Desktop\Second Hand Property prices.csv')
print(NewHP.head())
print(SecondHP.describe)
print(SecondHP.head())
print(SecondHP.describe())
CelticTigerYears2006_2008=np.array([305269,322634,305269])
CrashYears2009_2011=np.array([242033,228268,230303])
print(CelticTigerYears2006_2008.mean())
print(CrashYears2009_2011.mean())
