sistemas = ["Windows", "Android", "Linux", "iOS", "macOS"]
mobile = []
desktop = []

for so in sistemas:
    if so == "Android" or so == "iOS":
        mobile.append(so)
    else:
        desktop.append(so)

print("Sistemas operacionais móveis:", mobile)
print("Sistemas operacionais de desktop:", desktop)