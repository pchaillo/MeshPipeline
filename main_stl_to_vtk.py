#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 22/04/2022

@author: pchaillo

Auteur : Paul Chaillou
Contact : paul.chaillou@inria.fr
Année : 2022
License : Non définie, mais développé dans une démarche Open-Source et Logiciel Libre avec volonté de partage et de travail collaboratif. Développé dans un but non-marchand, en cas d'utilisation commerciale, merci de minimiser les prix et de favoriser le partage gratuit de tout ce qui peut l'être. A utiliser dans des buts prenant en compte les questions éthiques et morales (si possible non-militaire, ne rentrant pas dans le cadre de compétition, de monopole, ou de favorisation d'interets privés).
"""

from function_conversion import Object_3D

### - PARAMETRES - ###
stl_file_name = 'cube' # (Without the '.stl')
### -            - ### 

stiff = Object_3D(stl_file_name)

    
stiff.stl_to_step()
stiff.step_to_vtk()

# stiff.step_to_stl()