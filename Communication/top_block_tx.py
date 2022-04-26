#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# GNU Radio version: 3.7.13.5
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from gnuradio.wxgui import waterfallsink2
from grc_gnuradio import blks2 as grc_blks2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import pmt
import time
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "C:\Program Files\GNURadio-3.7\share\icons\hicolor\scalable/apps\gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 2e6
        self.if_gain = if_gain = 30
        self.bb_gain = bb_gain = 30

        ##################################################
        # Blocks
        ##################################################
        _if_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._if_gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_if_gain_sizer,
        	value=self.if_gain,
        	callback=self.set_if_gain,
        	label='if_gain',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._if_gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_if_gain_sizer,
        	value=self.if_gain,
        	callback=self.set_if_gain,
        	minimum=1,
        	maximum=50,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_if_gain_sizer)
        _bb_gain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._bb_gain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_bb_gain_sizer,
        	value=self.bb_gain,
        	callback=self.set_bb_gain,
        	label='bb_gain',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._bb_gain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_bb_gain_sizer,
        	value=self.bb_gain,
        	callback=self.set_bb_gain,
        	minimum=1,
        	maximum=50,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_bb_gain_sizer)
        self.wxgui_waterfallsink2_0 = waterfallsink2.waterfall_sink_c(
        	self.GetWin(),
        	baseband_freq=0,
        	dynamic_range=100,
        	ref_level=0,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=512,
        	fft_rate=15,
        	average=False,
        	avg_alpha=None,
        	title='Waterfall Plot',
        )
        self.Add(self.wxgui_waterfallsink2_0.win)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_c(
        	self.GetWin(),
        	title='Scope Plot',
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label='Counts',
        )
        self.Add(self.wxgui_scopesink2_0.win)
        self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + 'hackrf' )
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(145.02e6, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(20, 0)
        self.osmosdr_sink_0.set_if_gain(if_gain, 0)
        self.osmosdr_sink_0.set_bb_gain(bb_gain, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)

        self.digital_gmsk_mod_0 = digital.gmsk_mod(
        	samples_per_symbol=2,
        	bt=0.35,
        	verbose=False,
        	log=False,
        )
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((1, ))
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, 'C:\\Users\\RAJAT\\Desktop\\GMSK_Tx.txt', True)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blks2_packet_encoder_0 = grc_blks2.packet_mod_b(grc_blks2.packet_encoder(
        		samples_per_symbol=2,
        		bits_per_symbol=2,
        		preamble='',
        		access_code='',
        		pad_for_usrp=False,
        	),
        	payload_length=200,
        )



        ##################################################
        # Connections
        ##################################################
        self.connect((self.blks2_packet_encoder_0, 0), (self.digital_gmsk_mod_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blks2_packet_encoder_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.osmosdr_sink_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.wxgui_scopesink2_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.wxgui_waterfallsink2_0, 0))
        self.connect((self.digital_gmsk_mod_0, 0), (self.blocks_multiply_const_vxx_0, 0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.wxgui_waterfallsink2_0.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)

    def get_if_gain(self):
        return self.if_gain

    def set_if_gain(self, if_gain):
        self.if_gain = if_gain
        self._if_gain_slider.set_value(self.if_gain)
        self._if_gain_text_box.set_value(self.if_gain)
        self.osmosdr_sink_0.set_if_gain(self.if_gain, 0)

    def get_bb_gain(self):
        return self.bb_gain

    def set_bb_gain(self, bb_gain):
        self.bb_gain = bb_gain
        self._bb_gain_slider.set_value(self.bb_gain)
        self._bb_gain_text_box.set_value(self.bb_gain)
        self.osmosdr_sink_0.set_bb_gain(self.bb_gain, 0)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
