#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2023 Florian Kargl.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

from gnuradio import gr, gr_unittest
# from gnuradio import blocks
from gnuradio.phased_array_2d import calcPhase
from math import pi

class qa_calcPhase(gr_unittest.TestCase):

    def setUp(self):
        self.tb = gr.top_block()
        self.f = 1000000000
        self.c = 299792458
        self.d = (self.c / self.f) / 2

    def tearDown(self):
        self.tb = None


    def test_0deg(self):
        instance = calcPhase(num_antennas=4, antennas=[(0, 0), (0, self.d), (self.d, 0), (self.d, self.d)], f=self.f, azimuth=0, elevation=0)
        phase_offs = instance.calc_phase_offs()

        self.assertAlmostEqual(phase_offs[0], 0)
        self.assertAlmostEqual(phase_offs[1], 0)
        self.assertAlmostEqual(phase_offs[2], pi)
        self.assertAlmostEqual(phase_offs[3], pi)


    def test_90deg(self):
        instance = calcPhase(num_antennas=4, antennas=[(0, 0), (0, self.d), (self.d, 0), (self.d, self.d)], f=self.f, azimuth=90, elevation=0)
        phase_offs = instance.calc_phase_offs()

        self.assertAlmostEqual(phase_offs[0], 0)
        self.assertAlmostEqual(phase_offs[1], pi)
        self.assertAlmostEqual(phase_offs[2], 0)
        self.assertAlmostEqual(phase_offs[3], pi)

    def test_270deg(self):
        instance = calcPhase(num_antennas=4, antennas=[(0, 0), (0, self.d), (self.d, 0), (self.d, self.d)], f=self.f, azimuth=270, elevation=0)
        phase_offs = instance.calc_phase_offs()

        self.assertAlmostEqual(phase_offs[0], 0)
        self.assertAlmostEqual(phase_offs[1], -pi)
        self.assertAlmostEqual(phase_offs[2], 0)
        self.assertAlmostEqual(phase_offs[3], -pi)


    def test_45_45deg(self):
        instance = calcPhase(num_antennas=4, antennas=[(0, 0), (0, self.d), (self.d, 0), (self.d, self.d)], f=self.f, azimuth=45, elevation=45)
        phase_offs = instance.calc_phase_offs()

        self.assertAlmostEqual(phase_offs[0], 0)
        self.assertAlmostEqual(phase_offs[1], pi/2)
        self.assertAlmostEqual(phase_offs[2], pi/2)
        self.assertAlmostEqual(phase_offs[3], pi)


    def test_45_0deg(self):
        instance = calcPhase(num_antennas=4, antennas=[(0, 0), (0, self.d), (self.d, 0), (self.d, self.d)], f=self.f, azimuth=45, elevation=0)
        phase_offs = instance.calc_phase_offs()

        self.assertAlmostEqual(phase_offs[0], 0)
        self.assertAlmostEqual(phase_offs[1], 2.221441469079183)
        self.assertAlmostEqual(phase_offs[2], 2.221441469079183)
        self.assertAlmostEqual(phase_offs[3], 4.442882938158366)

    def test_270_15deg(self):
        instance = calcPhase(num_antennas=4, antennas=[(0, 0), (0, self.d), (self.d, 0), (self.d, self.d)], f=self.f, azimuth=270, elevation=15)
        phase_offs = instance.calc_phase_offs()

        self.assertAlmostEqual(phase_offs[0], 0)
        self.assertAlmostEqual(phase_offs[1], -3.0345454797823876)
        self.assertAlmostEqual(phase_offs[2], -5.574369613023855e-16)
        self.assertAlmostEqual(phase_offs[3], -3.0345454797823885)

if __name__ == '__main__':
    gr_unittest.run(qa_calcPhase)
