import requests
import pandas as pd

# Your base URL for the FPL API
base_url = "https://fantasy.premierleague.com/api/"


# Fetch general FPL data
def fetch_fpl_data():
    url = base_url + "bootstrap-static/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch FPL data.")
        return None


# Fetch detailed data for a specific player
def fetch_player_data(player_id):
    url = base_url + f"element-summary/{player_id}/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for player ID {player_id}.")
        return None


# Extract general player information
def extract_player_info(fpl_data):
    players = fpl_data['elements']
    player_info = []

    for player in players:
        player_info.append({
            'player_id': player['id'],
            'first_name': player['first_name'],
            'second_name': player['second_name'],
            'team_id': player['team'],
            'position_id': player['element_type'],
            'cost': player['now_cost'] / 10,  # Cost is in tenths of a million
            'total_points': player['total_points'],
            'minutes': player['minutes'],
            'goals_scored': player['goals_scored'],
            'assists': player['assists'],
            'clean_sheets': player['clean_sheets'],
            'yellow_cards': player['yellow_cards'],
            'red_cards': player['red_cards'],
            'saves': player['saves'],
            'influence': player['influence'],
            'creativity': player['creativity'],
            'threat': player['threat'],
            'ict_index': player['ict_index']
        })

    return pd.DataFrame(player_info)


# Extract team information
def extract_team_info(fpl_data):
    teams = fpl_data['teams']
    team_info = []

    for team in teams:
        team_info.append({
            'team_id': team['id'],
            'team_name': team['name'],
            'strength_attack_home': team['strength_attack_home'],
            'strength_attack_away': team['strength_attack_away'],
            'strength_defence_home': team['strength_defence_home'],
            'strength_defence_away': team['strength_defence_away']
        })

    return pd.DataFrame(team_info)


# Fetch detailed player data and compile into a DataFrame
def fetch_and_compile_detailed_player_data(player_ids):
    all_player_data = []

    for player_id in player_ids:
        detailed_data = fetch_player_data(player_id)

        if detailed_data:
            player_history = detailed_data['history']

            for match in player_history:
                all_player_data.append({
                    'player_id': player_id,
                    'fixture': match['fixture'],
                    'opponent_team': match['opponent_team'],
                    'total_points': match['total_points'],
                    'minutes': match['minutes'],
                    'goals_scored': match['goals_scored'],
                    'assists': match['assists'],
                    'clean_sheets': match['clean_sheets'],
                    'goals_conceded': match['goals_conceded'],
                    'yellow_cards': match['yellow_cards'],
                    'red_cards': match['red_cards'],
                    'saves': match['saves'],
                    'bonus': match['bonus'],
                    'bps': match['bps'],
                    'influence': match['influence'],
                    'creativity': match['creativity'],
                    'threat': match['threat'],
                    'ict_index': match['ict_index'],
                    'value': match['value'] / 10,  # Value is in tenths of a million
                    'transfers_balance': match['transfers_balance']
                })

    return pd.DataFrame(all_player_data)


# Main function to fetch, compile, and save the data
def main():
    # Fetch the general FPL data
    fpl_data = fetch_fpl_data()

    if fpl_data:
        # Extract player and team information
        player_df = extract_player_info(fpl_data)
        team_df = extract_team_info(fpl_data)

        # Fetch detailed player data
        detailed_player_df = fetch_and_compile_detailed_player_data(player_df['player_id'].tolist())

        # Merge the dataframes
        combined_df = pd.merge(detailed_player_df, player_df, on='player_id', how='left')
        combined_df = pd.merge(combined_df, team_df, left_on='opponent_team', right_on='team_id', how='left',
                               suffixes=('', '_opponent'))

        # Save the combined data to a CSV file
        combined_df.to_csv('fpl_combined_data.csv', index=False)
        print("Data saved to fpl_combined_data.csv")

    else:
        print("No data to process.")


if __name__ == "__main__":
    main()
