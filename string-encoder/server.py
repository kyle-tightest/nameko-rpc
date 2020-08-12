from nameko.rpc import rpc
from dahuffman import HuffmanCodec
from dahuffman import load_shakespeare

class StringEncoder:
    name = "string_encoder_service"

    def __init__(self):
        global codec
        codec = load_shakespeare()

    @rpc
    def encode(self, strings):
        if not isinstance(strings, list):
            return "input is not list"
        answer = dict()
        for original in list(strings):
            if original not in answer:
                encoded = codec.encode(original)
                hex_encoded = encoded.hex()
                answer.update({original : hex_encoded})

        return answer
    
    @rpc
    def decode(self, string):
        if not isinstance(string, str):
            return "input is not string"
        string = str(string)
        try:
            encodedbytes = bytes.fromhex(string)
        except:
            return "input is not valid Hex string"
        return codec.decode(encodedbytes)
        