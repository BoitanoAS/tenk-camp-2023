# Workshop instruksjoner
Skriv url til github repoet på tavlen:
https://tinyurl.com/tenkbotiano

## Meldings server:
Reset etter hver gruppe har vært innom
```bash
curl -X DELETE https://tenk-server.fly.dev/clear
```

###  Jupyterlab reset
Siden elevene deler brukere må vi slette tenk mappen etter bruk.

1. Logg in på gcp: https://console.cloud.google.com/compute/instances?project=boitano

1. Finn instans ved navn `tenk-v2`
1. ssh inn på serveren, naviger til `/home`
1. Kjør `sudo chmod +x jupyter-*` i terminalen for å få rett tilgang
1. Slett mappene under alle brukernavn med denne kommandoen: 

````bash
sudo find jupyter-usr*/ -type d -name "tenk-camp-2023" -exec rm -r {} +
````


# Other
## GCP Admin 
### Launch knapp
1. Bruk lenken til å generere url lenken som tar elevene fra github til workshoppen
    * https://nbgitpuller.readthedocs.io/en/latest/link.html
1. For å lage denne tregner man adressen til jupyter serveren den finner her i feltet external IP for `tenk-v2` instansen 
    - https://console.cloud.google.com/compute/instances?referrer=search&project=boitano 
    