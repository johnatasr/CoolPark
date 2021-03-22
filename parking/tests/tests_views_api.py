from rest_framework import status
from rest_framework.test import APITestCase


class ParkViewSetTests(APITestCase):
    """
    Tests of ParkViewSet in parking.views.py
    """

    def setUp(self):
        self.data = {"plate": "ABC-1234"}

    def test_check_in_with_data(self):
        response = self.client.post("/parking", data=self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_check_in_wrong_data(self):
        data = {"plate": "abc-1234"}
        response = self.client.post("/parking", data=data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_check_in_no_data(self):
        response = self.client.post("/parking")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_check_out_without_pay(self):
        self.client.post("/parking", data=self.data, format="json")
        response = self.client.put("/parking/1/out")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_check_out_with_pay(self):
        self.client.post("/parking", data=self.data, format="json")
        self.client.put("/parking/1/pay")
        response = self.client.put("/parking/1/out")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_check_in_without_id(self):
        self.client.post("/parking", data=self.data, format="json")
        self.client.put("/parking/1/pay")
        response = self.client.put("/parking/out")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_pay_with_id(self):
        self.client.post("/parking", data=self.data, format="json")
        response = self.client.put("/parking/1/pay")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_pay_without_id(self):
        self.client.post("/parking", data=self.data, format="json")
        response = self.client.put("/parking/pay")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_pay_already_paid(self):
        self.client.post("/parking", data=self.data, format="json")
        self.client.put("/parking/1/pay")
        response = self.client.put("/parking/1/pay")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_parking_history_with_plate(self):
        self.client.post("/parking", data=self.data, format="json")
        self.client.put("/parking/1/pay")
        self.client.put("/parking/1/out")
        response = self.client.get("/parking/ABC-1234")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_parking_history_without_plate(self):
        self.client.post("/parking", data=self.data, format="json")
        self.client.put("/parking/1/pay")
        self.client.put("/parking/1/out")
        response = self.client.get("/parking/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
