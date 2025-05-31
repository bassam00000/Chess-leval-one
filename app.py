
import streamlit as st
import chess
import chess.svg
import streamlit.components.v1 as components

st.set_page_config(page_title="Chess Training Plan", layout="wide")

st.title("♟️ Chess Training Game - Famous Plans")

st.markdown("""
This is a chess training game where each level represents a famous chess plan.
You will play against pre-programmed strategies inspired by classic tactical and strategic ideas.
""")

plans = {
    "Level 1: Scholar's Mate": [
        "e2e4", "e7e5", "d1h5", "b8c6", "f1c4", "g8f6", "h5f7"
    ],
    "Level 2: Fool's Mate": [
        "f2f3", "e7e5", "g2g4", "d8h4"
    ],
    "Level 3: Legal's Mate": [
        "e2e4", "e7e5", "g1f3", "b8c6", "f1c4", "d7d6", "f3e5", "c6e5", "d1h5", "e5f6", "h5f7"
    ]
}

level = st.selectbox("Select a Training Level", list(plans.keys()))

board = chess.Board()
moves = plans[level]

for move in moves:
    try:
        board.push_uci(move)
    except Exception as e:
        st.error(f"Invalid move in plan: {move}. Error: {e}")
        break

board_svg = chess.svg.board(board, size=500)
components.html(board_svg, height=500)

st.info("Try to play this plan against the board in your own session and analyze how to defend or counter it.")
