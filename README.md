# Python Fundamentals Applied to Bioinformatics

This repository contains a complete exercise on essential Python concepts with a focus on bioinformatics applications. The project involves creating a Conda environment, manipulating `.pdb` and `.csv` files, and applying data analysis and visualization techniques using core Python libraries.

## Project Structure

- `data/`: Contains input files (`1tup.pdb`, `actividad.csv`, `ciudades.tsv`)
- `scripts/python_basics_bioinfo.py`: Python script
- `README.md`: Project documentation

## Objective

To reinforce foundational Python knowledge for bioinformatics by working with structured and unstructured data, using libraries such as Pandas, Seaborn, and Matplotlib.

---

## Environment Setup

### A. Create a Conda environment with required libraries

```bash
conda create --name actividad1 pandas matplotlib seaborn spyder
conda activate actividad1
```

### B. Install specific version of NumPy

```bash
conda install numpy=1.25.0
```

### C. Check environments and installed packages

```bash
conda env list          # Show all environments
conda activate actividad1
conda list              # Show installed packages
```

---

## PDB File Handling and Visualization

### Tasks

- Extracted the **TITLE** and **AUTHOR** from `1tup.pdb`
- Parsed amino acid sequences from `SEQRES` lines using `with open()`
- Counted amino acids into a dictionary
- Created a bar chart with Seaborn showing amino acid frequencies

### Example Output

- **TITLE**: *TUMOR SUPPRESSOR P53 COMPLEXED WITH DNA*
- **AUTHOR**: *Y.CHO, S.GORINA, P.D.JEFFREY, N.P.PAVLETICH*

---

## Dataset Manipulation with Pandas

### Tasks on `actividad.csv` and `ciudades.tsv`

- Renamed columns: `id`, `dieta`, `pulsaciones`, `tiempo`, `actividad`
- Removed rows with missing values
- Counted levels in `dieta` and their frequency
- Used `groupby('actividad')` to compute:
  - Mean and standard deviation of `pulsaciones`
- Merged with city data using `merge(on='id')`

### Visualization

Used `relplot()` from Seaborn to show the relationship between `tiempo` and `pulsaciones` by `actividad` and `dieta` in a faceted plot.

---

## Python Concepts Practiced

- Context management with `with`
- Lists and dictionaries
- File parsing and filtering
- Pandas: `read_csv()`, `dropna()`, `groupby()`, `agg()`, `merge()`
- Seaborn and Matplotlib visualizations

---

## 👨‍💻 Author

**Oscar Saiz Gutierrez**  
MSc in Bioinformatics  

---

**Note:** This project was developed as part of the *Python Programming* course in the MSc in Bioinformatics.
