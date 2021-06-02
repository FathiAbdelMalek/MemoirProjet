from django.contrib import admin

from . import models


class ElconferencesAdmin(admin.AdminSite):
    index_title = 'Admin Panel'
    site_header = 'Elconferences Admin Panel'
    site_title = 'Elconferences'


site = ElconferencesAdmin(name='ElconferencesAdmin')


class ConferenceAdmin(admin.ModelAdmin):
    list_display = ('title', 'place', 'date', 'organizer')
    list_filter = ('place', 'date', 'organizer')
    fieldsets = (
        ('Title and Description and Place', {
            'fields': ('title', 'description', 'place'),
            'classes': ('collapse',),
        }),
        ('Important Dates', {
            'fields': ('date', 'submission_deadline', 'confirmation_deadline', 'payment_deadline'),
            'classes': ('collapse',),
        }),
        ('Price', {
            'fields': ('pre_price', 'post_price'),
            'classes': ('collapse',),
        }),
    )


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('user', 'article_name', 'conference', 'status')
    list_filter = ('status', 'conference')
    fieldsets = (
        ('User Information', {
            'fields': ('user', 'first_name', 'last_name', 'email'),
            'classes': ('collapse',),
        }),
        ('Submission Information', {
            'fields': ('conference', 'article_name', 'abstract', 'article', 'authors'),
            'classes': ('collapse',),
        }),
    )


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    fields = ()


site.register(models.Conference, ConferenceAdmin)
site.register(models.Submission, SubmissionAdmin)
site.register(models.Author, AuthorAdmin)
