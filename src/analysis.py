import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import plotly.express as px


data_path = 'data/CHATGPT.csv'

df = pd.read_csv(data_path)

print(df.head())
print(df.info())
print(df.columns)
print(df.describe())

missing_values = df['Review'].isnull().sum()
print(missing_values)

df['Review'] = df['Review'].fillna('No review')

print(df['label'].value_counts())

#Відображення локально через matplotlib
total = df['label'].value_counts().sum()
df['label'].value_counts().plot(kind='pie', autopct=lambda p: f'{p:.1f}% ({int(p*total/100)})', colors=['#ff9999','#66b3ff'],
    shadow=True)
plt.title('Distribution of Reviews')
#plt.show()

print(df['Review'].apply(type).value_counts())

#plotly і HTML
df['Review'] = df['Review'].fillna('')
df['Review'] = df['Review'].astype(str)
all_reviews = ' '.join(df['Review'])
words = all_reviews.split()
word_counts = Counter(words)
top_words = word_counts.most_common(10)
labels, counts = zip(*top_words)

fig = px.bar(x=labels, y=counts, title='Top 10 Most Common Words in Reviews', labels={'x': 'Words', 'y': 'Counts'}, color=labels, color_discrete_sequence=px.colors.qualitative.Vivid)

fig.write_html('top_words.html')
# print(word_counts.most_common(10))

label_counts = df['label'].value_counts()

fig_2 = px.pie(values=label_counts.values, names=label_counts.index, title='Distribution of Reviews', color_discrete_sequence=['#ff9999','#66b3ff'])

fig_2.write_html('distribution_of_reviews.html')