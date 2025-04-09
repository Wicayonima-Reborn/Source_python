def wish_list():
    belanja=[]

    while True:
        item=input("wish list\t:")
        belanja.append(item)
        print(f"[{item}] telah dimasukin")

        while True:
            Terus = input("\nAdakah barang lain?\t:")
            if Terus == 'y':
                break
            elif Terus == 'n':
                print("\nWish list akhir")
                for i, barang in enumerate(belanja, start=1):
                    print(f"{i}.{barang}")
                return
            else:
                print("Yang dimasukin tidak valid")

wish_list()    