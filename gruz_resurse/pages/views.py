from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from .forms import ContactForm
from django.core.mail import send_mail, EmailMessage

from .sending_email_service import send_email


class IndexView(TemplateView):
    """View the main page"""

    template_name = "pages/index.html"


class ContactsView(FormView):
    """View the main page"""

    template_name = "pages/contacts.html"
    form_class = ContactForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        send_email(form.cleaned_data, "Контакти")
        return super().form_valid(form)


class ServicesView(TemplateView):
    """View the main page"""

    template_name = "pages/services.html"


class ComputerDiagnosticView(FormView):
    """View the main page"""

    template_name = "pages/computer-diagnostic.html"
    form_class = ContactForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        send_email(form.cleaned_data, "Комп'ютерна діагностика")
        return super().form_valid(form)


class FuelView(FormView):
    """View the main page"""

    template_name = "pages/fuel.html"
    form_class = ContactForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        send_email(form.cleaned_data, "Оптовий продаж палива")
        return super().form_valid(form)


class DangerousCargoTransportationView(FormView):
    """View the main page"""

    template_name = "pages/dangerous-cargo-transportation.html"
    form_class = ContactForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        send_email(form.cleaned_data, "Доставка небезпечних вантажів")
        return super().form_valid(form)


class TradeInView(FormView):
    """View the main page"""
    template_name = "pages/trade-in.html"
    form_class = ContactForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        send_email(form.cleaned_data, "Trade-in")
        return super().form_valid(form)


class LeasingView(FormView):
    """View the main page"""

    template_name = "pages/leasing.html"
    form_class = ContactForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        send_email(form.cleaned_data, "Leasing")
        return super().form_valid(form)


class SemiTrailersAttentionView(TemplateView):
    """View the main page"""

    template_name = "pages/semi-trailers-attention.html"


class ProductView(TemplateView):
    """View the main page"""

    template_name = "pages/product.html"


class TrucksView(FormView):
    """View the main page"""

    template_name = "pages/trucks.html"
    form_class = ContactForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        send_email(form.cleaned_data, "Ремонт та продаж вантажівок")
        return super().form_valid(form)


class AboutUsView(TemplateView):
    """View the main page"""

    template_name = "pages/about-us.html"
