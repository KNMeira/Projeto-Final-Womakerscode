from django.shortcuts import render, get_object_or_404
from .forms import FormServico
from django.http import HttpResponse, FileResponse
from .models import Servico, ServicoAdicional
from fpdf import FPDF
from io import BytesIO
from django.contrib.auth import login as login_django
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

@login_required(login_url='login')
def novo_servico(request):
    if request.method == "GET":
        form = FormServico()
        return render(request, 'novo_servico.html', {'form': form})
    elif request.method == "POST":
        form = FormServico(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Salvo com sucesso')
        else:
            return render(request, 'novo_servico.html', {'form': form})
        
@login_required(login_url='login')        
def listar_servico(request):
    if request.method == "GET":
        servicos = Servico.objects.all()
        return render(request, 'listar_servico.html', {'servicos': servicos})

@login_required(login_url='login')    
def servico(request):
    servico = get_object_or_404(Servico, identificador=identificador)
    return render(request, 'servico.html', {'servico': servico})

@login_required(login_url='login')
def gerar_os(request):
    servico = get_object_or_404(Servico, identificador=identificador)

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font('Arial', 'B', 12)

    pdf.set_fill_color(240,240,240)
    pdf.cell(35, 10, 'Cliente:', 1, 0, 'L', 1)
    pdf.cell(0, 10, f'{servico.cliente.nome}', 1, 1, 'L', 1)

    pdf.cell(35, 10, 'Manutenções:', 1, 0, 'L', 1)

    categorias_manutencao = servico.categoria_manutencao.all()
    for i, manutencao in enumerate(categorias_manutencao):
        pdf.cell(0, 10, f'- {manutencao.get_titulo_display()}', 1, 1, 'L', 1)
        if not i == len(categorias_manutencao) -1:
            pdf.cell(35, 10, '', 0, 0)

    pdf.cell(35, 10, 'Data de início:', 1, 0, 'L', 1)
    pdf.cell(0, 10, f'{servico.data_inicio}', 1, 1, 'L', 1)
    pdf.cell(35, 10, 'Data de entrega:', 1, 0, 'L', 1)
    pdf.cell(0, 10, f'{servico.data_entrega}', 1, 1, 'L', 1)
    pdf.cell(35, 10, 'Protocolo:', 1, 0, 'L', 1)
    pdf.cell(0, 10, f'{servico.protocole}', 1, 1, 'L', 1)
    pdf.cell(35, 10, 'Preco total:', 1, 0, 'L', 1)
    pdf.cell(0, 10, f'{servico.protocole}', 1, 1, 'L', 1)
    
    pdf_content = pdf.output(dest='S').encode('latin1')
    pdf_bytes = BytesIO(pdf_content)
   
    return FileResponse(pdf_bytes, as_attachment=True, filename=f"os-{servico.protocole}.pdf")

@login_required(login_url='login')
def servico_adicional(request):
    identificador_servico = request.POST.get('identificador_servico')
    titulo = request.POST.get('titulo')
    descricao = request.POST.get('descricao')
    preco = request.POST.get('preco')

    servico_adicional = ServicoAdicional(titulo=titulo,
                                        descricao=descricao,
                                        preco=preco)
    
    servico_adicional.save()

    servico = Servico.objects.get(identificador=identificador_servico)
    servico.servicos_adicionais.add(servico_adicional)
    servico.save()

    return HttpResponse("Salvo")


def login(request):
     if request.method == "GET":
         return render(request, 'login.html')    
     else:
          username = request.POST.get('username')
          senha = request.POST.get('senha')

          user = authenticate(username=username, password=senha)

          if user:
               login_django(request, user)
               
               return redirect('clientes')
          else:
               return HttpResponse('Email ou senha inválidos')


def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else: 
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
     
        user = User.objects.filter(username=username).first()

        if user:
             return HttpResponse('Já existe um usuário com esse username')
        
        user = User.objects.create_user(username=username, email=email,  password=senha)
        user.save()
        return render(request ,'login.html')

@login_required(login_url='login')
def gerenciamentoPerfil(request):
    if request.method == "GET":
        return render(request, 'gerenciamentoPerfil.html')
    else:
        usuario = request.user
        if usuario.is_authenticated:
            email = request.POST.get('email')
            senha = request.POST.get('senha')
            usuario.email = email
            usuario.senha = senha
            usuario.save()
            messages.success(request, 'Perfil atualizado com sucesso')
        return render(request, 'gerenciamentoPerfil.html', {'usuario': usuario})