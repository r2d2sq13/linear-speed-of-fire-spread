import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def calculate_fire_spread_rate(D, t_us, t_a, t_rb, t_lok, S, V_j):
    t_j = (V_j * S) / 60
    t_po = t_us + t_a + t_j + t_rb + t_lok
    fire_spread_rate = D / t_po
    return fire_spread_rate, t_po

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
        fire_spread_rate, t_po = calculate_fire_spread_rate(D, t_us, t_a, t_rb, t_lok, S, V_j)
        st.markdown(f"### Wynik:")
        st.markdown(f"Prędkość liniowa rozprzestrzeniania się pożaru wynosi **{fire_spread_rate:.2f} m/min**.")

        # 1. 2D plot showing fire spread from above
        st.markdown("### Wykres rozprzestrzeniania się pożaru z góry (2D):")
        x = np.linspace(0, D, 100)
        y = fire_spread_rate * x
        plt.plot(x, y)
        plt.xlabel("Odległość [m]")
        plt.ylabel("Szerokość ognia [m]")
        plt.title("Rozprzestrzenianie się pożaru")
        st.pyplot(plt.gcf())
        plt.clf()

        # 2. Plot of fire spread rate over time
        st.markdown("### Wykres prędkości rozprzestrzeniania się pożaru w czasie:")
        time = np.linspace(0, t_po, 100)
        plt.plot(time, fire_spread_rate * np.ones_like(time))
        plt.xlabel("Czas [min]")
        plt.ylabel("Prędkość rozprzestrzeniania [m/min]")
        plt.title("Prędkość rozprzestrzeniania się pożaru w czasie")
        st.pyplot(plt.gcf())
        plt.clf()

        # 3. Plot of area covered by fire over time
        st.markdown("### Wykres powierzchni objętej pożarem w czasie:")
        area_covered = fire_spread_rate * time * D
        plt.plot(time, area_covered)
        plt.xlabel("Czas [min]")
        plt.ylabel("Powierzchnia objęta pożarem [m^2]")
        plt.title("Powierzchnia objęta pożarem w czasie")
        st.pyplot(plt.gcf())
        plt.clf()

        # 4. 3D plot showing fire spread (example)
        st.markdown("### Wykres 3D rozprzestrzeniania się pożaru:")
        from mpl_toolkits.mplot3d import Axes3D
        X, Y = np.meshgrid(x, y)
        Z = fire_spread_rate * X  # Example function for 3D spread
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, Z)
        plt.title("3D Rozprzestrzenianie się pożaru")
        st.pyplot(fig)
