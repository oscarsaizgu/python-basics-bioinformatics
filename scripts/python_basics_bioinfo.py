#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Oscar Saiz Gutierrez
Activity: Python Fundamentals for Bioinformatics
"""

# =====================================
# 1. PDB FILE HANDLING AND HISTOGRAM
# =====================================

# A. Extract TITLE and AUTHOR
pdb_file = 'data/1tup.pdb'
titulo = ""
autores = ""

with open(pdb_file, 'r') as file:
    for line in file:
        if line.startswith('TITLE'):
            titulo = line.strip()
        if line.startswith('AUTHOR'):
            autores = line.strip()

print(f"TITLE: {titulo}")
print(f"AUTHOR: {autores}")

# B. Extract amino acid sequence
aminoacidos_validos = ['ALA', 'CYS', 'ASP', 'GLU', 'PHE', 'GLY', 'HIS', 'ILE', 'LYS', 'LEU',
                       'MET', 'ASN', 'PRO', 'GLN', 'ARG', 'SER', 'THR', 'VAL', 'TRP', 'TYR']
aminoacidos = []

with open(pdb_file, 'r') as file:
    for line in file:
        if line.startswith('SEQRES'):
            amino_acids = line.split()[4:]
            aminoacidos.extend([aa for aa in amino_acids if aa in aminoacidos_validos])

print(aminoacidos)

# C. Count amino acids
aminoacidos_conteo = {}
for aa in aminoacidos:
    aminoacidos_conteo[aa] = aminoacidos_conteo.get(aa, 0) + 1

print(aminoacidos_conteo)

# D. Histogram
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_aa = pd.DataFrame({
    'Aminoacido': list(aminoacidos_conteo.keys()),
    'Frecuencia': list(aminoacidos_conteo.values())
})

sns.catplot(x='Aminoacido', y='Frecuencia', data=df_aa, kind='bar', palette='Set2', height=5, aspect=1.5)
plt.title('Frecuencia de Aminoácidos en SEQRES')
plt.xlabel('Aminoácido')
plt.ylabel('Frecuencia')
plt.tight_layout()
plt.show()

# =====================================
# 2. CSV DATA HANDLING AND VISUALIZATION
# =====================================

# A. Read and rename columns
actividad_file = 'data/actividad.csv'
df = pd.read_csv(actividad_file, sep=';')
df.columns = ['id', 'dieta', 'pulsaciones', 'tiempo', 'actividad']

# B. Drop missing values
print("Missing values per column:")
print(df.isnull().sum())
df = df.dropna()

# C. Frequency of 'dieta'
frecuencia_dieta = df['dieta'].value_counts()
print(f"Levels in 'dieta': {len(frecuencia_dieta)}")
print("Frequency per level:")
print(frecuencia_dieta)

# D. Group by 'actividad'
grupo_actividad = df.groupby('actividad')
lista_agrupada = list(grupo_actividad)
print("Grouped data example:")
for name, group in lista_agrupada:
    print(f"Group: {name}, Rows: {group.shape[0]}")

# E. Aggregation
agg_result = grupo_actividad['pulsaciones'].agg(['mean', 'std'])
agg_result.columns = ['Pulsaciones medias', 'Desviacion estandar']
print(agg_result)

# F. Merge with cities data
ciudades_file = 'data/ciudades.tsv'
df_ciudades = pd.read_csv(ciudades_file, sep='\t')
df_unido = pd.merge(df, df_ciudades, on='id', how='left')
print(df_unido.head())

# G. Relational plot with facets
relplot = sns.relplot(data=df_unido, x='tiempo', y='pulsaciones',
                      col='actividad', hue='dieta', palette='Set1')
relplot.fig.suptitle('Relación entre pulsaciones y tiempo por actividad y dieta', y=1.05)
relplot.set_axis_labels('Tiempo (min)', 'Pulsaciones')
plt.show()
