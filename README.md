# Video Birleştirici

Bu Python projesi, iki MP4 formatındaki videoyu birleştirmenizi sağlayan basit bir Tkinter tabanlı GUI uygulamasıdır. Proje, videoları birleştirmek için `moviepy` kütüphanesini kullanır.

## Özellikler

- İki MP4 video dosyasını seçme.
- Videoları ardışık olarak birleştirme.
- Birleştirilmiş videoyu otomatik olarak belirlenen klasöre kaydetme.

## Gereksinimler

- Python 3.x
- `moviepy` kütüphanesi
- `tkinter` kütüphanesi (Python'un standart kütüphanesi içinde gelir)

## Kurulum

1. Projeyi klonlayın veya indirin:

    ```bash
    git clone https://github.com/kullaniciadi/video-birlestirici.git
    cd video-birlestirici
    ```

2. Gerekli Python paketlerini yükleyin:

    ```bash
    pip install moviepy
    ```

## Kullanım

1. Python scriptini çalıştırın:

    ```bash
    python video_birlestirici.py
    ```

2. Uygulama açıldığında, "1. Videoyu Seç" butonuna tıklayarak ilk videoyu seçin.
3. "2. Videoyu Seç" butonuna tıklayarak ikinci videoyu seçin.
4. "Videoları Birleştir" butonuna tıklayın ve videoların birleştirilmesini bekleyin.
5. Birleştirilmiş video, proje dizininde `Birlesmis_Videolar` klasörü içinde `birlesmis_video.mp4` olarak kaydedilecektir.


## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakabilirsiniz.
