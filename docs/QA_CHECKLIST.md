# Contrôle qualité (QA)

Cette liste de contrôle doit être parcourue avant chaque publication du calendrier.

---

# 1. Validation des données

## JSON

- [ ] Tous les fichiers JSON sont valides.
- [ ] Tous les fichiers utilisent le format attendu.
- [ ] Aucun fichier vide.
- [ ] Aucun doublon d'identifiant (`id`).
- [ ] Aucun doublon d'identifiant unique (`uid`).

---

## Dates

- [ ] Toutes les dates sont au format `YYYYMMDD`.
- [ ] Toutes les dates correspondent au calendrier Retail Europe.
- [ ] Les dates de fin (`end`) respectent le principe DTEND exclusif.

---

## Catégories

- [ ] Toutes les catégories sont valides.
- [ ] Aucun événement dans une mauvaise catégorie.

---

## Descriptions

- [ ] Une ou deux phrases maximum.
- [ ] Commencent par un verbe d'action lorsque cela est pertinent.
- [ ] Aucune stratégie de jeu.
- [ ] Aucun spoiler inutile.
- [ ] Français correct.
- [ ] Style homogène.

---

## Titres

- [ ] Nom officiel Blizzard FR.
- [ ] Emoji cohérent.
- [ ] Aucun titre en anglais.

---

## Lieux

- [ ] Lieu principal uniquement.
- [ ] Nom officiel français.

---

## Sources

- [ ] Au moins une source.
- [ ] Sources accessibles.
- [ ] URLs HTTPS.

---

# 2. Validation technique

- [ ] `validate.py` ne retourne aucune erreur.
- [ ] `build.py` génère correctement le calendrier.
- [ ] `wow-eu.ics` est généré.
- [ ] Le fichier ICS est valide.
- [ ] Aucun UID dupliqué.

---

# 3. Contrôle GitHub

- [ ] README à jour.
- [ ] CHANGELOG mis à jour.
- [ ] Documentation cohérente.
- [ ] Workflow GitHub Actions fonctionnel.

---

# 4. Vérification du calendrier

- [ ] Import Outlook.
- [ ] Import Google Agenda.
- [ ] Import Apple Calendrier.

---

# 5. Vérification visuelle

- [ ] Emojis cohérents.
- [ ] Descriptions lisibles.
- [ ] Aucun caractère incorrect.
- [ ] Encodage UTF-8.

---

# Validation

Version :

Date :

Contrôlé par :

Remarques :
