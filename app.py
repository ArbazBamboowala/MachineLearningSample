import streamlit as st
import hashlib

# Function to calculate SHA256 hash
def calculate_hash(block_number, nonce, amount_dollars, name, data, previous_hash):
    block_data = f"{block_number}{nonce}{amount_dollars}{name}{data}{previous_hash}"
    return hashlib.sha256(block_data.encode()).hexdigest()

def main():
    st.title("Blockchain Simulation")

    # Initialize session state
    if 'previous_hash_1' not in st.session_state:
        st.session_state.previous_hash_1 = ""

    # User input fields for the first block
    st.sidebar.header("Block 1")
    block_number_1 = st.sidebar.number_input("Block Number 1", min_value=1, value=1, key="block_number_1")
    nonce_1 = st.sidebar.number_input("Nonce 1", min_value=0, value=0, key="nonce_1")
    amount_dollars_1 = st.sidebar.number_input("Amount (in Dollars) 1", min_value=0.0, value=0.0, step=0.01, key="amount_dollars_1")
    name_1 = st.sidebar.text_input("Name of Person 1", key="name_1")
    data_1 = st.sidebar.text_input("Data 1", key="data_1")

    # Button to mine the first block
    if st.sidebar.button("Mine Block 1"):
        # Calculate hash for the first block
        current_hash_1 = calculate_hash(block_number_1, nonce_1, amount_dollars_1, name_1, data_1, st.session_state.previous_hash_1)
        st.sidebar.write(f"Hash Value 1: {current_hash_1}")
        st.session_state.previous_hash_1 = current_hash_1

    # User input fields for the second block
    st.header("Block 2")
    st.write(f"Previous Input Hash Value: {st.session_state.previous_hash_1}")
    block_number_2 = st.number_input("Block Number 2", min_value=1, value=1, key="block_number_2")
    nonce_2 = st.number_input("Nonce 2", min_value=0, value=0, key="nonce_2")
    amount_dollars_2 = st.number_input("Amount (in Dollars) 2", min_value=0.0, value=0.0, step=0.01, key="amount_dollars_2")
    name_2 = st.text_input("Name of Person 2", key="name_2")
    data_2 = st.text_input("Data 2", key="data_2")

    # Button to mine the second block
    if st.button("Mine Block 2"):
        # Calculate hash for the second block using the hash value from the first block
        current_hash_2 = calculate_hash(block_number_2, nonce_2, amount_dollars_2, name_2, data_2, st.session_state.previous_hash_1)
        st.write(f"Hash Value 2: {current_hash_2}")

if __name__ == "__main__":
    main()
