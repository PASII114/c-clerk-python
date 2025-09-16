print("Guess where the joker card 🃏 is in the ♠️♥️♦️♣️pack♠️♥️♦️♣️ and win a prize")
print("You only have 5 attempts")

lvl1_position = 4
lvl2_position = 4
lvl3_position = 4
lvl4_position = 4

lvl1_attempt = 0
lvl2_attempt = 0
lvl3_attempt = 0
lvl4_attempt = 0

lvl1_max_attempt = 5
lvl2_max_attempt = 4
lvl3_max_attempt = 3
lvl4_max_attempt = 2

while lvl1_attempt < lvl1_max_attempt:
    print("1️⃣LEVEL 11️⃣ (Guess between 10 cards)")
    l1_input = int(input("Guess the position of the JOKER CARD: "))
    if l1_input > 10:
        print("There are only 10 cards in the first level. Please read the instructions again.")

    elif l1_input == lvl1_position:
        print("CONGRATULATIONS!!! YOU HAVE PASSED TO LEVEL 2")

        while lvl2_attempt < lvl2_max_attempt:
            print("2️⃣LEVEL 22️⃣ (Guess between 20 cards)")
            lvl2_input = int(input("Guess the position of the JOKER CARD: "))

            if lvl2_input > 20:
                print("There are only 20 cards in the first level. Please read the instructions again.")

            if lvl2_input == lvl2_position:
                print("CONGRATULATIONS!!! YOU HAVE PASSED TO LEVEL 3")

                while lvl3_attempt < lvl3_max_attempt:
                    print("3️⃣LEVEL 33️⃣ (Guess between 40 cards)")
                    lvl3_input = int(input("Guess the position of the JOKER CARD: "))
                    if lvl3_input > 40:
                        print("There are only 40 cards in the first level. Please read the instructions again.")

                    elif lvl3_input == lvl1_position:
                        print("CONGRATULATIONS!!! YOU HAVE PASSED TO LEVEL 4")

                        while lvl4_attempt < lvl4_max_attempt:
                            print("4️⃣LEVEL 44️⃣ (Guess between 20 cards)")
                            lvl4_input = int(input("Guess the position of the JOKER CARD: "))

                            if lvl4_input > 52:
                                print("There are only 52 cards in the first level. Please read the instructions again.")

                            if lvl4_input == lvl4_position:
                                print("CONGRATULATIONS!!! YOU HAVE WON THE BRAND NEW DECK OF CARDS")
                                exit()

                            else:
                                print("WOMP WOMP WOMP. Try again")
                                lvl4_attempt += 1

                        if lvl4_attempt == lvl4_max_attempt:
                            print("K.O")

                    else:
                        print("WOMP WOMP WOMP. Try again")
                        lvl3_attempt = lvl3_attempt + 1

                        if lvl3_attempt == lvl3_max_attempt:
                            print("K.O")

            else:
                print("WOMP WOMP WOMP. Try again")
                lvl2_attempt += 1

                if lvl2_attempt == lvl2_max_attempt:
                    print("K.O")

    else:
        print("WOMP WOMP WOMP. Try again")
        lvl1_attempt = lvl1_attempt + 1

        if lvl1_attempt == lvl1_max_attempt:
            print("K.O")