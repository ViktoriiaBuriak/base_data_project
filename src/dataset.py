import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

data_path = 'data/JEE_Rank_2016_2024.csv'

df = pd.read_csv(data_path)
# print(df.head())
# print(df.info())
# print(df.columns)
# print(df.describe())

df['Opening_Rank'] = pd.to_numeric(df['Opening_Rank'], errors='coerce')
df['Closing_Rank'] = pd.to_numeric(df['Closing_Rank'], errors='coerce')

print(df['Year'].value_counts())

yearly_data = df.groupby('Year')[['Opening_Rank', 'Closing_Rank']].mean().reset_index()

plt.plot(yearly_data.index, yearly_data['Opening_Rank'], label = 'Opening_Rank', marker = 'o')
plt.plot(yearly_data.index, yearly_data['Closing_Rank'], label = 'Closing_Rank', marker = 'o')

plt.xlabel('Year')
plt.ylabel('Rank')
plt.title('Opening vs Closing Ranks Over Time')
plt.legend()

#plt.show()

fig = px.line(yearly_data, x='Year', y=['Opening_Rank', 'Closing_Rank'],
              labels={'value': 'Rank', 'variable': 'Rank Type'},
              title='Opening vs Closing Ranks Over Time')

fig.update_traces(mode='lines+markers')# Додаємо маркери на кожну точку (для лінійних графіків)
fig.write_html('yearly_data.html')

institute_ranks = df.groupby('Institute')[['Opening_Rank', 'Closing_Rank']].mean().reset_index()

institute_ranks.plot(kind='bar', figsize=(10, 6))
plt.xlabel('Institute')
plt.ylabel('Average Rank')
plt.title('Comparison of Average Opening and Closing Ranks by Institute')
#plt.show()

fig_2 = px.bar(institute_ranks, x='Institute', y=['Opening_Rank', 'Closing_Rank'],
               labels={'value': 'Rank', 'variable': 'Rank Type'},
               title='Comparison of Average Opening and Closing Ranks by Institute')
fig_2.update_layout(barmode='group') # Додаємо групування стовпців

fig_2.write_html('institute_ranks.html')

gender_ranks = df.groupby('Gender')[['Opening_Rank', 'Closing_Rank']].mean()

gender_ranks.plot(kind='bar', figsize=(8, 8))

plt.xlabel('Gender')
plt.ylabel('Avarage Rank')
plt.title('Comparison of Average Opening and Closing Ranks by Gender')
#plt.show()

gender_ranks_opening = df.groupby('Gender')['Opening_Rank'].mean()
gender_ranks_closing = df.groupby('Gender')['Closing_Rank'].mean()

fig_3 = make_subplots(rows=1, cols=2, specs=[[{'type': 'domain'}, {'type': 'domain'}]], 
                      subplot_titles=['Opening Rank by Gender', 'Closing Rank by Gender'])
fig_3.add_trace(go.Pie(labels=gender_ranks_opening.index, values=gender_ranks_opening.values, 
                       name='Opening Rank by Gender'), 1, 1)

fig_3.add_trace(go.Pie(labels=gender_ranks_closing.index, values=gender_ranks_closing.values,
                       name='Closing Rank by Gender'), 1, 2)

fig_3.update_layout(title_text='Comparison of Average Opening and Closing Ranks by Gender')

fig_3.write_html('gender_ranks.html')


