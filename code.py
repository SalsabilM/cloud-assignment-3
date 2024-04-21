# import for using packedges
import pandas as pd
import nltk

# read data
df = pd.read_csv("paragraphs.txt",delimiter='\t')

# to stop words 
nltk.download('stopwords')
from nltk.corpus import stopwords
stw = set(stopwords.words('english'))
#remove stop words
df['text'] = df['text'].apply(lambda stwo : " ".join([w for w in str(stwo).split() if w not in stw]))

# to count each repated words after removing stopwords
from collections import Counter
words_count = df['text'].str.split(expand=True).stack().value_counts()
print(words_count)