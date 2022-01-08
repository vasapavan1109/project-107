import pandas as pd
import plotly_express as px
import csv

df = pd.read_csv(r"C:\Users\rajuv\Desktop\whitehatjrprojects\datavisualproject\data.csv")
fig = px.scatter(df,x = "attempt", y = "student_id",color = "level",title = "STUDENT MARK")
fig.show()
