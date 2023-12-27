import matplotlib.pyplot as plt
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
figure=px.bar(data,x=data["MoM"],title="man of the match in 2023 world cup",color="MoM")
figure.show()
#highest scorer in total matches
figure=px.bar(data,x=data["highest scorer"],y=data["runs"],color="highest scorer")
figure.show()
# best bowler in each match
figure=px.bar(data,x=data["highest wickets"],title=" best bowler in world cup 2023",color="highest wickets")
figure.show()
#TOSS DECISIONS
toss = data["Toss decision"].value_counts()
label = toss.index
counts = toss.values
colors = ['red','lightgreen']

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='toss desicions in world cup 2023')
fig.update_traces(hoverinfo='percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()
# WON BY RUNS OR WICKETS
won_by = data["won by"].value_counts()
label = won_by.index
counts = won_by.values
colors = ['red','lightgreen']

fig = go.Figure(data=[go.Pie(labels=label, values=counts)])
fig.update_layout(title_text='Number of Matches Won By Runs/Wickets')
fig.update_traces(hoverinfo='percent', textinfo='value', textfont_size=30,
                  marker=dict(colors=colors, line=dict(color='black', width=3)))
fig.show()
#best stadium to bowl first
fig = go.Figure()
fig.add_trace(go.Bar(x=data["Venue"],y=data["1st innings wickets"],name='First innings wickets',marker_color='blue'))
fig.add_trace(go.Bar(x=data["Venue"],y=data["2nd innings wickets"],name='Second innings wickets',marker_color='green'))
fig.update_layout(barmode='group',xaxis_tickangle=-15,title=" best stadium to bowl first")
fig.show()
#best stadium to bat first
fig = go.Figure()
fig.add_trace(go.Bar(x=data["Venue"],y=data["1st innings score"],name='First innings score',marker_color='blue'))
fig.add_trace(go.Bar(x=data["Venue"],y=data["2nd innings score"],name='Second innings score',marker_color='red'))
fig.update_layout(barmode='group',xaxis_tickangle=-15,title=" best stadium to bat first")
fig.show()
#best scores and wicket taker in each time
figure=px.bar(data,x=data["highest scorer"],y=data["runs"],color="highest scorer",title="highest run scorer in each match")
figure.show()
figure=px.bar(data,x=data["highest wickets"],title=" best bowler in world cup 2023")
figure.show()
# comparison between two innings
plt.figure(figsize=(45,10))
x=data['Date']
y=data['1st innings score']
y1=data['2nd innings score']
plt.xlabel('Date');
plt.ylabel('runs');
plt.title('Score in both innings')
plt.plot(x,y,ls='--',marker='*',ms=12)
plt.plot(x,y1,marker='o',ms=10)
plt.legend(['1st innings score','2nd innings score'])
