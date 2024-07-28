import os
import json
import csv

json_dir = "./data/t20s_json/"

match_data_list = []

world_cup_teams = [
    "Australia",
    "India",
    "England",
    "New Zealand",
    "Pakistan",
    "South Africa",
    "West Indies",
    "Sri Lanka",
    "Bangladesh",
    "Afghanistan",
    "Uganda",
    "Ireland",
    "Scotland",
    "Netherlands",
    "Namibia",
    "United States of America",
    "Nepal",
    "Canada",
    "Oman",
    "Papua New Guinea",
]
home_teams = {
    "United States of America": ["United States of America"],
    "West Indies": ["West Indies"],
}

# team ranking as of 05-26-2024

icc_ranking = {
    "India": 1,
    "Australia": 2,
    "England": 3,
    "South Africa": 4,
    "New Zealand": 5,
    "West Indies": 6,
    "Pakistan": 7,
    "Sri Lanka": 8,
    "Bangladesh": 9,
    "Afghanistan": 10,
    "Ireland": 11,
    "Scotland": 13,
    "Namibia": 14,
    "Netherlands": 15,
    "Nepal": 17,
    "Oman": 18,
    "United States of America": 19,
    "Papua New Guinea": 20,
    "Uganda": 22,
    "Canada": 23
}

def clean_venue(venue):
    if venue:
        return venue.split(",")[0].strip()
    return venue


for filename in os.listdir(json_dir):
    if filename.endswith(".json"):
        filepath = os.path.join(json_dir, filename)
        with open(filepath, "r") as f:
            data = json.load(f)
            if data["info"].get("gender") != "male":
                continue
            try:
                venue = clean_venue(data["info"].get("venue", ""))
                date = data["info"].get("dates", [""])[0]
                teams = data["info"].get("teams", ["", ""])
                team_A = teams[0] if len(teams) > 0 else ""
                team_B = teams[1] if len(teams) > 1 else ""
                
                team_A_score, team_B_score = 0, 0
                team_A_wickets, team_B_wickets = 0, 0
                for innings in data['innings']:
                    if innings['team'] == team_A:
                        for over in innings['overs']:
                            for delivery in over['deliveries']:
                                team_A_score += delivery['runs']['total']
                                team_A_wickets += len(delivery.get('wickets', []))
                    elif innings['team'] == team_B:
                        for over in innings['overs']:
                            for delivery in over['deliveries']:
                                team_B_score += delivery['runs']['total']
                                team_B_wickets += len(delivery.get('wickets', []))

                if team_A in world_cup_teams and team_B in world_cup_teams:
                    winner = data["info"].get("outcome", {}).get("winner", "")
                    toss_winner = data["info"].get("toss", {}).get("winner", "")
                    toss_decision = data["info"].get("toss", {}).get("decision", "")
                    team_A_ranking = icc_ranking.get(team_A, '')
                    team_B_ranking = icc_ranking.get(team_B, '')
                    is_home_team_A = 1 if team_A in home_teams.get(team_A, []) else 0
                    is_home_team_B = 1 if team_B in home_teams.get(team_B, []) else 0
                    
                    match_data_list.append(
                        [
                            venue,
                            date,
                            team_A,
                            team_B,
                            team_A_ranking,
                            team_B_ranking,
                            winner,
                            team_A_score,
                            team_A_wickets,
                            team_B_score,
                            team_B_wickets,
                            is_home_team_A,
                            is_home_team_B,
                            toss_winner,
                            toss_decision,
                        ]
                    )
            except KeyError as e:
                print(f"KeyError in file {filename}: {e}")

csv_file = "t20_wc24_match_data.csv"
with open(csv_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(
        [
            "Venue",
            "Date",
            "Team_A",
            "Team_B",
            "Team_A_Ranking",
            "Team_B_Ranking",
            "Winner",
            "Team_A_Score",
            "Team_A_Wickets_Lost",
            "Team_B_Score",
            "Team_B_Wickets_Lost",
            "Is_Home_Team_A",
            "Is_Home_Team_B",
            "Toss_Winner",
            "Toss_Decision",
        ]
    )
    writer.writerows(match_data_list)

print(f"CSV file has been created: {csv_file}")
