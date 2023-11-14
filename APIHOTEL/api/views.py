from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.
class Home(APIView):
    template_name="index.html"
    def get(self, request):
        return render(request,self.template_name) 
    
class About(APIView):
    template_name="about.html"
    def get(self, request):
        return render(request,self.template_name) 
    
class Amenities(APIView):
    template_name="amenities.html"
    def get(self, request):
        return render(request,self.template_name) 
    
class Bookings(APIView):
    template_name="bookings.html"
    def get(self, request):
        return render(request,self.template_name) 
    
class Contact(APIView):
    template_name="contact.html"
    def get(self, request):
        return render(request,self.template_name) 
    
class Failed(APIView):
    template_name="failed.html"
    def get(self, request):
        return render(request,self.template_name) 
    
class Faqs(APIView):
    template_name="faqs.html"
    def get(self, request):
        return render(request,self.template_name) 
    
class Gallery(APIView):
    template_name="gallery.html"
    def get(self, request):
        return render(request,self.template_name) 
    
class Privacy(APIView):
    template_name="privacy-policy.html"
    def get(self, request):
        return render(request,self.template_name) 
    
class Rooms(APIView):
    template_name="rooms.html"
    def get(self, request):
        return render(request,self.template_name) 
class Success(APIView):
    template_name="success.html"
    def get(self, request):
        return render(request,self.template_name) 