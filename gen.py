import os
import random
import string
from colorama import init, Fore

# Initialisation de colorama
init(autoreset=True)

# ASCII art modifiable
ascii_art = r"""                                                                                          
                                                _______                                   
              __.....__        _..._             \  ___ `'.                                
  .--./)  .-''         '.    .'     '.            ' |--.\  \                               
 /.''\\  /     .-''"'-.  `. .   .-.   .           | |    \  '               .|             
| |  | |/     /________\   \|  '   '  |           | |     |  '    __      .' |_     __     
 \`-' / |                  ||  |   |  |           | |     |  | .:--.'.  .'     | .:--.'.   
 /("'`  \    .-------------'|  |   |  |           | |     ' .'/ |   \ |'--.  .-'/ |   \ |  
 \ '---. \    '-.____...---.|  |   |  |           | |___.' /' `" __ | |   |  |  `" __ | |  
  /'""'.\ `.             .' |  |   |  |          /_______.'/   .'.''| |   |  |   .'.''| |  
 ||     ||  `''-...... -'   |  |   |  |          \_______|/   / /   | |_  |  '.'/ /   | |_ 
 \'. __//                   |  |   |  |                       \ \._,\ '/  |   / \ \._,\ '/ 
  `'---'                    '--'   '--'                        `--'  `"   `'-'   `--'  `" 
"""

def generate_email(domain="gmail.com"):
    """Génère une adresse e-mail aléatoire avec le domaine spécifié."""
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"{username}@{domain}"

def generate_password(length=12):
    """Génère un mot de passe aléatoire."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=length))

def create_account_folder(folder_name="account"):
    """Crée un dossier pour stocker les comptes."""
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def save_accounts_to_file(folder_name, accounts, service_name):
    """Sauvegarde tous les comptes dans un fichier spécifique au service."""
    file_path = os.path.join(folder_name, f"{service_name}.txt")
    with open(file_path, 'w') as f:
        for email, password in accounts:
            f.write(f"Adresse e-mail : {email}\n")
            f.write(f"Mot de passe : {password}\n\n")

def generate_spotify_account():
    """Génère un compte Spotify Premium fictif."""
    email = generate_email()
    password = generate_password()
    return email, password

def generate_netflix_account():
    """Génère un compte Netflix fictif."""
    email = generate_email()
    password = generate_password()
    return email, password

def main():
    # Affichage de l'ASCII art en rouge
    print(Fore.RED + ascii_art)
    
    print(Fore.WHITE + "Générateur de comptes")
    print("1. Générer des comptes Spotify Premium")
    print("2. Générer des comptes Netflix")

    # Demander le choix de l'utilisateur
    choice = input("Veuillez choisir une option (1 ou 2) : ")

    # Demander le nombre de comptes à générer
    try:
        number_of_accounts = int(input("Combien de comptes souhaitez-vous générer ? "))
    except ValueError:
        print("Veuillez entrer un nombre valide.")
        return

    # Créer le dossier pour les comptes
    create_account_folder()

    # Liste pour stocker les comptes
    accounts = []

    # Générer les comptes en fonction du choix
    if choice == '1':
        for i in range(1, number_of_accounts + 1):
            email, password = generate_spotify_account()
            accounts.append((email, password))
            print(f"Compte Spotify {i} généré : {email} | Mot de passe : {password}")
        service_name = "spotify"
    elif choice == '2':
        for i in range(1, number_of_accounts + 1):
            email, password = generate_netflix_account()
            accounts.append((email, password))
            print(f"Compte Netflix {i} généré : {email} | Mot de passe : {password}")
        service_name = "netflix"
    else:
        print("Choix invalide. Veuillez entrer 1 ou 2.")
        return

    # Sauvegarder tous les comptes dans un fichier spécifique au service
    save_accounts_to_file("account", accounts, service_name)

    print(Fore.GREEN + f"{number_of_accounts} comptes ont été générés et sauvegardés dans le fichier '{service_name}.txt' dans le dossier 'account'.")

if __name__ == "__main__":
    main()