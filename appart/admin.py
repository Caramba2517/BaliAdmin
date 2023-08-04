from django.contrib import admin
from django.forms import ClearableFileInput
from appart.models import RentUser, Location, Apartment, Feedback, SaveAp, SaveRequest, SendMessageForAll, \
    SendMessageForChooseUser
from django import forms


class ApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = "__all__"


class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'location', 'date')
    search_fields = ('id', 'author__username', 'location__name')
    list_filter = ('aps_type', 'location', 'bedroom', 'rent_term')
    ordering = ('-date',)
    readonly_fields = ('date',)
    form = ApartmentForm

    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            self.readonly_fields = ()
        else:
            self.readonly_fields = ('date',)
        form = super().get_form(request, obj, **kwargs)
        return form

    def get_readonly_fields(self, request, obj=None):
        if obj is None:
            return ()
        else:
            return 'date',

    def has_change_permission(self, request, obj=None):
        if obj is not None and request.user == obj.author:
            return True
        return request.user.is_superuser or request.user.has_perm('appart.can_edit_owned_apartment')

    def has_delete_permission(self, request, obj=None):
        if obj is not None and request.user == obj.author:
            return True
        return request.user.is_superuser or request.user.has_perm('appart.can_delete_owned_apartment')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    class Meta:
        model = Apartment


admin.site.register(RentUser)
admin.site.register(Location)
admin.site.register(Feedback)
admin.site.register(SaveAp)
admin.site.register(SaveRequest)
admin.site.register(SendMessageForAll)
admin.site.register(SendMessageForChooseUser)
admin.site.register(Apartment, ApartmentAdmin)
