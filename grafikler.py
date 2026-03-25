import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# 1. Veriyi Oku
# data.csv dosyasını hafızaya alıyoruz
try:
    df = pd.read_csv('data.csv')
except FileNotFoundError:
    print("Hata: 'data.csv' dosyası bulunamadı. Lütfen önce veri üretici scriptini çalıştırın.")
    exit()

print("Veri başarıyla yüklendi. Grafikler hazırlanıyor...\n")

# ==========================================================
# 1. SEABORN: HİSTOGRAM (Çan Eğrisi)
# ==========================================================
plt.figure(figsize=(10, 6))

# Daha şık bir arka plan stili belirleyelim
sns.set_theme(style="whitegrid")

# histplot: Hem histogram kutularını (bins) hem de yoğunluk eğrisini (kde) çizer
sns.histplot(data=df, x='Calisma_Suresi', kde=True, color='mediumorchid', bins=20, edgecolor='white')

plt.title('Öğrencilerin Çalışma Süresi Dağılımı\n(Normal Dağılım / Çan Eğrisi)', fontsize=15, fontweight='bold')
plt.xlabel('Çalışma Süresi (Saat)', fontsize=12)
plt.ylabel('Öğrenci Sayısı', fontsize=12)

# Grafiği görsel olarak kaydet
seo_filename_1 = 'histogram_can_egrisi.png'
plt.savefig(seo_filename_1, dpi=300, bbox_inches='tight')
print(f"✅ [1. SEÇENEK] Seaborn Histogram Grafiği '{seo_filename_1}' olarak kaydedildi.")
plt.close() # Diğer grafikle çakışmaması için bellekteki resmi temizle


# ==========================================================
# 2. PLOTLY: İNTERAKTİF 3 BOYUTLU GRAFİK
# ==========================================================
# 3D Uzay için Eksenler: X=Çalışma Süresi, Y=Sınav Puanı, Z=Öğrenci ID
# Aynı zamanda noktaların rengini puanlarına göre renklendiriyoruz ki harika görünsün.
fig = px.scatter_3d(
    df, 
    x='Calisma_Suresi', 
    y='Sinav_Puani', 
    z='ID',
    color='Sinav_Puani', # Yüksek alanlar farklı, düşük alanlar farklı renk olacak
    color_continuous_scale=px.colors.sequential.Plasma, # Güzel ve modern bir palet
    opacity=0.8, # Noktaların hafif şeffaf olması iç içe geçtiklerinde güzel durur
    title='Etkileşimli 3 Boyutlu Veri Uzayı (Fareyle Çevirebilirsiniz)'
)

# Etkileşimli özellikleri (zoom, pan, hover) barındıran HTML dosyası olarak kaydet
seo_filename_2 = 'interaktif_3d.html'
fig.write_html(seo_filename_2)
print(f"✅ [3. SEÇENEK] Plotly 3D Etkileşimli Grafik '{seo_filename_2}' olarak HTML formatında kaydedildi.")
print(f"   -> Bu HTML dosyasını çift tıklayarak Google Chrome/Safari gibi bir tarayıcıda açabilirsiniz!")
