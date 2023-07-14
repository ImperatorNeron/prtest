from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from .forms import ContactForm, FeedbackForm

from .sending_email_service import send_email, send_feedback_email


class BaseContactFormView(FormView):
    """Base view for pages with feedback form"""

    template_name = None
    form_class = FeedbackForm
    success_url = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["feedback_form"] = context["form"]
        return context

    def form_valid(self, form):
        # Send message
        context = self.get_context_data()
        try:
            send_feedback_email(form.cleaned_data)
        except Exception as e:
            context[
                "errors"
            ] = "Помилка серверу, повідомлення не відправлене! Натисніть щоб закрити повідомлення!"
            return self.render_to_response(context=context)
        return super().form_valid(form)

    def form_invalid(self, form):
        context = self.get_context_data()
        # Add the error message here
        context[
            "errors"
        ] = "Невірно введені дані, повідомлення не відправлене! Натисніть щоб закрити повідомлення!"
        return self.render_to_response(context=context)


class BaseContactFeedbackFormsView(TemplateView):
    """Base view for pages with contact and feedback forms"""

    template_name = None
    contact_form_class = ContactForm
    feedback_form_class = FeedbackForm
    redirect_url = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add two forms to the context
        context["contact_form"] = self.contact_form_class()
        context["feedback_form"] = self.feedback_form_class()
        return context

    def form_validation(self, request, current_form, send_mail_method):
        error_message = "Невірно введені дані, повідомлення не надіслалося! " \
                        "Натисніть щоб закрити повідомлення!"
        if current_form.is_valid():
            try:
                send_mail_method(form_data=current_form.cleaned_data)
                return HttpResponseRedirect(self.redirect_url)
            except Exception as e:
                error_message = "Помилка серверу, повідомлення не відправлене! " \
                                "Натисніть щоб закрити повідомлення!"
        return render(
            request,
            self.template_name,
            {
                "contact_form": current_form if "contact_form" in request.POST else self.contact_form_class(),
                "feedback_form": current_form if "feedback_form" in request.POST else self.feedback_form_class(),
                "errors": error_message,
            },
        )

    def post(self, request):
        if "contact_form" in request.POST:
            # Process the submitted ContactForm if present in the POST data
            contact_form = self.contact_form_class(request.POST, request.FILES)
            return self.form_validation(request, contact_form, send_email)

        if "feedback_form" in request.POST:
            # Process the submitted FeedbackForm if present in the POST data
            feedback_form = self.feedback_form_class(request.POST)
            return self.form_validation(request, feedback_form, send_feedback_email)


class IndexView(BaseContactFormView):
    """View the main page"""

    template_name = "pages/index.html"
    success_url = reverse_lazy("index")


class ContactsView(BaseContactFeedbackFormsView):
    """View the contact page"""

    template_name = "pages/contacts.html"
    redirect_url = reverse_lazy("contacts")


class ServicesView(BaseContactFormView):
    """View the services page"""

    template_name = "pages/services.html"
    success_url = reverse_lazy("services")


class ComputerDiagnosticView(BaseContactFeedbackFormsView):
    """View the computer diagnostic page"""

    template_name = "pages/computer-diagnostic.html"
    redirect_url = reverse_lazy("contacts")


class FuelView(BaseContactFeedbackFormsView):
    """View the page with the sale of fuel in bulk"""

    template_name = "pages/fuel.html"
    redirect_url = reverse_lazy("fuel")


class DangerousCargoTransportationView(BaseContactFeedbackFormsView):
    """View page about transportation of dangerous goods"""

    template_name = "pages/dangerous-cargo-transportation.html"
    redirect_url = reverse_lazy("danger")


class TradeInView(BaseContactFeedbackFormsView):
    """View the trade-in page"""

    template_name = "pages/trade-in.html"
    redirect_url = reverse_lazy("trade-in")


class LeasingView(BaseContactFeedbackFormsView):
    """View the leasing page"""

    template_name = "pages/leasing.html"
    redirect_url = reverse_lazy("leasing")


class SemiTrailersAttentionView(BaseContactFormView):
    """View the semi-trailer page"""

    template_name = "pages/semi-trailers-attention.html"
    success_url = reverse_lazy("attention")


class ProductView(BaseContactFormView):
    """View the product page"""

    template_name = "pages/product.html"
    success_url = reverse_lazy("product")


class TrucksView(BaseContactFeedbackFormsView):
    """View the page repair and sale of trucks"""

    template_name = "pages/trucks.html"
    redirect_url = reverse_lazy("trucks")


class AboutUsView(BaseContactFormView):
    """View the about us page"""

    template_name = "pages/about-us.html"
    success_url = reverse_lazy("about")
