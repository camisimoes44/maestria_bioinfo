import streamlit as st
import pandas as pd
import MySQLdb
import time
import numpy as np
#import altair as alt
import SessionState

@st.cache 

def insertarLinea():
	"""
	Inserta una línea horizontal
	"""
	st.markdown('<hr>', unsafe_allow_html=True)


st.set_option('deprecation.showfileUploaderEncoding', False)  # desactiva un warning del file_uploader


# menú lateral (sidebar)
st.sidebar.write("### Menu")
titulo_pag1 = "Stage 1 - Variant classification and expert training"
titulo_pag2 = "Stage 2 - Variant classification by experts (training set)"
titulo_pag3 = "Statistics"
pagina = st.sidebar.selectbox("Please select a page:", (titulo_pag1, titulo_pag2, titulo_pag3))	
st.image("logo3.png",use_column_width=True)
#st.markdown('# Human genome sequence variant interpretation')


###########################################################################################################################################################
#											PAG. 1
###########################################################################################################################################################

if pagina == titulo_pag1:
	st.markdown('## ' + titulo_pag1)  # título de la página

	rules = st.sidebar.button("Need to remember ACGMG rules?")
		
	if rules:
		st.image("rules.png",use_column_width=True)

	# inputs de usuario
	session_state = SessionState.get(name="", button_sent=False)

	session_state.name = st.text_input(" Enter your name ", "")
	experience = st.selectbox(" What do you consider to be your level of expertise in the interpretation of variants?", ('Novice', 'Advanced Beginner', 'Competent', 'Proficient', 'Expert'))


	session_state.button_sent = st.button("Load new variant")

	insertarLinea()

	
	if session_state.button_sent :  # se ejecuta cuando se clickea btn_saludar
		 #st.balloons()
	
		with st.spinner('Wait for it...'):
			time.sleep(0.5)
		
		data = pd.read_csv("prueba.csv")
		st.write(data)
		session_state.label = st.selectbox('According to the information provided above, the classification of the variant corresponds to:', ('Benign', 'Likely Benign', 'VUS', 'Likely Pathogenic', 'Pathogenic'))	

		session_state.sub = st.button("Submit classification")
		if session_state.sub:
			st.success('Done!')


	insertarLinea()

	


############################################################################################################################################################

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



