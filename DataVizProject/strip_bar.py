import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd
import numpy as np


# df = px.data.tips()
# fig = px.strip(df, y="total_bill", x="day",orientation='h')

df = pd.read_csv('C:/Users/Mayukh/Downloads/superconduct/train.csv')

# dff = df[['critical_temp','wtd_gmean_Valence']]
# dff['a'] = pd.cut(dff['wtd_gmean_Valence'], bins=[0,1,2,3,4,5,6,7], precision = 0).astype('str')
# # a = a.tolist()
# # dff1 = pd.DataFrame(a,b)
# dff = dff.groupby('a')

# # Plotly Express
# fig = px.strip(data_frame=dff,
#     x = dff.index, y='wtd_gmean_Valence',
#     # hover_data=['State', 'Pct of Colonies Impacted'],
#     # color_continuous_scale=px.colors.sequential.YlOrRd,
#     # labels={'Pct of Colonies Impacted': '% of Bee Colonies'},
#     template='plotly_dark')

# fig.show()

dff = df[['critical_temp','number_of_elements']]
a = pd.qcut(dff['number_of_elements'], q=6, precision = 0,duplicates='drop').astype('str')
temp = pd.DataFrame({'count':a.value_counts()})
temp = temp.sort_values('count')
fig=px.bar(data_frame=temp,
y='count',
color=temp.index)   

fig.show()