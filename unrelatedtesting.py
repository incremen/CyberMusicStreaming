import base64
from custom_logging import debug_vars, CustomLogger

custom_logger = CustomLogger()
def bytes_to_binary_string(bytes):
    binary_string = bin(int.from_bytes(bytes, byteorder='big'))[2:]
    binary_string = binary_string.zfill(8 * len(bytes))
    
    binary_string_with_gaps = ' '.join([binary_string[i:i+8] for i in range(0, len(binary_string), 8)])
    
    return binary_string_with_gaps

# Example usage
# message = b"Sm9uIERvZQ=="
message = b"abcd"
decoded = base64.b64decode(message)
binary_representation = bytes_to_binary_string(message)
binary_of_decoded = bytes_to_binary_string(decoded)
debug_vars(message, decoded, binary_representation, binary_of_decoded)
