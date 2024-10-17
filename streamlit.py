import streamlit as st

# Título de la aplicación
st.title("Interfaz con barra lateral")

# Barra lateral con botones
button1 = st.sidebar.button("Gráficas de precios")
button2 = st.sidebar.button("Gráficas de variables")
button3 = st.sidebar.button("Gráficas de precios afectados por variables")
button4 = st.sidebar.button("Modelos predictivos")

option = 0

if button1:
    option = 0
elif button2:
    option = 1
elif button3:
    option = 2
elif button4:
    option = 3

# Mostrar contenido basado en el botón seleccionado
if option == 0:
    st.header("Conjunto de Elementos 1")
    st.write("Aquí puedes mostrar el primer conjunto de elementos.")
    st.button("Botón 1")
    st.button("Botón 2")
    
elif option == 1:
    st.header("Conjunto de Elementos 2")
    st.write("Aquí puedes mostrar el segundo conjunto de elementos.")
    st.checkbox("Checkbox 1")
    st.checkbox("Checkbox 2")
    
elif option == 2:
    st.header("Conjunto de Elementos 3")
    st.write("Aquí puedes mostrar el tercer conjunto de elementos.")
    st.slider("Deslizador 1", 0, 100)
    
elif option == 3:
    st.header("Conjunto de Elementos 4")
    st.write("Aquí puedes mostrar el cuarto conjunto de elementos.")
    st.selectbox("Selecciona una opción", ["Opción A", "Opción B", "Opción C"])

# Mensaje de pie de página
st.write("Usa los botones en la barra lateral para navegar entre los conjuntos de elementos.")


