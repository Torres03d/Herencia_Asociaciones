# run_tests.py
import unittest

if __name__ == "__main__":
    print("🔍 Ejecutando todas las pruebas unitarias...\n")
    suite = unittest.TestLoader().discover('tests')  
    runner = unittest.TextTestRunner(verbosity=2)    # Muestra más detalle en la salida
    runner.run(suite)
