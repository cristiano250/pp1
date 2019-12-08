import statistics

wynagrodzenie=[21600,4350,3920,5590,3250,4010]

srednia=statistics.mean(wynagrodzenie)
print('Średnia arytmetyczna wynagrodzenia w firmie to: {}zł'.format(srednia))
mediana=statistics.median(wynagrodzenie)
print('Mediana wynagrodzenia w firmie to: {}zł'.format(mediana))
odchylenie=statistics.pstdev(wynagrodzenie)
print('Odchylenie standardowe wynosi: {}'.format(odchylenie))