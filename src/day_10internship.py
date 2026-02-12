import pandas as pd

data={
      
      "CustomerID":[101,102,101,104,105],
      "Name":["Umar","Farooq",None,"Asif","Maaz"],
      "Age":[20,21,23,None,50],
      "City":["Bijapur",None,"   Delhi","PUNE","Delhi"],
      "Payment":["UPI",None,"Card","Cash","UPI"]
      
      }

df=pd.DataFrame(data)

df.head()#shows first 5 rows
df.head(2)#shows specific rows
df.info()

#checking missing values
print("missing values per column")
print(df.isna().sum())

#filling missing values(stastical approach)
df["Age"]=df["Age"].fillna(df["Age"].mean())
df["Name"]=df["Name"].fillna("Unknown")
df["City"]=df["City"].fillna(df["City"].mode()[0])#most occured name
df["Payment"]=df["Payment"].fillna(df["Payment"].mode()[0])

#check data types 
print(df.dtypes)

#converting data types
df["Age"]=df["Age"].astype(int)
print(df.dtypes)

#string cleaning
df["City"]=df["City"].str.strip()#removing spaces
df["City"]=df["City"].str.lower()
print(df["City"])

#duplicate handling
print(df)
print(df.duplicated().sum())#duplicates are not on this dataset
df=df.drop_duplicates()
df.shape


#task 1
import pandas as pd
import numpy as np
#start creating directory 
data = {
    "student_id": [1, 1, 3, 4, 5, 6, 1],
    "name": ["asif", "dalal", None, np.nan, "asif", "pig", "asif"],
    "city": ["bangalore", "gulbarga", None, np.nan, "wadi", "shabad", "bangalore"]
}

df = pd.DataFrame(data)

print("Shape BEFORE cleaning:", df.shape)

print("\nMissing Values Report:")
print(df.isna().sum())

numeric_columns = df.select_dtypes(include=['number']).columns

for col in numeric_columns:
    median_value = df[col].median()
    df[col] = df[col].fillna(median_value)

duplicate_count = df.duplicated().sum()
print("\nNumber of duplicate rows found:", duplicate_count)

df = df.drop_duplicates()

print("\nShape AFTER cleaning:", df.shape)

print("\nData cleaning completed successfully!")

#task 2
import pandas as pd
import numpy as np

data = {
    "student_id": [1, 2, 3, 4, 5, 6],
    "name": ["asif", "dalal", None, np.nan, "asif", "pig"],
    "city": ["bangalore", "gulbarga", None, np.nan, "wadi", "shabad"],
    "Price": ["$100", "$250", "$175", "$300", "$400", "$150"],
    "Date": ["2024-01-01", "2024-02-15", "2024-03-10", "2024-04-05", "2024-05-12", "2024-06-20"]
}

df = pd.DataFrame(data)

print("Initial Data Types:")
print(df.dtypes)

df["Price"] = df["Price"].str.replace("$", "", regex=False).astype(float)

df["Date"] = pd.to_datetime(df["Date"])

print("\nData Types After Conversion:")
print(df.dtypes)

print("\nUpdated DataFrame:")
print(df)

#task 3
import pandas as pd
data3={
       "Location":[" New York","new york","NEW YORK ","New York"]
       }
df3=pd.DataFrame(data3)
print(df3)
#before cleaning
df3.groupby("Location").size()
print(df3["Location"].unique())
#cleaning
df3["Location"]=df3["Location"].str.strip()
df3["Location"]=df3["Location"].str.title()#or you can use str.lower
#after cleaning
print(df3["Location"].unique())
df3.groupby("Location").size()