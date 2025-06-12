# -*- coding: utf-8 -*-
"""
Created on Mon May 19 00:53:51 2025

@author: Sam Cutmore
"""
import ezdxf

def dat_to_dxf(dat_file, dxf_file):
    with open(dat_file, 'r') as f:
        lines = f.readlines()

    coords = []
    for line in lines[1:]:  # Skip header
        if line.strip() == '':
            continue
        x, y = map(float, line.strip().split())
        coords.append((x, y))

    doc = ezdxf.new(dxfversion='R2000')
    msp = doc.modelspace()
    msp.add_lwpolyline(coords, close=True)
    doc.saveas(dxf_file)

dat_to_dxf("ag26.dat", "ag26_clean.dxf")
