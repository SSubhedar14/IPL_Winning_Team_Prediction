import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model
with open('pipe.pkl', 'rb') as f:
    pipe = pickle.load(f)

# Define function to predict winning team
def predict_winning_team(BattingTeam, bowling_Team, city, runs_left, balls_left, wickets_left, total_run_x, crr, rrr):
    # Create a DataFrame with input data
    input_data = pd.DataFrame({
        'BattingTeam': [BattingTeam],
        'Bowling Team': [bowling_Team],
        'City': [city],
        'runs_left': [runs_left],
        'balls_left': [balls_left],
        'wickets_left': [wickets_left],
        'total_run_x': [total_run_x],
        'crr': [crr],
        'rrr': [rrr]
    })
    
    # Predict
    prediction = pipe.predict(input_data)[0]
    
    # Predict winning team
    if prediction == 1:  # Assuming 1 represents winning
        winning_team = BattingTeam
    else:
        winning_team = bowling_Team
    
    return winning_team

# Streamlit UI
def main():
    st.title('Cricket Winning Team Prediction')
    st.write('Enter the details to predict the winning team')

    # Input fields
    BattingTeam = st.selectbox('Select Batting Team', ['Chennai Super Kings', 'Delhi Capitals', 'Kings XI Punjab', 'Kolkata Knight Riders', 'Mumbai Indians', 'Rajasthan Royals', 'Royal Challengers Bangalore','Sunrisers Hyderabad', 'Gujarat Titans', 'Lucknow Super Giants'])  # Add more teams
    bowling_Team = st.selectbox('Select Bowling Team', ['Chennai Super Kings', 'Delhi Capitals', 'Kings XI Punjab', 'Kolkata Knight Riders', 'Mumbai Indians', 'Rajasthan Royals', 'Royal Challengers Bangalore','Sunrisers Hyderabad', 'Gujarat Titans', 'Lucknow Super Giants'])  # Add more teams
    city = st.text_input('Enter City')
    runs_left = st.number_input('Runs Left', value=0)
    balls_left = st.number_input('Balls Left', value=0)
    wickets_left = st.number_input('Wickets Left', value=0)
    total_run_x = st.number_input('Total Run', value=0)
    crr = st.number_input('Current Run Rate')
    rrr = st.number_input('Required Run Rate')

    # Predict button
    if st.button('Predict Winning Team'):
        winning_team = predict_winning_team(BattingTeam, bowling_Team, city, runs_left, balls_left, wickets_left, total_run_x, crr, rrr)
        st.write(f'Predicted Winning Team: {winning_team}')

if __name__ == '__main__':
    main()
