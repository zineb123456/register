import streamlit as st
import pandas as pd
import os

FICHIER_DONNEES = "visiteurs.csv"

# Configuration de la page
st.set_page_config(page_title="Registre des Visiteurs", page_icon="📋", layout="centered")

st.title("📋 Registre des Visiteurs")
st.write("Bienvenue ! Veuillez remplir le formulaire ci-dessous pour soumettre votre demande.")

# --- 1. FORMULAIRE VISITEURS (Accessible à tous) ---
with st.form("form_visiteur", clear_on_submit=True):
    nom = st.text_input("Nom complet :")
    probleme = st.text_area("Description du problème / Motif de la visite :")
    bouton_soumettre = st.form_submit_button("➕ Enregistrer la demande")

if bouton_soumettre:
    if not nom.strip():
        st.warning("⚠️ Veuillez entrer votre nom.")
    elif not probleme.strip():
        st.warning("⚠️ Veuillez décrire le problème.")
    else:
        # Enregistrement des données dans le fichier CSV
        nouveau_visiteur = pd.DataFrame([{"Nom": nom.strip(), "Problème": probleme.strip()}])
        
        if os.path.exists(FICHIER_DONNEES):
            nouveau_visiteur.to_csv(FICHIER_DONNEES, mode='a', header=False, index=False, encoding="utf-8-sig")
        else:
            nouveau_visiteur.to_csv(FICHIER_DONNEES, mode='w', header=True, index=False, encoding="utf-8-sig")
            
        st.success(f"✅ Merci {nom}, votre demande a bien été enregistrée !")

# --- 2. ESPACE ADMINISTRATEUR (Protégé par mot de passe) ---
st.divider()

# Barre latérale pour la connexion admin
st.sidebar.header("🔐 Accès Administrateur")
mot_de_passe = st.sidebar.text_input("Mot de passe pour voir la liste :", type="password")

# Vous pouvez modifier "admin123" par le mot de passe de votre choix
if mot_de_passe == "admin123":
    st.header("📊 Liste des problèmes et demandes enregistrés")
    if os.path.exists(FICHIER_DONNEES):
        df = pd.read_csv(FICHIER_DONNEES)
        st.dataframe(df, use_container_width=True)
    else:
        st.info("Aucune demande n'a encore été enregistrée.")
elif mot_de_passe != "":
    st.sidebar.error("Mot de passe incorrect !")
