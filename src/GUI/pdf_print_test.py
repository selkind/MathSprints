from PyQt5 import QtGui, QtCore
from src.GUI.Page import Page


class Window:
    def __init__(self):
        pass

    def print_screen(self, widget):
        filename = "test.pdf"

        '''
        Potential to take string argument of page sizes and use a dictionary to map
        to Qpage sizes. then use that size as parameter during page size instantiation
        '''
        page_size = QtGui.QPageSize(QtGui.QPageSize.Letter)

        printer = QtGui.QPdfWriter(filename)
        printer.setPageSize(QtGui.QPdfWriter.Letter)
        printer.setPageMargins(QtCore.QMarginsF())

        page_resolution = printer.logicalDpiY()
        y_pixels_page = QtGui.QPageSize.sizePixels(page_size.id(), page_resolution).height()

        y_pixels_widget = widget.pages[0].size().height()

        scaling = y_pixels_page / y_pixels_widget

        print("pixels: {}".format(y_pixels_page))

        print("widgetsize: {}".format(widget.size()))
        print("scaling: {}".format(scaling))
        painter = QtGui.QPainter(printer)
        painter.scale(scaling, scaling)
        widget.pages[0].render(painter)
        if len(widget.pages) > 1:
            for i in widget.pages[1:]:
                printer.newPage()
                i.render(painter)

        painter.end()
