# GHGL aan elkaar knopen


* Maak nieuwe repository (public) vanuit een template of open een bestaande GH repo. (Hier is aangenomen dat er al een GH workflow bestaat)
* Ga naar GL en maak een nieuw project met dezelfde naam als de repo op GH (zodat zichtbaar is dat het om dezelfde repo gaat).
* Kies voor *Import project* en vervolgens *GitHub*.
* Je wordt nu gevraagd om een personal access token in te voeren welke aan gemaakt moet worden op GH.
* Klik op de link [https://github.com/settings/tokens](personal access token) in GL.
* Klik op *Generate new token* en kies voor classic. 
* Maak een titel, kies een expiration date en vink repo en workflow aan, zie printscreen

![](GHPAT.PNG)

* Klik *Generate token* en kopieer de PAT in de GL en klik *Authenticate*.  
* Importeer nu de repo die je wilt kopiëren.
* Wanneer alle bestanden zijn gekopieerd van GH naar GL, ga naar je GL repo, klik op *settings* en dan *access tokens* om een nieuwe access token aan te maken. Kies voor *owner* en vink *api*, *read_repository* en *write_repository* aan. Kies een zo lang mogelijke *expiration date* zodat GH zo lang mogelijk schrijfrechten naar GL heeft.
* Kopieer de access token en ga naar GH / secrets and variables / actions en creeer een *New repository secret*. Geef deze een duidelijk naam, bijv. *GLPAT*.
* Open de github workflow en voeg onderstaande script toe aan de workflow (onderaan)

```
name: Sync Changed Files to GitLab

on:
  push:
    branches: [main]

jobs:
  sync-changes:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout GitHub repo (source)
        uses: actions/checkout@v4

      - name: Set up GitLab repo (destination)
        env:
          GITLAB_TOKEN: ${{ secrets.GLGH_PAT }}
        run: |
          # Clone GitLab repo
          git clone https://oauth2:${GITLAB_TOKEN}@gitlab.tudelft.nl/opentextbooks/TN_MechaRela.git gitlab-mirror
          
          # Set up Git config
          cd gitlab-mirror
          git config user.name "GitHub Actions"
          git config user.email "actions@github.com"
          cd ..

      - name: Copy only changed files
        run: |
          # Compare and copy only changed files from GitHub to GitLab clone
          rsync -av --delete --exclude='.git' --exclude='gitlab-mirror/' ./ ./gitlab-mirror/

      - name: Commit and push changes
        env:
          GITLAB_TOKEN: ${{ secrets.GLGH_PAT }}
        run: |
          cd gitlab-mirror
          git add .
          
          # Only commit if there are changes
          if ! git diff --cached --quiet; then
            git commit -m "Sync changed files from GitHub"
            git push https://oauth2:${GITLAB_TOKEN}@gitlab.tudelft.nl/opentextbooks/TN_MechaRela.git main
          else
            echo "No changes to commit"
          fi
```

* Let op, vervang de GL repo link en de naam van de repository secret (hier GLPAT).
* De connectie tussen GH en GL is nu gemaakt. Elke commit naar GH wordt nu ook gecommit naar GL.
* rsync vergelijkt bestanden op basis van wijzigingsdatum en bestandsgrootte. Dit zorgt ervoor dat alleen gewijzigde of nieuwe bestanden naar GitLab gekopieerd worden. 

