import pandas as pd
var = pd.date_range(start ='22-07-2020',  
         end ='19-01-2021', freq ='d') 
for val in var: 
    print(val) 
