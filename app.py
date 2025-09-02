import pandas as pd
import plotly.express as px
import streamlit as st
     
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

st.header('Análisis interactivo de vehículos en EE.UU.')

st.write("""
Esta aplicación permite explorar visualmente un conjunto de datos de anuncios de venta de coches.
Puedes activar las visualizaciones usando las casillas de verificación a continuación.
""")

# Casilla para mostrar histograma
show_histogram = st.checkbox('Mostrar histograma de odómetro')

if show_histogram:
    st.write('Histograma del kilometraje de los vehículos')
    fig_hist = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig_hist, use_container_width=True)

# Casilla para mostrar gráfico de dispersión
show_scatter = st.checkbox('Mostrar gráfico de dispersión entre odómetro y precio')

if show_scatter:
    st.write('Relación entre kilometraje y precio')
    fig_scatter = px.scatter(car_data, x='odometer', y='price', color='condition')
    st.plotly_chart(fig_scatter, use_container_width=True)
