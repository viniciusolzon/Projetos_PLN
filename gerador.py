import nltk
from nltk.corpus import brown
from nltk.probability import FreqDist, ConditionalFreqDist

# Load and preprocess the data
text = brown.words()
# print(text[:50])
# input()

# Create a bigram language model
bigrams = nltk.bigrams(text)
cfd = ConditionalFreqDist(bigrams)


# Generate text
seed_text = "The quick election"
generated_text = seed_text

for i in range(10):
    # Find the next word using the bigram model
    next_word = cfd[seed_text].max()
    generated_text += " " + next_word
    seed_text = next_word

print(generated_text)
