import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Rastgelelik için seed belirleme (opsiyonel, sonuçların tekrarlanabilir olması için)
np.random.seed(42)

# 2. Veri seti boyutu
num_rows = 500

# 3. ID Sütunu (1'den 500'e kadar)
ids = np.arange(1, num_rows + 1)

# 4. Çalışma Süresi Sütunu (0 ile 10 saat arası, normal dağılım)
# Ortalama 5 saat, standart sapma 2.5 saat olsun.
calisma_suresi = np.random.normal(loc=5.0, scale=2.5, size=num_rows)
# Süreleri 0 ile 10 arasında sınırlandırıyoruz (0'dan küçük veya 10'dan büyük olamaz)
calisma_suresi = np.clip(calisma_suresi, 0, 10)
# Daha gerçekçi olması için 2 ondalık basamağa yuvarlayalım
calisma_suresi = np.round(calisma_suresi, 2)

# 5. Sınav Puanı Sütunu (0 ile 100 arası, çalışma süresi ile ilişkili)
# Temel puan: çalışma süresinin bir katı (örneğin her saat için ortalama 8 puan katkısı) ve başlangıç puanı (örneğin 25)
# Formül: Puan = 25 + (8 * Calisma_Suresi) + Rastgele Sapma (Gürültü)
# Sapma (gürültü) puanların dümdüz bir çizgi olmasını engeller, gerçek hayattaki gibi dağılım sağlar.
gurultu = np.random.normal(loc=0.0, scale=8.0, size=num_rows)
sinav_puani = 25 + (8 * calisma_suresi) + gurultu

# Puanları 0 ile 100 arasında sınırlandıralım
sinav_puani = np.clip(sinav_puani, 0, 100)
# Notlar genellikle tam sayıdır, tam sayıya çevirelim
sinav_puani = np.round(sinav_puani).astype(int)

# 6. Veri Setini (DataFrame) Oluşturma
df = pd.DataFrame({
    'ID': ids,
    'Calisma_Suresi': calisma_suresi,
    'Sinav_Puani': sinav_puani
})

# 7. CSV Dosyasına Kaydetme
csv_filename = 'data.csv'
df.to_csv(csv_filename, index=False)
print(f"Veriler '{csv_filename}' adlı dosyaya başarıyla kaydedildi.")

# 8. Scatter Plot (Dağılım Grafiği) Oluşturma
plt.figure(figsize=(10, 6)) # Grafiğin boyutlarını ayarla
plt.scatter(df['Calisma_Suresi'], df['Sinav_Puani'], color='royalblue', alpha=0.7, edgecolors='w', s=50)

# Grafik başlıkları ve etiketleri
plt.title('Çalışma Süresi ve Sınav Puanı İlişkisi', fontsize=14, fontweight='bold')
plt.xlabel('Çalışma Süresi (Saat)', fontsize=12)
plt.ylabel('Sınav Puanı (0-100)', fontsize=12)

# Izgara (grid) ekleme
plt.grid(True, linestyle='--', alpha=0.6)

# 9. Grafiği PNG olarak Kaydetme
plot_filename = 'iliski.png'
plt.savefig(plot_filename, dpi=300, bbox_inches='tight') # Yüksek çözünürlükte (300 dpi) kaydet
print(f"Grafik '{plot_filename}' adlı dosyaya başarıyla kaydedildi.")
