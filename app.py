import streamlit as st
import players

if 'count' not in st.session_state:
    st.session_state['count'] = 0


st.title("PyPicks")
st.text_input(
        label = "Enter a player", 
        key = "nba_player")

if st.button(
        label = "Search", 
        key = "nba_player_button"):

    if st.session_state['nba_player']:

        player = players.Player()
        results = player.search_players(st.session_state['nba_player'])
        st.session_state['player_search'] = results

if 'player_search' in st.session_state:

    st.selectbox(
                 label = "results", 
                 options = st.session_state['player_search'], 
                 key = 'nba_player_list',
                 format_func = lambda x: x['full_name']
                 )

if st.button(
            label = "Select player",
            key = "nba_players_list_button"):
    pass
    