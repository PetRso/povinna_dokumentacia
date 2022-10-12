# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import pandas as pd

zodpovednost = [' ', 'riaditeľ', 'zástupca', 'učiteľ', 'vychovávateľ', 'zriaďovateľ', 'rada školy ']
institucie = ['Materská škola', 'Základná škola (ročník 1-9)', 'Centrum voľného času']
typy = ['Pedagogická', 'Ďalšia']
shorts = {'Materská škola': 'MŠ', 'Základná škola (ročník 1-9)':'ZŠ',
          'Centrum voľného času': 'CVČ'}

df = pd.read_excel('zoznam_dokumentacie.xlsx',
                   header=0, skiprows=1)

st.title('Katalóg povinnej dokumentácie')
st.write('Prototyp pre povinne vedenú pedagogickú dokumentáciu.')

cols = st.columns((1, 1, 1, 1))
institucia = cols[0].selectbox('Inštitúcia', institucie)
osoba = cols[1].selectbox('Zodpovedná osoba', zodpovednost)
typ = cols[2].selectbox('Typ', typy)
chk_nepovinna = cols[3].checkbox('nepovinná')
chk_neplatna = cols[3].checkbox('neplatná')

st.write('\n')
if (not chk_nepovinna) & (not chk_neplatna):
    cols = ['Názov', 'Vedená/ý v ', 'Zodpovednosť']
    i = df['Vedená/ý v '].str.contains(shorts[institucia])
    i2 = df['Zodpovednosť'].str.contains(osoba)
    st.write(df.loc[i & i2, cols])