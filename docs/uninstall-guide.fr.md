# Comment désinstaller correctement Letter Dispatcher (et pourquoi retirer l'icône ne suffit pas toujours)

Quand vous « installez » Letter Dispatcher, le navigateur ne se contente pas de placer un raccourci sur le bureau — il enregistre l'application comme un vrai programme séparé (sur Android, on appelle ça un WebAPK ; Windows et Mac utilisent un mécanisme similaire). Si vous retirez seulement l'icône de l'écran d'accueil ou du bureau, le système peut continuer à considérer l'application comme installée — et une nouvelle tentative d'installation affiche alors un message du type « Application déjà installée », le bouton d'installation ne fonctionnant plus.

Pour réinstaller proprement, il faut supprimer l'application elle-même, pas seulement son icône. Voici comment faire selon le système.

## Android (Chrome)

1. Ouvrez **Paramètres du téléphone → Applications** (ou « Applications et notifications »).
2. Trouvez **Letter Dispatcher** dans la liste.
3. Appuyez sur **Désinstaller**.

Un moyen plus rapide, sans fouiller dans les paramètres : tapez `chrome://apps` dans la barre d'adresse de Chrome — toutes les applications web installées y sont listées ; appui long dessus puis **Supprimer**.

Une fois cela fait, ouvrez à nouveau le site dans Chrome — le bouton d'installation proposera de réinstaller depuis zéro.

## Windows (Chrome ou Edge)

1. Tapez `chrome://apps` dans la barre d'adresse (`edge://apps` pour Edge).
2. Trouvez **Letter Dispatcher** → clic droit → **Supprimer/Désinstaller**.

Ou directement via Windows : **Paramètres → Applications → Applications installées** → trouvez Letter Dispatcher → **Désinstaller**.

## macOS (Safari)

Si l'application a été ajoutée via **Fichier → Ajouter au Dock** :

1. Trouvez l'icône Letter Dispatcher dans le Dock (ou dans le dossier **Applications**).
2. Faites-la glisser vers la Corbeille — comme une application normale.

Si elle a plutôt été installée via Chrome/Edge sur Mac, utilisez la même méthode `chrome://apps` que pour Windows ci-dessus.

## iPhone / iPad

Sur iOS, la suppression d'un raccourci « Sur l'écran d'accueil » est complète et propre — aucune étape supplémentaire n'est nécessaire :

1. Appuyez et maintenez l'icône sur l'écran d'accueil.
2. Choisissez **Supprimer l'app** → **Supprimer**.

Vous pouvez ensuite ajouter le raccourci à nouveau via Safari (Partager → « Sur l'écran d'accueil »).

## Si rien ne fonctionne

Parfois, le navigateur « se souvient » encore de l'installation même après l'avoir supprimée via `chrome://apps`. Dans ce cas, une remise à zéro complète des données du site règle le problème :

1. Ouvrez [https://skymaverick171.github.io/letter-dispatcher/](https://skymaverick171.github.io/letter-dispatcher/) dans Chrome.
2. Cliquez sur l'icône du cadenas (ou ⓘ) à gauche de l'adresse → **Paramètres du site**.
3. Choisissez **Réinitialiser les autorisations et effacer les données**.

Ou allez dans `chrome://settings/content/all`, trouvez `skymaverick171.github.io` dans la liste, et supprimez-le. Cela réinitialise complètement le statut d'installation, et le bouton d'installation refonctionne comme la toute première fois.

**Important :** effacer les données du site supprime aussi les contacts/lettres enregistrés localement dans ce navigateur (ils y sont stockés directement, sans sauvegarde dans le cloud) — si vous n'avez encore rien sauvegardé, utilisez d'abord **« Copy for Google Sheets »** ou **« Download CSV »** dans l'onglet Contacts pour ne rien perdre.
