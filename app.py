
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
        "e2e4", "e7e5", "Qd1h5", "Nb8c6", "Bf1c4", "Ng8f6", "Qh5xf7"
    ],
    "Level 2: Fool's Mate Defense": [
        "e2e3", "f7f6", "d1h5", "g7g6", "h5xg6"
    ],
}

level = st.selectbox("Select a Training Level", list(plans.keys()))

board = chess.Board()
moves = plans[level]

for move in moves:
    if board.is_legal(chess.Move.from_uci(move)):
        board.push(chess.Move.from_uci(move))

board_svg = chess.svg.board(board, size=500)
components.html(board_svg, height=500)

st.info("Try to play this plan against the board in your own session and analyze how to defend or counter it.")
