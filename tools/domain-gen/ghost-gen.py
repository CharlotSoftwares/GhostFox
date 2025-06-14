import os
import base64
import pathlib
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives import serialization

# Paths
KEY_DIR = os.path.expanduser("~/.ghostnet/keys/")
os.makedirs(KEY_DIR, exist_ok=True)

# Generate keypair
private_key = Ed25519PrivateKey.generate()
public_key = private_key.public_key()

# Export public key bytes and encode domain
pub_bytes = public_key.public_bytes(
    encoding=serialization.Encoding.Raw,
    format=serialization.PublicFormat.Raw
)
domain = base64.b32encode(pub_bytes).decode("utf-8").lower().rstrip("=") + ".shdw"

# Export private key
priv_bytes = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

# Save private key
key_path = os.path.join(KEY_DIR, domain.replace(".shdw", "") + ".key")
with open(key_path, "wb") as f:
    f.write(priv_bytes)

# Output
print(f"Domain: {domain}")
print(f"Private key saved to: {key_path}")
