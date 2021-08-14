import pandas as pd
import plotly.express as px
df = pd.read_csv("Copy+of+data+-+data.csv")

figure = px.scatter(df, x = "cases", y = "country", title = "Number of COVID Cases Per Country")
figure.show()