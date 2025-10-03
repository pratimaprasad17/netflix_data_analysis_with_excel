import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

df = pd.read_excel("netflix_wordcloud.xlsx")
text = " ".join(df["Description"].dropna().astype(str))
custom = df["Stop words"].dropna().astype(str).str.lower().tolist()

stopwords = set(STOPWORDS)
stopwords.update(custom)

wc = WordCloud(
    background_color='darkgray',
    colormap='Reds',
    stopwords=stopwords,
    width=1000,
    height=500
).generate(text)

wc.to_file("netflix_wordcloud_v6.png")
