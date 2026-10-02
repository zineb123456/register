import streamlit as st
import pandas as pd
import os

FICHIER_DONNEES = "visiteurs.csv"

# Configuration de la page web
st.set_page_config(page_title="Registre des Visiteurs", page_icon="📋", layout="centered")

st.title("📋 Registre des Visiteurs")
st.write("Bienvenue ! Veuillez remplir le formulaire ci-dessous.")

# --- FORMULAIRE DE SAISIE ---
with st.form("form_visiteur", clear_on_submit=True):
    nom = st.text_input("Nom complet du visiteur :")
    probleme = st.text_area("Description du problème / Motif de visite :")
    bouton_soumettre = st.form_submit_button("➕ Enregistrer le visiteur")

if bouton_soumettre:
    if not nom.strip():
        st.warning("⚠️ Veuillez entrer un nom.")
    elif not probleme.strip():
        st.warning("⚠️ Veuillez décrire le problème.")
    else:
        # Création d'une nouvelle ligne de données
        nouveau_visiteur = pd.DataFrame([{"Nom": nom.strip(), "Problème": probleme.strip()}])

        # Enregistrement dans un fichier CSV
        if os.path.exists(FICHIER_DONNEES):
            nouveau_visiteur.to_csv(FICHIER_DONNEES, mode='a', header=False, index=False, encoding="utf-8")
        else:
            nouveau_visiteur.to_csv(FICHIER_DONNEES, mode='w', header=True, index=False, encoding="utf-8")

        st.success(f"✅ Merci {nom}, votre demande a bien été enregistrée !")

# --- AFFICHAGE DE LA LISTE DES VISITEURS ---
st.divider()
st.subheader("📋 Liste des visiteurs enregistrés")

if os.path.exists(FICHIER_DONNEES):
    df = pd.read_csv(FICHIER_DONNEES)
    st.dataframe(df, use_container_width=True)
else:
    st.info("Aucun visiteur n'a encore été enregistré.")
