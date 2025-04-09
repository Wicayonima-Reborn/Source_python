import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
 
# Data sampel
X = np.array([[100, 2, 1], [150, 3, 2], [200, 3, 2.5], [120, 2, 1.5], [180, 3, 2.5],
            [250, 4, 3], [130, 2, 1.5], [220, 4, 2.5], [180, 3, 2], [200, 3, 2],
            [170, 3, 2], [160, 3, 1.5], [140, 2, 1.5], [210, 4, 2], [240, 4, 3],
            [190, 3, 2.5], [270, 4, 3], [230, 4, 2.5], [260, 5, 3], [280, 5, 3.5]])
 
y = np.array([300, 400, 500, 350, 450, 600, 320, 550, 470, 480,
            430, 380, 340, 490, 580, 460, 620, 570, 640, 680])
 
# Membagi data menjadi data latih dan data uji
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
 
# Membuat model Regresi Linear
model = LinearRegression()
 
# Melatih model
model.fit(X_train, y_train)
 
# Menguji model
predictions = model.predict(X_test)
 
 
 
# Evaluasi Model
# Menambahkan hasil prediksi dan harga asli ke dalam DataFrame
df = pd.DataFrame(X_test, columns=['Luas Tanah', 'Jumlah Kamar Tidur', 'Jumlah Kamar Mandi'])
df['Harga Asli'] = y_test
df['Prediksi Harga'] = predictions
df['Akurasi'] = 100 - (abs(predictions - y_test)/y_test)*100
 
# Menghitung akurasi
accuracy = r2_score(y_test, predictions)
print("Akurasi model:", round(accuracy, 2))
 
# Menampilkan DataFrame
df