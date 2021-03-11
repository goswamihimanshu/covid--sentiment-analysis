import streamlit as st

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#import plotly.express as px
from wordcloud import WordCloud,STOPWORDS
import create_wordcloud


dataset_loc = "data/Corona_NLP_train.csv"
image_loc = "img/covid.gif"
pos_loc = "img/pos.png"
neg_loc = "img/neg.png"

# sidebar
def load_sidebar():
    st.sidebar.subheader("Twitter Covid 19 Sentiment")
    st.sidebar.success("Analyze how people in Covid situation expressed their feeling on Twitter")
    st.sidebar.info("This data originally came from Kaggle")
    st.sidebar.warning("Made with :heart: :sunglasses:")

# data
@st.cache
def load_data(dataset_loc):
    df = pd.read_csv(dataset_loc)
    df = df.loc[:, ['Sentiment','OriginalTweet']]
    return df


def load_description(df):
        # Preview of the dataset
        st.header("Data Preview")
        preview = st.radio("Choose Head/Tail?", ("Top", "Bottom"))
        if(preview == "Top"):
            st.write(df.head())
        if(preview == "Bottom"):
            st.write(df.tail())

        # display the whole dataset
        if(st.checkbox("Show complete Dataset")):
            st.write(df)

        # Show shape
        if(st.checkbox("Display the shape")):
            st.write(df.shape)
            dim = st.radio("Rows/Columns?", ("Rows", "Columns"))
            if(dim == "Rows"):
                st.write("Number of Rows", df.shape[0])
            if(dim == "Columns"):
                st.write("Number of Columns", df.shape[1])

        # show columns
        if(st.checkbox("Show the Columns")):
            st.write(df.columns)


# WordCloud
def load_wordcloud(df, kind):
    temp_df = df.loc[df['Sentiment']==kind, :]
    words = ' '.join(temp_df['text'])
    cleaned_word = " ".join([word for word in words.split() if 'http' not in word and not word.startswith('@') and word != 'RT'])
    wc = WordCloud(stopwords=STOPWORDS, background_color='black', width=1600, height=800).generate(cleaned_word)
    wc.to_file("img/wc.png")


def load_viz(df):
        st.header("Data Visualisation")
        # show tweet sentiment count
        st.subheader("Seaborn - Tweet Sentiment Count")
        st.write(sns.countplot(x='Sentiment', data=df))
        st.pyplot()


        # Show WordCloud
        st.subheader("Word Cloud")
        type = st.radio("Choose the sentiment?", ("positive", "negative"))
        if(os.path.isfile(pos_loc)==False or os.path.isfile(neg_loc)==False):
            create_wordcloud.main()
        if(type=="positive"):
            st.image(pos_loc, use_column_width = True)
        else:
            st.image(neg_loc, use_column_width = True)



def main():

    # sidebar
    load_sidebar()

    # Title/ text
    st.title('Covid 19 Tweets Sentiment Analysis')
    st.image(image_loc, use_column_width = True)
    st.text('Analyze how people in Covid situation expressed their feeling on Twitter')

    # loading the data
    df = load_data(dataset_loc)

    # display description
    load_description(df)

    # data viz
    load_viz(df)




if(__name__ == '__main__'):
    main()
