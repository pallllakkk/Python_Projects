import qrcode as qr
img = qr.make("https://open.spotify.com/")
img.save("spotify.png")