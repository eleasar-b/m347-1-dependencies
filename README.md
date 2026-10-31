# Demo Abhängigkeiten (M347 Block 1)
 
`app_a.py` läuft nur mit Pydantic 1, `app_b.py` nur mit Pydantic 2.
 
## Vorbereitung (einmalig, PowerShell)
 
```powershell
wsl --install -d Ubuntu-24.04 # falls noch nicht vorhanden
mkdir C:\wsl
wsl --export Ubuntu-24.04 C:\wsl\ubuntu.tar
wsl --import m347-1-demo-a C:\wsl\m347-1-demo-a C:\wsl\ubuntu.tar
wsl --import m347-1-demo-b C:\wsl\m347-1-demo-b C:\wsl\ubuntu.tar

git clone https://github.com/eleasar-b/m347-1-dependencies.git C:\Development
```
 
## Vorbereitung in beiden Distros
 
`wsl -d m347-1-demo-a` bzw. `wsl -d m347-1-demo-b` (importierte Distros starten als root):
 
```bash
apt update && apt install -y python3-pip
echo 'export PIP_BREAK_SYSTEM_PACKAGES=1' >> ~/.bashrc
python3 -c "import pydantic" # Schlägt mit `ModuleNotFoundError` fehl
```
 
`PIP_BREAK_SYSTEM_PACKAGES` erlaubt `pip install` ins System-Python (PEP 668). So bleibt der Befehl auf der Folie kurz.
 
## Ablauf
 
In beiden Terminals: `cd /mnt/c/Development/m347-1-dependencies`
 
| # | Distro | Befehl | Ergebnis |
| --- | --- | --- | --- |
| 1 | demo-a | `python3 app_a.py` | `ModuleNotFoundError: No module named 'pydantic'` |
| 2 | demo-a | `pip install pydantic==1.10.27` | installiert |
| 3 | demo-a | `python3 app_a.py` | `{'gruss': 'Hallo von App A'}` |
| 4 | demo-b | `pip install pydantic==2.14.2` | installiert |
| 5 | demo-b | `python3 app_b.py` | `{'gruss': 'Hallo von App B'}` |
| 6 | demo-b | `python3 app_a.py` | `PydanticImportError: BaseSettings has been moved to the pydantic-settings package` |
| 7 | demo-a | `python3 app_b.py` | `AttributeError: 'Cfg' object has no attribute 'model_dump'` |
 
Optionales Finale auf demo-b: `pip install pydantic==1.10.27`. Danach läuft App A, jedoch App B nicht mehr.
 
## Zurücksetzen
 
```bash
pip uninstall -y pydantic   # reicht, damit Schritt 1 wieder scheitert
```
 
Oder beide Distros mit `wsl --unregister m347-1-demo-a` / `m347-1-demo-b` löschen und neu importieren.