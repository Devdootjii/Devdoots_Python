# 1. Custom Error Banaya
class LowKDRatioError(Exception):
    def __init__(self, message):
        super().__init__(message)

# 2. Player ka Blueprint
class Player:
    def __init__(self, name, kd_ratio):
        self.name = name
        self.kd_ratio = kd_ratio

# 3. Main Team Manager Class
class EsportsTeam:
    def __init__(self, team_name):
        self.team_name = team_name
        self.roster = [] # Select hue players is list mein aayenge

    # Player ko team mein lene ka logic
    def recruit_player(self, player):
        try:
            # Agar KD 2.5 se kam hai, toh jaan-boojh kar error feko
            if player.kd_ratio < 2.5:
                raise LowKDRatioError(f"Rejected: {player.name} ka KD sirf {player.kd_ratio} hai. Minimum 2.5 chahiye!")
            
            # Agar error nahi aaya, toh player ko list mein add kar do
            self.roster.append(player)
            print(f"Success: {player.name} ko team mein le liya gaya hai! (KD: {player.kd_ratio})")
            
        except LowKDRatioError as e:
            # Custom error ko yahan pakda aur print kiya
            print(e)

    # Final team ko text file mein save karna
    def save_team(self):
        with open("team_roster.txt", "w") as file:
            file.write(f"--- {self.team_name} Official Roster ---\n")
            for p in self.roster:
                file.write(f"Player: {p.name} | KD: {p.kd_ratio}\n")
        print("\nTeam data 'team_roster.txt' mein save ho gaya hai!")

# --- 4. Main Program (Testing) ---
if __name__ == "__main__":
    # Nayi team banayi
    devdoots_squad = EsportsTeam("Devdoots Gaming")

    # 3 Players ke objects banaye
    p1 = Player("Balram", 3.2)
    p2 = Player("Ritesh", 1.8)  # Iska KD kam hai, yeh reject hoga
    p3 = Player("Divyansh", 2.9)

    print("--- Recruitment Shuru ---")
    
    # Trial shuru
    devdoots_squad.recruit_player(p1)
    devdoots_squad.recruit_player(p2)
    devdoots_squad.recruit_player(p3)

    # Data file mein save karo
    devdoots_squad.save_team()