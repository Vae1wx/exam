from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView
from .models import Papers, Question
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# Create your views here.

class HomeView(TemplateView):
    template_name = "home.html"



class PapersListView(ListView):
    model = Papers
    context_object_name = 'papers'
    template_name = "paper_list.html"
    
    # def get(self, request):
    #     papers = Papers.objects.all() 
    #     context = {}
    #     context['papers'] = papers
    #     return render(request, 'paper_list.html', context)

class PapersDetailView(DetailView):
    def get(self, request, pk):
        paper = get_object_or_404(Papers, pk=pk)
        question_num = Question.objects.filter(paper_title=paper.id).count()
        question = Question.objects.filter(paper_title=paper.id)
        context = {}
        context['paper'] = paper
        context['question'] = question
        context['question_num'] = question_num
        return render(request, 'detail.html', context)



class PapersCreateView(LoginRequiredMixin, CreateView):
    model = Papers
    fields = ['paper_title', 'subject']
    template_name = "set_paper.html"
    success_url = reverse_lazy('set_questions')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class QuestionDetailView(DetailView):
    queryset = Question.objects.all()
    def post(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        queryset = Question.objects.all()
        
        context = {}
        
        context['question'] = question
        
        return render(request, 'set_questions.html', context)




class QuestionCreateView(CreateView):
    model = Question
    fields = ['paper_title', 'title', 'answer', 'right_answer', 'score']
    template_name = "set_questions.html"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class QuestionUpdateView(UpdateView):
    model = Question
    fields = ['answer']
    template_name = "result.html"
    

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_context_data(self, ** kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.get_object()
        context["paper"] = Papers.objects.filter(id=obj.paper_title_id)
        context["previous_question"] = Question.objects.filter(paper_title_id=obj.paper_title_id).filter(
            pk__lt=obj.pk).last()
        context["next_question"] = Question.objects.filter(paper_title_id=obj.paper_title_id).filter(
            pk__gt=obj.pk).first()
        # print(obj.title)
        return context
    
    def post(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        paper = get_object_or_404(Papers, pk=question.paper_title_id)
        question.answer = request.POST.get('answer')
        right_answer = self.get_object().right_answer
        if question.answer == right_answer:
            paper.paper_score = self.get_object().score
            
        
        question.save()
        paper.save()
        print(paper)
        return redirect(request.path_info)


class Check_answerView(DetailView):

    def get(self, request, pk):
        paper = get_object_or_404(Papers, pk=pk)
        question_num = Question.objects.filter(paper_title=paper.id).count()
        question = Question.objects.filter(paper_title=paper.id)
        an = request.POST.get('answer')
        
        context = {}
        context['paper'] = paper
        context['question'] = question
        context['question_num'] = question_num
        return render(request, 'check.html', context)
    
