import csv
import matplotlib.pyplot as plt

def daten_einlesen(dateipfad):
    """Liest Buchdaten aus einer CSV-Datei ein."""
    buchdaten = []
    with open(dateipfad, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            buchdaten.append(row)
    return buchdaten

def suche_autor(buchdaten, autor):
    """Sucht alle Bücher eines bestimmten Autors."""
    return [buch for buch in buchdaten if buch['Autor'].lower() == autor.lower()]

def visualisiere_veroeffentlichungsjahre(buecher, autor):
    """Erstellt ein Diagramm der Veröffentlichungsjahre für Bücher eines Autors."""
    jahre = [int(buch['Jahr']) for buch in buecher]
    jahr_counts = {jahr: jahre.count(jahr) for jahr in set(jahre)}
    
    plt.bar(jahr_counts.keys(), jahr_counts.values())
    plt.title(f"Veröffentlichungsjahre von Büchern des Autors {autor}")
    plt.xlabel("Jahr")
    plt.ylabel("Anzahl der Bücher")
    plt.show()

def neuen_autor_hinzufuegen(dateipfad, titel, autor, jahr):
    """Fügt ein neues Buch zu den Daten hinzu."""
    with open(dateipfad, 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([titel, autor, jahr])

# Hauptprogramm
def main():
    dateipfad = 'bibliothek.csv'

    print("Buchsuche in der Bibliothek")
    buchdaten = daten_einlesen(dateipfad)
    
    while True:
        print("\nMenü:")
        print("1. Suche nach einem Autor")
        print("2. Neuen Autor und Buch hinzufügen")
        print("3. Beenden")
        auswahl = input("Bitte wählen Sie eine Option: ")

        if auswahl == '1':
            autor = input("Geben Sie den Namen des Autors ein: ")
            buecher = suche_autor(buchdaten, autor)
            if buecher:
                print(f"Gefundene Bücher von {autor}:")
                for buch in buecher:
                    print(f"- {buch['Titel']} ({buch['Jahr']})")
                visualisiere_veroeffentlichungsjahre(buecher, autor)
            else:
                print(f"Keine Bücher von {autor} gefunden.")

        elif auswahl == '2':
            titel = input("Titel des Buches: ")
            autor = input("Autor des Buches: ")
            jahr = input("Veröffentlichungsjahr des Buches: ")
            neuen_autor_hinzufuegen(dateipfad, titel, autor, jahr)
            print(f"Das Buch '{titel}' von {autor} wurde hinzugefügt.")

        elif auswahl == '3':
            print("Programm beendet.")
            break

        else:
            print("Ungültige Option. Bitte versuchen Sie es erneut.")

if __name__ == "__main__":
    main()
