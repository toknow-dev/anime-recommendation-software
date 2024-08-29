print("Welcome to the Anime Recommendation software Ver 0,01. Please answer the following questions.")

# Recommendation Variables

anime_genre = ["action", "adventure", "comedy", "drama", "slice_of_life",
                "fantasy", "magic", "supernatural", "horror", "mystery",
                "psychological", "romance", "sci-fi"]

anime_length = ["short", "medium", "long"]

# Recommendation Genre

action = [
    "\nAttack on Titan (87 episodes, ongoing)",
    "\nOne Punch Man (24 episodes + 1 OVA)",
    "\nMy Hero Academia (138 episodes, ongoing)",
    "\nDemon Slayer (55 episodes, ongoing)",
    "\nFullmetal Alchemist: Brotherhood (64 episodes)"
]

adventure = [
    "\nHunter x Hunter (2011) (148 episodes)",
    "\nOne Piece (1076 episodes, ongoing)",
    "\nMade in Abyss (25 episodes + 2 movies)",
    "\nJoJo's Bizarre Adventure (190 episodes, ongoing)",
    "\nSword Art Online (96 episodes)"
]

comedy = [
    "\nKonoSuba: God's Blessing on This Wonderful World! (20 episodes + 2 OVAs + 1 movie)",
    "\nNichijou (My Ordinary Life) (26 episodes)",
    "\nThe Disastrous Life of Saiki K. (120 episodes, 5–7 minutes each)",
    "\nGintama (367 episodes)",
    "\nGrand Blue (12 episodes)"
]

drama = [
    "\nClannad: After Story (24 episodes)",
    "\nYour Lie in April (22 episodes)",
    "\nAnohana: The Flower We Saw That Day (11 episodes)",
    "\nMarch Comes in Like a Lion (44 episodes)",
    "\nBanana Fish (24 episodes)"
]

slice_of_life = [
    "\nBarakamon (12 episodes)",
    "\nNatsume's Book of Friends (74 episodes, ongoing)",
    "\nLaid-Back Camp (25 episodes)",
    "\nHyouka (22 episodes)",
    "\nNon Non Biyori (36 episodes + 2 movies)"
]

fantasy = [
    "\nRe:Zero - Starting Life in Another World (50 episodes)",
    "\nThat Time I Got Reincarnated as a Slime (50 episodes)",
    "\nThe Rising of the Shield Hero (38 episodes, ongoing)",
    "\nThe Ancient Magus' Bride (36 episodes, ongoing)",
    "\nBlack Clover (170 episodes)"
]

magic = [
    "\nLittle Witch Academia (25 episodes)",
    "\nCardcaptor Sakura (70 episodes + 3 movies)",
    "\nPuella Magi Madoka Magica (12 episodes + 3 movies)",
    "\nFate/stay night: Unlimited Blade Works (26 episodes)",
    "\nThe Irregular at Magic High School (39 episodes + 1 movie)"
]

supernatural = [
    "\nDeath Note (37 episodes)",
    "\nNoragami (25 episodes + 4 OVAs)",
    "\nMob Psycho 100 (37 episodes)",
    "\nBlue Exorcist (37 episodes + 2 OVAs)",
    "\nD.Gray-man (116 episodes)"
]

horror = [
    "\nAnother (12 episodes)",
    "\nParanoia Agent (13 episodes)",
    "\nHigurashi: When They Cry (50 episodes)",
    "\nTokyo Ghoul (48 episodes)",
    "\nElfen Lied (13 episodes + 1 OVA)"
]

mystery = [
    "\nSteins;Gate (24 episodes + 1 OVA + 1 movie)",
    "\nErased (12 episodes)",
    "\nDeath Parade (12 episodes)",
    "\nThe Promised Neverland (23 episodes)",
    "\nSerial Experiments Lain (13 episodes)"
]

psychological = [
    "\nPsycho-Pass (41 episodes)",
    "\nParanoia Agent (13 episodes)",
    "\nErased (12 episodes)",
    "\nThe Tatami Galaxy (11 episodes)",
    "\nMonster (74 episodes)"
]

romance = [
    "\nToradora! (25 episodes)",
    "\nYour Lie in April (22 episodes)",
    "\nFruits Basket (2019) (63 episodes)",
    "\nClannad: After Story (24 episodes)",
    "\nNodame Cantabile (47 episodes)"
]

sci_fi = [
    "\nCowboy Bebop (26 episodes)",
    "\nSteins;Gate (24 episodes + 1 OVA + 1 movie)",
    "\nPsycho-Pass (41 episodes)",
    "\nGhost in the Shell: Stand Alone Complex (52 episodes)",
    "\nCode Geass: Lelouch of the Rebellion (50 episodes)"
]

# Inputs

name = str(input("\nWhat is your name: "))

age = int(input("\nWhat is your age: "))

genre = str(input(f"\nWhich of these genre are you most interested in {anime_genre}: "))

# length = str(input(f"What length would you prefer {anime_length}: "))

answer = input("Do you want to see your anime recommendations (yes or no): ")

if answer == "yes":
    if genre == "action":
        for anime in action:
            print(anime)
    elif genre == "adventure":
        for anime in adventure:
            print(anime)
    elif genre == "comedy":
        for anime in comedy:
            print(anime)
    elif genre == "drama":
        for anime in drama:
            print(anime)
    elif genre == "slice_of_life":
        for anime in slice_of_life:
            print(anime)
    elif genre == "fantasy":
        for anime in fantasy:
            print(anime)
    elif genre == "magic":
        for anime in magic:
            print(anime)
    elif genre == "supernatural":
        for anime in supernatural:
            print(anime)
    elif genre == "horror":
        for anime in horror:
            print(anime)
    elif genre == "mystery":
        for anime in mystery:
            print(anime)
    elif genre == "psychological":
        for anime in psychological:
            print(anime)
    elif genre == "romance":
        for anime in romance:
            print(anime)
    elif genre == "sci-fi":
        for anime in sci_fi:
            print(anime)
else:
    print("Program is shutting down.")

print(f"\nThank you {name.title()} for using Anime Recommendation software Ver 0,01")