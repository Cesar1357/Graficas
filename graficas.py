from ast import Lambda
import csv
from dataclasses import replace
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

info = pd.read_csv('./Nuevo.csv')
stars = pd.DataFrame(info)

radius = stars['Radius'].to_list()
mass = stars['Mass'].to_list()
gravity = stars['Gravity'].to_list()

fig = px.bar(x=mass, y=radius,title="Masa y Radio")
fig.show()

fig2 = px.scatter(x=mass, y=gravity,title="Masa y gravedad")
fig2.show()

fig3 = px.scatter(x=radius, y=gravity,title="Radio y gravedad")
fig3.show()

plt.figure(figsize=(10,5))
sns.lineplot(gravity, marker='o', color='red')
plt.title('Gravedad')
plt.show()