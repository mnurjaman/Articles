import re


# Fungsi pencarian kata dalam artikel
def search_word(article, word):
    """
    Menghitung berapa kali suatu kata muncul dalam artikel menggunakan regular expressions (regex).

    Parameter:
        article (str): Teks artikel yang akan dicari.
        word (str): Kata yang ingin dicari dalam artikel.

    Mengembalikan:
        int: Jumlah kemunculan kata dalam artikel.
    """
    # Membuat pola regex untuk mencari kata secara lebih tepat, memperhatikan kata utuh
    pattern = r"\b" + re.escape(word.lower()) + r"\b"
    matches = re.findall(pattern, article.lower())
    return len(matches)


# Fungsi untuk mengganti kata dalam artikel
def replace_word(article, old_word, new_word):
    """
    Mengganti semua kemunculan kata tertentu dengan kata baru menggunakan regex,
    mempertahankan kapitalisasi asli kata yang diganti.

    Parameter:
        article (str): Teks artikel yang akan diubah.
        old_word (str): Kata yang ingin diganti.
        new_word (str): Kata pengganti yang akan menggantikan kata lama.

    Mengembalikan:
        str: Artikel yang telah dimodifikasi dengan kata yang diganti.
    """

    def replace(match):
        # Menangani penggantian kata dengan mempertahankan kapitalisasi
        word = match.group(0)
        if word.islower():
            return new_word.lower()
        elif word.istitle():
            return new_word.title()
        else:
            return new_word.upper()

    # Membuat pola regex untuk mengganti kata yang ditemukan dalam artikel
    pattern = r"\b" + re.escape(old_word) + r"\b"
    return re.sub(pattern, replace, article)


# Fungsi untuk mengurutkan kata-kata dalam artikel secara abjad
def sort_words(article):
    """
    Mengurutkan kata-kata dalam artikel secara abjad tanpa angka, menghilangkan duplikasi,
    dan menampilkan informasi jumlah kata yang terurut.

    Parameter:
        article (str): Teks artikel yang kata-katanya akan diurutkan.

    Mengembalikan:
        str: Daftar kata yang terurut dengan total kata yang ditemukan.
    """
    # Menemukan semua kata yang terdiri dari huruf (mengabaikan angka dan tanda baca)
    words = re.findall(r"\b[a-zA-Z]+\b", article.lower())

    # Mengurutkan kata dan menghilangkan duplikasi
    sorted_words = sorted(set(words))

    # Format output dengan penomoran dan kapitalisasi
    formatted_output = "\n".join(
        [f"{i+1}. {word.capitalize()}" for i, word in enumerate(sorted_words)]
    )
    total_words = len(sorted_words)

    return f"Total {total_words} kata:\n\n{formatted_output}"


# Fungsi untuk menampilkan menu program
def display_menu():
    """
    Menampilkan menu utama program yang memungkinkan pengguna memilih fitur yang diinginkan.
    """
    print("\n========== Program Artikel ==========")
    print("1. 🔍 Pencarian Kata")
    print("2. ✏️ Penggantian Kata")
    print("3. 🔠 Pengurutan Kata")
    print("4. ❌ Keluar")
    print("======================================")


# Fungsi utama untuk menjalankan program
def menu_program():
    """
    Menjalankan menu utama program, memungkinkan pengguna untuk memilih berbagai fitur.

    Fitur-fitur yang tersedia:
    - Pencarian kata dalam artikel
    - Penggantian kata dalam artikel
    - Pengurutan kata dalam artikel
    - Keluar dari program
    """
    global article  # Menggunakan artikel global agar dapat diubah selama eksekusi program
    while True:
        try:
            display_menu()  # Menampilkan menu utama
            choice = input(
                "Pilih menu (1/2/3/4): "
            ).strip()  # Meminta pilihan menu dari pengguna

            if choice == "1":
                # Fitur pencarian kata
                word = input("Masukkan kata yang ingin dicari: ").strip()
                count = search_word(article, word)
                print(f'Kata "{word}" ditemukan sebanyak {count} kali.')

            elif choice == "2":
                # Fitur penggantian kata
                old_word = input("Masukkan kata yang ingin diganti: ").strip()
                new_word = input("Masukkan kata pengganti: ").strip()
                article = replace_word(article, old_word, new_word)
                print("Artikel setelah penggantian kata:")
                print(article)

            elif choice == "3":
                # Fitur pengurutan kata
                sorted_words = sort_words(article)
                print("Kata-kata yang terurut secara abjad:")
                print(sorted_words)

            elif choice == "4":
                # Keluar dari program
                print("Terima kasih telah menggunakan Program Artikel. Sampai jumpa!")
                break  # Keluar dari program

            else:
                # Pilihan menu tidak valid
                print("Pilihan tidak valid. Silakan coba lagi.")

        except Exception as e:
            # Menangani kesalahan jika terjadi error selama eksekusi
            print(f"Terjadi kesalahan: {e}")


# Program utama dimulai disini
if __name__ == "__main__":
    # Masukkan artikel yang akan diubah di bawah ini
    article = """
    Dalam kehidupan suatu negara, pendidikan memegang peranan yang amat penting untuk menjamin kelangsungan hidup negara dan bangsa, karena pendidikan merupakan wahana untuk meningkatkan dan mengembangkan kualitas sumber daya manusia. Seiring dengan perkembangan teknologi komputer dan teknologi informasi, sekolah-sekolah di Indonesia sudah waktunya mengembangkan Sistem Informasi manajemennya agar mampu mengikuti perubahan jaman.
SISKO mampu memberikan kemudahan pihak pengelola menjalankan kegiatannya dan meningkatkan kredibilitas dan akuntabilitas sekolah dimata siswa,
orang tua siswa, dan masyakat umumnya.Penerapan teknologi informasi untuk menunjang proses pendidikan telah menjadi kebutuhan bagi lembaga pendidikan di
Indonesia. Pemanfaatan teknologi informasi ini sangat dibutuhkan untuk meningkatkan efisiensi dan produktivitas bagi manajemen pendidikan. Keberhasilan
dalam peningkatan efisiensi dan produktivitas bagi manajemen pendidikan akan ikut menentukan kelangsungan hidup lembaga pendidikan itu sendiri. Dengan kata lain
menunda penerapan teknologi informasi dalam lembaga pendidikan berarti menunda kelancaran pendidikan dalam menghadapi persaingan global. Pemanfaatan teknologi informasi diperuntukkan bagi peningkatan kinerja
lembaga pendidikan dalam upayanya meningkatkan kualitas Sumber Daya Manusia Indonesia. Guru dan pengurus sekolah tidak lagi disibukkan oleh pekerjaan-pekerjaan operasional, yang sesungguhnya dapat digantikan oleh komputer. Dengan demikian
dapat memberikan keuntungan dalam efisien waktu dan tenaga. Penghematan waktu dan kecepatan penyajian informasi akibat penerapan
teknologi informasi tersebut akan memberikan kesempatan kepada guru dan pengurus sekolah untuk meningkatkan kualitas komunikasi dan pembinaan kepada siswa.
Dengan demikian siswa akan merasa lebih dimanusiakan dalam upaya mengembangkan kepribadian dan pengetahuannya. Sebagai contoh yang paling utama adalah sistem penjadwalan yang harus dilakukan setiap awal semester. Biasanya membutuhkan waktu lama untuk menyusun penjadwalan, Dengan SISKO dapat selesai dalam waktu singkat. Untuk
mempermudah bagian administrasi kurikulum sekolah, SISKO menyediakan fasilitas istimewa yang merupakan inti dari sistem kurikulum sekolah yaitu membantu dalam
pembuatan penjadwalan mata pelajaran sekolah yang dapat diproses tidak lebih lama dari 10 menit. Administrator hanya akan memasukkan kondisi dari masing-masing guru yang akan mengajar baik itu dalam 1 minggu seorang guru dapat mengajar berapa
jam, selain itu dapat juga melakukan pemesanan tempat dan penempatan hari libur masing-masing guru dalam 1 minggu masa mengajar. Setelah semua kondisi dimasukkan, sistem akan memproses semua data tersebut sehingga menghasilkan jadwal yang optimal dan dapat langsung dipakai karena sistem akan mendeteksi
sehingga tidak akan ada jadwal yang bertumpukan satu dengan yang lainnya. Setelah semua kondisi dimasukkan, sistem akan memproses semua data
tersebut sehingga menghasilkan jadwal yang optimal dan dapat langsung dipakai karena sistem akan mendeteksi sehingga tidak akan ada jadwal yang bertumpukan satu
dengan yang lainnya. Setelah permasalahan penjadwalan dapat ditangani dengan baik, hal yang tidak kalah pentingnya adalah memasukkan data siswa. Program SISKO telah menyediakan fasilitas untuk penanganan penilaian
siswa yang secara langsung memasukkan nilai ke dalam raport dan siap dicetak. Untuk sistem penilaian siswa, yang dapat melakukan pengisian hanya Guru yang mengajar
mata pelajaran. Sistem penilaian telah disesuaikan dengan KBK sehingga masing-masing guru dapat memasukkan deskripsi narasi dari mata pelajaran. Untuk menampilkan data penilaian dapat disesuaikan kembali dengan kebijaksanaan dari
masing-masing lembaga pendidikan apakah ingin menampilkan data nilai akhir siswa maupun menampilkan data nilai siswa setiap kali mengadakan test ataupun tugas tertentu.
Selain Modul untuk penjadwalan dan Modul Penilaian siswa, SISKO juga memberikan fasilitas untuk bagian administrasi keuangan sekolah dalam hal
pembayaran SPP siswa. Bagian administrasi dapat langsung mengecek siapa siswa yang mempunyai tunggakan SPP dan untuk detail histori pembayaran SPP dari
masing-masing siswa dapat dicetak seperti mencetak buku tabungan di bank sehingga mempermudah pekerjaan pihak administrasi keuangan. Administrasi keuangan dapat langsung melakukan pengaturan data pembayaran masing-masing siswa sesuai dengan kebutuhan dan dapat diubah sewaktu-waktu apabila ada kenaikan pembayaran
SPP. Apabila siswa tersebut akan melakukan pembayaran, petugas dapat langsung memasukkan data. Hal sama juga dapat dilakukan untuk Data pembayaran Sumbangan Sukarela dan Tabungan Karyawisata.
    """
    menu_program()  # Memulai program
