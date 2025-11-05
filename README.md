# Tetris Game
Tetris-game ist ein Spiel, das man auf der Konsole eines Computers ausführen kann.

## Installation
Das Klonen dieses Repository mit dem Befehl 'git clone' und der Web-URL funktioniert sowohl unter Windows als auch unter Linux.

Suche zunächst einen passenden Speicherort für das Repository und erstelle dort einen neuen Ordner.
Anschließend wechsle über die Konsole, wie etwa die Windows-Eingabeaufforderung (CMD) oder Bash, mit dem Befehl 'cd' in das gewünschte Verzeichnis.
![image alt](https://github.com/weng0/tetris-game-weng0/blob/main/bilder/neue_Ordner.JPG)
Für Windows-Nutzern könnte das per CMD so aussehen:
![image alt](https://github.com/weng0/tetris-game-weng0/blob/main/bilder/cmd_ordner_gewechselt.JPG)

Klone das Repository, indem du das eingibst:
```bash
![image alt](git clone https://github.com/weng0/tetris-game-weng0.git)
```
https://github.com/weng0/tetris-game-weng0/blob/main/bilder/cmd_geklont.JPG

### Fehlende Curses-Modul nachinstallieren
Das Tetris Spiel funktioniert erst, wenn das entsprechende Modul installiert ist. Insbesondere Windows-Nutzern müssen diesen Schritt ausführen. Gib dazu in der CMD folgenden Befehl ein:
```bash
pip install windows-curses
```

### Issues
...


## Usage
Um das Spiel zu starten, wechsle in den Ordner tetris-game-weng0 und vergrößere das Konsolenfenster.
```bash
py ./tetris-game.py
```
![image alt](https://github.com/weng0/tetris-game-weng0/blob/main/bilder/spiel_beginn.JPG)

### Spielregeln

Bei Tetris geht es darum, unterschiedlich geformte Blöcke nacheinander auf das Spielfeld fallen zu lassen.
Ziel ist es, zu verhindern, dass sich die Blöcke bis zum oberen Rand des Spielfelds auftürmen.
Dies gelingt, indem man die Blöcke nach links oder rechts bewegt, um passende Lücken zu füllen.

(Bild Steuerung Taste L u R)

Sobald man eine passende Lücke gefunden hat, kann man den Block mit der Pfeiltaste nach unten schneller fallen lassen.

(Bild Down-Taste)

Wenn durch das Platzieren eines Blocks eine Reihe vollständig gefüllt ist, wird diese aufgelöst und man erhält einen Punkt.

Passt ein Block nicht in die Lücke, kann man ihn rotieren, bis er die richtige Form hat.
Zum Rotieren verwende die Taste R.

(Bild Rotation)
