# This class is responsible for filtering questions according to the technical skills
import os
import nltk.tokenize

import pandas as pd

# Loading the Questions.csv and Tags.csv data sets into Python
from gtts import gTTS

url1 = r"C:\Users\HP\Documents\Academic Folder\L4S1\Comprehensive Group Project\Stack Overflow Data Set\Questions.csv"
questionsDataFrame = pd.read_csv(url1, encoding='latin-1')

url2 = r"C:\Users\HP\Documents\Academic Folder\L4S1\Comprehensive Group Project\Stack Overflow Data Set\Tags.csv"
tagsDataFrame = pd.read_csv(url2, encoding='latin-1')

# To print the entire dataframe
# print(questionsDataFrame.head)
# To print the dataframe statistics
# print(questionsDataFrame.shape)
# To print the first 5 rows
# print(questionsDataFrame.head(5))
# To print the last 5 rows
# print(questionsDataFrame.tail(5))

# Merging the two data frames
mergedDataFrame = (pd.merge(questionsDataFrame, tagsDataFrame, left_on='Id', right_on='Id', how='left'))

# Creating a random sample from the DataFrame
sampleDataFrame = mergedDataFrame.sample(n=100, replace=True, weights=None, random_state=None, axis=None)
# print(sampleDataFrame.head(100))

# Grouping the dataset based on the Tag
# print(sampleDataFrame.groupby('Tag').size())
grouped_dataframe = sampleDataFrame.groupby('Tag')
# for key, item in grouped_dataframe:
# print(grouped_dataframe.get_group(key), "\n\n")

try:
    selectedDataFrame = grouped_dataframe.get_group('java')
    print(selectedDataFrame)
    selectedQuestions = selectedDataFrame.Body
    print(selectedQuestions)
    question = str(selectedQuestions)
    questions_list = []
    questions_list = question.split("<p>")
    print(questions_list)
    selectedQuestion = questions_list[1]
    modifiedQuestion_list = selectedQuestion.split('.')
    modifiedQuestion = modifiedQuestion_list[0]
    print(modifiedQuestion)

    # print(selectedQuestion)

except:
    print("No Java questions in the random sample. Please try again")

# Tesxt to speech conversion

try:
    language = 'en'
    myobj = gTTS(text=modifiedQuestion, lang=language, slow=False)
    myobj.save("Question.mp3")
    os.system("Question.mp3")
except:
    print("No question to be asked")
