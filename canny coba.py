import cv2

def main():
    # Membuka kamera (biasanya kamera default menggunakan indeks 0)
    cap = cv2.VideoCapture(0)

    # Memeriksa apakah kamera berhasil dibuka
    if not cap.isOpened():
        print("Error: Tidak dapat mengakses kamera.")
        return

    while True:
        # Membaca frame dari kamera
        ret, frame = cap.read()
        if not ret:
            print("Error: Tidak dapat membaca frame dari kamera.")
            break

        # Konversi frame ke grayscale untuk edge detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Penerapan algoritma Canny Edge Detection
        edges = cv2.Canny(gray, 100, 200)

        # Menampilkan frame asli dan hasil edge detection
        cv2.imshow('Original Frame', frame)
        cv2.imshow('Canny Edge Detection', edges)

        # Keluar dari loop jika tombol 'q' ditekan
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Melepaskan kamera dan menutup semua jendela
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()