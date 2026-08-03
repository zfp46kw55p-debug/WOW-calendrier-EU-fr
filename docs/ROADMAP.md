# Feuille de route

Ce document présente les objectifs du projet **WoW Calendrier EU FR**.

Il permet de suivre les évolutions prévues et de définir le périmètre de chaque version.

---

# Vision

Créer le calendrier iCalendar (ICS) francophone de référence pour **World of Warcraft Retail Europe**.

Le projet privilégie :

- la fiabilité ;
- la simplicité ;
- la cohérence ;
- la pérennité.

---

# Version 1.0

Objectif : disposer d'un calendrier stable, documenté et entièrement fonctionnel.

## Données

- [ ] Holidays
- [ ] Micro-holidays
- [ ] Weekly Events
- [ ] Fishing Events
- [ ] World Bosses
- [ ] Seasons
- [ ] Special Events
- [ ] History

---

## Documentation

- [x] README
- [x] CONTRIBUTING
- [x] CHANGELOG
- [x] EDITORIAL_POLICY
- [x] STYLE_GUIDE
- [x] DATA_SOURCES
- [x] QA_CHECKLIST
- [ ] ARCHITECTURE

---

## Scripts

- [ ] build.py
- [ ] validate.py
- [ ] event_data.py
- [ ] check.py

---

## GitHub

- [ ] Workflow CI
- [ ] Validation automatique
- [ ] Génération automatique du calendrier
- [ ] Publication du fichier ICS

---

# Version 1.1

Améliorations possibles après la première publication.

## Données

- Rotation complète des événements hebdomadaires.
- Nouveaux événements ajoutés par Blizzard.
- Vérification annuelle des dates.

## Fonctionnalités

- Validation avancée des données.
- Contrôles supplémentaires.
- Amélioration des messages d'erreur.

---

# Version 1.2

Évolutions à long terme.

Exemples :

- prise en charge d'autres langues ;
- prise en charge d'autres régions ;
- génération de plusieurs calendriers ;
- nouvelles catégories d'événements.

---

# Hors périmètre

Le projet n'a pas vocation à :

- remplacer Wowhead ;
- remplacer les guides de jeu ;
- expliquer les stratégies ;
- détailler les récompenses.

Il fournit uniquement les informations nécessaires à un calendrier.

---

# Priorité actuelle

1. Finaliser les données.
2. Vérifier les scripts.
3. Publier la version 1.0.
4. Assurer la maintenance.

---

# Maintenance

Après la publication de la version 1.0 :

- vérifier régulièrement les annonces Blizzard ;
- contrôler les changements d'événements ;
- mettre à jour les dates annuelles ;
- maintenir la documentation.

Le projet évolue progressivement afin de conserver une qualité constante.
