from rest_framework import routers
from .api import LeadViewSet

router = routers.DefaultRouter()

#Register route
#End Point = api/leads
#Pass in viewset LeadViewSet
router.register('api/leads', LeadViewSet, 'leads')

#Basically just give us the router thats registered
#for this endpoint
urlpatterns = router.urls
