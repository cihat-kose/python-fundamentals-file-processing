# Gokstad Akademiet – Arbeidskrav 1 (Python)

## Oversikt
Dette repositoriet inneholder løsningsforslagene til Arbeidskrav 1 i Python. Oppgavene dekker grunnleggende programmering, datastrukturer, funksjoner, filhåndtering og enkel dataanalyse, og følger kravene i `python2025_arbeidskrav1_oppgavetekst.pdf`.

## Prosjektstruktur
| Mappe | Innhold |
| --- | --- |
| `oppgave1_grunnprogrammering/` | Interaktive skript som trener på summasjon, strenglengde, multiplikasjonstabeller og listeoperasjoner (`oppgave1_1.py`–`oppgave1_5.py`). |
| `oppgave2_datastrukturer/` | Løsningsforslag som validerer datoer, splitter/strukturerer lister og dictionaries, og sorterer data (`oppgave2_1.py`–`oppgave2_6.py`). |
| `oppgave3_funksjoner/` | Funksjoner for IPv4-validering, datoforskjell, RGB→HEX-konvertering og enkel funksjonstesting (`oppgave3_1.py`–`oppgave3_4.py`). |
| `oppgave4_opprette_filstruktur_og_sortere_filer/` | Skript som genererer en filstruktur med tilfeldige filer og sorterer dem etter filtype (`oppgave4_1.py`, `oppgave4_2.py`). |
| `oppgave5_fil_analyse/` | CSV-data (`bokutlån.csv`) og analyser som summerer forlengelser, teller sjangre, beregner lånetid, finner manglende innleveringer og mest utlånte titler (`oppgave5_1.py`–`oppgave5_5.py`). |

## Komme i gang
1. Installer Python 3.11 eller nyere.
2. Klon repositoriet eller pakk det ut lokalt.
3. Naviger til rotmappen i et terminalvindu.
4. Kjør ønsket skript med `python path/til/fil.py`. (Flere skript i Oppgave 1 og Oppgave 2 ber om input i terminalen.)

### Tips for oppgavekategoriene
- **Oppgave 1**: Kjør filene direkte for å løse små terminaloppgaver.
- **Oppgave 2**: Skriptene leser/bygger datastrukturer i minnet og skriver resultatet til terminalen.
- **Oppgave 3**: Hver fil definerer én hovedfunksjon; du kan importere funksjonene i egne tester eller kjøre filene direkte for eksempler.
- **Oppgave 4**: Kjør `oppgave4_1.py` først for å generere `Files/`. Deretter sorterer `oppgave4_2.py` filene inn i `SortedFiles/`. Skriptene kan kjøres flere ganger for å regenerere strukturen.
- **Oppgave 5**: Programfilene leser `bokutlån.csv`. Sørg for at filen ligger i samme mappe når skriptene kjøres.

## Leveringsrutine (arbeidskrav)
- Arbeidskrav publiseres i temaet «Arbeidskrav» på Min GA og leveres i den tilhørende innleveringen.
- Lag en tydelig hovedmappe for prosjektet. Du kan bruke undermapper pr. oppgave (som i dette repositoriet) eller velstrukturerte filnavn i én mappe.
- Pakk hele prosjektmappen som `.zip` før innlevering.

## Bruk av AI
Bruk av AI er tillatt så lenge all relevant bruk dokumenteres. Ta vare på prompt og svar for AI-verkøy som har bidratt direkte til løsningen, og inkluder dem i README eller i en egen fil. Alternativt kan du oppgi at AI ikke er brukt for en bestemt del. Denne README-en er utarbeidet ved hjelp av ChatGPT for å oppsummere prosjektet; kildekoden er skrevet manuelt.
