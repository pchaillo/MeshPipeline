#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 17:26:49 2021

@author: pchaillo

Auteur : Paul Chaillou
Contact : paul.chaillou@inria.fr
Année : 2022
License : Non définie, mais développé dans une démarche Open-Source et Logiciel Libre avec volonté de partage et de travail collaboratif. Développé dans un but non-marchand, en cas d'utilisation commerciale, merci de minimiser les prix et de favoriser le partage gratuit de tout ce qui peut l'être. A utiliser dans des buts prenant en compte les questions éthiques et morales (si possible non-militaire, ne rentrant pas dans le cadre de compétition, de monopole, ou de favorisation d'interets privés).

"""
FREECADPATH = '/usr/lib/freecad/lib' # path to your FreeCAD.so or FreeCAD.dll file

import sys
sys.path.append(FREECADPATH)
import FreeCAD, Part, Mesh
from math import sin,cos, tan,sqrt, acos,radians
import openpyscad as ops

import gmsh
import os
import pygmsh 
#import shutil
import numpy as np
import meshio


# import pymeshlab as pms # NOT WORKING


class Object_3D():

    def __init__(self,file_name,scad_name = 'null'):
        # Paths
        path = os.path.dirname(os.path.abspath(__file__))
        self.stlPath = path + '/STL/'
        self.stepPath = path + '/STEP/'
        self.vtkPath = path + '/VTK/'  
        self.filename = file_name
        self.name_stl = file_name + '.stl'
        self.name_step = file_name + '.step'
        self.name_vtk = file_name+'.vtk'
        self.path_stl = self.stlPath + self.name_stl
        self.path_step = self.stepPath + self.name_step
        self.path_vtk = self.vtkPath + self.name_vtk

    def step_to_vtk(self):  
        gmsh.initialize()
        gmsh.open(self.path_step)
        gmsh.model.occ.synchronize() 
        n = gmsh.model.getDimension()
        s = gmsh.model.getEntities(n)
        l = gmsh.model.geo.addSurfaceLoop([s[i][1] for i in range(len(s))])
        gmsh.model.geo.addVolume([l])
        gmsh.model.geo.synchronize() 
        gmsh.model.mesh.generate(3)
        gmsh.model.occ.synchronize()
        gmsh.write(self.path_vtk)
        gmsh.finalize()
        
    def stl_to_step(self): 
        doc = FreeCAD.newDocument()
        mesh = Mesh.Mesh(self.path_stl)
        shape = Part.Shape()
        shape.makeShapeFromMesh(mesh.Topology,0.1)
        solid = doc.addObject("Part::Feature", "Shape")
        solid.Shape = shape
        solid.Shape.exportStep(self.path_step)

    def step_to_stl(self):
        gmsh.initialize()
        gmsh.open(self.path_step)
        gmsh.model.occ.synchronize() 
        n = gmsh.model.getDimension()
        s = gmsh.model.getEntities(n)
        l = gmsh.model.geo.addSurfaceLoop([s[i][1] for i in range(len(s))])
        gmsh.model.geo.addVolume([l])
        gmsh.model.geo.synchronize() 
        gmsh.model.mesh.generate(3)
        gmsh.model.occ.synchronize()
        new_stl_path = self.stlPath + 'solid_' + self.name_stl
        gmsh.write(new_stl_path)
        gmsh.finalize()
