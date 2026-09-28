import hashlib
import json
from datetime import datetime
from dataclasses import dataclass, asdict


@dataclass
class Block:
    index: int
    timestamp: str
    note: str
    previous_hash: str
    nonce: int = 0
    hash: str = ""

    def calculate_hash(self):
        block_data = {
            "index": self.index,
            "timestamp": self.timestamp,
            "note": self.note,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce,
        }
        encoded = json.dumps(block_data, sort_keys=True).encode("utf-8")
        return hashlib.sha256(encoded).hexdigest()

    def mine(self, difficulty=2):
        target = "0" * difficulty
        self.nonce = 0
        while True:
            self.hash = self.calculate_hash()
            if self.hash.startswith(target):
                return self.hash
            self.nonce += 1


class Blockchain:
    def __init__(self, difficulty=2):
        self.difficulty = difficulty
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        block = Block(
            index=0,
            timestamp=datetime.now().isoformat(timespec="seconds"),
            note="Genesis Block",
            previous_hash="0",
        )
        block.hash = block.calculate_hash()
        return block

    def add_note(self, note):
        if not note or not note.strip():
            raise ValueError("Note cannot be empty.")

        previous = self.chain[-1]
        block = Block(
            index=len(self.chain),
            timestamp=datetime.now().isoformat(timespec="seconds"),
            note=note.strip(),
            previous_hash=previous.hash,
        )
        block.mine(self.difficulty)
        self.chain.append(block)
        return block

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.calculate_hash():
                return False, f"Block {current.index} has been modified."

            if current.previous_hash != previous.hash:
                return False, f"Block {current.index} has an invalid previous hash."

            if not current.hash.startswith("0" * self.difficulty):
                return False, f"Block {current.index} does not satisfy proof of work."

        return True, "Blockchain is valid."

    def tamper_with_block(self, index, new_note):
        if index <= 0 or index >= len(self.chain):
            raise ValueError("Choose a non-genesis block index.")
        self.chain[index].note = new_note
        # Intentionally do NOT recalculate the hash.

    def to_dict_list(self):
        return [asdict(block) for block in self.chain]
