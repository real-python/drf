import hashlib


def Encode_SHA256(data):
    result = hashlib.sha256(data.encode())
    return result.hexdigest()


def Encode_SHA384(data):
    result = hashlib.sha384(data.encode())
    return result.hexdigest()


def Encode_SHA224(data):
    result = hashlib.sha224(data.encode())
    return result.hexdigest()


def Encode_SHA512(data):
    result = hashlib.sha512(data.encode())
    return result.hexdigest()