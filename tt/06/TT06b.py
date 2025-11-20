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

# kuukaudet 1, 3, 5, 7, 8, 10, 12: 31 päivää
# kuukaudet 4, 6, 9, 11: 30 päivää
# kuukausi 2: 28 päivää (tai 29)

if 1 <= k <= 12:
    if k == 1 or k == 3 or k == 5 or k == 7 or k == 8 or k == 10 or k == 12:
        p = 31
    elif k == 2:
        p = 28  # HUOM! Ei tunnista karkausvuotta!
    elif k == 4 or k == 6 or k == 9 or k == 11:
        p = 30

    print(f'Kuukaudessa numero {k} on {p} päivää.')
else:
    print(f'Kuukauden numero ei kelpaa!')

###############################################################################
# EOF
