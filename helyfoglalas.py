while True:

    with open("helyek.txt", "r", encoding="utf-8") as f:
        tartalom = f.read().split()

    terem = [x for x in tartalom]

    for i in range(0, len(terem), 10):
        print(" ".join(terem[i:i+10]))

    foglalas = int(input("Melyik helyet szeretnéd lefoglalni: ")) - 1


    if foglalas >= 0 and foglalas < 30:

        if terem[foglalas] == "x":
            print("Ez a hely már foglalt, válassz másikat!")
            continue

        terem[foglalas] = "x"
        print("Hely lefoglalva!")

        for i in range(0, len(terem), 10):
            print(" ".join(terem[i:i+10]))

        with open("helyek.txt", "w", encoding="utf-8") as f:
            f.write(" ".join(terem))

        break

    else:
        print("Nincs ilyen hely, kérem válasszon másikat!")
        continue
