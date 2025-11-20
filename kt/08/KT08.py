###############################################################################
# 4A00HB81 Python-ohjelmointi (TAMK 2025)
# =============================================================================
# KT08.py
#
# Opiskelija: Rihu Miska
# Päiväys: 2025-11.07
#
###############################################################################
# Tehtävänanto:
#
# Samaan tapaan kuin aiemmassa tuntitehtävässä (TT13), tietovisassa on n
# kappaletta kysymyksiä. Tässä niille kuitenkin on mahdollista antaa m
# vastausvaihtoehtoa (enintään 26 kappaletta, merkitty a, b, c, ... z). Ohjelma
# esittää kysymykset ja vastausvaihtoehdot pelaajalle, ja kysyy minkä
# vastauksen hän valitsee. Jos vastaus on oikein, pelaaja saa pisteen (enintään
# n p.). Jos vastaus on väärin, siitä ilmoitetaan. Jos pelaaja valitsee
# kirjaimen, joka ei kuulu millekään vastausvaihtoehdolle, hänelle ilmoitetaan
# siitä, ja esitetään kysymys uudelleen.
#
# Kun kaikki kysymykset on esitetty ja vastaukset saatu, kerrotaan pelaajalle
# montako pistettä hän sai (esim. "Sait 6/10 oikein.", jos visassa on 10
# kysymystä, ja pelaaja vastasi oikein kuuteen niistä.)
#
# Tässä versiossa kysymykset, vastausvaihtoehdot ja tieto oikeasta vastauksesta
# tallennetaan tiedostoon, josta ne luetaan kun ohjelma alkaa. Tämä antaa
# mahdollisuuden muokata kysymyksiä ja vastausvaihtoehtoja ilman että itse
# ohjelmaan tarvitsee tehdä muutoksia, ja jopa korvata ne kokonaan omilla
# versioilla. Sama ohjelma siis voi toimia millä tahansa kysymyksillä, joita on
# mielivaltaisen monta, jos tiedoston sisältöä muokataan sopivasti.
#
# Tiedoston sisällön pitää olla seuraavan kaltainen. Tiedostossa on
# mielivaltainen määrä m+3 riviä käsittäviä yksiköitä, jotka kaikki ovat
# seuraavaa muotoa:
#
# kysymys
# vastausvaihtoehto a
# vastausvaihtoehto b
# vastausvaihtoehto c
# vastausvaihtoehto ...
# x
# tyhjä rivi
#
# missä x on oikean vastauksen kirjain (a ... z), ja tyhjä rivi tarkoittaa
# juuri sellaista.
#
# Ohjelman pitää lukea kaikki tällaiset yksiköt, joista jokainen vastaa yhtä
# kokonaista kysymystä. Ne voi olla kätevintä lukea listaan, joka sisältää
# sanakirjoja, kuten aiemmassa tuntitehtävässäkin tehtiin. Jokaisessa
# sanakirjassa on kysymysteksti, vastausvaihtoehdot sekä oikean vastauksen
# kirjain.
#
# Ensimmäisen yksikön perusteella tiedetään kuinka monta vastausvaihtoehtoa
# kysymyksissä on. Jos seuraavissa yksiköissä on eri määrä vaihtoehtoja,
# kysymystiedostossa on virhe. Ohjelman pitää ilmoittaa tästä ja lopettaa
# toiminta hallitusti, eli kysymyksiä ei tällöin esitetä pelaajalle lainkaan.
# Samoin toimitaan myös, jos tiedostossa oleva oikean vastauksen kirjain ei
# sovi yhteen vastausvaihtoehtojen määrän kanssa (esim. annettu kolme
# vastausvaihtoehtoa, mutta oikean vastauksen kirjain on d).
#
# Esimerkki kokonaisesta kysymystiedostosta, jossa on kolme kysymystä ja kolme
# vastausvaihtoehtoa per kysymys, voisi olla tällainen:
#
# -----------------------------------------------------------------------------
# Kuka seuraavista ei ole Monty Python -komediaryhmän jäsen?
# Michael Palin
# Terry Jones
# Charlie Chaplin
# c
#
# Kuka on Python-ohjelmointikielen alkuperäinen kehittäjä?,
# Larry Wall
# Bjarne Stroustrup
# Guido van Rossum
# c
#
# Minkä alkuaineen kemiallinen merkki on Si?
# pii
# seleeni
# tina
# a
#
# -----------------------------------------------------------------------------
#
# Huomaa tyhjät rivit yksiköiden välillä, myös viimeisen yksikön perässä.
#
# Testaamista varten kannattaa kehitellä itse toinen kysymys-vastaus-tiedosto,
# jossa on eri määrä vastausvaihtoehtoja. (Vinkki: tähän voi riittää
# sellainenkin, jossa on vain yksi vaihtoehto.)
#
# Ohjelman pitää numeroida kysymykset ja varustaa vastausvaihtoehdot
# kirjaimella silloin kun niitä esitetään käyttäjälle. Kysymykset ja niiden
# vastausvaihtoehdot esitetään siinä järjestyksessä kuin ne ovat
# kysymystiedostossa. Tiedoston nimen saa itse päättää (jos haluat, voit myös
# antaa sen komentoriviparametrina, kts. Pythonin sys.argv).
#
# Vinkki: kannattaa lukea tiedoston rivit yksi kerrallaan, ja pitää yllä tietoa
# siitä, missä mennään, eli onko viimeksi luettu rivi kysymysteksti,
# vastausvaihtoehto, oikean vastauksen kirjain vai tyhjä rivi, joka kertoo,
# että kysymys vaihtuu.
#
# Tehtävän voi palauttaa myös ZIP-pakettina, että saa ohjelman, tiedoston ja
# oppimispäiväkirjan kätevästi samaan nippuun. Kaiken materiaalin voi myös
# toimittaa oppimispäiväkirjassa, kunhan se on muotoiltu niin, että ohjelman ja
# kysymystiedoston (tai -tiedostot) saa helposti käyttöön (eli ei
# kuvakaappauksina). tähän
#
###############################################################################
import sys

QUESTION_FILE_NAME = "KT08_questions.txt"
POSSIBLE_ANSWER_KEYS = "abcdefghijklmnopqrstuvwxyz"

# Constants for question dictionary keys for error free usage.
KEY_QUESTION_TEXT = "text"
KEY_ANSWER_OPTIONS = "answer_options"
KEY_CORRECT_KEY = "correct_key"

# Exit codes
ERR_INVALID_ANSWER_KEY_INDEX = 1
ERR_INVALID_CORRECT_ANSWER_KEY = 2

score = 0
max_score = 0


def read_questions_from_file(filename):
    """
    Reads questions, answer options, and correct answer keys from a file.
    :param filename: file to read
    :return: list of question dictionaries containing question text, list of
    answer options, and correct answer key.
    """
    questions = []

    with open(filename, "r", encoding="utf-8") as f:
        index = 0
        line_index = 0
        question = {}

        for line in f:
            line_index += 1
            line = line.strip()  # Remove trailing whitespace, including \n.

            if index == 0:
                # New question
                question = {
                    KEY_QUESTION_TEXT: line,
                    KEY_ANSWER_OPTIONS: {},
                    KEY_CORRECT_KEY: "",
                }
            elif len(line) > 1:
                # Answer option
                key_index = index - 1
                # Maximum number of answer options is exceeded.
                if key_index >= len(POSSIBLE_ANSWER_KEYS):
                    print(f"Too many answer options! (line {line_index})")
                    sys.exit(ERR_INVALID_ANSWER_KEY_INDEX)
                key = POSSIBLE_ANSWER_KEYS[key_index]
                question[KEY_ANSWER_OPTIONS][key] = line
            elif len(line) == 1:
                # Correct answer key, a ... z
                correct_key = line
                # Validate the key exists in the answer keys.
                if correct_key not in question[KEY_ANSWER_OPTIONS].keys():
                    print(
                        f"Invalid correct answer key '{correct_key}'! "
                        f"(line {line_index})"
                    )
                    sys.exit(ERR_INVALID_CORRECT_ANSWER_KEY)
                question[KEY_CORRECT_KEY] = correct_key
                questions.append(question)
            elif len(line) == 0:
                # Empty line
                index = 0
                continue  # Skip increasing the index.

            index += 1

    return questions


def print_question(question, index):
    """
    Prints the question text and the answer options.
    :param question: question dictionary
    :param index: index of the question in the array
    """
    number = index + 1
    text = question[KEY_QUESTION_TEXT]
    answer_options = question[KEY_ANSWER_OPTIONS]
    print(f"{number}. {text}")

    for k in answer_options:
        print(f"{k}) {answer_options[k]}")


def read_selection(answer_keys):
    """
    Reads the answer selection from the user. If the user enters an invalid
    option, they are prompted to try again.
    :param answer_keys: list of possible answer keys
    :return the selected answer key
    """
    retry = True
    selection = ""

    while retry:
        selection = input("Vastauksesi: ").lower()
        if selection not in answer_keys:
            print("Virheellinen valinta, yritä uudestaan.")
            continue
        retry = False

    return selection


questions = read_questions_from_file(
    input("Anna kysymykset sisältävän " "tiedoston polku: ")
)
max_score = len(questions)

print(f"Tervetuloa tietovisaan! Kysymyksiä on {max_score}.")
print()

for question in questions:
    question_number = questions.index(question)
    print_question(question, question_number)
    selected_answer = read_selection(question[KEY_ANSWER_OPTIONS].keys())
    evaluation = ""

    if selected_answer == question[KEY_CORRECT_KEY]:
        evaluation = "Vastasit oikein!"
        score += 1
    else:
        evaluation = "Vastasit väärin!"

    print(evaluation)
    print()

print(f"Tietovisa päättyi. Sait {score}/{max_score} pistettä.")

###############################################################################
# EOF
