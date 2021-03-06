from zope.traversing.api import getName
from zope.component import getMultiAdapter
from zope.publisher.browser import BrowserPage
from worldcookery.pdf.interfaces import IPDFPresentation

class PDFView(BrowserPage):

    def __call__(self):
        filename = getName(self.context) + '.pdf'
        response = self.request.response
        response.setHeader('Content-Disposition',
                           'attachment; filename=%s' % filename)
        response.setHeader('Content-Type', 'application/pdf')
        return getMultiAdapter((self.context, self.request),
                               IPDFPresentation)