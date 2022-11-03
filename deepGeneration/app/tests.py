from django.test import TestCase

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(name="charles", age=30, email="charles.beniac@gmail.com", mdp="secret")
        

    def test_for_test_method_name_length(self):
        """User lenght return the correct value"""
        charles = User.objects.get(name="charles")
        self.assertEqual(charles.for_test_method_name_length(), 7)


class MyappViewsTestCase(TestCase):
        def setUp(self):
            self.charles = User.objects.create(name="charles", age=30, email="charles.beniac@gmail.com", mdp="secret")
            self.benoit = User.objects.create(name="benoit", age=30, email="charles.beniac@gmail.com", mdp="secret")
            self.alain = User.objects.create(name="alain", age=30, email="charles.beniac@gmail.com", mdp="secret")
   
    # def test_user_list_authenticated_user(self):
    #         """ Not authentificated users are not allowed """   
    #         url = reverse('user-list')
    #         response = self.client.get(url)
    #         self.assertTemplateNotUsed(response, 'myapp/user_list.html')
    #         self.failUnlessEqual(response.status_code, 302)
        
        def test_user_list(self):
            """user list views is correctly define
                - return 200 status code
                - return correct context
                - return correct template
            """

            # On s'authentifie avant d'accéder à la page.  
            # self.client.login(username='charles', password='secret')

            url = reverse('user-list')
            response = self.client.get(url)
        
            # On teste si le code n'a pas rencontré de bug et que l'url existe bien
            self.failUnlessEqual(response.status_code, 200)

            # On teste le contexte passé au template.
            self.assertIsInstance(response.context['users'], QuerySet )
            self.assertEqual(len(response.context['users']), 3)

            
            # On teste que c'est bien le bon template qui est utilisé
            self.assertTemplateUsed(response, 'myapp/user_list.html')
            
            # On logout l'utilisateur
            # self.client.logout()    



# Il faut ensuite lancer:

# ./manage.py test myapp -v2