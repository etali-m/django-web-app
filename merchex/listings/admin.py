from django.contrib import admin

from listings.models import Band

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre') #liste des gens des champs que nous souhaitons afficher

admin.site.register(Band, BandAdmin)

