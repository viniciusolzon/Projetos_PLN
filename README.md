# Processamento de Linguagem Natural
Trabalhos implementados ao decorrer da disciplina de Processamento de Linguagem Natural
* O trabalho 1 cnosiste na implementação de um modelo de linguagem capaz de executar o método
de visualização de Shannon para geração de texto.
  - O modelo foi utilizando trigramas, ou seja, a probabilidade da
      próxima palavra escolhida leva em consideração duas palavras
      anteriores: P(wn|wn−2, wn−1).
  - O texto é gerado através de amostragem. Isto é, a próxima palavra é escolhida de forma aleatória, mas levando em consideração as probabilidades.
      Assim, palavras mais provavéis são escolhidas com maior frequência, mas palavras
      pouco provavéis também podem ser escolhidas.
    
* O trabalho 2 consiste na implementação de um classificador Naive Bayes para análise de sentimentos.
  - O texto utilizado no treinamento e no teste foi pré-processado para incluir
      o prefixo “NAO_” de acordo com a seguinte regra:
  - O prefixo “NAO_” é adicionado a cada palavra após um
      token de negação (não, nem, nunca, jamais, tampouco) até a próxima
      pontuação. São consideradas pontuações: . , ? ! ;
  - O treino foi realizado com 80% dos dados e o teste com 20%. Por fim, é efetuado o
      cálculo da acurácia do classificador aplicado aos dados de teste, o qual é comparado com
      o resultado do Naive Bayes sem a utilização do prefixo “NAO_”.

* O trabalho 3 consiste na implementação de uma rede neural recorrente (RNN ou LSTM) para classificar um conjunto de dados sobre notícias de acordo com suas categorias.
