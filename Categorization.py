# This class is responsible for categorizing the questions into three levels

import nltk.tokenize

text: str = "What are the main object orientation concepts?"
sentences = nltk.sent_tokenize(text, 'english')
for sentence in sentences:
    print(sentence)

    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        print(words)

        level1Words = ['What is', 'What are', 'Is it', 'Define', 'State', 'List', 'Recall', 'what is', 'what are', 'is it', 'define', 'state', 'list', 'recall']
        level2Words = ['Why', 'Explain', 'Classify', 'Describe', 'Discuss', 'Identify', 'why', 'explain', 'classify', 'describe', 'discuss', 'identify' ]
        level3Words = ['How', 'Demonstrate', 'Illustrate', 'Sketch', 'how', 'demonstrate', 'illustrate', 'sketch']

        for x in level1Words:
            if x in sentence:
                print('This is a memory-recall question')

        for x in level2Words:
            if x in sentence:
                print('This is a comprehensive level question')

        for x in level3Words:
            if x in sentence:
                print('This is an application level question')

        else:
            print("Can not categorize the given question into defined levels")
