import random

watt = 60  # Assume each lamp uses 60 watts
volt = 230  # Standard voltage in many European countries

# Function to switch lamp status
def skift_lampe_status(rum_status, rum, status):
    rum_status[rum] = status
    return rum_status

# Function to calculate total power consumption
def samlet_strømforbrug(rum_status, watt, volt):
    tændte_lamper = sum(1 for status in rum_status.values() if status == "tændt")
    samlet_watt = tændte_lamper * watt
    ampere = samlet_watt / volt
    return samlet_watt, ampere

# Function to simulate the room lighting control
def strøm_af_lamper(hvor_mange_rum, brugere, watt, volt):
    rum_status = {rum: "slukket" for rum in hvor_mange_rum}
    brugere_i_rum = {bruger: None for bruger in brugere}

    for bruger in brugere:
        test_bruger_rum = random.choice(hvor_mange_rum)
        if brugere_i_rum[bruger] is not None:
            rum_status[brugere_i_rum[bruger]] = "slukket"

        rum_status[test_bruger_rum] = "tændt"
        brugere_i_rum[bruger] = test_bruger_rum
        print(f"{bruger} er gået ind i rummet: {test_bruger_rum}")

    rum_info = {rum: {'status': rum_status[rum], 'personer': [bruger for bruger, rum_valg in brugere_i_rum.items() if rum_valg == rum]} for rum in hvor_mange_rum}

    samlet_watt, ampere = samlet_strømforbrug(rum_status, watt, volt)

    forbrugs_info = {
        'samlet_watt': samlet_watt,
        'ampere': ampere
    }

    return rum_info, forbrugs_info

if __name__ == "__main__":
    hvor_mange_rum = ["Køkken", "Stue", "Soveværelse", "Badeværelse", "Gang", "Kontor", "Børneværelse", "Kælder"]
    brugere = ["Alice", "Bob", "Charlie", "David", "Erika"]
    strøm_af_lamper(hvor_mange_rum, brugere, watt, volt)
