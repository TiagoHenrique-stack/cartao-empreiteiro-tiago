import qrcode

link = "https://seulink.streamlit.app"  # depois a gente troca pelo link real
qr = qrcode.make(link)
qr.save("qr_code.png")
print("QR Code salvo como qr_code.png")