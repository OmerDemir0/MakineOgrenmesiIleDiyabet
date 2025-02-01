import tkinter as tk
from tkinter import messagebox
import pandas as pd
import pickle
import random as rn


model = pickle.load(open('diabets.sav', 'rb'))
root = tk.Tk()
root.title("Diyabet Tahmin")
root.geometry("650x650+500+75")



# Diyet listesini gösterme fonksiyonu
def diyet_listesini_goster():
    diyet_penceresi = tk.Toplevel(root)
    diyet_penceresi.geometry("350x425+375+115")
    diyet_penceresi.title("Diyet Listesi")

    # Diyet listesinden rastgele birini seç
    diyet = rn.choice(diyet_listeleri)

    # Diyet listesini pencerede göster
    for öğün, yiyecekler in diyet.items():
        tk.Label(diyet_penceresi, text=f"{öğün}:").pack(anchor='w')
        for yiyecek in yiyecekler:
            tk.Label(diyet_penceresi, text=f"  - {yiyecek}").pack(anchor='w')
        tk.Label(diyet_penceresi, text="").pack(anchor='w')


def predict():
    try:
        # Girdi verileri alınır
        pregnancies = int(entry_pregnancies.get())
        glucose = float(entry_glucose.get())
        blood_pressure = float(entry_blood_pressure.get())
        skin_thickness = float(entry_skin_thickness.get())
        insulin = float(entry_insulin.get())
        height = float(entry_height.get())
        weight = float(entry_weight.get())
        diabetes_pedigree_function = float(entry_diabetes_pedigree_function.get())
        age = int(entry_age.get())

        # BMI hesaplanır
        bmi = weight / ((height / 100) ** 2)

        # Veri DataFrame'e dönüştürülür
        input_data = pd.DataFrame([[glucose, bmi, age, pregnancies , skin_thickness, 
                                        insulin, diabetes_pedigree_function, blood_pressure]],
                                  columns=["Glucose" , "BMI", "Age", "Pregnancies", "SkinThickness",
                                        "Insulin", "DiabetesPedigreeFunction", "BloodPressure"])

        # Modelin tahmini yapılır
        prediction = model.predict(input_data)

        # Tahmin sonucuna göre mesaj kutusu oluşturulur
        result = "Diyabet Pozitif" if prediction[0] == 1 else "Diyabet Negatif"
        messagebox.showinfo("Tahmin Sonucu", result)

        # Eğer tahmin pozitifse diyet listesi gösterilir
        if prediction[0] == 1:
            diyet_listesini_goster()

    except Exception as e:
        # Hata durumunda hata mesajı gösterilir
        messagebox.showerror("Error", str(e))



labels = ["Glikoz", "Boy","Kilo", "Yaş", "Gebelikler", "Cilt Kalınlığı", "İnsülin", "Diyabet Soy Ağacı Fonksiyonu", "Kan Basıncı"]
entries = []

# Ana çerçeve oluşturma ve sayfada ortalamak
frame = tk.Frame(root)
frame.pack(pady=20)  # Dikey boşluk ekleyerek çerçeveyi sayfanın ortasına hizalama

for label in labels:
    # Etiketleri oluşturma ve yerleştirme
    tk.Label(frame, text=label).pack(padx=5, pady=(5, 0), anchor="w")

    # Giriş alanlarını oluşturma ve yerleştirme
    entry = tk.Entry(frame)
    entry.pack(padx=5, pady=(0, 10), anchor="w")

    # Giriş alanlarını listeye ekleme
    entries.append(entry)

# Predict butonunu ekleyerek çerçeveyi doldurma
tk.Button(root, text="Tahmin Et", command=predict).pack(pady=10)

entry_glucose, entry_height, entry_weight, entry_age, entry_pregnancies, entry_skin_thickness, entry_insulin,  entry_diabetes_pedigree_function,  entry_blood_pressure   = entries






diyet_listeleri = [
    {
        "Kahvaltı": ["Yulaf ezmesi", "Taze meyve", "Yağsız yoğurt"],
        "Ögle Yemegi": ["Izgara tavuk", "Tam buğday ekmeği", "Yeşil salata"],
        "Akşam Yemeği": ["Somon balığı", "Kinoa", "Buharda pişmiş sebzeler"],
        "Ara Ögünler": ["Badem", "Elma dilimleri", "Humus"]
    },
    {
        "Kahvaltı": ["Tam buğday ekmeği üzerine avokado", "Haşlanmış yumurta", "Yeşil çay"],
        "Ögle Yemegi": ["Hindi göğsü", "Kinoa salatası", "Yoğurt"],
        "Akşam Yemeği": ["Izgara sebzeler", "Kepekli makarna", "Izgara tavuk"],
        "Ara Ögünler": ["Chia pudingi", "Böğürtlen", "Badem"]
    },
    {
        "Kahvaltı": ["Chia tohumu ve badem sütü karışımı", "Muz", "Yeşil çay"],
        "Ögle Yemegi": ["Izgara balık", "Bulgur pilavı", "Salata"],
        "Akşam Yemeği": ["Tavuk fajita", "Esmer pirinç", "Izgara sebzeler"],
        "Ara Ögünler": ["Havuç dilimleri", "Ceviz", "Yoğurt"]
    },
    {
        "Kahvaltı": ["Tam tahıllı tost", "Yer fıstığı ezmesi", "Taze meyve"],
        "Ögle Yemegi": ["Nohutlu salata", "Esmer pirinç", "Tavuk göğsü"],
        "Akşam Yemeği": ["Sebzeli omlet", "Yeşil salata", "Tam buğday ekmeği"],
        "Ara Ögünler": ["Yaban mersini", "Fındık", "Yoğurt"]
    },
    {
        "Kahvaltı": ["Kepekli simit", "Az yağlı peynir", "Domates, salatalık"],
        "Ögle Yemegi": ["Mercimek çorbası", "Izgara köfte", "Tam buğday ekmeği"],
        "Akşam Yemeği": ["Sebzeli makarna", "Izgara hindi", "Yeşil salata"],
        "Ara Ögünler": ["Badem sütü", "Kuru üzüm", "Elma"]
    }
]

root.mainloop()