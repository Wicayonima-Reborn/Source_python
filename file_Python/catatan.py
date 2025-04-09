import json

file_name = "catatan.json"

def load_catatan():
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return[]

def save_catatan(catatan):
    with open(file_name, 'w') as file:
        return json.dump(catatan, file, indent=4)
    
def tambah_catatan():
    judul = input("Masukkan Judul Catatan: ")
    isi = input('Masukkan Isi Catatan: ')
    data = load_catatan()
    new_note = {
        'id' : len(data) + 1,
        'judul' : judul,
        'isi' : isi
    }
    data.append(new_note)
    save_catatan(data)
    print('')

def lihat_catatan():
    data = load_catatan()
    if not data:
        return
    for note in data:
        print(f"{note['id']}. {note['judul']} - {note['isi']}")



def menu():
    while True:
        print("\n--- Aplikasi Catatan ---")
        print("1. Lihat Catatan")
        print("2. Tambah Catatan")
        print("3. Hapus Catatan")
        print("4. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            lihat_catatan()
        elif pilihan == "2":
            tambah_catatan()
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid!")
menu()