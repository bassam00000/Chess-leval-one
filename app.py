
import streamlit as st
import chess
import chess.svg
import streamlit.components.v1 as components

# إعداد الصفحة
st.set_page_config(page_title="Chess Trainer", layout="wide")
st.title("♟️ Chess Training: Scholar's Mate")

st.markdown("""
تعلم خطة "ماتة العالم" خطوة بخطوة.
""")

# خطة Scholar’s Mate
moves = [
    "e2e4", "e7e5",
    "d1h5", "b8c6",
    "f1c4", "g8f6",
    "h5f7"  # كش مات
]

board = chess.Board()

for move in moves:
    try:
        board.push_uci(move)
    except Exception as e:
        st.error(f"خطأ في الحركة: {move} - {e}")
        break

# عرض الرقعة
board_svg = chess.svg.board(board, size=500)
components.html(board_svg, height=500)

st.success("تم تنفيذ خطة Scholar's Mate. هل يمكنك الدفاع ضدها؟")
