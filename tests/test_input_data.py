import unittest

from main import InputData


class InputDataTests(unittest.TestCase):
    def testValidXML(self):
        expected_dict = {
            'policy.1234.title': 'ELQUESE',
            'policy.1234.control_list.control.1111.statement': 'TEXTO QUE QUIERO SACAR',
            'policy.1234.control_list.control.1111.description': 'TEXT EXAMPLE DESCRIPTION',
            'policy.1234.control_list.control.2222.statement': 'OTRO TEXTO QUE QUIERO SACAR',
            'policy.1234.control_list.control.2222.subcontrol.control.3333.statement': 'el texto 3'
        }
        parsed_dict = InputData(path='input_001.xml').get_dict()
        self.assertDictEqual(parsed_dict, expected_dict)
