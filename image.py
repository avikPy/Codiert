from PIL import Image

DELIMITER = "<<<END>>>"

def text_to_bits(text):
    data = text.encode("utf-8")
    bits = []
    for byte in data:
        for i in range(8):
            bits.append((byte >> (7 - i)) & 1)
    return bits

def bits_to_text(bits):
    bytes_list = []
    for i in range(0, len(bits), 8):
        byte = 0
        for b in bits[i:i+8]:
            byte = (byte << 1) | b
        bytes_list.append(byte)
    data = bytes(bytes_list)
    return data.decode("utf-8", errors="ignore")

def encode_image(input_image, output_image, secret_text):
    img = Image.open(input_image)
    img = img.convert("RGB")
    pixels = list(img.getdata())

    secret_text += DELIMITER
    bits = text_to_bits(secret_text)

    if len(bits) > len(pixels) * 3:
        raise ValueError("Текст слишком большой для этой картинки")

    new_pixels = []
    bit_index = 0

    for r, g, b in pixels:
        if bit_index < len(bits):
            r = (r & ~1) | bits[bit_index]
            bit_index += 1
        if bit_index < len(bits):
            g = (g & ~1) | bits[bit_index]
            bit_index += 1
        if bit_index < len(bits):
            b = (b & ~1) | bits[bit_index]
            bit_index += 1

        new_pixels.append((r, g, b))

    img.putdata(new_pixels)
    img.save(output_image)
    return 1

def decode_image(image_path):
    img = Image.open(image_path)
    pixels = list(img.getdata())

    bits = []

    for r, g, b in pixels:
        bits.append(r & 1)
        bits.append(g & 1)
        bits.append(b & 1)

    text = bits_to_text(bits)

    end_index = text.find(DELIMITER)
    if end_index != -1:
        return (text[:end_index])




