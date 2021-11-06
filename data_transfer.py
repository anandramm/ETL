from pandas import DataFrame,read_csv
from sqlalchemy import create_engine

data=read_csv(r"C:\Users\Anandram Mariappan\Desktop\Data.csv")
df=data
df.drop(columns=["address","grades"],axis=1,inplace=True)
print(df.head(5))

with open(r"C:\Users\Anandram Mariappan\Desktop\postgresql_cre.txt","r")as fp:
    cred=fp.read()

engine=create_engine(cred)
df.to_sql("data",engine)