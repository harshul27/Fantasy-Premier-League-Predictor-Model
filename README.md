# Fantasy-Premier-League-Gameweek-Lineup-Predictor-Model

## Overview
This project is a Fantasy Premier League (FPL) predictor model that leverages data science techniques to help FPL managers make informed decisions. It analyzes player performance, fixture difficulty, and other factors to provide suggestions for team selection, captaincy, and chip usage.

## Features
- **Data Collection:**
    - Collects comprehensive data from the official FPL website.
    - Gathers detailed information for every player, covering various performance metrics.
- **Player Suggestions:**
    - Suggests replacements for players in the manager's current squad based on their performance in the previous 3 Gameweeks (GWs).
    - Recommends favorable players for swaps based on user-defined criteria.
- **Playing Time Prediction:**
    - Identifies players who are highly likely to play 90 minutes or more than 60 minutes. This is determined by checking if a player has scored more than 2 points in over 75% of their gameweek summaries.
- **Captaincy Favorites:**
    - Predicts captain favorites for a particular GW by analyzing:
        - Player's attacking threat.
        - Ease of the upcoming match.
        - Historical performance (if the player scored well against the same team in the first leg).
        - Bonus points earned.
        - Form in the previous 3 GWs.
- **Chip Usage Suggestions:**
    - **Triple Captain:** Recommends using when:
        - There is a Double Gameweek (DGW) with easy fixtures.
        - A player has an easy fixture and has averaged 9 points or more in the previous 5 GWs.
    - **Bench Boost:** Suggests using when:
        - The entire squad is fit.
        - The bench players have relatively easier fixtures, especially if they are star players.
    - **Wildcard:** Advises using when:
        - The team has significant injuries (2 or more players with less than 75% chance of playing).
        - The manager is planning to make more than 3 transfers in a single GW. (To be used twice in a season).
    - **Free Hit:** Recommends using when:
        - There are a limited number of teams playing in a GW.
        - There is an unusually large number of matches in a gameweek (e.g., blank and double gameweeks).

## Technical Details
- **Machine Learning Models:** Utilizes trained and tuned Random Forest and Logistic Regression models.
- **Training Data:** Models were trained on over 100 gameweeks of player performance data, encompassing more than 500 athletes.
- **Performance Boost:** Achieved a 20% boost in prediction accuracy by leveraging:
    - Time-series smoothing techniques.
    - Fixture difficulty weighting.
    - Trend factors.
- **Reporting & Visualization:** Features an automated scoring system and data visualizations created with Seaborn and Matplotlib to provide weekly player performance summaries with a 24-hour turnaround.

## Future Enhancements
- Dynamic weekly prediction of optimal fantasy player lineups for each gameweek.
- Suggestion of improvements to current fixed players with a constraint of making a maximum of 1-2 changes.

## How to Use/Installation
*(Instructions to be added. This section will typically include steps on how to set up the environment, install dependencies, and run the scripts.)*

For now, you can explore the following scripts:
- `scrapedata.py`: Fetches and compiles player and team data from the FPL API.
- `requestfplapi.py`: Contains functions to interact with the FPL API.

## Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## License
Distributed under the MIT License. See `LICENSE` file for more information. (Assuming MIT, a `LICENSE` file would need to be created if one doesn't exist).
