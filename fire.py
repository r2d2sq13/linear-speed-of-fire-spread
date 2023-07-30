import streamlit as st

def calculate_fire_spread_rate(D, t_us, t_a, t_rb, t_lok, S, V_j):
    t_j = (V_j * S) / 60
    t_po = t_us + t_a + t_j + t_rb + t_lok
    fire_spread_rate = D / t_po
    return fire_spread_rate

st.title("Prędkość liniowa rozprzestrzeniania się pożaru")
with st.form(key='fire_spread_form'):
    st.markdown("### Parametry")
    D = st.number_input("Droga rozprzestrzeniania się ognia [m]", value=100)
    t_us = st.number_input("Czas ukrytego spalania [min]", value=2)
    t_a = st.number_input("Czas alarmowania [min]", value=1)
    t_rb = st.number_input("Czas rozwinięcia bojowego [min]", value=3)
    t_lok = st.number_input("Czas lokalizacji pożaru [min]", value=5)
    S = st.number_input("Odległość od strażnicy do miejsca pożaru [km]", value=10)
    V_j = st.number_input("Średnia prędkość jazdy [km/h]", value=50)

    submit_button = st.form_submit_button(label="Oblicz")
    
    if submit_button:
        fire_spread_rate = calculate_fire_spread_rate(D, t_us, t_a, t_rb, t_lok, S, V_j)
        st.markdown(f"### Wynik:")
        st.markdown(f"Prędkość liniowa rozprzestrzeniania się pożaru wynosi **{fire_spread_rate:.2f} m/min**.")
