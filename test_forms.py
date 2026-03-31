def test_invalid_url(self):
    response = self.client.get("/invalid-url/")
    self.assertEqual(response.status_code, 404)
