# 0. INTRODUCTION
CE PROJET A PRIS PLACE DANS LE CADRE DU COURS SUR LES COMPILATEURS DISPENSÉ A LA HAUTE ÉCOLE ARC PENDANT L'ANNÉE SCOLAIRE 2015-2016. IL A ÉTÉ DEMANDÉ AUX ÉTUDIANTS D'INVENTER LEUR PROPRE LANGAGE DE PROGRAMMATION DANS LE BUT DE L'INTERPRÉTER, DE LE COMPILER, OU DE LE TRANSCRIRE DANS UN AUTRE LANGAGE DE PROGRAMMATION DÉJA EXISTANT. CE PROJET A POUR BUT DE SENSIBILISER LES ELÈVES AUX PROBLÈMES DE CONCEPTION QU'ONT RENCONTRÉS LES LANGAGES DE PROGRAMMATION COURRAMENT UTILISÉS, AINSI QUE D'APPRÉHENDER LES OUTILS ET LES MÉCANIQUES QUI ENTRENT EN OEUVRE LORS DE L'INTERPRÉTATION, LA COMPILATION OU LA TRANSCRIPTION D'UN LANGAGE.

# 1. OBJECTIF
LE LANGAGE DE PROGRAMMATION INVENTÉ S'APELLE LE `SOMELANGUAGE`. LE BUT EST DE S'INSPIRER DE MOTS DE LANGUE ANGLAISE PRÉFIXÉS DE `SOME` POUR ARTICULER DES CONCEPTS CONNUS DE PROGRAMMATION.

LE LANGAGE SERA INTERPRÉTÉ POUR SIMPLIFIER LA TÂCHE, PUISQUE SI L'ON SOUHAITE TOUCHER LES DIFFÉRENTS CONCEPTS CONNUS DE LA PROGRAMMATION, NOUS FERONS FACE A UN LANGAGE PLUS COMPLEXE CAR IL EST COMPOSÉ DE PLUS D'ÉLÉMENTS.

# 2. SPECIFICATIONS
LE SOMELANGUAGE AINSI QUE TOUS LES DOCUMENTS DE RÉFÉRENCES ET DE DOCUMENTATION DOIVENT ÊTRE ÉCRIT ENTIÈREMENT EN MAJUSCULE.
L'UTILISATEUR POURRA STOCKER DES VARIABLES ET CRÉER DES FONCTIONS EN QUANTITÉ LIMITÉES VIA LES ACCESSEURS APPROPRIÉS DÉFINI PAR LE LANGAGE.

## 2.1 DÉPENDANCES
L'INTERPRÉTEUR DU LANGAGE EST IMPLÉMENTÉ EN PYTHON 3.5.0 AVEC PLY 3.8.

## TYPES
L'INTERPRÊTEUR RECONNAIT LES NOMBRES ENTIERS ET LES NOMBRES FLOTTANTS, AINSI QUE LES BOOLEANS. LE TYPAGE SE FAIT AUTOMATIQUEMENT POUR LES NOMBRES. IL EST POSSIBLE DE DÉCLARER DES CHARS INDIRECTEMENT (VOIR SECTION FONCTIONS DE BASES).

| VALEUR | SOMELANGUAGE |
|--------|--------------|
| TRUE | SOMEWHAT REAL |
| FALSE | SOMEWHAT UNREAL |

## OPÉRATIONS

| OPÉRATION MATHÉMATIQUE OU LOGIQUE | SOMELANGUAGE                          |
|-----------------------------------|---------------------------------------|
| ADDITION (A + B)                  | EXPRESSION PLUS EXPRESSION            |
| SOUSTRACTION (A - B)              | EXPRESSION MINUS EXPRESSION           |
| MULTIPLICATION (A * B)            | EXPRESSION MINUS EXPRESSION           |
| ET (A & B)                        | \<EXPRESSION\> AND \<EXPRESSION\>             |
| OU (A | B)                        | \<EXPRESSION\> OR \<EXPRESSION\>             |
| NON (!A)                        | NOT \<EXPRESSION\>             |

### MATHEMATIQUES
### LOGIQUES

## CONDITION ET BOUCLES

## FONCTIONS DE BASES

| NOM | UTILISATION | DÉFINITION | NOTE |
|-----|-----|-----|-----|
| SOME STYLE FOR | SOME STYLE FOR \<EXPRESSION\> | DONNE LE CHAR REPRÉSENTÉ PAR LA VALEUR ASCII DONNÉE | EXPRESSION DOIT REPRÉSENTER UN NOMBRE |

# MOTS RESERVÉS

## PRISE EN MAIN
