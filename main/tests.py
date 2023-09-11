from django.test import TestCase, Client

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')
    
    # Check untuk bagian show_main pada view, dan memeriksa response
    def check_app_detail (self):
        # Mengirimkan request ke view show_main
        response = Client().get('/main/')
        
        # Menggecek apakah response status code adalah 200
        self.assertEquals(response.status_code, 200)

        self.assertEquals(response.context['app'], 'Sparkle Sphere')
        self.assertEquals(response.context['name'], 'Rumintang Jessica H')
        self.assertEquals(response.context['class'], 'PBP A')