import wifi_qrcode_generator as qr
import os
from PIL import ImageDraw
from PIL import Image
from PIL import ImageFont


def generate_qr_code(ssid_config, general_config, output_file, hidden=False):
    font_location = os.path.join("Fonts", "FontsFree-Net-arial-bold.ttf")
    extra_font = ImageFont.truetype(font_location, size=16)
    qrCode = qr.wifi_qrcode(ssid_config.ssid_name, hidden, ssid_config.ssid_encryption, ssid_config.ssid_password)
    qrCode.make_image().save(output_file, format='PNG')
    qrImage = Image.open(output_file)
    qrImageWidth, qrImageHeight = qrImage.size
    textWidth = (qrImageWidth/2) - (extra_font.getbbox(f"Wifi: {ssid_config.ssid_name}")[2]/2)
    textHeight = qrImageHeight - 30
    layer = ImageDraw.Draw(qrImage)
    layer.text((textWidth, textHeight), f"Wifi: {ssid_config.ssid_name}", font=extra_font, fill="black")
    # qrImage.show()
    qrImage.save(output_file)
