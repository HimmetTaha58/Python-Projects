import random


def kart_cek(deste):
    random_card = random.choice(deste)
    deste.remove(random_card)
    return random_card


def kart_deste_oluştur():
    suits = ['♥', '♠', '♦', '♣']
    cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    all_cards = [(suit, card) for suit in suits for card in cards]
    return all_cards


def kart_degeri(kart):
    """Kart değerini sayısal olarak döndürür."""
    if kart[1] == "Ace":
        return 1
    elif kart[1] in ["J", "Q", "K"]:
        return 10
    else:
        return int(kart[1])


def set_kontrol_ve_indir(player_hands):
    kart_sayilari = {}
    for kart in player_hands:
        kart_degeri = kart[1]
        if kart_degeri in kart_sayilari:
            kart_sayilari[kart_degeri] += 1
        else:
            kart_sayilari[kart_degeri] = 1

    setler = []
    for kart_degeri, adet in kart_sayilari.items():
        if adet >= 3:
            set = [kart for kart in player_hands if kart[1] == kart_degeri][:3]
            setler.append(set)

    if not setler:
        print("Herhangi bir setiniz yok")
    else:
        for set in setler:
            for kart in set:
                player_hands.remove(kart)
            print(f"Set indirildi: {set}")

    seriler = []
    suits = ['♥', '♠', '♦', '♣']
    for suit in suits:
        suit_kartlar = sorted([kart for kart in player_hands if kart[0] == suit], key=lambda x: kart_degeri(x))
        seri = []
        for kart in suit_kartlar:
            if not seri or kart_degeri(kart) == kart_degeri(seri[-1]) + 1:
                seri.append(kart)
            else:
                if len(seri) >= 3:
                    seriler.append(seri)
                seri = [kart]
        if len(seri) >= 3:
            seriler.append(seri)

    if not seriler:
        print("Herhangi bir seriniz yok")
    else:
        for seri in seriler:
            for kart in seri:
                player_hands.remove(kart)
            print(f"Seri indirildi: {seri}")

    return player_hands, setler, seriler


def oyuncu_oyna(player_num, player_hands, atilan_kartlar, deste):
    print(f"Oyuncu {player_num}'nin eli:")
    print([f"{kart[0]}{kart[1]}" for kart in player_hands])

    user_choice = input("(1) Desteden mi yoksa (2) Atılmış kart destesinden mi kart çekeceksiniz? ")
    if user_choice.isdigit():
        num = int(user_choice)
        if num == 1:
            kart = kart_cek(deste)
            print(f"Çektiğiniz kart: {kart}")
            player_hands.append(kart)
            print("Güncellenen eliniz:")
            print([f"{kart[0]}{kart[1]}" for kart in player_hands])
        elif num == 2:
            if len(atilan_kartlar) == 0:
                print("\nHenüz herhangi bir kart atılmamış\n")
                return player_hands, atilan_kartlar
            else:
                kart = atilan_kartlar.pop()
                player_hands.append(kart)
                print("Güncellenen eliniz:")
                print([f"{kart[0]}{kart[1]}" for kart in player_hands])
        else:
            print("\nGeçerli bir numara girin\n")
            return player_hands, atilan_kartlar

        set_seri = input("Herhangi bir set ya da seri koymak ister misiniz (e / h): ")
        if set_seri.lower() == "e":
            player_hands, setler, seriler = set_kontrol_ve_indir(player_hands)
            print("Güncellenen eliniz:")
            print([f"{kart[0]}{kart[1]}" for kart in player_hands])

        kart_index = int(input("Bir kart atın (Atmak istediğiniz kartın sırasını girin): "))  # Sayı olma hata kontrolü
        if 1 <= kart_index <= len(player_hands):
            atilan_kart = player_hands[kart_index - 1]
            atilan_kartlar.append(atilan_kart)
            player_hands.remove(atilan_kart)
            print(f"\nKart {''.join(atilan_kart)} atılan kartlar listesine eklendi\n")
        else:
            print("\nGeçerli bir kart sırası girin\n")
    else:
        print("\nBir numara girin\n")

    return player_hands, atilan_kartlar


def kazanan_belirle(player1_hands, player2_hands):
    def el_puan_hesapla(hands):
        """Bir oyuncunun elindeki kartların puanını hesaplar."""
        return sum(kart_degeri(kart) for kart in hands)

    player1_puan = el_puan_hesapla(player1_hands)
    player2_puan = el_puan_hesapla(player2_hands)

    print(f"Oyuncu 1'in puanı: {player1_puan}")
    print(f"Oyuncu 2'nin puanı: {player2_puan}")

    if player1_puan < player2_puan:
        print("Oyun bitti. Oyuncu 1 kazandı!")
    elif player1_puan > player2_puan:
        print("Oyun bitti. Oyuncu 2 kazandı!")
    else:
        print("Oyun bitti. Beraberlik!")


# Oyun döngüsü
while True:
    deste = kart_deste_oluştur()
    atilan_kartlar = []

    player1_hands = [kart_cek(deste) for _ in range(10)]
    player2_hands = [kart_cek(deste) for _ in range(10)]

    oyun_bitti = False

    while not oyun_bitti:
        player1_hands, atilan_kartlar = oyuncu_oyna(1, player1_hands, atilan_kartlar, deste)
        if len(player1_hands) == 0:
            print("Oyuncu 1 oyunu bitirdi!")
            oyun_bitti = True
            continue

        player2_hands, atilan_kartlar = oyuncu_oyna(2, player2_hands, atilan_kartlar, deste)
        if len(player2_hands) == 0:
            print("Oyuncu 2 oyunu bitirdi!")
            oyun_bitti = True

    kazanan_belirle(player1_hands, player2_hands)

    devam = input("Başka bir oyun oynamak ister misiniz? (e / h): ")
    if devam.lower() != 'e':
        break
