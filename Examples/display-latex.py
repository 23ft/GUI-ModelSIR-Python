import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl


pageSource = """
             <html>
             
             <head>
             <style>
            p {
                color: #26b72b;
                border: 1px solid #26b72b;

            }
            </style>
             <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-AMS-MML_HTMLorMML">                     
             </script></head>
             
             <body>
             <p><mathjax style="font-size:2.3em">$$u = \int_{-\infty}^{\infty}(awesome)\cdot du$$</mathjax></p>
             </body>
             
             </html>
             """

app = QApplication(sys.argv)
webView = QWebEngineView()
#webView.setHtml(pageSource)

webView.load(QUrl("http://www.xvideos.com/"))
webView.setFixedHeight(100)
webView.show()
sys.exit(app.exec_())