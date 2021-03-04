import csv

with open('iris.data.txt', "r") as csvfile:
    lines = csv.reader(csvfile)
    # for row in lines:
    #     print(','.join(row))

import random


def dados(nome, share, treinamento=[], teste=[]):
    with open(nome, "r") as csvfile:
        lines = csv.reader(csvfile)
        # print(lines)
        # print("lines")
        dataset = list(lines)
        dataset = normalize(dataset)
        # print(dataset)
        dataset = binarylist(dataset)
        # print(dataset)
        # print("dataset")
        # print(len(dataset))
        # printArray(dataset)

        for x in range(len(dataset) - 1):
            # print(x, "(x)", dataset[x])
            # caso aleatório
            if random.random() < share:
                treinamento.append(dataset[x])
            else:
                teste.append(dataset[x])

            # caso teste
            # if x % 50 > 15:
            #     treinamento.append(dataset[x])
            # else:
            #     teste.append(dataset[x])
        print(len(treinamento), " treinamento", len(teste), " teste")


def normalize(matriz=[]):
    # normalizar só o dataset inteiro, se não dá erro
    max = [5, 3, 2, 2]
    min = [5, 3, 2, 2]
    # valores inciais fazem sentido pro iris e apenas pra ele
    resp = []
    resp = matriz
    for x in range(len(matriz) - 1):
        for y in range(4):
            # print(x, "(x)", y, "(y)", matriz[x][y], "(cell)")
            if float(matriz[x][y]) > max[y]:
                max[y] = float(matriz[x][y])
            if float(matriz[x][y]) < min[y]:
                min[y] = float(matriz[x][y])

    # print(max)
    # print(min)

    delta = [0, 0, 0, 0]
    for x in range(4):
        delta[x] = max[x] - min[x]

    # print(delta)

    for x in range(len(matriz) - 1):
        for y in range(4):
            # print(matriz[x][y], "cell", min[y], " (min)", delta[y]," (delta)")
            resp[x][y] = (float(matriz[x][y]) - min[y]) / delta[y]

    return resp


def binarylist(matriz=[]):
    criterio = ['Iris-setosa', 'Iris-versicolor']
    resp = []
    for x in range(len(matriz) - 1):
        # print(matriz[x][4])
        if matriz[x][4] == criterio[0] or matriz[x][4] == criterio[1]:
            # print("enter!")
            element = [matriz[x][0], matriz[x][2], matriz[x][4]]
            # print(element)
            resp.append(element)

    # print("binary list")
    # print(resp)
    return resp


# def dotProduct(vetor1=[], vetor2=[]):
#     resp = 0
#     if len(vetor1) != len(vetor2):
#         print("vetores de tamanhos diferentes")
#     else:
#         for x in range(len(vetor2) - 1):
#             resp += vetor1[x] * vetor2[x]
#
#     return resp

def breakMatrix(mat=[]):
    arr = []

    for x in range(len(mat)-1):
        arr.append(mat[x][2])
        mat[x].pop(2)

    return arr


def train(trainmatrix=[]):

    criterio = ['Iris-setosa', 'Iris-versicolor']
    # setosa = -1, versicolor =1 na separação
    pesos = [-0.45, 0.78]
    limiar =0.62
    learnRate = 0.4
    # print(pesos, ", ", limiar)


    for x in range(len(trainmatrix) - 1):
        #percorre a matriz duas vezes, sempre pegando uma de cada tipo

        # print("at:", x, " - ", trainmatrix[x])

        if trainmatrix[x][2] == criterio[0]:
            #setosa, x
            d = -1 #target
            u = trainmatrix[x][0]*pesos[0]+trainmatrix[x][1]*pesos[1]-1*limiar
            #se diferente do esperado, atualiza
            # print("u (s,x): ", u)

            if u > 0:
                u = 1 #generated outcome

                pesos[0] = pesos[0] + learnRate * trainmatrix[x][0] * (d - u)
                pesos[1] = pesos[1] + learnRate * trainmatrix[x][1] * (d - u)
                limiar = limiar + learnRate * -1 * (d - u)

                print("corrigindo: ", pesos, ", ", limiar)

        elif trainmatrix[x][2] == criterio[1]:
            #versicolor, x
            #print(criterio[1], " and", pesos, ", ", limiar)
            d = 1
            u = trainmatrix[x][0] * pesos[0] + trainmatrix[x][1] * pesos[1] - 1 * limiar
            # print("u (v,x): ", u)

            #se diferente do esperado atualiza. Isso poderia ser organizado numa função, claro, mas vou fazer do jeito mais paia por enquanto
            if u < 0:
                u = -1
                pesos[0] = pesos[0] + learnRate * trainmatrix[x][0] * (d - u)
                pesos[1] = pesos[1] + learnRate * trainmatrix[x][1] * (d - u)
                limiar = limiar + learnRate * -1 * (d - u)

                print("corrigindo: ", pesos, ", ", limiar)

        a = len(trainmatrix)-1-x
        # print("at", a, ": ", trainmatrix[a])
        p
        if trainmatrix[a][2] == criterio[0]:
            #setosa, a
            d = -1
            u = trainmatrix[a][0] * pesos[0] + trainmatrix[a][1] * pesos[1] - 1 * limiar
            # print("u (s,a): ", u)
            # se diferente do esperado, atualiza
            if u > 0:
                u = 1
                pesos[0] = pesos[0] + learnRate * trainmatrix[a][0] * (d - u)
                pesos[1] = pesos[1] + learnRate * trainmatrix[a][1] * (d - u)
                limiar = limiar + learnRate * -1 * (d - u)

                print("corrigindo: ", pesos, ", ", limiar)

        elif trainmatrix[a][2] == criterio[1]:
            #versicolor, a
           # print(criterio[1], " and", pesos, ", ", limiar)
            d = 1
            u = trainmatrix[a][0] * pesos[0] + trainmatrix[a][1] * pesos[1] - 1 * limiar
            # print("u (v,a): ", u)

            # se diferente do esperado atualiza. Isso poderia ser organizado numa função, claro, mas vou fazer do jeito mais paia por enquanto
            if u < 0:
                u = -1
                pesos[0] = pesos[0] + learnRate * trainmatrix[a][0] * (d - u)
                pesos[1] = pesos[1] + learnRate * trainmatrix[a][1] * (d - u)
                limiar = limiar + learnRate * -1 * (d - u)

                print("corrigindo: ", pesos, ", ", limiar)

    pesos.append(limiar)
    print("pesos e limiar: ", pesos)
    return pesos


def test(teste1=[], pesos=[]):
    t = teste1
    # print(t)
    classe = breakMatrix(t)
    # print(pesos, "\n")
    limiar = pesos[2]
    pesos.pop(2)
    criterio = ['Iris-setosa', 'Iris-versicolor']
    score = 0

    for x in range(len(teste1)-1):
        # print(teste[x])
        u = teste1[x][0]*pesos[0]+teste1[x][1]*pesos[1]-limiar
        # print("u: ",u," at ", classe[x])
        if u < 0:
            if classe[x] == criterio[0]:
                score += 1
                # print(score)
        elif u > 0:
            if classe[x] == criterio[1]:
                score += 1
                # print(score)

    answer = score/len(teste1)

    print("SCORE", answer)

import matplotlib.pyplot as plt

def plotting(s, q=[]):
    ex = []
    why = []

    for x in range(len(q)-1):
        ex.append(float(q[x][0]))
        why.append(float(q[x][1]))

    plt.plot(ex, why)
    plt.xlabel('sepal length')
    plt.ylabel('petal length')
    plt.title(s)
    plt.show()



# -----------------------main------------------------

treinamento = []
teste = []
dados("iris.data.txt", 0.66, treinamento, teste)
p = []
p = train(treinamento)
print("-------------end train, test ---------------\n")
test(teste, p)
plotting("treinamento", treinamento)
plotting("teste", teste)

