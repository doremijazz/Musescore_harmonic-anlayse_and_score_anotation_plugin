##### Main analysis harmonie MXL score ####
print("code de github, je vais m'exécuter")
import sys
import os
from urllib.parse import urlparse

from music21 import *
from tkinter.filedialog import *
from tkinter import *
from PIL import ImageTk, Image

import interface
import data_extraction
import harmonic_context_analysis
import harmonic_analysis
import display

p = urlparse(sys.argv[1])
score_path = os.path.abspath(os.path.join(p.netloc, p.path))
freq = sys.argv[2]
double = int(sys.argv[3])
print(score_path, freq, double)

def score_analysis(score_XML, freq, freq_nb_double):
    
    nb_voices = len(score_XML.parts)

    print("Data extraction")
    SATB_chord = data_extraction.main(score_XML, nb_voices)

    print("Analyze harmonic context")
    SATB_chord, tab_modulation, freq_num = harmonic_context_analysis.main(SATB_chord, freq, freq_nb_double)

    print("Hermonic nalysis")
    L_accord_anglo, degres, chiffrage = harmonic_analysis.main(score_XML, SATB_chord, tab_modulation)
    print(L_accord_anglo)
    print("Display harmonic analysis -> MuseScore")
    #score_analysed =
    display.write_analyse (score_XML, degres, chiffrage, freq_num, L_accord_anglo, tab_modulation)

    #score_analysed.show()
    save_2D_Tableau (L_accord_anglo)


    print("END")
    return

def save_2D_Tableau (tableau):
    # Nom du fichier dans lequel vous souhaitez enregistrer le tableau
    nom_fichier = "analyse_tmp.pkl"

    # Ouvrir le fichier en mode écriture binaire (wb) pour l'enregistrement
    with open(nom_fichier, 'wb') as fichier:
        pickle.dump(tableau, fichier)

    return 

def main(filepath, freq, freq_nb_double):
    #result_inte = interface.main()
    #filepath, freq, freq_nb_double = result_inte
    #print(freq)

    #filepath = "~/Desktop/bwv2.6.mxl"
    #freq = "noire"
    #freq_nb_double = 4
    

    score_XML = converter.parse(filepath)

    #lance le programme
    score_analysis(score_XML, freq, freq_nb_double)
    return 

main(score_path, freq, double)
