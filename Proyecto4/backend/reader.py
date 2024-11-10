import yaml

class Reader(object):
    def __init__(self, filename):
      self.filename = filename
      self.estados = []
      self.alfabeto = []
      self.alfabetoEntrada = []
      self.tape_alphabet = []
      self.q0 = None
      self.aceptacion = None
      self.rechazo = None
      self.transiciones = {}
      self.cinta = []
      self.posCabezal = None
      self.get_states_and_alphabets()
      self.get_create_Transitions()
    
    def get_states_and_alphabets(self):
      with open(self.filename, 'r') as file:
        tm_machine = yaml.safe_load(file)
      self.estados = tm_machine['q_states']['q_list']
      self.alfabeto = tm_machine['alphabet']
      self.alfabetoEntrada = self.alfabeto
      self.tape_alphabet = tm_machine['tape_alphabet'] + self.alfabeto
      self.q0 = tm_machine['q_states']['initial']
      self.aceptacion = tm_machine['q_states']['final']
      self.rechazo = tm_machine['q_states']['reject']
      self.posCabezal = tm_machine['posHead']
      self.cadena = tm_machine['simulation_strings'][0]
    
    def get_create_Transitions(self):
      with open(self.filename, 'r') as file:
         tm_machine = yaml.safe_load(file)
      transiciones = {}
      lista_params = tm_machine['delta']
      valor = ''
      for l in lista_params:
        if valor != l['params']['initial_state']:
          valor = l['params']['initial_state']
          transiciones[valor] = {}
        input_value = l['params']['tape_input']
        transiciones[valor][input_value] = [l['output']['final_state'], 
                                            l['output']['tape_output'],
                                            l['output']['tape_displacement']]
      self.transiciones = transiciones