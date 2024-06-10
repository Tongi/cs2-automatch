import time
from fiktiv_ude_temperatur import measure_outdoor_temperature

stue_temperatur = 15
gemmelse_af_manuelt_valg = []
hvor_mange_rum = ['redskabsrum', 'køkken', 'voksen_værelse', 'børne_værelse', 'badeværelse', 'stue', 'walk_in_closet', 'bad', 'arbejdskontor']

def bestemmelse_af_varme(bestemmelse_af_temperatur):
    if bestemmelse_af_temperatur == stue_temperatur:
        gemmelse_af_manuelt_valg.append(bestemmelse_af_temperatur)
    elif bestemmelse_af_temperatur < stue_temperatur:
        gemmelse_af_manuelt_valg.append(bestemmelse_af_temperatur)
    elif bestemmelse_af_temperatur > stue_temperatur:
        gemmelse_af_manuelt_valg.append(bestemmelse_af_temperatur)
    return bestemmelse_af_temperatur

def check_temperature(selvvalgt_temperatur):
    stue_temperatur_med_ude_temperatur = measure_outdoor_temperature() - 3
    udendørs_temperatur = measure_outdoor_temperature()

    if selvvalgt_temperatur != stue_temperatur_med_ude_temperatur:
        stue_temperatur_med_ude_temperatur = selvvalgt_temperatur

    rum_temperaturer = {rum: stue_temperatur_med_ude_temperatur for rum in hvor_mange_rum}
    print(f"udendørs {udendørs_temperatur}\nrum temperatur{stue_temperatur_med_ude_temperatur}")
    return udendørs_temperatur, rum_temperaturer

if __name__ == "__main__":
    bestemmelse_af_temperatur = int(input("Bestemmelse af hvor varmt du vil have det i huset: "))
    selvvalgt_temperatur = bestemmelse_af_varme(bestemmelse_af_temperatur)
    print(check_temperature(selvvalgt_temperatur))
