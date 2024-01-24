import bluetooth
import time

def trouver_peripheriques_bluetooth():
    devices = bluetooth.discover_devices(duration=8, lookup_names=True, device_class=0)
    return devices

def distance_bluetooth(adresse_mac):
    rssi = bluetooth.read_rssi(adresse_mac)
    distance = 10 ** ((-69 - rssi) / (10 * 2))
    return distance

def mesurer_distance_en_boucle():
    while True:
        peripheriques = trouver_peripheriques_bluetooth()

        if peripheriques:
            for adresse_mac, nom, _ in peripheriques:
                distance = distance_bluetooth(adresse_mac)
                print(f"Nom: {nom}, Adresse MAC: {adresse_mac}, Distance approximative: {distance:.2f} mètres")
        else:
            print("Aucun périphérique Bluetooth trouvé.")

        # Intervalle de 5 secondes entre chaque mesure
        time.sleep(5)

# Appeler la fonction pour mesurer en boucle
mesurer_distance_en_boucle()
