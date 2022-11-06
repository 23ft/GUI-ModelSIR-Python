"""
  >> Styles for Control Inventary App with mysql and Pyside6


  >> page colors: http://www.creativecolorschemes.com/resources/free-color-schemes/gray-tone-color-scheme.shtml

"""
# STYLES CSS APP

init_values_panel = """
    font-size: 12px; 
    qproperty-alignment: AlignJustify; 
    font-family: 'Kanit', sans-serif;
    font-family: 'Oswald', sans-serif;
    font-weight: bold;
    padding: 5px;
    border-left: .5px solid #9C3D54;
    border-right: .5px solid #9C3D54;
    background-color: #EEB76B
    

"""

firstTab_Frames_css = """
#FirstFrame {
    background-color: #EEB76B
}

#s-label, #r-label, #i-label , #tasa_contagios_label, #poblacion_total{
    background-color: #EEB76B
}

#SecondFrame {
    background-color: #EEB76B
}

"""

qlabel_css_twoframe = """
font-size: 10px; 
qproperty-alignment: AlignJustify; 
font-family: 'Kanit', sans-serif;
font-family: 'Oswald', sans-serif;
font-weight: bold;
background-color: #EEB76B
"""

qlabel_css_params = """                                
font-size: 12px; 
qproperty-alignment: AlignJustify; 
font-family: 'Kanit', sans-serif;
font-family: 'Oswald', sans-serif;
font-weight: bold;

"""

btn_menu_css = """
    #btn_menu{
        padding: 5px;
        margin-top: 20px;
        margin-left: 5px;
        margin-right: 10px;
        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,
                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);

    }
    
    #btn_config{
        margin-left: 5px;
        margin-right: 10px;
        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                 stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,
                                 stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);

    }




"""

main_css = """
    
    /*background: qlineargradient( 
                                x1:0, 
                                y1:0, 
                                x2:0, 
                                y2:1,
                                stop:0 rgb(0, 0, 0),
                                stop:1.0 rgb(30, 30, 30));*/
    background-color: #E2703A;
"""

login_css = """

    #header {
        background-color: rgb(0, 0, 10)
    }

    #login_23ft {
        /*border: 2px solid black;*/
        /*padding-left: 50px;*/
        color: #eee;
        margin: 0px auto;
    }



"""