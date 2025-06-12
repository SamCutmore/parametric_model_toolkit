# Parametric model Tools

A collection of scripts and resources I've made for parametric CAD and simulation.

---

## Directory: `airfoil/`

This directory contains utility scripts for:

- Parsing XFOIL polar data files
- Converting airfoil coordinate files to DXF format for CAD modeling.

Contents:

- `XFOIL_PolarDataParser.py` — Extracts data from XFOIL polar files for plotting and analysis.
- `dat2dxf.py` — Converts `.dat` airfoil coordinate files to `.dxf` for CAD import.

---

## Dependencies

Required Python packages:

- `pandas`
- `matplotlib`
- `ezdxf`
