from django.core.urlresolvers import reverse_lazy
from django.db import transaction
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.shortcuts import render
from rest_framework import viewsets
from .serializer import *
from .forms import *
from Realestate4.logger import log
class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
class AgentReferalViewSet(viewsets.ModelViewSet):
    queryset = AgentReferal.objects.all()
    serializer_class = AgentReferalSerializer
class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
class PropertyTypeViewSet(viewsets.ModelViewSet):
    queryset = PropertyType.objects.all()
    serializer_class = PropertyTypeSerializer
class AgentList(ListView):
    model = Agent
def agentproperty(request):
    try:
        form = PropertyTypeForm()
        if request.method == "POST":
            form = PropertyTypeForm(request.POST)
            if form.is_valid():
                p = PropertyType ()
                p.description = form.cleaned_data["description"]
                p.save()

            else:
                form = PropertyTypeForm()

        ag = PropertyType.objects.all()
        return render(request, "agentproperty.html", {"agentproperty": ag, "form": form})
    except:
        print("property not valid")
def agentlocation(request):

    form = LocationForm()
    if request.method == "POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            l = Location ()
            l.location_name = form.cleaned_data["location_name"]
            l.city_name = form.cleaned_data["city_name"]

            l.save()

        else:
            form = LocationForm()
    lo = Location.objects.all()
    return render(request, "agentlocation.html", {"agentlocation": lo, "form": form})

class AgentCreate(CreateView):
    model = Agent
    fields = ['first_name', 'first_name' 'age', 'education', 'company_name', 'specialization','experience','agent_notes',
              'mobile_number','phone_number','email_id','media_name', 'property_type', 'location']
    log.error(fields)
class AgentAddrLocArefCreate(CreateView):
    model = Agent
    fields = ['first_name', 'last_name', 'age', 'education', 'company_name', 'specialization', 'experience',  'agent_notes',
              'mobile_number','phone_number','email_id','media_name', 'property_type', 'location']
    success_url = reverse_lazy('agent-list')
    log.info(fields)

    def get_context_data(self, **kwargs):

        data = super(AgentAddrLocArefCreate, self).get_context_data(**kwargs)
        log.info('AgentAddrLocArefCreate data')
        if self.request.POST:
            log.info('AgentAddrLocArefCreate requst is pass')

            data['address'] = AddressFormSet(self.request.POST)
            data['agentreferal'] = AgentReferalFormSet(self.request.POST)
        else:

            data['address'] = AddressFormSet()
            data['agentreferal'] = AgentReferalFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        try:

            address = context['address']
            agentreferal = context['agentreferal']

            with transaction.atomic():
                self.object = form.save()

                if address.is_valid() and agentreferal.is_valid():

                    address.instance = self.object
                    agentreferal.instance = self.object

                    address.save()
                    agentreferal.save()
                    log.error(context['name'] + "," + validate_first_name + validate_last_name + ('validation is roung'))
            return super(AgentAddrLocArefCreate, self).form_valid(form)

        except:
            print("hello")

class AgentUpdate(UpdateView):
    model = Agent
    success_url = '/'
    fields = ['first_name', 'last_name', 'age', 'education', 'company_name', 'specialization', 'experience',
              'agent_notes', 'mobile_number','phone_number','email_id','media_name', 'property_type', 'location']


class AgentAddrLocArefUpdate(UpdateView):
    model = Agent
    fields = ['first_name', 'last_name', 'age', 'education', 'company_name', 'specialization', 'experience',
              'agent_notes', 'mobile_number','phone_number','email_id','media_name', 'property_type', 'location']
    success_url = reverse_lazy('agent-list')


    def get_context_data(self, **kwargs):
        data = super(AgentAddrLocArefUpdate, self).get_context_data(**kwargs)
        log.info('AgentAddrLocArefUpdate data')

        if self.request.POST:
            log.info('AgentAddrLocArefUpdate requst is pass')

            #form1 = AgentForm(self.request.POST, self.request.FILES)
            #if form1.is_valid():
                #log.info(self.request.FILES['first_name'])

            data['address'] = AddressFormSet(self.request.POST, instance=self.object)
            data['agentreferal'] = AgentReferalFormSet(self.request.POST, instance=self.object)
        else:

            data['address'] = AddressFormSet(instance=self.object)
            data['agentreferal'] = AgentReferalFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        #log.debug(context)

        address = context['address']
        agentreferal = context['agentreferal']
        log.info('AgentAddrLocArefUpdate data is valid')

        with transaction.atomic():
            self.object = form.save()

            if address.is_valid() and agentreferal.is_valid():


                address.instance = self.object
                agentreferal.instance = self.object

                address.save()
                agentreferal.save()

        return super(AgentAddrLocArefUpdate, self).form_valid(form)


class AgentDelete(DeleteView):
    model = Agent
    success_url = reverse_lazy('agent-list')
    log.warning('agent delete')





