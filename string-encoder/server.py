from nameko.rpc import rpc
from dahuffman import HuffmanCodec
from dahuffman import load_shakespeare
import base64

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
                b64encoded = base64.b64encode(encoded).decode('utf-8')
                answer.update({original : b64encoded})

        return answer
        
        