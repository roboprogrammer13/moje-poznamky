import streamlit as st

st.title("Moje blba webová aplikace 🚀")

jmeno = st.text_input("Jak se jmenuješ?")

if jmeno:
    st.write(f"Ahoj {jmeno}! Dneska je skvělý den na programování.")
    
    pocet = st.slider("Jak moc tě baví Python?", 0, 100, 50)
    st.write(f"Tvoje nadšení je na úrovni: {pocet}%")

# Přidání grafu je otázka jednoho řádku
st.line_chart([1, 5, 2, 6, 3, 10])