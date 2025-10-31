###############################################################################
# 4A00HB81 Python-ohjelmoitni (TAMK 2025)
# =============================================================================
# TT05.py
#
# Tämä esimerkki on tarkoitettu omatoimisen oppimisen tueksi ohjelmoinnin
# opiskeluun. Muu käyttö kielletty.
#
###############################################################################

rajoitus = int(input('Anna hissin painorajoitus (kg): '))
paino1 = int(input('Anna henkilön 1 paino (kg): '))
paino2 = int(input('Anna henkilön 2 paino (kg): '))
paino3 = int(input('Anna henkilön 3 paino (kg): '))
paino4 = int(input('Anna henkilön 4 paino (kg): '))

yhteispaino = paino1 + paino2 + paino3 + paino4

#print(f'Yhteispaino = {yhteispaino} kg, painorajoitus {rajoitus} kg')

if yhteispaino > rajoitus:
    print('Painorajoitus ylitetty, hissiä ei saa käyttää!')
    print('(hissi ei suostu liikkumaan)')
else:
    print('Kiitos, hissi on käytettävissänne!')
    print('(hissi lähtee liikkeelle)')

###############################################################################
# EOF
