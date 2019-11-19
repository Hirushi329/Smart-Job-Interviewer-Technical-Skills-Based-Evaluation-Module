import pandas as pd

# Loading the Questions.csv into Python

url1 = r"C:\Users\HP\Documents\Academic Folder\L4S1\Comprehensive Group Project\Stack Overflow Data Set\Questions.csv"
questionsDataFrame = pd.read_csv(url1, encoding='latin-1')
print(questionsDataFrame.columns)

# Creating a random sample from the DataFrame
sampleDataFrame = questionsDataFrame.sample(n=1000, replace=True, weights=None, random_state=None, axis=None)
# print(sampleDataFrame.head(100))

# Grouping the dataset based on the Score
print(sampleDataFrame.groupby('Score').size())
grouped_dataframe = sampleDataFrame.groupby('Score')

threshold_score = grouped_dataframe['Score'] = 10
selectedQuestions = grouped_dataframe['Score' > threshold_score]
# for key, item in grouped_dataframe:
#  print(grouped_dataframe.get_group(key), "\n\n")

# try:
#     score = int('Score')
# except ValueError as err:
#     pass
#
# selectedQuestions = grouped_dataframe[[score > 10]]
# for key, item in selectedQuestions:
#     print(selectedQuestions.get_group(key), "\n\n")
