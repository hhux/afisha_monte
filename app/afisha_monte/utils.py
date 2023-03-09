import uuid


def generate_id(*args):
    return uuid.uuid3(uuid.NAMESPACE_OID, name=str(hash(args)))

