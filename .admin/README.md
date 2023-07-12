# Workshop instruksjoner

1. Legg ut en lapp på hver pult med brukernavn og passord. Dette skal elevene bruke til å logge inn på sin personlige jupyterhub

2. Skriv url til github repoet på tavlen:
https://tinyurl.com/tenkbotiano

## Meldings server:
TODO: Burde vi resette denne etter hver gruppe?

## GCP Admin 
### Launch knapp
1. Bruk lenken til å generere url lenken som tar elevene fra github til workshoppen
    * https://nbgitpuller.readthedocs.io/en/latest/link.html
1. For å lage denne tregner man adressen til jupyter serveren den finner her i feltet external IP for `tenk-camp-vm` instansen 
    - https://console.cloud.google.com/compute/instances?referrer=search&project=boitano 
    

1. Fyll inn de andre feltene og oppdater README filen til prosjektet

###  Jupyterlab admin

1. For å gjøre admin arbeid må du åpne en web-terminal, koble til med ssh.

1. Naviger til `home` dir og hvis du sliter med tilgang til de ulike mappene kjør `sudo chmod +x jupyter-*` i terminalen

1. Det eneste admin arbeidet som er nødvendig er å slette alle tenk-camp-2023 mappene fra de ulike brukerene dette kan gjøres med følgende kommando:

    ````bash
    sudo find jupyter-usr*/ -type d -name "tenk-camp-2023" -exec rm -r {} +
    ````
