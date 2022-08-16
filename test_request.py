"""
unittest for dta api
"""
import unittest
import requests

URL = "http://0.0.0.0:6000/query"
PARAMS = {"COUNTRY": "VN"}



class TestQuery(unittest.TestCase):
    """
    unittest class
    """
    def test_query(self):
        """
        test if request has return status code 200
        :return:
        """
        r = requests.get(URL, PARAMS)
        self.assertEqual(r.status_code, 200, "connection fail with status code {}".format(r.status_code))

    def test_data(self):
        """
        test if number of data items return from api is more than 0
        :return:
        """
        r = requests.get(URL, PARAMS)
        if r.status_code == 200:
            self.assertGreater(len(r.json()), 0, "data return has no item")


if __name__ == "__main__":
    unittest.main()
