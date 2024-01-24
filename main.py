import bluetooth
import time
import json
import os

if os.path.exists("config.json"):
    print("File config.json found")
    with open("config.json", "r") as f:
        config = json.load(f)
    print("Successfully recovered configuration")
else:
    print("config.json file not found")
    print("Scanning bluetooth devices...")
    config = {}
    temp_data = {}
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    print("Found {} devices.".format(len(nearby_devices)))

    for addr, name in nearby_devices:
        print("  {} - {}".format(addr, name))
        temp_data[name] = addr
    
    current_name = input("Please type the name of your phone : ")
    while not current_name in temp_data.keys():
        current_name = input("Sorry, can't find your phone, please type exactly your phone's name : ")
    current_mac = temp_data[current_name]
    config["macadress"] = current_mac

    with open("config.json", "w") as f:
        print("Successfully created config.json")
        json.dump(config, f, indent=4)
    print("Successfully dump config")

def trouver_peripheriques_bluetooth():
    print("Scanning devices...")
    devices = bluetooth.discover_devices(duration=8, lookup_names=True)
    return devices

def distance_bluetooth(adresse_mac):
    # Utilisez pybluez pour lire le RSSI
    sock = bluetooth.BluetoothSocket(bluetooth.L2CAP)
    sock.connect((adresse_mac, 1))
    rssi = sock.getsockopt(bluetooth.SOL_BLUETOOTH, bluetooth.SO_RSSI, 1)
    sock.close()
    distance = 10 ** ((-69 - rssi) / (10 * 2))
    return distance

def mesurer_distance_en_boucle():
    while True:
        peripheriques = trouver_peripheriques_bluetooth()

        if peripheriques:
            for adresse_mac, nom in peripheriques:
                if adresse_mac == config["macadress"]:
                    # distance = distance_bluetooth(adresse_mac)
                    distance = 10
                    print(f"Nom: {nom}, Adresse MAC: {adresse_mac}, Distance approximative: {distance:.2f} mètres")
        else:
            print("Aucun périphérique Bluetooth trouvé.")


# Appeler la fonction pour mesurer en boucle
mesurer_distance_en_boucle()
