"""Acts."""
from io import BytesIO

from pdfminer.converter import HTMLConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

from utils import filex

from documents_lk._common import log

TEST_ACT_FILE = 'src/documents_lk/assets/test_act.pdf'


def _pdf_to_html(pdf_file):
    """Run."""
    with open(TEST_ACT_FILE, 'rb') as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)

        rsrcmgr = PDFResourceManager()
        output_string = BytesIO()
        device = HTMLConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
        html = output_string.getvalue().decode()

        html_file = pdf_file[:-3] + 'html'
        filex.write(html_file, html)
        log.info(
            '_pdf_to_html: Converted %s to %s (%dKB)',
            pdf_file,
            html_file,
            len(html) / 1000,
        )


if __name__ == '__main__':
    _pdf_to_html('src/documents_lk/assets/test_act.pdf')
