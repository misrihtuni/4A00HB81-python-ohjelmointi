###############################################################################
# 4A00HB81 Python-ohjelmointi (TAMK 2025)
# =============================================================================
# TT02.py
#
# Tämä esimerkki on tarkoitettu omatoimisen oppimisen tueksi ohjelmoinnin
# opiskeluun. Muu käyttö kielletty.
#
###############################################################################

kulutus = int(input('Anna sähkönkulutus (kWh): '))
print(f'Sähkönkulutus: {kulutus} kWh')

myynnin_perusmaksu = 1.79 # €/kk
myynnin_energiamaksu = 0.0629 # e/kWh
siirron_perusmaksu = 3.98 # €/kk
siirron_energiamaksu = 0.031868 # e/kWh
vero = 0.0279372 # e/kWh

myynti = myynnin_perusmaksu + kulutus * myynnin_energiamaksu
siirto = siirron_perusmaksu + kulutus * siirron_energiamaksu
summa = kulutus * vero + myynti + siirto

print(f'Arvioitu sähkölasku on {round(summa, 2)} euroa')

###############################################################################
# EOF
