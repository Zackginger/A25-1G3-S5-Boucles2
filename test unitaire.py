import pytest
from SolutionDebug2 import retrait

def test_retrait():
    montant_initial=1000
    solde= montant_initial
    retrait1=100
    retrait2=20
    resultatattendu=880

    solde = retrait(solde, retrait1)
    resultatobtenu = retrait(solde, retrait2)

    assert resultatattendu == resultatobtenu

    def test_retrait2():
        montant_initial = 1000
        solde = montant_initial
        retrait1 = 900
        retrait2 = 200
        resultatattendu = 0

        solde = retrait(solde, retrait1)
        resultatobtenu = retrait(solde, retrait2)

        assert resultatattendu == resultatobtenu

def test_retrait3():
    montant_initial=1000
    solde= montant_initial
    retrait1=100
    retrait2=-20
    resultatattendu=900

    solde = retrait(solde, retrait1)
    resultatobtenu = retrait(solde, retrait2)

    assert resultatattendu == resultatobtenu

def test_retrait4():
    montant_initial=1000
    solde= montant_initial
    retrait1=900
    retrait2=99.5
    resultatattendu=0.5

    solde = retrait(solde, retrait1)
    resultatobtenu = retrait(solde, retrait2)

    assert resultatattendu == resultatobtenu
