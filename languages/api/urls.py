from django.urls import path
from .views import LanguageView, LanguageDetailView, ProgrammerView, ProgrammerDetailView, ParadigmView, ParadigmDetailView

urlpatterns = [
    # for language
    path('language/', LanguageView.as_view()),
    path('language/<int:pk>/', LanguageDetailView.as_view()),

    # for paradigm
    path('paradigm/', ParadigmView.as_view()),
    path('paradigmm/<int:pk>/', ParadigmDetailView.as_view()),

    # for paradigm
    path('programmer/', ProgrammerView.as_view()),
    path('programmer/<int:pk>/', ProgrammerDetailView.as_view()),
]
