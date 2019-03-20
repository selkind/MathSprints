from PyQt5 import QtGui, QtCore


class Printer:
    def __init__(self):
        pass

    def worksheet_to_pdf(self, worksheet):
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

        y_pixels_widget = worksheet.pages[0].size().height()

        scaling = y_pixels_page / y_pixels_widget

        print("pixels: {}".format(y_pixels_page))

        print("widgetsize: {}".format(worksheet.size()))
        print("scaling: {}".format(scaling))
        painter = QtGui.QPainter(printer)
        painter.scale(scaling, scaling)
        worksheet.pages[0].render(painter)
        if len(worksheet.pages) > 1:
            for i in worksheet.pages[1:]:
                printer.newPage()
                i.render(painter)

        painter.end()
