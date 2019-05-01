# coding=<ASCII>

def compute(placement, time, rate):
  return placement * (1 + rate)**time

def interest():

  try:
    placement = int(input("Quel montant souhaitez-vous placer sur votre compte ?"))
    time = int(input("Combien d'annees souhaitez-vous placer votre argent ?"))
    rate = float(input("Quel est le taux d'interet ?"))

    if placement < 0 or time < 0 or rate < 0:
      raise ValueError
    else:
      roi = 0
      roi = compute(placement, time, rate)

  except ValueError as erreur:
    print("La valeur n'est pas valide \n")
    print(erreur)

  else:
    print("Ce placement va vous rapporter {:.2f} euros".format(roi))



print("Nous allons calculer ensemble votre retour sur capital !")
interest()
