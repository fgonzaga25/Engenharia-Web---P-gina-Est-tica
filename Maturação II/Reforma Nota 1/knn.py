from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import numpy as np

# Gerar dados de exemplo
np.random.seed(42)
X = np.random.rand(100, 2)  # características
y = (X[:, 0] + X[:, 1] > 1).astype(int)  # rótulos (0 ou 1)

# Dividir dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar o modelo k-NN
knn_model = KNeighborsClassifier(n_neighbors=3)

# Treinar o modelo
knn_model.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
y_pred = knn_model.predict(X_test)

# Avaliar a acurácia do modelo
accuracy = accuracy_score(y_test, y_pred)
print(f'Acurácia: {accuracy:.2f}')

# Exibir relatório de classificação
print('Relatório de Classificação:')
print(classification_report(y_test, y_pred))