import numpy as np
import sys

# Werte aus Boyles Experiment
#x = np.array([1.0, 1.5, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0, 24.0, 28.0, 32.0])
#y = np.array([29.750, 19.125, 14.375, 9.5, 7.125, 5.625, 4.875, 4.250, 3.750, 3.375, 3.0, 2.625, 2.250, 2.0, 1.875, 1.750, 1.5, 1.375, 1.250])

# Werte aus Keplers Experiment
# x = np.array([1.0, 4.0, 9.0]) #Distance (D)
# y = np.array([1.0, 8.0, 27.0]) #Period(P)

# andere synthetische Werte (für x / y ↑ 3 = c)
#x = np.array([1, 8, 64])
#y = np.array([1, 2, 4])

# Werte vom Abkühlen des Arduinos
# Zeit (Sekunden)
#x = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430])
# Temperatur (Grad Celsius)
#y = np.array([23.75, 23.42, 21.32, 19.68, 18.42, 16.93, 15.2, 14.09, 13.44, 13.35, 12.76, 12.26, 11.92, 11.75, 11.61, 11.24, 10.87, 10.34, 9.69, 9.27, 9.01, 8.62, 8.18, 7.81, 7.53, 7.19, 6.19, 6.73, 6.43, 6.16, 6.01, 5.93, 5.7, 5.34, 5.28, 5.24, 5.05, 4.97, 4.87, 4.81, 4.68, 4.51, 4.39, 4.33])


# NEU Werte vom Abkühlen des Arduinos
# Zeit (s)
x = np.array([13.44, 13.35, 12.76, 12.26, 11.92, 11.75, 11.61, 11.24, 10.87, 10.34, 9.69, 9.27, 9.01, 8.62, 8.18, 7.81, 7.53, 7.19, 6.19, 6.73, 6.43, 6.16, 6.01, 5.93, 5.7, 5.34, 5.28, 5.24, 5.05, 4.97, 4.87, 4.81, 4.68, 4.51, 4.39, 4.33])
#Temperatur (° C)
y = np.array([80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430])


averagex = np.mean(x)
averagey = np.mean(y)
maxerlabweichung = 40 # Maximal zugelassene Abweichung in %
a = 1 #Exponent für x für print
b = 1 #Exponent für y für print
c = 1 #counter
d = 1 #für while

#Funktion zur Berechnung von Durchschnitt, Min, Max und Abweichung
def min_max_abw():
    # Berechnung von Durchschnitt, Maximal- und Minimalwert
    average = np.mean(xy)
    maxxy = np.max(xy)
    minxy = np.min(xy)

    # Maximalen Abweichung vom Durchschnitt
    abweichungnumb = np.abs([maxxy - average, minxy - average])
    maxabweichungnumb = np.max(abweichungnumb)

    #Abweichung in %
    abweichung = (maxabweichungnumb / average) * 100

    return average, maxxy, minxy, maxabweichungnumb, abweichung

# im Falle eines antiproportinalen Zusammenhangs
def antiproportional(average, maxxy, minxy, maxabweichungnumb, abweichung):
    # Überprüfung der Abweichung
    if abweichung < maxerlabweichung:
        print("\n\n\n")
        # Ergebnisse ausgeben
        print(" - x entspricht T (Temperatur); y entspricht t (Zeit) - ")
        print("Durchschnitt von (x ↑",a,"* y ↑",b,"):", average)
        print("Maximaler Wert:", maxxy)
        print("Minimaler Wert:", minxy)
        print("\nMaximale Abweichung vom Durchschnitt (Absolute Zahl):", maxabweichungnumb)
        print("Maximale Abweichung vom Durchschnitt (%):", abweichung, "%")
        print("Maximal zugelassene Abweichung:", maxerlabweichung, "%")
        print("\nErgebnis:")
        
        print("(x ↑",a,"* y ↑",b,") = konstant (antiproportional)")
        print("(Die Abweichung vom Durchschnitt überschreitet die maximal zugelassene Abweichung nicht)")
        sys.exit()
    else:
        print("Durchschnitt von (x ↑",a,"/ y ↑",b,"):", average)
        print("Maximaler Wert:", maxxy)
        print("Minimaler Wert:", minxy)
        print("\nMaximale Abweichung vom Durchschnitt (Absolute Zahl):", maxabweichungnumb)
        print("Maximale Abweichung vom Durchschnitt (%):", abweichung, "%")
        print("Maximal zugelassene Abweichung:", maxerlabweichung, "%")
        print("\nErgebnis:")
        
        print("(x ↑",a,"* y ↑",b,") ist nicht konstant (nicht antiproportional)")
        print("(Die Abweichung vom Durchschnitt überschreitet die maximal zugelassene Abweichung)")
        

# im Falle eines proportionalen Zusammenhangs
def proportional(average, maxxy, minxy, maxabweichungnumb, abweichung):
    # Überprüfung der Abweichung
    if abweichung < maxerlabweichung:
        print("\n\n\n")
        # Ergebnisse ausgeben
        print(" - x entspricht T (Temperatur); y entspricht t (Zeit) - ")
        print("Durchschnitt von (x ↑",a,"/ y ↑",b,"):", average)
        print("Maximaler Wert:", maxxy)
        print("Minimaler Wert:", minxy)
        print("\nMaximale Abweichung vom Durchschnitt (Absolute Zahl):", maxabweichungnumb)
        print("Maximale Abweichung vom Durchschnitt (%):", abweichung, "%")
        print("Maximal zugelassene Abweichung:", maxerlabweichung, "%")
        print("\nErgebnis:")
        
        print("(x ↑",a,"/ y ↑",b,") = konstant (proportional)")
        print("(Die Abweichung vom Durchschnitt überschreitet die maximal zugelassene Abweichung nicht)")
        sys.exit()
    else:
        print("Durchschnitt von (x ↑",a,"/ y ↑",b,"):", average)
        print("Maximaler Wert:", maxxy)
        print("Minimaler Wert:", minxy)
        print("\nMaximale Abweichung vom Durchschnitt (Absolute Zahl):", maxabweichungnumb)
        print("Maximale Abweichung vom Durchschnitt (%):", abweichung, "%")
        print("Maximal zugelassene Abweichung:", maxerlabweichung, "%")
        print("\nErgebnis:")
        
        print("(x ↑",a,"/ y ↑",b,") ist nicht konstant (nicht proportional)")
        print("(Die Abweichung vom Durchschnitt überschreitet die maximal zugelassene Abweichung)")

try:
    #Antiproportionaler Zusammenhang
    if (x[1] > x[-1] and y[1] < y[-1]) or (x[1] < x[-1] and y[1] > y[-1]):
        print("Antiproportionaler Zusammenhang 1")
        xy = x * y
        average, maxxy, minxy, maxabweichungnumb, abweichung = min_max_abw()
        antiproportional(average, maxxy, minxy, maxabweichungnumb, abweichung)

        #Was soll passieren, wenn xy nicht konstantt ist (nicht antiproportional)?
        while d == 1: 
            #if (xy[1] > xy[-1] and x[1] < x[-1]) or (xy[1] < xy[-1] and x[1] > x[-1]): #Antiproportional
                c = c + 1
                print("Zusammenhang", c )
                a = a + 1 #Exponent von x erhöhen
                xy = xy * x
                average, maxxy, minxy, maxabweichungnumb, abweichung = min_max_abw()
                antiproportional(average, maxxy, minxy, maxabweichungnumb, abweichung)
        
            #else: #Proportional
            #    c = c + 1
            #    print("Zusammenhang", c )
            #    b = b + 1 #Exponent von y erhöhen
            #    xy = xy / y
            #    average, maxxy, minxy, maxabweichungnumb, abweichung = min_max_abw()
            #    antiproportional(average, maxxy, minxy, maxabweichungnumb, abweichung)

    #Proportionaler Zusammenhang
    else:
        print("Proportionaler Zusammenhang")
        xy = x / y
        average, maxxy, minxy, maxabweichungnumb, abweichung = min_max_abw()
        proportional(average, maxxy, minxy, maxabweichungnumb, abweichung)

        #Was soll passieren, wenn x/y nicht konstantt ist (nicht proportional)?
        while d == 1:
            if (xy[1] > xy[-1] and x[1] > x[-1]) or (xy[1] < xy[-1] and x[1] < x[-1]): #Proportional
                c = c + 1
                print("Zusammenhang", c )
                b = b + 1 #Exponent von y erhöhen
                xy = xy / y
                average, maxxy, minxy, maxabweichungnumb, abweichung = min_max_abw()
                proportional(average, maxxy, minxy, maxabweichungnumb, abweichung)

            else: #Antiproportional
                c = c + 1
                print("Zusammenhang", c )
                a = a + 1 #Exponent von x erhöhen
                xy = xy * x
                average, maxxy, minxy, maxabweichungnumb, abweichung = min_max_abw()
                proportional(average, maxxy, minxy, maxabweichungnumb, abweichung)


except SystemExit: #Dient dem Verhindern einer Errormessage bei Verwendung von sys.exit() Fehlerbehandlung:
    pass # Keine Fehlermeldung anzeigen, wenn das Programm gestoppt wurde
