###############################################################################
# 4A00HB81 Python-ohjelmointi (TAMK 2025)
# =============================================================================
# TT06a.py
#
# Tämä esimerkki on tarkoitettu omatoimisen oppimisen tueksi ohjelmoinnin
# opiskeluun. Muu käyttö kielletty.
#
###############################################################################

k = int(input('Anna kuukauden numero (1 - 12): '))

p = 0
if k == 1:
    p = 31
elif k == 2:
    p = 28  # HUOM! Ei tunnista karkausvuotta!
elif k == 3:
    p = 31
elif k == 4:
    p = 30
elif k == 5:
    p = 31
elif k == 6:
    p = 30
elif k == 7:
    p = 31
elif k == 8:
    p = 31
elif k == 9:
    p = 30
elif k == 10:
    p = 31
elif k == 11:
    p = 30
elif k == 12:
    p = 31

if p != 0:
    print(f'Kuukaudessa numero {k} on {p} päivää.')
else:
    print('Tarkista kuukauden numero!')

###############################################################################
# EOF
