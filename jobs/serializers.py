from rest_framework import serializers
from .models import JobListing


class JobListingSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobListing
        fields = ('creator', 'created', 'title', 'description', 'compensation', 'location', 'location_latitude', 'location_longitude', 'skills', 'remote', 'employer_name', 'employer_website', 'contact_name', 'contact_email')


