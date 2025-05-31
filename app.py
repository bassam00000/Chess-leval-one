
import streamlit as st
import chess
import chess.svg
import streamlit.components.v1 as components

st.set_page_config(page_title="Chess Training Plan", layout="wide")

st.title("♟️ Chess Training Game - Famous Plans")

st.markdown("""
Each level in this chess trainer demonstrates a classic tactical plan. 
Study how the strategy unfolds move-by-move.
""")

plans = {
    "Level 1: Scholar's Mate": [
        "e2e4", "e7e5", "d1h5", "b8c6", "f1c4", "g8f6", "h5f7"
    ],
    "Level 2: Fool's Mate": [
        "f2f3", "e7e5", "g2g4", "d8h4"
    ],
    "Level 3: Legal's Mate": [
        "e2e4", "e7e5", "g1f3", "d7d6", "f1c4", "c8g4", "f3e5", "g4d1", "e5f7", "d1e2", "e1e2"
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

st.info("You can now replay this plan or test defending against it.")
