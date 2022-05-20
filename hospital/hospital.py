class Hospital:
  def __init__(self, nome, endereco):
    self.nome = nome
    self.endereco = endereco
    self.administradores = []
    self.enfermeiros = []
    self.medicos = []
    self.pacientes = {}
    self.matricula = 1 # A primeira pessoa contratada receberá esse número.
    self.pagamentos = []

  def contratar(self, funcionario):
    funcionario.matricula = self.matricula # Vincula a matricula a um funcionário
    self.matricula += 1 # Incrementa a matrícula
    if type(funcionario) == Administrador:
      self.administradores.append(funcionario.nome_completo())
    elif type(funcionario) == Enfermeiro:
      self.enfermeiros.append(funcionario.nome_completo())
    elif type(funcionario) == Medico:
      self.medicos.append(funcionario.nome_completo())
    else:
      print("Você não pode contratar")

  def entrada(self, paciente):
    self.pacientes[paciente.cpf] = 'Não avaliado' # É possível utilizar outra chave nessa lista

  def saida(self, paciente):
    del self.pacientes[paciente.cpf]

  def diagnostico(self, paciente, medico, diagnostico):
    self.pacientes[paciente.cpf] = "Diagnóstico: " + diagnostico + " dado por " + medico.nome_completo()

  def pagamento(self, administrador, funcionario, valor):
    if type(administrador) == Administrador: # Apenas o administrador pode efetuar o pagamento
      mensagem = administrador.nome_completo() + " pagou R$" + str(valor) + " para " + funcionario.nome_completo()
      self.pagamentos.append(mensagem)
    else:
      print("Falha no pagamento")

  def listar_funcionarios(): # TODO
    pass


class Administrador:
  def __init__(self, primeiro_nome, sobrenome, idade):
    self.primeiro_nome = primeiro_nome
    self.sobrenome = sobrenome
    self.idade = idade
    self.matricula = None # Inicializado vazio

  def nome_completo(self):
    return self.primeiro_nome + " " + self.sobrenome

class Enfermeiro:
  def __init__(self, primeiro_nome, sobrenome, idade):
    self.primeiro_nome = primeiro_nome
    self.sobrenome = sobrenome
    self.idade = idade
    self.matricula = None # Inicializado vazio

  def nome_completo(self):
    return self.primeiro_nome + " " + self.sobrenome

class Medico:
  def __init__(self, primeiro_nome, sobrenome, idade, crm, especialidade):
    self.primeiro_nome = primeiro_nome
    self.sobrenome = sobrenome
    self.idade = idade
    self.crm = crm
    self.matricula = None # Inicializado vazio
    self.especialidade = especialidade

  def nome_completo(self):
    return self.primeiro_nome + " " + self.sobrenome

class Paciente:
  def __init__(self, primeiro_nome, sobrenome, idade, cpf):
    self.primeiro_nome = primeiro_nome
    self.sobrenome = sobrenome
    self.idade = idade
    self.cpf = cpf

  def nome_completo(self):
    return self.primeiro_nome + " " + self.sobrenome

hospital = Hospital('Materdei', 'Av. do Contorno')
paciente1 = Paciente('Guilherme', 'Vidal', 34, '000.000.000-00')
paciente2 = Paciente('Casimiro', 'Rodrigues', 29, '000.000.000-01')
medico1 = Medico('Tereza', 'Cristina', 45, '23232', 'neuro')
medico2 = Medico('José', 'Rubino', 62, '11111', 'pediatria')
admin1 = Administrador('Maria', 'Cecilia', 19)
hospital.contratar(admin1)
hospital.contratar(medico1)
hospital.contratar(medico2)
hospital.entrada(paciente1)
hospital.entrada(paciente2)
hospital.diagnostico(paciente1, medico1, 'Dores de cabeça')
print(hospital.pacientes)
hospital.pagamento(admin1, medico1, 2000)
hospital.pagamento(admin1, medico2, 1000)
print(hospital.pagamentos)
