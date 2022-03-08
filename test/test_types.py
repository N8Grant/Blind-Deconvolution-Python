from pylab.image.restoration.blind_deconv import blind_deconvolution
import unittest
import numpy as np

class TestTypes(unittest.TestCase):
    def test_return_type(self):
        random_img = np.random.uniform((28,28))
        self.assertEqual(type(np.array()), blind_deconvolution(random_img))

    def test_type_error(self):
        # check that s.split fails when the separator is not a string
        with self.assertRaises(Exception):
            blind_deconvolution([[1,2,3],
                                 [1,2,3],
                                 [1,2,3]])

if __name__ == '__main__':
    unittest.main()