import pandas as pd

# Loading the Questions.csv into Python

url1 = r"C:\Users\HP\Documents\Academic Folder\L4S1\Comprehensive Group Project\Stack Overflow Data Set\Questions.csv"
questionsDataFrame = pd.read_csv(url1, encoding='latin-1')
print(questionsDataFrame.columns)

# Creating a random sample from the DataFrame
sampleDataFrame = questionsDataFrame.sample(n=1000, replace=True, weights=None, random_state=None, axis=None)
# print(sampleDataFrame.head(100))

# Grouping the dataset based on the Score
# print(sampleDataFrame.groupby('Score').size())
# grouped_dataframe = sampleDataFrame.groupby('Score')
print(sampleDataFrame[sampleDataFrame['Score']==sampleDataFrame['Score'].max()].Score)