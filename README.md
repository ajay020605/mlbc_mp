# 🔗 Mini Blockchain Notes

A small educational blockchain project built using **Python** and **Streamlit**.

The application lets you:

- Add notes as blockchain blocks
- Calculate SHA-256 hashes
- Link every block to the previous block
- Use a simple Proof-of-Work mechanism
- Validate the blockchain
- Demonstrate what happens when a block is tampered with

## Project structure

```text
mini_blockchain_notes/
│
├── app.py              # Streamlit user interface
├── blockchain.py       # Blockchain and Block classes
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

## Requirements

- Python 3.9+
- pip

## Installation

Open a terminal in the project folder:

```bash
python -m venv venv
```

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the project

```bash
streamlit run app.py
```

Your browser should open the application automatically. If it does not, Streamlit will show a local URL in the terminal.

## How the blockchain works

Each block contains:

- `index` — block number
- `timestamp` — creation time
- `note` — the user's note
- `previous_hash` — hash of the previous block
- `nonce` — number used by Proof of Work
- `hash` — SHA-256 hash of the block data

Example:

```text
Block 1
Note: Completed Python practice
Previous Hash: abc123...
Nonce: 57
Hash: 00f8a1...
```

The next block stores the previous block's hash:

```text
Block 2
Previous Hash: 00f8a1...
```

This creates a chain of linked blocks.

## What is Proof of Work here?

The project uses a small difficulty value of `2`. Mining repeatedly changes the `nonce` until the block hash begins with two zeroes:

```text
00a91f...
```

This is intentionally simple so that the project runs quickly on a normal laptop.

## Try the tamper test

1. Add two or more notes.
2. Scroll to **Tamper Test**.
3. Select a block.
4. Change its note.
5. Click **Tamper With Selected Block**.
6. The validation message should change to invalid.

Why? The stored hash was created from the original note. Changing the note changes the correct hash, but the stored hash was not changed.

## Important limitation

This is an educational blockchain simulation. It does not use a peer-to-peer network, wallets, cryptocurrency, a public blockchain, or a distributed consensus network.

## Resume description

**Mini Blockchain Notes | Python, SHA-256, Streamlit**

- Developed a lightweight blockchain-based notes application using Python and Streamlit.
- Implemented SHA-256 hashing, previous-hash linking, Proof of Work, and blockchain validation.
- Built a tamper-detection demonstration showing how modifying block data invalidates the chain.

## Possible future improvements

- Add SQLite database storage
- Add user login
- Add search and filtering
- Add export to CSV/JSON
- Add a block visualization
- Add a REST API using FastAPI
