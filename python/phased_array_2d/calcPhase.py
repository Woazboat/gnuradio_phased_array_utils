#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2023 Florian Kargl.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#


import numpy as np
from gnuradio import gr
import ast

class calcPhase(gr.sync_block):
    """
    Calculate the phase offsets for a phased array given a beam steering angle
    Parameters:
    num_antennas -- Number of antennas (must match the number of elements in the antennas parameter)
    antennas -- Array of antenna positions in the format '[(x0, y0), (x1, y1), ...]' (distances in meters)
    f -- Signal frequency
    azimuth -- Azimuth angle in degrees between 0 and 360
    elevation -- Elevation angle in degreees between 0 and 90

    Output:
    Phase offset in rad
    """
    def __init__(self,
                 num_antennas=9,
                 antennas = """[
                     (0.0, 0.0),
	             (0.299792458, 0.0),
	             (0.599584916, 0.0),
	             (0.0, 0.299792458),
	             (0.299792458, 0.299792458),
	             (0.599584916, 0.299792458),
                     (0.0, 0.599584916),
	             (0.299792458, 0.599584916),
	             (0.599584916, 0.599584916),
                 ]""",
                 f=500000000,
                 azimuth=50,
                 elevation=50):

        self.set_parameters(antennas, f, azimuth, elevation)
        self.c = 299792458 # speed of light in m/s
        self.ref = (0, 0) # reference point

        gr.sync_block.__init__(self,
            name="Array Phase Offsets",
            in_sig=[],
            out_sig=[np.float32]*len(self.antennas))



    def set_parameters(self, antennas, f, azimuth, elevation):
        self.antennas = ast.literal_eval(antennas) if type(antennas) is str else antennas
        self.f = f
        self.azimuth = azimuth % 360
        self.elevation = elevation

        boresight_angle = 90 - self.elevation
        self.az = np.radians(self.azimuth)
        self.ba = np.radians(boresight_angle)


    def calc_phase_offs(self):
        offsets = [(av - rv for av, rv in zip(a, self.ref)) for a in self.antennas]

        phase_offs = [np.sqrt(x**2 + y**2) * np.cos(self.az - np.arctan2(y, x)) * np.sin(self.ba) * 2 * np.pi * self.f / self.c for x,y in offsets]
        return phase_offs

    def work(self, input_items, output_items):
        for i, offs in enumerate(self.calc_phase_offs()):
            output_items[i][:] = offs

        return len(output_items[0])
