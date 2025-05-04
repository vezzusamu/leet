
# La seguente classe rappresenta una calcolatrice semplice
# con metodi per somma, sottrazione, moltiplicazione e divisione.
# Ogni metodo accetta due numeri e restituisce il risultato
# dell'operazione. La divisione gestisce anche il caso di
# divisione per zero sollevando un'eccezione.
class Calcolatrice:
    def somma(self, a, b):
        return a + b

    def sottrai(self, a, b):
        return a - b

    def moltiplica(self, a, b):
        return a * b

    # Eccezione sollevata se si tenta di dividere per zero
    # Indica un errore di runtime, deve essere gestito
    def dividi(self, a, b):
        if b == 0:
            raise ValueError("Divisione per zero non permessa")
        return a / b
    
# La seguente classe mi permette di testare la calcolatrice
import unittest

class TestCalcolatrice(unittest.TestCase):
    def setUp(self):
        self.calcolatrice = Calcolatrice()

    def test_somma(self):
        self.assertEqual(self.calcolatrice.somma(2, 3), 5)
        self.assertEqual(self.calcolatrice.somma(-1, 1), 0)
        self.assertEqual(self.calcolatrice.somma(0, 0), 0)
    
    def test_sottrai(self):
        self.assertEqual(self.calcolatrice.sottrai(5, 3), 2)
        self.assertEqual(self.calcolatrice.sottrai(3, 5), -2)
        self.assertEqual(self.calcolatrice.sottrai(0, 0), 0)

    def test_moltiplica(self):
        self.assertEqual(self.calcolatrice.moltiplica(2, 3), 6)
        self.assertEqual(self.calcolatrice.moltiplica(-1, 1), -1)
        self.assertEqual(self.calcolatrice.moltiplica(0, 5), 0)

    def test_dividi(self):
        self.assertEqual(self.calcolatrice.dividi(6, 3), 2)
        self.assertEqual(self.calcolatrice.dividi(-6, 3), -2)
        self.assertEqual(self.calcolatrice.dividi(0, 1), 0)
        
        with self.assertRaises(ValueError):
            self.calcolatrice.dividi(5, 0)

    
# Questo è il punto di ingresso principale per eseguire i test
if __name__ == '__main__':
    # Questo comando esegue tutti i test definiti nella classe TestCalcolatrice
    unittest.main()
