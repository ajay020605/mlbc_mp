import streamlit as st
from blockchain import Blockchain

st.set_page_config(page_title="Mini Blockchain Notes", page_icon="🔗", layout="wide")

if "blockchain" not in st.session_state:
    st.session_state.blockchain = Blockchain(difficulty=2)

bc = st.session_state.blockchain

st.title("🔗 Mini Blockchain Notes")
st.write("A beginner-friendly blockchain project built with Python and Streamlit.")

valid, message = bc.is_valid()
if valid:
    st.success("✅ " + message)
else:
    st.error("❌ " + message)

st.divider()

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📝 Add a Note")
    note = st.text_area(
        "Enter your note",
        placeholder="Example: Completed my Python practice today.",
        height=120,
    )
    if st.button("⛓️ Add Note to Blockchain", type="primary"):
        if not note.strip():
            st.warning("Please enter a note first.")
        else:
            block = bc.add_note(note)
            st.success(f"Note added as Block #{block.index}")
            st.rerun()

with col2:
    st.subheader("📊 Blockchain Info")
    st.metric("Total Blocks", len(bc.chain))
    st.metric("Notes", max(0, len(bc.chain) - 1))
    st.metric("Difficulty", bc.difficulty)

st.divider()

st.subheader("⛓️ Blockchain")

for block in bc.chain:
    with st.container(border=True):
        st.markdown(f"### Block #{block.index}")
        st.write(f"**Note:** {block.note}")
        st.caption(f"Timestamp: {block.timestamp}")
        st.code(f"Hash: {block.hash}\nPrevious Hash: {block.previous_hash}\nNonce: {block.nonce}")

st.divider()

st.subheader("🧪 Tamper Test")
st.write("Change a note without recalculating its hash. The blockchain should become invalid.")

if len(bc.chain) > 1:
    block_index = st.selectbox(
        "Select a block",
        options=list(range(1, len(bc.chain))),
        format_func=lambda x: f"Block #{x}: {bc.chain[x].note[:45]}"
    )
    new_note = st.text_input("New note", placeholder="This is a modified note")

    if st.button("⚠️ Tamper With Selected Block"):
        if not new_note.strip():
            st.warning("Enter the modified note first.")
        else:
            bc.tamper_with_block(block_index, new_note)
            st.error("Block modified without updating its hash.")
            st.rerun()
else:
    st.info("Add at least one note to use the tamper test.")

st.caption("Educational project — this is a simplified blockchain demonstration, not a production blockchain.")
