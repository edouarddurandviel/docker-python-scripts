Authentification des e-mails

SPF : publier un enregistrement DNS listant les adresses IP autorisées à envoyer des messages pour votre domaine.

DKIM : signer cryptographiquement les messages sortants pour garantir leur intégrité.

DMARC : définir une politique de traitement (quarantaine ou rejet) pour les courriels qui échouent aux contrôles SPF et DKIM.

Chiffrement et connexions

TLS obligatoire : forcer l'utilisation de connexions chiffrées pour le transit des messages (SMTP) et la lecture (IMAP/POP).

Certificats valides : installer des certificats SSL/TLS à jour (ex: Let's Encrypt) et désactiver les protocoles obsolètes (SSLv3, TLS 1.0/1.1).

Filtrage et protection systèmeAntivirus et antispam : intégrer des outils comme ClamAV et SpamAssassin (ou une passerelle dédiée) pour bloquer les logiciels malveillants et les spams.

Pare-feu et ports : restreindre les accès aux services d'administration et configurer un système anti-brute-force (comme Fail2ban) pour bloquer les tentatives de connexion répétées.