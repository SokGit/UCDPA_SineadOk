#Import Pandas as Pd/Import numpy as np
import pandas as pd
import numpy as np
#HP=HousePrice/Second Hand House Price=SecondHP
NewHP=pd.read_csv(r'C:\Users\soksi\Downloads\form_41a-price-new-property-area-by_year_2.csv')
SecondHP=pd.read_csv(r'C:\Users\soksi\Downloads\form_41c-price-sh-property-area-by_year_1.csv')
print(NewHP.head())
print(NewHP.describe())
print(SecondHP.head())
print(SecondHP.describe())
