from hdwallet import HDWallet
from hdwallet.utils import generate_mnemonic
from hdwallet.symbols import BTC
from typing import Optional

import json

STRENGTH: int = 128  # Default is 128
LANGUAGE: str = "english"  # Default is english
MNEMONIC = generate_mnemonic(LANGUAGE, STRENGTH)

PASSPHRASE: Optional[str] = None

hdwallet: HDWallet = HDWallet(symbol=BTC)

hdwallet.from_mnemonic(
    mnemonic=MNEMONIC, language=LANGUAGE, passphrase=PASSPHRASE
)

print(json.dumps(hdwallet.dumps(), indent=4, ensure_ascii=False))