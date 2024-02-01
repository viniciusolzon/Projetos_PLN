import re
from collections import Counter

regex = "[a-zA-ZçÇãÃõÕáÁéÉíÍóÓúÚâÂêÊîÎôÔûÛàÀ]+"

data = open("alice.txt").read()

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
def p_trigram(w1, w2, w3):
    count_w1w2 = 0
    count_w1w2w3 = 0

    for i in range(len(tokens)-1):
        if tokens[i] == w1 and tokens[i+1] == w2:
            count_w1w2 += 1

    for i in range(len(tokens)-1):
        if tokens[i] == w1 and tokens[i+1] == w2 and tokens[i+2] == w3:
            count_w1w2w3 += 1
    
    # print(count_w1w2)
    # print(count_w1w2w3)
    return count_w1w2w3/count_w1w2

print(p_trigram("Alice", "was", "not"))
