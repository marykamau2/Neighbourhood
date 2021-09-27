
# from django.test import TestCase
# from .models import Profile,Post,Business,Neighbourhood
# from django.contrib.auth.models import User

# class TestProfile(TestCase):
#     def setUp(self):
#         self.user = User(username = 'doryn',email= 'doryn@gmail.com', password = '3rt5')
#         self.user.save()
        
#         self.neighbourhood = Neigbourhood(name = 'Goster', description = 'Next to Bamburi', police_number = 910, healthcenter_number = 56 )
#         self.neighbourhood.save()
        
#         self.profile = Profile(user=self.user, name='doryn', bio='my bio',profile_picture = 'image.png', location = 'kmos', neighbourhood = self.neighbourhood)
        
#     def test_instance(self):
#         self.assertTrue(isinstance(self.profile, Profile))
        
#     def test_save_profile(self):
#         profiles = Profile.objects.all()
#         self.assertTrue(len(profiles)>0)
        
#     def test_delete_profile(self):
#         profile = Profile.objects.all().delete()
#         self.assertTrue(len(profile)>0)
        
#     def tearDown(self):
#         Profile.objects.all().delete()
        
# class TestNeigbourhood(TestCase):
#     def setUp(self):
#         self.neighbourhood = Neigbourhood(name = 'Kianda', description = 'My heighbourhood', location='Keiyo',admin ='andy',neighbourhood_logo='logo.png', police_number = 0, healthcenter_number = 0,occupants_count='4' )
#         self.neighbourhood.save()
        
#     def test_instance(self):
#         self.assertTrue(isinstance(self.neighbourhood, Neigbourhood))
        
#     def test_save_heighbourhood(self):
#         hood = Neigbourhood.objects.all()
#         self.assertTrue(len(hood)>0)
        
#     def test_delete_neighbourhood(self):
#         hoods = Neigbourhood.objects.all().delete()
#         self.assertTrue(len(hoods)>0)
        
        
# class TestBusiness(TestCase):
#     def setUp(self):
#         self.user = User(username = 'mary',email= 'mmarynjerikamau@gmail.com', password = '123')
#         self.user.save()
        
#         self.neighbourhood = Neigbourhood(name = 'Kmos', description = 'My neighbourhood', police_number = 0, health_number = 0 )
#         self.hood.save()
        
    
#         self.busins = Business(name = 'Kuku base', email= 'kukubase@gmail.com', description = 'chicken base', neighbourhood=self.hood, user=self.user)
        
        
#     def test_instance(self):
#         self.assertTrue(isinstance(self.busins, Business))
        
#     def test_save_hood(self):
#         business = Business.objects.all()
#         self.assertTrue(len(business)>0)
        
#     def test_delete_hood(self):
#         business = Business.objects.all().delete()
#         self.assertTrue(len(business)>0)