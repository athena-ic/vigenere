import unittest
from vigenere.cipher import vigdecrypt, vigencrypt

class TestCipher(unittest.TestCase):
    def test_encrypt(self):
        """
        test case for the encryption
        """
        message = "imperialcollege"
        keyword = "MATRIXMATRIXMAT"
        encrypted = "UMIVZFMLVFTIQGX"
        answer = vigencrypt(message, keyword)
        self.assertEqual(encrypted, answer)
    
    def test_decrypt(self):
        """
        test case for the decryption
        """
        message = "UMIVZFMLVFTIQGX"
        decrypted = "imperialcollege"
        keyword = "MATRIXMATRIXMAT"
        answer = vigdecrypt(message, keyword)
        self.assertEqual(decrypted, answer)

if __name__ == '__main__':
    unittest.main()