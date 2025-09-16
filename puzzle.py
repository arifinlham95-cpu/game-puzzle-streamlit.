import streamlit as st
import random

st.title("🎮 Game Puzzle Angka 3x3")

# Buat puzzle 3x3
if "board" not in st.session_state:
    nums = list(range(1, 9)) + [None]  # angka 1-8 + kotak kosong
    random.shuffle(nums)
    st.session_state.board = [nums[i:i+3] for i in range(0, 9, 3)]

board = st.session_state.board

# Fungsi cek menang
def is_solved(b):
    flat = sum(b, [])
    return flat == list(range(1, 9)) + [None]

# Render papan
for row in board:
    cols = st.columns(3)
    for i, val in enumerate(row):
        if val is None:
            cols[i].button(" ", key=str(row)+str(i))
        else:
            if cols[i].button(str(val), key=str(row)+str(i)):
                # Cari posisi kosong
                empty_pos = [(r, c) for r in range(3) for c in range(3) if board[r][c] is None][0]
                r_empty, c_empty = empty_pos
                r_val = board.index(row)
                c_val = row.index(val)

                # Cek apakah bisa ditukar (atas, bawah, kiri, kanan)
                if abs(r_empty - r_val) + abs(c_empty - c_val) == 1:
                    board[r_empty][c_empty], board[r_val][c_val] = board[r_val][c_val], None
                    st.session_state.board = board
                    st.experimental_rerun()

# Tampilkan status
if is_solved(board):
    st.success("🎉 Selamat! Puzzle selesai!")
