import unittest
import main

class TestGrep(unittest.TestCase):

    def test_grep(self):
        tests = [
            ("files/test.txt", "h", ["hhola", "hcau", "chuli"]),
            ("files/test.txt", " ", [" ", " ", "numeros 789"]),
            ("files/test.txt", "12(52)?", ["1234", "1252"]),
            ("files/test.txt", "(1|2|3|4|5|6|7|8|9|0)+", ["1234", "1252", "513", "numeros 789"]),
            ("files/test.txt", ".....", ["hhola", "diego", "chuli", "numeros 789"]),
            ("files/constitucion.txt", "Ley", ["Ley N 24", "Ley"]),
            ("files/constitucion.txt", "(1|2|3|4|5|6|7|8|9|0)+", ["Ley N 24", "430", "Ordenase la publicacion del texto oficial de la Constitucion Nacional sancionada en 1853 con las reformas de los anos 1860 1866 1898 1957 y 1994", "Sancionada Diciembre 15 de 1994", "Promulgada Enero 3 de 1995", "ARTICULO 1", " Ordenase la publicacion del texto oficial de la Constitucion Nacional sancionada en 1853 con las reformas de los anos 1860 1866 1898 1957 y 1994 que es el que se transcribe a continuacion", "Articulo 1", "Articulo 2", "Articulo 3"]),
            ("files/constitucion.txt", "Ley|ARTICULO|24|Articulo", ['Ley N 24', 'Ley', 'ARTICULO 1', 'Articulo 1', 'Articulo 2', 'Articulo 3']),
            ("files/telefonos.txt", "54 9 11........", ["54 9 1117428196", "54 9 1156434343", "54 9 1178434343", "54 9 117843434343", "cosas antes 54 9 1117428196 cosas despues", "54 9 1112469424"]),
            ("files/telefonos.txt", "54 9 11((43)?|(..))(43)+", ["54 9 1156434343", "54 9 1178434343", "54 9 117843434343"]),
        ]

        for i, (filename, regex, expected) in enumerate(tests):
            with self.subTest(f"#{i}: regex: {regex}, file: {filename}"):
                got = main.execute(regex, filename)
                self.assertEqual(expected, got)

if __name__ == '__main__':
    unittest.main()