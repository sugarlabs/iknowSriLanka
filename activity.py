#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sugargame
import sugargame.canvas
import pygame
from sugar3.activity import activity
from sugar3.activity.widgets import DescriptionItem
from sugar3.activity.widgets import StopButton
from sugar3.activity.widgets import ActivityButton
from sugar3.graphics.toolbarbox import ToolbarBox
import conozco


class Activity(activity.Activity):

    def __init__(self, handle):
        activity.Activity.__init__(self, handle)

        self.max_participants = 1
        self.build_toolbar()
        self.game = conozco.Conozco(self)
        self.game.canvas = sugargame.canvas.PygameCanvas(self,
            main=self.game.principal,
            modules=[pygame.display, pygame.font])
        self.set_canvas(self.game.canvas)
        self.game.canvas.grab_focus()

    def build_toolbar(self):
        toolbar_box = ToolbarBox()

        activity_button = ActivityButton(self)
        toolbar_box.toolbar.insert(activity_button, 0)
        activity_button.show()

        description_item = DescriptionItem(self)
        toolbar_box.toolbar.insert(description_item, -1)
        description_item.show()

        separator = Gtk.SeparatorToolItem()
        separator.props.draw = False
        separator.set_expand(True)
        toolbar_box.toolbar.insert(separator, -1)
        separator.show()

        stop_button = StopButton(self)
        toolbar_box.toolbar.insert(stop_button, -1)
        stop_button.show()

        self.set_toolbar_box(toolbar_box)
        toolbar_box.show()

    def read_file(self, filepath):
        # FIXME Move read configuration from conzoco.py to activity.py
        pass

    def write_file(self, filepath):
        # FIXME Move write configuration from conzoco.py to activity.py
        self.game.save_stats()
        pass
