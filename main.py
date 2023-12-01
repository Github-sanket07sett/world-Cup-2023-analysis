import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default = "plotly_white"
path="/content/drive/MyDrive/Dataset/World-Cup-2023-Schedule edit(final edit)1.csv"
data = pd.read_csv(path)
print(data.head())
figure = px.bar(data,x=data["match winner"],title="Number of Matches Won by teams in  World Cup 2023",color="match winner",color_discrete_sequence=["grey", "green" , "red",  "green", 
 "orange", "blue", "blue", "yellow", "orange","blue"])
figure.show()
#Number of mom awards
figure=px.bar(data,x=data["MoM"],title="man of the match in 2023 world cup")
figure.show()
#highest scorer in total matches
figure=px.bar(data,x=data["highest scorer"],y=data["runs"],color="highest scorer")
figure.show()
