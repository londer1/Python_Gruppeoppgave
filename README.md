# Boknettside

Nettsiden: [Boknettsida](https://boknettsida.streamlit.app/)

Hvis linken ikke fungerer, kan du kjøre nettsiden lokalt ved å gjøre dette:
1. Installer Streamlit: `pip install streamlit`
2. Bruk `cd` for å finne mappen der filen ligger, og `ls` for å se filene.
3. Kjør siden med: `streamlit run bookshelf.py` (eller en av de andre filene).

Hvis du ikke finner filene, sjekk de andre branchene – de kan ligge der.

## Om prosjektet

Vi er tre stykker som jobber sammen med å lage en nettside hvor du kan kjøpe bøker. Alt er laget med Python, og vi bruker Streamlit til å vise nettsiden. For å holde oversikt over bøkene bruker vi SQLite til å lagre:
- Hvor mange bøker som er på lager
- Tittel på bøkene
- Pris på hver bok
