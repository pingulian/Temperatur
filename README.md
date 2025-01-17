*Temperatur-Zeit.ino*

Sekündlich werden Temperaturwerte ausgelesen. Die Werte können per BLE an ein Smartphone gesendet werden. Auf den Smartphone ist dafür beispielsweise die App "nRF Connect" nötig.
Der Arduino kann nun auch ohne Verbindung zu einem Computer genutzt werden.

Bemerkungen:

(1) der Arduino beginnt bei der Zeit -20 an, damit man eine kurze Vorbereitungszeit hat.

(2) in "nRF Connect" muss als Kodierung für die zu empfangenden Daten "UTF-8" eingestellt werden.

(3) Zum Beheben von Problemen: Falls der Arduino bei Verbindung des Smartphones über BLE direkt abstürzt, liegt dies möglicherweise an einer instabilen Stromversorgung (z.B. Powerbank voll aufladen oder an ein Smartphone anschließen).




*Temperatur.py*

BACON1 mit Temperaturwerten.
Stellt mit idealisierten Werten den antiproportionalen Zusammenhang x*y = konst. fest.
