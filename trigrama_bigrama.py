from collections import defaultdict, Counter
from nltk.util import ngrams
import re

regex = "[a-zA-ZçÇãÃõÕáÁéÉíÍóÓúÚâÂêÊîÎôÔûÛàÀ]+"

data = open("alice.txt").read().lower()

tokens = re.findall(regex, data)
tokens_count = Counter(tokens)

# Probabilidade de um bigrama
def p_bigram(w1, w2):
    count_w1 = tokens_count[w1]
    count_w1w2 = 0

    for i in range(len(tokens)-1):
        if tokens[i] == w1 and tokens[i+1] == w2:
            count_w1w2 += 1

    return count_w1w2/count_w1

# Probabilidade de um trigrama
def p_trigrama(trigrama):
    count_w1w2 = 0
    count_w1w2w3 = 0

    for i in range(len(tokens)-1):
        if tokens[i] == trigrama[0] and tokens[i+1] == trigrama[1]:
            count_w1w2 += 1

    for i in range(len(tokens)-2):
        if tokens[i] == trigrama[0] and tokens[i+1] == trigrama[1] and tokens[i+2] == trigrama[2]:
            count_w1w2w3 += 1

    return count_w1w2w3/count_w1w2

# Obtém todos os trigramas da "base de dados" 
trigramas = list(ngrams(tokens, 3))

# Calcula probabilidade de todos os trigramas e guarda em um dicionário
prob_dict = {}
for i in range(len(trigramas)):
    prob_dict[trigramas[i]] = p_trigrama(trigramas[i])

print(prob_dict)
#country, capital = random.choice(list(d.items()))
#capital = random.choice(list(d.values()))