import base64
raw="just a string"
encoded = base64.b64encode(raw.encode("utf-8"))
decoded = base64.b64decode(encoded)
print(raw)
print(encoded)
print(decoded)
print(decoded.decode("utf-8"))