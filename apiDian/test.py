from django.test import TestCase, Client
import request
import hashlib

class ApiDianTest(TestCase):

    @classmethod
    def setup(self):
        self.client = Client()

    @patch('requests.post')
    def test_post_reportes(self):
        #Ejemplo correcto
        hashEnviar = hashlib.sha256(str('Productos salchipapa: 2000').encode('utf-8'))
        digestEnviar = hashEnviar.hexdigest()
        payload1 = {'hash': digestEnviar, 'informacion': 'Productos salchipapa: 2000'}
        #Ejemplo de cuando ocurriría un error con el hash-digest.
        hashEnviar = hashlib.sha256(str('Productos salchipapa: 3000').encode('utf-8'))
        digestEnviar = 'digest incorrecto'
        payload2 = {'hash': digestEnviar, 'informacion': 'Productos salchipapa: 3000'}
        #Obtenemos las respuestas
        r1 = requests.post('https://apidian.club/reportes/reportes/post', data=payload1)
        r2 = requests.post('https://apidian.club/reportes/reportes/post', data=payload2)

        self.assertEqual(r1.status_code, requests.codes.ok)
        print(r2.status_code)
