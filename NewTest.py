# This class is responsible for filtering questions according to the technical skills
import os
import pandas as pd
from gtts import gTTS
import nltk.tokenize


# Loading the Questions.csv and Tags.csv data sets into Python

def question_selection(technical_skill):

    tag = technical_skill
    url1 = r"C:\Users\HP\Desktop\Comprehensive Group Project\Stack Overflow Data Set\Questions.csv"
    questionsDataFrame = pd.read_csv(url1, encoding='latin-1')

    url2 = r"C:\Users\HP\Desktop\Comprehensive Group Project\Stack Overflow Data Set\Tags.csv"
    tagsDataFrame = pd.read_csv(url2, encoding='latin-1')

    mergedDataFrame = (pd.merge(questionsDataFrame, tagsDataFrame, left_on='Id', right_on='Id', how='left'))


    sampleDataFrame = mergedDataFrame.sample(n=300, replace=True, weights=None, random_state=None, axis=None)
    grouped_dataframe = sampleDataFrame.groupby('Tag')
    selectedDataFrame = grouped_dataframe.get_group(tag)
    selectedQuestions = selectedDataFrame.to_csv(columns=['Title'], sep='\t', index=False)
    print(selectedQuestions)
    selectedQuestionsList = []
    selectedQuestionsList = selectedQuestions.split("\n")
    print(selectedQuestionsList)
    return selectedQuestionsList



