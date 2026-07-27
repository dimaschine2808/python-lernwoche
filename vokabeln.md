# Programmier-Vokabeln für Einsteiger

Die meisten Begriffe beim Programmieren sind Englisch. Wenn du sie kennst, verstehst du Tutorials, Fehlermeldungen und Code viel leichter. Lern sie nach und nach – nicht alle auf einmal.

---

## Schon benutzt (Tag 1 & 2)

**variable** (Variable)
Eine „Box" mit Namen, in der du einen Wert speicherst. Beispiel: `alter = 21`

**string** (Zeichenkette / Text)
Text in Anführungszeichen. Beispiel: `"Hallo"`. Merksatz: **str** = String = Text.

**integer** (Ganzzahl)
Eine ganze Zahl ohne Komma. Beispiel: `5`, `-3`, `100`. Kurzform in Python: `int`

**float** (Kommazahl)
Eine Zahl mit Komma (im Englischen mit Punkt). Beispiel: `3.14`, `0.75`

**print** (ausgeben / drucken)
Zeigt etwas auf dem Bildschirm an. Beispiel: `print("Hallo")`

**input** (Eingabe)
Fragt den Nutzer nach etwas. Beispiel: `input("Wie heißt du? ")`

**f-string** (formatierter String)
Text, in den man Variablen direkt einbauen kann. Beispiel: `f"Hallo {name}"`

**function** (Funktion)
Ein Befehl, der etwas tut. `print()` und `input()` sind Funktionen. Erkennbar an den Klammern `()`.

**syntax** (Syntax)
Die „Grammatik" einer Programmiersprache – die Regeln, wie Code geschrieben werden muss.

**error** (Fehler)
Eine Fehlermeldung. Kein Grund zur Panik – sie sagt dir, was nicht stimmt und wo.


## Tag 3 

**condition** (Bedingung)

Eine Prüfung, die True oder False ergibt. Beispiel: ,,alter >= 18" 

**and / or** (und / oder)
Verbindet zwei Bedingungen. 'and' = beide muessen zutreffen, 'or' = eine reicht.

**modulo** (Restwert, Zeichen '%')
Gibst den Rest einer Division zurück. '7 % 2' ergibt '1'. Damit prüft man gerade/ungerade. 

**indentation**  (Einddrückung)
Die Leerzeichen am Zeilenanfangen. In Python Pflicht - sie zeigen, was zu einem 'if' gehört. 

**ValueError** (Wertfehler)
Fehlermeldung, wenn ein Wert nicht ins erwartete Format passt - z. B. Text, der keine Zahl ist 



## Tag 4 

**loop** (Schleife) 
Wiederholt einen Codeblock mehrmahls, ohne dass man ihn kopieren muss. 

**for loop** (Zählschleife) 
Schleife fuer den Fall, dass man weiss, wie oft wiederholt werden soll. 

**while loop** (Bedingungsschleife)
Läuft so lange, wie eine Bedingung wahr ist. Beispiel: 'while zahl >= 0:'

**range** (Bereich)
Erzeugt eine Zahlenfolge für Schleifen. ´range (1, 11)´ gibt 1 bis 10 - der Endweder ist immer ausgeschlossen!
Mit drittem Wert auch rückwärts: ´range(10, -1, -1)´ = Start, Ende, Schrittweise.

**iteration** (Durchlauf)
Ein einzelner Durchgang einer Schleife. Bei 'range(5)' gibt es fünf iterationen. 

**counter variable** (Zählvariable)
Die Variable, die bei jedem Durchlauf den nächsten Wer bekommt - meist 'i' genannt. 

**infinte loop** (Endlosschleife) 
Eine Schleife, ddie nie endet, weil sich ddie Bedingung nie ändert. Abbrechen mit `Strg + C`. 


## Tag 5 

**list**  (Liste)
Speichert mehrere Werte in einer Variable. Beispiel: '["Matrix, "inception"]'

**index** (Inex / Position)
Die Position eines Elements. Beginnt bei 0! 'liste[0]' ist das erste Element, 'liste[-1]' das letzte. 

**append** (anhängen)
Fuegt ein Element hinten an die Liste an. Beispiel: 'filme.append("Heat")'

**len** (lenght / Laenge)
Gibt die Anzahl er Elemente zurueck. Beispiel: 'len(filme)'

**NameError** (Namensfehler)
Fehlermeldung, wenn Python eine Variable nicht erkennt - meist Tippfehler oder falsche Gross-/Kleinschreibung.\

**case-sensitive** (Gross/Kleinschreibung beachtend)
Python unterscheidet strikt: 'Filme', 'filme' und 'FILME' sind verschiedene Variablen. 












---

## Rund um Git & GitHub

**repository / repo** (Repository)
Ein Projekt-Ordner, den Git verwaltet. Dein Code-Zuhause.

**commit** (Festschreibung)
Ein gespeicherter Stand deiner Änderungen. Wie ein Speicherpunkt im Spiel.

**push** (hochladen)
Deine lokalen Commits zu GitHub hochladen.

**pull** (herunterholen)
Änderungen von GitHub zu dir herunterladen.

**branch** (Zweig)
Eine parallele Arbeitslinie im Projekt. Der Standard heißt `main`.

**clone** (klonen)
Ein Repo von GitHub auf deinen Computer kopieren.

**blame** ("Schuld")
Git-Funktion, die zeigt, wer welche Zeile geschrieben hat. (Ja, GitHub übersetzt das lustig mit „Schuld".)

---

## Kommt bald (Tag 3–7)

**condition** (Bedingung)
Eine Ja/Nein-Prüfung. Beispiel: „Ist die Zahl größer als 10?"

**if / else** (wenn / sonst)
Lässt das Programm Entscheidungen treffen. „**Wenn** X, dann..., **sonst**..."

**loop** (Schleife)
Wiederholt etwas mehrmals, ohne Code zu kopieren.

**list** (Liste)
Speichert mehrere Werte in einer Variable. Beispiel: `["Apfel", "Birne", "Kirsche"]`

**parameter** (Parameter)
Ein Wert, den du einer Funktion mitgibst. Bei `print("Hallo")` ist `"Hallo"` das Argument.

**return** (zurückgeben)
Wenn eine Funktion ein Ergebnis zurückliefert.

**import** (importieren)
Zusätzliche Werkzeuge ins Programm holen. Beispiel: `import random` für Zufallszahlen.

---

## Häufige englische Wörter in Fehlermeldungen

| Englisch | Bedeutung |
|----------|-----------|
| `not defined` | nicht definiert (Variable existiert nicht / Tippfehler) |
| `invalid` | ungültig |
| `expected` | erwartet (da fehlt etwas) |
| `unexpected` | unerwartet (da ist etwas zu viel) |
| `missing` | fehlt |
| `line` | Zeile (sagt dir, WO der Fehler ist) |
| `division by zero` | Teilen durch Null (geht nicht!) |

---

**Lern-Tipp:** Du musst diese Wörter nicht auswendig pauken. Sie prägen sich von selbst ein, während du sie benutzt. Schau einfach ab und zu hier rein, wenn dir ein Begriff unklar ist.