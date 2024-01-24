import bluetooth
import time

def trouver_peripheriques_bluetooth():
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
                distance = distance_bluetooth(adresse_mac)
                print(f"Nom: {nom}, Adresse MAC: {adresse_mac}, Distance approximative: {distance:.2f} mètres")
        else:
            print("Aucun périphérique Bluetooth trouvé.")

        # Intervalle de 5 secondes entre chaque mesure
        time.sleep(5)

# Appeler la fonction pour mesurer en boucle
mesurer_distance_en_boucle()
