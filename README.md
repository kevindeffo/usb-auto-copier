# USB Auto Copier

🖥️ Un script Python pour copier automatiquement un fichier (`ouvre_moi.txt`) sur toute clé USB insérée, compatible avec **Linux** et **Windows**.

## 🚀 Fonctionnalités

- Détecte automatiquement l’insertion d’une clé USB.
- Copie le fichier `ouvre_moi.txt` depuis le **répertoire personnel de l'utilisateur** :
  - Sous **Linux** : `/home/<nom_utilisateur>/ouvre_moi.txt`
  - Sous **Windows** : `C:\Users\<nom_utilisateur>\ouvre_moi.txt`
- Évite les copies multiples grâce à un fichier `.ouvre_moi.txt.copied`.
- Fonctionne à la fois sur **Windows** et **Linux**.
- Surveillance continue jusqu’à interruption manuelle (`Ctrl+C`).

## 🛠️ Prérequis

- Python 3.6+
- Aucun module externe requis (`os`, `time`, `shutil`, `platform`, `pathlib`)

## 📦 Installation

Clone ce dépôt et place ton fichier `ouvre_moi.txt` dans ton dossier personnel :

```bash
git clone https://github.com/utilisateur/usb-auto-copier.git
cd usb-auto-copier
```

Place ensuite ton fichier `ouvre_moi.txt` à l’emplacement suivant selon ton système :

- **Linux** : `/home/<ton_nom_utilisateur>/ouvre_moi.txt`
- **Windows** : `C:\Users\<ton_nom_utilisateur>\ouvre_moi.txt`

## 🏃‍♂️ Utilisation

### ▶️ Lancer le script

```bash
python usb_watcher.py
```

### 🔁 Comportement

- Le script détecte chaque clé USB insérée.
- Il copie automatiquement le fichier sur la clé (sauf si déjà fait).
- Si tu retires la clé et la rebranches ou alors branche une nouvelle, elle est détectée.