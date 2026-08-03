# Sources de données

Ce document recense les sources utilisées pour maintenir le projet **WoW Calendrier EU FR**.

L'objectif est de garantir la cohérence des données et de faciliter les mises à jour futures.

---

# Principe général

Les informations sont toujours recherchées selon l'ordre de priorité suivant.

## 1. Client officiel World of Warcraft (FR)

Référence absolue pour :

- les noms des événements ;
- les noms des zones ;
- les noms des PNJ ;
- les traductions françaises.

Lorsque le client fournit une traduction officielle, elle prévaut sur toute autre source.

---

## 2. Blizzard France

https://worldofwarcraft.blizzard.com/fr-fr/

Utilisé pour :

- annonces officielles ;
- calendrier annuel ;
- nouveautés ;
- changements d'événements.

---

## 3. Wowhead France

https://www.wowhead.com/fr/

Utilisé pour :

- fiches d'événements ;
- localisation des PNJ ;
- récompenses ;
- dates ;
- descriptions.

Wowhead FR est généralement la meilleure référence communautaire francophone.

---

## 4. Blizzard International

https://worldofwarcraft.blizzard.com/

Utilisé lorsque l'information n'existe pas en français.

---

## 5. Wowhead International

https://www.wowhead.com/

Permet de vérifier :

- identifiants ;
- mécaniques ;
- changements PTR ;
- informations absentes de Wowhead FR.

---

## 6. Warcraft Wiki

https://warcraft.wiki.gg/

Utilisé principalement pour :

- contexte historique ;
- événements anciens ;
- références encyclopédiques.

---

# Sources par catégorie

## Holidays

Priorité :

1. Blizzard FR
2. Wowhead FR

---

## Micro-holidays

Priorité :

1. Client FR
2. Wowhead FR
3. Blizzard FR

---

## Weekly Events

Priorité :

1. Blizzard
2. Wowhead

---

## Fishing Events

Priorité :

1. Wowhead
2. Blizzard

---

## World Bosses

Priorité :

1. Wowhead
2. Blizzard

---

## Seasons

Priorité :

1. Blizzard

---

## History

Priorité :

1. Warcraft Wiki
2. Wowhead

---

# Vérification des données

Avant toute modification importante :

- vérifier au moins deux sources lorsque cela est possible ;
- privilégier la version française ;
- vérifier les dates européennes ;
- contrôler que les traductions correspondent au client.

---

# En cas de conflit

Si plusieurs sources donnent des informations différentes :

1. le client officiel prévaut ;
2. Blizzard prévaut sur les sites communautaires ;
3. Wowhead prévaut sur les autres sites communautaires.

Les divergences importantes doivent être signalées dans une issue GitHub avant modification.

---

# Objectif

Les données du calendrier doivent rester :

- fiables ;
- vérifiables ;
- reproductibles ;
- faciles à mettre à jour lors de chaque nouvelle extension.
