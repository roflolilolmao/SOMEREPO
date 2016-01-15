# 0. INTRODUCTION
CE PROJET A PRIS PLACE DANS LE CADRE DU COURS SUR LES COMPILATEURS DISPENSÉ A LA HAUTE ÉCOLE ARC PENDANT L'ANNÉE SCOLAIRE 2015-2016. IL A ÉTÉ DEMANDÉ AUX ÉTUDIANTS D'INVENTER LEUR PROPRE LANGAGE DE PROGRAMMATION DANS LE BUT DE L'INTERPRÉTER, DE LE COMPILER, OU DE LE TRANSCRIRE DANS UN AUTRE LANGAGE DE PROGRAMMATION DÉJA EXISTANT. CE PROJET A POUR BUT DE SENSIBILISER LES ELÈVES AUX PROBLÈMES DE CONCEPTION QU'ONT RENCONTRÉS LES LANGAGES DE PROGRAMMATION COURRAMENT UTILISÉS, AINSI QUE D'APPRÉHENDER LES OUTILS ET LES MÉCANIQUES QUI ENTRENT EN OEUVRE LORS DE L'INTERPRÉTATION, LA COMPILATION OU LA TRANSCRIPTION D'UN LANGAGE.

# 1. OBJECTIF
LE LANGAGE DE PROGRAMMATION INVENTÉ S'APELLE LE `SOMELANGUAGE`. LE BUT EST DE S'INSPIRER DE MOTS DE LANGUE ANGLAISE PRÉFIXÉS DE `SOME` POUR ARTICULER DES CONCEPTS CONNUS DE PROGRAMMATION.

LE LANGAGE SERA INTERPRÉTÉ POUR SIMPLIFIER LA TÂCHE, PUISQUE SI L'ON SOUHAITE TOUCHER LES DIFFÉRENTS CONCEPTS CONNUS DE LA PROGRAMMATION, NOUS FERONS FACE A UN LANGAGE PLUS COMPLEXE CAR IL EST COMPOSÉ DE PLUS D'ÉLÉMENTS.

# 2. SPECIFICATIONS
LE SOMELANGUAGE AINSI QUE TOUS LES DOCUMENTS DE RÉFÉRENCES ET DE DOCUMENTATION DOIVENT ÊTRE ÉCRIT ENTIÈREMENT EN MAJUSCULE.
L'UTILISATEUR POURRA STOCKER DES VARIABLES ET CRÉER DES FONCTIONS EN QUANTITÉ LIMITÉES VIA LES ACCESSEURS APPROPRIÉS DÉFINI PAR LE LANGAGE.

## 2.1. DÉPENDENCES
L'INTERPRÉTEUR DU LANGAGE EST IMPLÉMENTÉ EN PYTHON 3.5.0 AVEC PLY 3.8.

## 2.2. TYPES
L'INTERPRÊTEUR RECONNAIT LES NOMBRES ENTIERS ET LES NOMBRES FLOTTANTS, AINSI QUE LES BOOLEANS. LE TYPAGE SE FAIT AUTOMATIQUEMENT POUR LES NOMBRES. IL EST POSSIBLE DE DÉCLARER DES CHARS INDIRECTEMENT (VOIR SECTION FONCTIONS DE BASES).

| VALEUR | SOMELANGUAGE |
|--------|--------------|
| TRUE | SOMEWHAT REAL |
| FALSE | SOMEWHAT UNREAL |

##2.3. VARIABLES
LES VARIABLES SONT DÉCLARÉES COMME SUIT: SOMETHING \<VAR\> IS \<EXPRESSION\>.

LES VARIABLES REPRÉSENTENT UNE EXPRESSION QUI SONT SIMPLEMENT APPELÉES COMME SUIT: SOMETHING \<VAR\>

CES VARIABLES SONT ÉGALEMENT DES DICTIONNAIRES ET CONTIENNENT DES LISTES. C'EST À DIRE QU'IL EXISTE DES ACCESSEURS PERMETTANT D'AVOIR PLUSIEURS VALEURS DANS LA MÊME VARIABLE.

PAR EXEMPLE:

SOMETHING UGLY IS 3. SOMETHING UGLY SOMEPLACE CROWDED IS 4.

DANS CE CAS, LA VARIABLE UGLY CONTIENT 3, MAIS ÉGALEMENT 4 AVEC L'ACCESSEUR CROWDED. (CE QUI, EN PYTHON, POURRAIT RESSEMBLER À : UGLY = {None: 3, 'CROWDED': 4})

LES VARIABLES CONTIENNENT ÉGALEMENT DES LISTES, QUI SONT ACCÉDÉES COMME SUIT: SOMETHING FLAT SOMEWHERE ORDERED.

LA DÉCLARATION D'UNE LISTE SE FAIT DE CETTE MANIÈRE: 

SOMETHING \<VAR\> SOMEWHERE ORDERED IS RESPECTIVELY \<PARAMS\>. 

(SE RÉFÉRER À LA SECTION PARAMÈTRES)

ON PEUT ACCÉDER À UN ÉLÉMENT DE LA LISTE DE CETTE MANIÈRE:

FOR SEAT \<EXPRESSION\> OF SOMETHING \<VAR\>, OÙ \<EXPRESSION\> REPRÉSENTE UN NOMBRE.

##2.4. FONCTIONS

LES FONCTIONS DOIVENT ÊTRE DÉCLARÉES AU DÉBUT DU PROGRAMME.

HERE'S SOMEONE \<FUNC_NAME\> (WITH \<PARAMS\>) : \<FUNC_BODY\>.

\<FUNC_BODY\> REPRÉSENTE LE CORPS DE LA FONCTION. IL EST POSSIBLE DE RENVOYER UN RÉSULTAT AVEC L'INSTRUCTION GIVE ME \<EXPRESSION\>.

LES FONCTIONS PEUVENT PRENDRE DES PARAMÈTRES EN ARGUMENT AVEC LE MOT-CLEF WITH, LES PARAMÈTRES DOIVENT ÊTRE UNE VARIABLE OU UN EMPLACEMENT DANS UN DICTIONNAIRE.

L'APPEL D'UNE FONCTION SE FAIT COMME SUIT: SOMEONE \<FUNC_NAME\> (, DO THE THING WITH THAT ONE/THOSE ONES: \<PARAMS\>)

##2.5. PARAMÈTRES
LES PARAMÈTRES SONT UNE SUITE D'EXPRESSIONS, SÉPARÉES PAR DES VIRGULES.
\<EXPRESSION\>, \<EXPRESSION\>, …, \<EXPRESSION\> OU SIMPLEMENT UNE EXPRESSION SEULE.

## 2.6. OPÉRATIONS

| OPÉRATION MATHÉMATIQUE OU LOGIQUE | SOMELANGUAGE                          |
|-----------------------------------|---------------------------------------|
| ADDITION (A + B)                  | EXPRESSION PLUS EXPRESSION            |
| SOUSTRACTION (A - B)              | EXPRESSION MINUS EXPRESSION           |
| MULTIPLICATION (A * B)            | EXPRESSION MINUS EXPRESSION           |
| DIVISION (A / B)                  | \<EXPRESSION\> OUT OF \<EXPRESSION\>  |
| ET (A ∧ B)                        | \<EXPRESSION\> AND \<EXPRESSION\>             |
| OU (A ∨ B)                        | \<EXPRESSION\> OR \<EXPRESSION\>             |
| NON (!A)                        | NOT \<EXPRESSION\>             |
| PLUS GRAND QUE (A > B) | \<EXPRESSION\> GREATER THAN <\EXPRESSION\> |
| PLUS PETIT QUE (A < B) | \<EXPRESSION\> SMALLER THAN <\EXPRESSION\> |
| EST EGAL A (A = B) | \<EXPRESSION\> EQUAL TO <\EXPRESSION\> |

LES OPÉRATIONS MATHÉMATIQUES SONT L'ADDITION, LA SOUSTRACTION, LA MULTIPLICATION ET LA DIVISION. LES RÉSULTAT DE CES OPÉRATIONS EST UNE VALEUR NUMÉRIQUE.

LES OPÉRATIONS LOGIQUES SONT : ET, OU, NON, PLUS GRAND QUE, PLUS PETIT QUE, EST ÉGAL A ; ET LE RÉSULTAT DE CES OPÉRATIONS EST UNE VALEUR BOOLEENE. LES OPÉRATION LOGIQUES SONT PRINCIPALEMENT UTILISÉES DANS LE CADRE DES BOUCLES (CF. BOUCLES)

## 2.7. BOUCLES
LES BOUCLES SE RÉALISENT A L'AIDE D'UNE SYNTAXE ASSEZ SPÉCIALE. 

`<OUVERTURE>, \<CONDITION\>: \<EXPRESSIONS\> <CLÔTURE>

AVEC :
* <\OUVERTURE\> : 'FOR SOMETIMES, `
* <\CLÔTURE\> : 'THIS KEPT GOING ON. `
* <\CONDITION\> : UNE EXPRESSION BOOLEENNE
* <\EXPRESSIONS\> : UNE SUITE D'\<EXPRESSION\>'

`FOR SOMETIMES,` EST L'INSTRUCTION QUI PERMET D'INDIQUER LE POINT DE DÉPART DE LA BOUCLE. 
`\<CONDITION\>` EST L'EXPRESSION BOOLEENNE QUI INDIQUE SI LA BOUCLE DOIT S'ARRÊTER OU NON.  TANT QUE LA CONDITION EST VRAI (`SOMEWHAT REAL`), LES INSTRUCTIONS SITUÉES APRÈS LES DEUX-POINTS (`:`) VONT S'EXÉCUTER SÉQUENTIELLEMENT JUSQU'AU MARQUEUR <CLÔTURE> AVANT DE REVÉRIFIER LA CONDITION. AUSSITÔT QUE LA CONDITION EST ÉVALUÉE A FAUX (`SOMEWHAT UNREAL`), L'EXÉCUTION DU CODE REPRENDS APRÈS LE MARQUEUR \<CLÔTURE\>.

## 2.8. FONCTIONS DE BASES

NOM: SOME STYLE FOR

UTILISATION: SOME STYLE FOR \<EXPRESSION\>

DÉFINITION: DONNE LE CHAR REPRÉSENTÉ PAR LA VALEUR ASCII DONNÉE

NOTE: EXPRESSION DOIT REPRÉSENTER UN NOMBRE


NOM: EXPLORE

UTILISATION: EXPLORE SOMETHING \<VAR_NAME\> (SOMEWHERE ORDERED) WITH SOMEONE \<FUNC_NAME\> (, DO THE THING WITH THOSE ONES: \<PARAMS\>)

DÉFINITION: POUR CHAQUE VALEUR DANS LE DICTIONNAIRE \<VAR_NAME\>, APPELLE LA FONCTION \<FUNC_NAME\> AVEC LA VALEUR POUR PREMIER PARAMÈTRE DONNÉ. SI LE MODIFICATEUR SOMEWHERE ORDERED EST UTILISÉ, LA FONCTION EST APPELLÉE AVEC CHAQUE ÉLÉMENT DE LA LISTE DE \<VAR_NAME\>. ON PEUT DONNER DES PARAMÈTRES À LA FONCTION, LE PREMIER PARAMÈTRE DANS LA FONCTION SERA TOUJOURS LA VALEUR DU DICTIONNAIRE OU DE LA LISTE. SI LA FONCTION RETOURNE UNE VALEUR, ELLE REMPLACE CELLE DU DICTIONNAIRE OU DE LA LISTE.


NOM: CALL

UTILISATION: CALL \<FUNCTION\>

DÉFINITION: APPELLE UNE FONCTION.


NOM: COULD BE

UTILISATION: SOMETHING \<VAR\> COULD BE \<ACCESSOR\>

DÉFINITION: RENVOIE VRAI SI \<ACCESSOR\> EXISTE DANS \<VAR\>, SINON FAUX.

## 2.9 COMMENTAIRES

COMME DANS LA PLUPART DES LANGAGES DE PROGRAMMATION, L'UTILISATEUR A LA POSSIBILITE D'ECRIRE DES PORTIONS DE TEXTE A L'INTENTION DU LECTEUR DE SON CODE, ET NON À CELLE DU COMPILATEUR. CE DERNIER DOIT DONC AVOIR UN MOYEN DE RECONNAÎTRE CES PORTIONS DE TEXTE DANS LE BUT DE LES IGNORER.

LA FACON D'ÉCRIRE UN COMMENTAIRE EN SOMELANGUAGE CONSISTE À ENTOURER LA PARTIE DE TEXTE CONCERNÉ PAR DES PARENTHÈSES. TOUT CE QUI SE SITUE A L'INTÉRIEUR DE PARENTHÈSES SERA ENTIÈREMENT IGNORÉ. IL EST POSSIBLE D'IMBRIQUER LES PARENTHÈSES, CE QUI VEUT DIRE QUE TANT QU'UNE PARENTHÈSE EST OUVERTE, L'INTERPRÉTEUR VA CONTINUER D'IGNORER LE TEXTE QUI SUIT JUSQU'À CE QUE TOUTE LES PARENTHÈSES SOIENT FERMÉES. A NOTER QU'IL N'EST PAS POSSIBLE D'ÉCHAPPER LES CARACTÈRES DE PARENTHÈSES ET QUE L'ON NE PEUT DONC PAS LES CITER TEL QUELS, MÊME DANS UN COMMENTAIRE.

# 3. MOTS RESERVÉS
LES MOTS RÉSERVÉS SE DÉCLINENT EN PLUSIEURS CATÉGORIES. IL Y A LES MOTS FONCTIONNELS, QUI SERVENT, SEUL OU EN COMBINAISON AVEC D'AUTRES MOTS, A EXPRIMER UNE FONCTIONNALITÉ DU LANGAGE. IL Y A LES MOTS UTILITAIRES QUI SERVENT A PRÉCISER CERTAINES FONCTIONNALITÉS.

CERTAINS MOTS FONCTIONNELS N'ONT AUCUNE UTILITÉ LORSQUE EXPRIMÉS SEULS. UNE PHRASE FONCTIONNELLE, COMPOSÉS DE MOTS, IMPLIQUE QUE TOUT LES MOTS COMPOSANT LA PHRASE SOIENT RÉSERVÉS

LES OPÉRATEURS MATHÉMATIQUES ET LOGIQUES ÉTANT DES MOTS ET NON DES SYMBOLES, EN FONT BIEN ÉVIDEMMENT DES MOTS RÉSERVÉS.

## 3.1. MOTS FONCTIONNELS
ICI SONT DÉCRITS TOUT LES MOTS FONCTIONNELS POUVANT S'UTILISER SEUL EN TANT QUE TEL, OU ACCOMPAGNÉS DE MOT UTILITAIRES.

| MOT | DESCRIPTION SIMPLE |
|---|---|
|SOMETHING | ACCES A UNE VARIABLE |
|SOMEWHAT | INDICATEUR BOOLEEN |
|SOMEPLACE | ACCES A UNE LISTE DE VARIABLES|
|SOMEONE | ACCESEUR DE FONCTION|
|SOMEBODY| ACCESSEUR DE FONCTION |
|HERE'S| DÉFINITION DE FONCTION|
| EXPLORE | MAPPING SUR TOUTE LES VALEURS D'UN \<SOMETHING\> |
| CALL | APPEL DE FONCTION |

## 3.2. PHRASES FONCTIONNELLES
ICI SONT DÉCRITES TOUTES LES PHRASES FONCTIONNELLES PERMETTANT D'ACCOMPLIR UNE ACTION DANS LE SOMELANGUE. LES PHRASES DOIVENT ÊTRE EXPRIMÉES TELLES QUELS POUR ÊTRE INTERPRÉTÉES CORRECTEMENT.

| PHRASE | DESCRIPTION SIMPLE |
|---|---|
| FOR SOMETIMES, | DÉBUT DE BOUCLE |
| THIS KEPT GOING ON. | FIN DE BOUCLE |
| SOME OF IT IS REAL |  todo |
| SOMEWHERE ORDERED | todo |
| IS RESPECTIVELY | todo |
| COULD BE | todo |
| SHOW ME | todo |
| SOME STYLE FOR | todo |
| DO THE THING WITH THAT ONE | INDICATEUR DE PARAMÈTRE(S) |
| DO THE THING WITH THOSE ONES | INDICATEUR DE PARAMÈTRE(S) |
| GIVE ME | RÉCUPÉRATEUR DE VALEUR |



## 3.3. MOTS UTILITAIRES
ICI SONT DÉCRIT TOUTS LES MOTS QUI PERMETTENT SERVANT A PRÉCISER DES FONCTIONNALITÉS DU LANGAGE. IL S'AGIT EXCLUSIVEMENT D'ACCESSEURS POUR LES VARIABLES ET LES FONCTIONS.

| VARIABLES SIMPLES | LISTE DE VARIABLES | FONCTIONS   |
|-------------------|--------------------|-------------|
| UGLY              | DUSTY              | BEAUTIFUL   |
| OLD               | GLOOMY             | JOYFUL      |
| BLUNT             | CHARMING           | AMAZING     |
| DUMB              | CROWDED            | MESMERIZING |
| FLAT              | POPULAR            | SEXY        |
| TINY              | BURLESQUE          | BRILLIANT   |
| USELESS           | DARK               | NICE        |
| LAZY              | STORMY             | WORTHY      |
| NAUGHTY           | NOISY              | FUNNY       |
| MACHIAVELLIAN     | ANCIENT            | LOGICAL     |
| STINGY            | DRY                | HELPFUL     |
| MOODY             | DESERTIC           | KEEN        |
| SELFISH           | BUSTLING           | VIGILIANT   |
| GREEDY            | POLLUTED           | BRAVE       |
| GULLIBLE          | LIVELY             | PASSIONATE  |
| DOGMATIC          | PICTURESQUE        | GENEROUS    |

# 4. PRISE EN MAIN

LE PRÉSENT PROJET EST LIVRÉ AVEC DES EXEMPLES DE PROGRAMME SIMPLES QUI PERMETTENT D'APPRÉHENDER LE LANGAGE ET SES POSSIBILITÉS. VOICI UNE LISTE DES EXEMPLES ET LES ÉLÉMENTS DU LANGAGE QUI SONT MIS EN AVANT.

## HELLO.TXT
UNE SIMPLE SUITE D'INSTRUCTION, TRÈS RÉPÉTITIVES QUI VONT AFFICHER LE TEXTE `Hello world!` À L'ÉCRAN

## HELLO_LIST.TXT
DANS LE MÊME GENRE QU HELLO.TXT, A LA DIFFÉRENCE QUE L'ON UTILISE D'ABORD UN LISTE POUR STOCKER LES VALEURS DES CARACTÈRES PUIS UNE BOUCLE POUR PARCOURIR CETTE LISTE EN AFFICHER LE CONTENU.

## HELLO_LIST_MAP.TXT
ENCORE UN `Hello world!` MAIS ENCORE PLUS EFFICACE QUE LES PRÉCÉDENTS. ON DÉFINIT D'ABORD UNE FONCTION DONT LE BUT EST D'AFFICHER LE CARACTÈRE DU PARAMÈTRE QUI LUI EST DONNÉ. ENSUITE, ON DÉFINIT NOTRE LISTE DE VALEURS REPRÉSENTANT NOTRE TEXTE. FINALEMENT, ON UTILISE LE MAPPING POUR APPLIQUER LA FONCTION DÉFINIE TOUT À L'HEURE SUR CHAQUE ÉLÉMENT DE LA LISTE.

## MAP_DOUBLE.TXT
ICI, L'ON DÉCLARE DEUX FONCTIONS.
* LA PREMIÈRE PREND UN PARAMÈTRE ET VA RENVOYER LE DOUBLE DE SA VALEUR
* LA SECONDE PREND DEUX PARAMÈTRES ET VA AFFICHER LA VALEUR DU PREMIER, ET L'ASCII DU SECOND.

ENSUITE, ON UTILISE DE LE DICTIONNAIRE (LISTE NOMMÉE) DE FLAT POUR DÉFINIR QUELQUES VALEURS. ENFIN, ON UTILISE LA PUISSANCE DU MAPPING POUR APPELER SUCCESSIVEMENT LES DEUX FONCTIONS SUR LES VALEURS QU'ON A DÉFINI. ON CONSTATERA L'AJOUT D'UN PARAMÈTRE À L'AIDE `DO THE THING WITH THAT ONE` POUR COMPLÉTER LE FAIT QUE LA SECONDE FONCTION PRENNE DEUX PARAMÈTRES, MAIS QUE LE MAPPING NE LIS LES VALEURS QU'UN PAR UN.

## FIBONACCI_ITERATIVE.TXT
CET EXEMPLE VA GÉNÉRER LES 15 PREMIERS TERMES DE LA SÉQUENCE DE FIBONACCI. EN PREMIER LIEU, ON DÉTERMINE QUATRE VARIABLES. TOUTES INITIALISÉES AVEC LA VALEUR 1, LA PREMIÈRE SERVIRA DE POINT DE COMPARAISON POUR LA BOUCLE QUI VA GÉNÉRER LA SÉQUENCE. LES TROIS AUTRES REPRÉSENTENT LES DEUX DERNIERS TERMES DE LA SÉQUENCE DE FIBONACCI AINSI QU'UNE PLACE POUR CONTENIR LE PROCHAIN TERME. QUAND LE NOUVEU TERME EST GÉNÉRÉ, ON DÉCALE NOS VALEURS DANS NOS VARIABLES POUR RETROUVER LA MÊME STRUCTURE ET PROCÉDER À LA GÉNÉRATION DU TERME SUIVANT.

## FIBONACCI_RECURSIVE.TXT
ICI, ON APELLE UNE FONCTION RÉCURSIVE AVEC TROIS PARAMÈTRES, LES DEUX PREMIERS TERMES DE LA SÉQUENCE DE FIBONACCI, A SAVOIR : 1 ET 1., PUIS LA VALEUR LIMITE A LAQUELLE ON SOUHAITE ARRÊTER LA SÉQUENCE. LA FONCTION, DÉFINIE AU DÉBUT DU FICHIER SE TIENT COMME SUIT. LA FONCTION PRENDS DEUX PARAMÈTRES ET AFFICHE LE PREMIER, SUIVI D'UN ESPACE. ENSUITE ON VÉRIFIE LA CONDITION D'ARRÊT AVEC UN `SOMEHOW`. SI LA VALEUR DU SECOND TERME (NON AFFICHÉ), EST PLUS GRANDE QUE LA VALEUR LIMITE, ON SE CONTENTE D'AFFICHER LA VALEUR DU PREMIER TERME. SINON, ON CALCULE LE TERME SUIVANT ET L'ON RAPELLE LA FONCTION RÉCURSIVE AVEC LE DERNIER ET LE NOUVEAU TERME (ET LA LIMITE) POUR CONTINUER LA GÉNÉRATION DE LA SÉQUENCE.

# 5. CONCLUSION
