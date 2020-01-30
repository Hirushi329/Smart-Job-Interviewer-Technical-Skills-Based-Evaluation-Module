# Responsible for carrying out the execution flow
import nltk
from TextToSpeech.NewTest import question_selection
from TextToSpeech.TextToSpeechConversion import text_to_speech_conversion

# retrieving the technical skills from the database

# retrieving questions from the data set
technical_Skill: str = "java"
selectedQuestionsList = question_selection(technical_Skill)
length = len(selectedQuestionsList)

for i in range(length):
    selectedQuestion = selectedQuestionsList[i]
    # print('Selected Question:' + selectedQuestion)

    # categorizing the questions into levels
    sentences = nltk.sent_tokenize(selectedQuestion, 'english')
    for sentence in sentences:
        print(sentence)

        for sentence in sentences:
            words = nltk.word_tokenize(sentence)
            # print(words)

            level1Words = ['What is', 'What are', 'Is it', 'Define', 'State', 'List', 'Recall', 'what is', 'what are',
                           'is it', 'define', 'state', 'list', 'recall']
            level2Words = ['Why', 'Explain', 'Classify', 'Describe', 'Discuss', 'Identify', 'why', 'explain',
                           'classify', 'describe', 'discuss', 'identify']
            level3Words = ['How', 'Demonstrate', 'Illustrate', 'Sketch', 'how', 'demonstrate', 'illustrate', 'sketch']

            for x in level1Words:
                if x in sentence:
                    print('This is a memory-recall question')
                    text_to_speech_conversion(sentence)
                    # answer = text_to_speech_conversion(sentence)
                    # result = evaluation(answer)

            for x in level2Words:
                if x in sentence:
                    print('This is a comprehensive level question')
                    text_to_speech_conversion(sentence)
                    # answer = text_to_speech_conversion(sentence)
                    # result = evaluation(answer)

            for x in level3Words:
                if x in sentence:
                    print('This is an application level question')
                    text_to_speech_conversion(sentence)
                    # answer = text_to_speech_conversion(sentence)
                    # result = evaluation(answer)

            else:
                print("Can not categorize the given question into defined levels")
