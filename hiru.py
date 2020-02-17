import nltk

text = "What is Java? Java is a programming lanuage. What is Python? Python is a programming language. How are you today? What is"
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
tokens = tokenizer.tokenize(text)
print(tokens)

level1Words = ['What is', 'What are', 'Is it', 'Define', 'State', 'List', 'Recall', 'what is', 'what are',
                   'is it', 'define', 'state', 'list', 'recall']
level2Words = ['Why', 'Explain', 'Classify', 'Describe', 'Discuss', 'Identify', 'why', 'explain',
                   'classify', 'describe', 'discuss', 'identify']
level3Words = ['How', 'Demonstrate', 'Illustrate', 'Sketch', 'how', 'demonstrate', 'illustrate', 'sketch']

for x in level1Words:
    if x in tokens:
        print('This is a memory-recall question')