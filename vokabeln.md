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

## Tag 6

**dictionary / dict** (Wörterbuch)
Speichert Werte als Schlüssel-Wert-Paare, nicht nach Position wie eine Liste. Beispiel: `vokabeln = {"Blume": "Flower"}`

**key** (Schlüssel)
Der Name, über den man einen Wert im Dictionary findet. Bei `vokabeln["Blume"]` ist `"Blume"` der Key.

**value** (Wert)
Der Wert, der zu einem Key gehört. Bei `vokabeln["Blume"]` ist `"Flower"` der Value.

**.items()** (Einträge)
Gibt alle Schlüssel-Wert-Paare eines Dictionarys zurück, z. B. für `for key, value in vokabeln.items():`

**in** (Mitgliedschaftstest)
Prüft, ob etwas enthalten ist. Bei Dictionarys prüft `wort in vokabeln` nur die Keys, nicht die Values.


## Tag 7

**break** (abbrechen)
Beendet eine Schleife sofort, egal ob die eigentliche Bedingung noch erfüllt wäre. Meist zusammen mit `if` benutzt.

**while True** (Endlos-Schleife mit Ausstieg)
Läuft absichtlich für immer, bis irgendwo im Code ein `break` ausgeführt wird. Häufiges Muster für "frag immer wieder, bis der Nutzer aufhören will".

**strip()** (Leerzeichen entfernen)
Entfernt Leerzeichen (und Zeilenumbrüche) am Anfang und Ende eines Strings. Nützlich bei Vergleichen mit `input()`, weil ein Tippfehler-Leerzeichen sonst den Vergleich scheitern lässt.

**insert** (einfügen)
Fügt ein Element an einer bestimmten Position in die Liste ein, nicht nur ans Ende wie `append`. Beispiel: `liste.insert(1, "Kaffee")`

**remove** (entfernen)
Löscht das erste Element mit einem bestimmten Wert aus der Liste. Beispiel: `liste.remove("Milch")`

**pop** (herausnehmen)
Entfernt das letzte Element (oder eins an einem Index) und gibt es gleichzeitig zurück. Beispiel: `letztes = liste.pop()`

**sort / reverse** (sortieren / umkehren)
`sort()` sortiert die Liste aufsteigend (mit `reverse=True` absteigend), `reverse()` dreht die Reihenfolge einfach um, ohne zu sortieren.

**count** (zählen)
Gibt zurück, wie oft ein Wert in der Liste vorkommt. Beispiel: `zahlen.count(3)`

**slicing** (Ausschneiden)
Holt sich einen Teilbereich einer Liste über `[start:stop:schritt]`. Beispiel: `zahlen[:3]` = erste drei Elemente.


## Tag 8

**def** (Funktion definieren)
Leitet die Definition einer eigenen Funktion ein. Beispiel: `def ist_gerade(zahl):`

**argument** (Argument)
Der konkrete Wert, der beim Aufruf an eine Funktion übergeben wird. Bei `ist_gerade(4)` ist `4` das Argument; `zahl` in der Funktionsdefinition ist der Parameter.

**boolean / bool** (Wahrheitswert)
Ein Wert, der nur `True` oder `False` sein kann. Beispiel: `zahl % 2 == 0` liefert einen Boolean.


## Tag 9

**nested loop** (verschachtelte Schleife)
Eine Schleife innerhalb einer anderen Schleife. Die innere Schleife läuft für jeden Durchgang der äußeren Schleife vollständig durch.

**outer loop / inner loop** (äußere / innere Schleife)
Die äußere Schleife wählt zum Beispiel eine `gruppe`; die innere Schleife verarbeitet anschließend jede einzelne `zahl` dieser Gruppe.

**nested condition** (verschachtelte Bedingung)
Ein `if` innerhalb eines anderen `if`. Die innere Bedingung wird nur geprüft, wenn die äußere Bedingung erfüllt ist.


## Tag 10

**try** (versuchen)
Markiert einen Codeblock, in dem ein erwartbarer Fehler auftreten kann. Python versucht, diesen Code normal auszuführen.

**except** (Fehler abfangen)
Wird ausgeführt, wenn im zugehörigen `try`-Block der angegebene Fehler auftritt. So kann das Programm verständlich reagieren, statt abzustürzen.

**ValueError** (Wertfehler)
Entsteht zum Beispiel, wenn `int()` einen Text wie `"Hallo"` in eine ganze Zahl umwandeln soll.

**continue** (nächster Durchlauf)
Bricht nur den aktuellen Schleifendurchlauf ab und beginnt sofort mit dem nächsten. In Tag 10 wird damit nach einer falschen Eingabe erneut gefragt.

**min / max** (Minimum / Maximum)
`min(liste)` gibt den kleinsten und `max(liste)` den größten Wert einer nicht leeren Liste zurück.

**sum** (Summe)
Addiert alle Zahlen einer Liste. Zusammen mit `len()` lässt sich damit der Durchschnitt berechnen.


## Tag 11

**file** (Datei)
Speichert Daten dauerhaft auf einem Datenträger. Anders als Variablen bleibt der Inhalt nach dem Ende des Programms erhalten.

**open()** (Datei öffnen)
Öffnet eine Datei zum Lesen oder Schreiben. Beispiel: `open("einkaufsliste.txt", "r", encoding="utf-8")`

**with** (Kontextblock)
Sorgt dafür, dass eine geöffnete Datei nach dem eingerückten Block automatisch wieder geschlossen wird.

**file mode** (Dateimodus)
Bestimmt, was mit einer Datei geschieht: `"r"` liest, `"w"` überschreibt und `"a"` hängt neuen Inhalt an.

**write()** (schreiben)
Schreibt einen String in eine geöffnete Datei. Ein Zeilenumbruch muss bei Bedarf mit `"\n"` ergänzt werden.

**readlines()** (Zeilen lesen)
Liest alle Zeilen einer Datei und gibt sie als Liste von Strings zurück. Die Zeilen enthalten normalerweise noch `"\n"`.

**encoding / UTF-8** (Zeichenkodierung)
Legt fest, wie Textzeichen gespeichert und gelesen werden. `encoding="utf-8"` unterstützt unter anderem Umlaute zuverlässig.


## Tag 12

**key access** (Schlüsselzugriff)
Ruft einen Dictionary-Wert über seinen Schlüssel ab. Beispiel: `lager["Milch"]`

**dictionary assignment** (Dictionary-Zuweisung)
Legt einen neuen Schlüssel an oder ersetzt den Wert eines vorhandenen Schlüssels. Beispiel: `lager["Mandeln"] = 4`

**KeyError** (Schlüsselfehler)
Entsteht beim direkten Zugriff auf einen Schlüssel, der nicht im Dictionary existiert. Eine vorherige Prüfung mit `in` verhindert diesen Fehler.


## Tag 13

**get()** (Wert sicher abrufen)
Liest einen Dictionary-Wert und liefert bei einem fehlenden Schlüssel einen Ersatzwert. Beispiel: `lager.get(produkt, 0)`

**default value** (Standardwert)
Der Ersatzwert, der benutzt wird, wenn kein passender Eintrag existiert. Bei `lager.get(produkt, 0)` ist `0` der Standardwert.

**+=** (erhöhen und zuweisen)
Addiert einen Wert und speichert das Ergebnis direkt zurück. `bestand += 4` bedeutet `bestand = bestand + 4`.

**-=** (verringern und zuweisen)
Zieht einen Wert ab und speichert das Ergebnis direkt zurück. `bestand -= 2` bedeutet `bestand = bestand - 2`.

**comparison / assignment** (Vergleich / Zuweisung)
`==` prüft, ob zwei Werte gleich sind. `=` weist einen Wert zu; `+=` und `-=` verändern und speichern ihn.


## Tag 14

**module / import** (Modul / importieren)
Ein Modul stellt zusätzliche Funktionen bereit. Mit `import json` werden die JSON-Werkzeuge geladen.

**JSON** (JavaScript Object Notation)
Ein verbreitetes Textformat für strukturierte Daten. Python-Dictionaries können damit lesbar in einer Datei gespeichert werden.

**json.dump()** (JSON speichern)
Schreibt Python-Daten in eine geöffnete JSON-Datei. Reihenfolge: `json.dump(daten, datei)` — Inhalt zuerst, Datei danach.

**json.load()** (JSON laden)
Liest JSON-Daten aus einer geöffneten Datei und erzeugt daraus wieder Python-Daten, zum Beispiel ein Dictionary.

**indent** (Einrückung)
Formatiert gespeichertes JSON mit Einrückungen. `indent=4` macht die Datei für Menschen leichter lesbar.

**ensure_ascii** (ASCII-Ersetzung steuern)
Mit `ensure_ascii=False` bleiben Umlaute und andere Unicode-Zeichen in der JSON-Datei direkt lesbar.

**relative path** (relativer Dateipfad)
Ein Pfad ohne vollständige Laufwerksangabe. Er beginnt im aktuellen Arbeitsordner, nicht automatisch im Ordner der Python-Datei.

**working directory** (Arbeitsordner)
Der Ordner, von dem aus ein Programm gestartet wird. Bei dir war das `C:\Users\dimik\PythonProjekte`.

**FileNotFoundError** (Datei nicht gefunden)
Entsteht, wenn Python am angegebenen Pfad keine Datei findet. Bei relativen Pfaden sollte zuerst der Arbeitsordner geprüft werden.

**persistence** (dauerhafte Speicherung)
Bedeutet, dass Änderungen nach dem Programmende erhalten bleiben. Dafür gilt hier die Reihenfolge: laden, verändern, speichern.


## Tag 19

**not in** (nicht enthalten)
Prüft, ob ein Wert nicht in einer Sammlung vorhanden ist. `produkt not in lager` erkennt ein unbekanntes Produkt.

**boolean return value** (boolescher Rückgabewert)
Eine Funktion gibt `True` für Erfolg und `False` für Misserfolg zurück. Der aufrufende Code kann damit entscheiden, ob anschließend gespeichert werden soll.

**guard clause** (frühe Abbruchprüfung)
Eine ungültige Situation wird am Anfang einer Funktion geprüft und mit `return` beendet. Dadurch bleibt der erfolgreiche Ablauf übersichtlich.


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

## Weitere Grundbegriffe zum Nachschlagen

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
