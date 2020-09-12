import streamlit as st
import pandas as pd
import MySQLdb

def insertarLinea():
	"""
	Inserta una línea horizontal
	"""
	st.markdown('<hr>', unsafe_allow_html=True)

st.set_option('deprecation.showfileUploaderEncoding', False)  # desactiva un warning del file_uploader

# menú lateral (sidebar)
st.sidebar.write("### Menú")
titulo_pag1 = "Página 1: leer de inputs"
titulo_pag2 = "Página 2: leer de archivo"
titulo_pag3 = "Página 3: leer de base de datos"
pagina = st.sidebar.selectbox("Página a mostrar:", (titulo_pag1, titulo_pag2, titulo_pag3))	
st.markdown('# Prueba Streamlit')

if pagina == titulo_pag1:
	with st.echo(code_location="below"):  # muestra el código fuente de la página en la parte inferior
		st.markdown('## ' + titulo_pag1)  # título de la página

		# inputs de usuario
		name = st.text_input("Escribí tu nombre", "")
		sexo = st.radio("¿De qué sexo sos?", ("Femenino", "Masculino"))
		color = st.selectbox('¿Cuál es tu color favorito?', ('Amarillo', 'Azul', 'Rojo', 'Verde'))
		edad = st.slider("¿Cuál es tu edad?", 1, 100, 18, 1)

		btn_saludar = st.button("Saludar")

		if btn_saludar:  # se ejecuta cuando se clickea btn_saludar
			if sexo == "Femenino":
				genero = "una mujer"
			else:
				genero = "un hombre"
			st.write("¡Hola " + name + "!")
			st.write("Eres " + genero + " de " + str(edad) + " años y te gusta el color " + color)
		insertarLinea()

elif pagina == titulo_pag2:
	with st.echo(code_location="below"):
		st.markdown('## ' + titulo_pag2)
		
		uploaded_file = st.file_uploader("Elige un archivo CSV", type="csv")
		if uploaded_file is not None:
			data = pd.read_csv(uploaded_file)
			st.write(data)  # muestra el DataFrame como tabla interactiva
		insertarLinea()

elif pagina == titulo_pag3:
	with st.echo(code_location="below"):
		st.markdown('## ' + titulo_pag3)
		# st.write("Esta página está vacía")

		consultar = st.button("Conectar con MySQL")

		if consultar:
			db_conn = MySQLdb.connect(host="localhost", user="root", passwd="mysql.363%", db="information_schema", port=3306)
			query = "SELECT * FROM INNODB_SYS_TABLES"
			cursor = db_conn.cursor()
			cursor.execute(query)
			data = cursor.fetchall()
			db_conn.close()
			data_df = pd.DataFrame(data)
			st.write("Vista de tabla")
			st.write(data_df)
			st.write("Plot de algunas de las columnas")
			st.line_chart(data_df[[0, 3, 4]])  # plotear la primer columna del dataframe
			st.selectbox("Select cargado a partir de una columna", data_df[1])

		insertarLinea()