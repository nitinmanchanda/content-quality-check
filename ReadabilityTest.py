# coding=utf-8
import textstat

# reference: https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests
# reference: https://pypi.org/project/textstat/

# url = https://www.omio.com/trains/paris/london
text = "Trains in Europe are a convenient way of traveling between cities, with a number of train companies offering domestic and international routes. Trains from Paris to London are incredibly fast and convenient, with high-speed Eurostar trains traveling between the cities in about 2.5 hours. Eurostar trains depart from Paris frequently during the day from early morning until evening, providing plenty of travel options. Paris to London train travel time ranges between 2 hours 15 minutes and 2 hours 30 minutes, depending on the chosen departure time. Eurostar's Paris to London trains leave from Paris Gare du Nord station and travel directly to London St Pancras International. Peak times tend to be in the morning around 8:30 a.m. and 4:30 p.m. in the afternoon."
print "Flesch Reading Ease: " + str(textstat.flesch_reading_ease(text))
print "Flesch Kincaid Grade: " + str(textstat.flesch_kincaid_grade(text))
print "Smog Index: " + str(textstat.smog_index(text))
print "Coleman Liau Index: " + str(textstat.coleman_liau_index(text))
print "Automated Readability Index: " + str(textstat.automated_readability_index(text))
print "Dale Chall Readability Score: " + str(textstat.dale_chall_readability_score(text))
print "Difficult Words: " + str(textstat.difficult_words(text))
print "Linsear Write Formula: " + str(textstat.linsear_write_formula(text))
print "Gunning Fog: " + str(textstat.gunning_fog(text))
print "Text Standard: " + str(textstat.text_standard(text))
print "==========\n"

# url = https://de.omio.com/bahn/berlin/amsterdam-rdudx
textstat.set_lang('de_DE')
text = "Bahn von Berlin nach Amsterdam \
Tagtäglich verbinden mehrere Schnellzüge der Deutschen Bahn Berlin mit Amsterdam auf direktem Wege: Einfach am Hauptbahnhof einsteigen, entspannt zurücklehnen und nach 6,5 Stunden im Herzen der niederländischen Metropole aussteigen. Zusätzlich bestehen zahlreiche genauso schnelle Verbindungen mit einmaligem Umsteigen in Hannover oder Duisburg. Einfacher und komfortabler geht es kaum! \
Welche Bahngesellschaften fahren von von Berlin nach Amsterdam? \
Alle Verbindungen mit der Bahn von Berlin nach Amsterdam werden von der Deutschen Bahn angeboten. Fast täglich fahren 7 ICs der DB direkt vom Berliner Hauptbahnhof nach Amsterdam Centraal. Der erste IC verlässt Berlin bereits in den frühen Morgenstunden und erreicht mittags Amsterdam. Der letzte IC fährt am späten Nachmittag in Berlin ab und kommt noch vor Mitternacht in Amsterdam an. \
Daneben besteht die Möglichkeit, in Hannover oder Duisburg in ICs oder ICEs nach Amsterdam umzusteigen. Wer die längere Dauer und das mehrmalige Umsteigen nicht scheut, kann auch die landschaftliche attraktive Route über Ostfriesland wählen: Dabei führt die Fahrt mit der Bahn von Berlin nach Amsterdam über Hamburg, Bremen, Leer/Ostfriesland, Groningen und Almere. \
\
Wie lange dauert die Bahnfahrt von Berlin nach Amsterdam? \
Die direkte Fahrt mit der Bahn von Berlin nach Amsterdam dauert exakt 6,5 Stunden. Doch auch die Umsteigeverbindungen über Hannover oder Duisburg benötigen nicht länger für die gesamte Strecke, da die Bahn bis Hannover bzw. Duisburg weniger Zwischenhalte einlegt. \
Wie viel kostet ein Zugticket von Berlin nach Amsterdam? \
Bei kurzfristigem Ticketkauf kostet die Fahrt mit der Bahn von Berlin nach Amsterdam je nach Zug zwischen 70 und 120 Euro (einfache Strecke, 2. Klasse). Da täglich viele Züge zur Auswahl stehen, sind die Chancen recht hoch, ein günstiges Ticket zu ergattern. Wer mindestens einen Monat im Voraus bucht, erhält meist auch noch den Sparpreis Europa für 39,90 Euro (2. Klasse) und kann so die gesamte Strecke mit der Bahn von Berlin nach Amsterdam und zurück für nur knapp 80 Euro bewältigen. \
\
Bahnhöfe auf der Strecke Berlin – Amsterdam \
An welchem Bahnhof fährt die Bahn in Berlin los? Alle ICs in Richtung Amsterdam (auch mit Umsteigen in Hannover oder Duisburg) fahren am Berliner Hauptbahnhof ab. Dieser ist bestens an den ÖPNV angeschlossen und u. a. mit der U-Bahn-Linie U55, den Trambahnen M5, M8 und M10 sowie den S-Bahnen S5, S7 und S75 zu erreichen. \
\
An welchem Bahnhof kommt die Bahn in Amsterdam an? Die Bahn von Berlin nach Amsterdam kommt am Hauptbahnhof von Amsterdam (Centraal) am Hafen der Stadt an. Von hier sind die meisten Hotels und Sehenswürdigkeiten innerhalb des Grachtenrings bequem zu Fuß zu erreichen. Die Tramlinien 4, 9, 24 und 26 verbinden den Hauptbahnhof mit verschiedenen Stadtvierteln, die Metrolinien 51, 53 und 54 mit den Vororten."
print "Flesch Reading Ease: " + str(textstat.flesch_reading_ease(text))
print "Flesch Kincaid Grade: " + str(textstat.flesch_kincaid_grade(text))
print "Smog Index: " + str(textstat.smog_index(text))
print "Coleman Liau Index: " + str(textstat.coleman_liau_index(text))
print "Automated Readability Index: " + str(textstat.automated_readability_index(text))
print "Dale Chall Readability Score: " + str(textstat.dale_chall_readability_score(text))
print "Difficult Words: " + str(textstat.difficult_words(text))
print "Linsear Write Formula: " + str(textstat.linsear_write_formula(text))
print "Gunning Fog: " + str(textstat.gunning_fog(text))
print "Text Standard: " + str(textstat.text_standard(text))
