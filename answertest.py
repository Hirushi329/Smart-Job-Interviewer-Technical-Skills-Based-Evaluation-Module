import pandas as pd
from gtts import gTTS
import nltk.tokenize


# Loading the Questions.csv and Tags.csv data sets into Python

# def answer_generation():

url1 = r"C:\Users\HP\Documents\Academic Folder\L4S1\Comprehensive Group Project\Stack Overflow Data Set\Questions.csv"
questionsDataFrame = pd.read_csv(url1, encoding='latin-1')

url2 = r"C:\Users\HP\Documents\Academic Folder\L4S1\Comprehensive Group Project\Stack Overflow Data Set\Answers.csv"
answersDataFrame = pd.read_csv(url2, encoding='latin-1')

mergedDataFrame = (pd.merge(questionsDataFrame, answersDataFrame, left_on='Id', right_on='ParentId', how='left'))
print("Merged successfully")

print(mergedDataFrame.loc[mergedDataFrame['ParentId'] == 90])
