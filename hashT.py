class HashTable:
    def __init__(self, capacidade):
        self.tabela = [None] * ((2 * capacidade) + 1)
        
    def hash_insert(T, chave) :
        i = 0
        j = chave % len(T)

        while i < len(T):
            if T[j] == None:
                T[j] = chave
                print(f"E: {j}")
            else:
                i += 1
                j = (j + 1) % len(T)

        print('Toda memoria utilizada')
        return 'hashIsFull'
    
    def hash_search(T, chave) :
        i = 0
        j = chave % len(T)

        while i < len(T):
            if T[j] == None:
                return None
            if T[j] == chave:
                print(f'E: {j}') # found j
            else:
                i += 1
                j = (j + 1) % len(T)

        print('NE')


      

capacidade = int(input())
myhash = HashTable(capacidade)
n_commands = int(input())

for x in range(n_commands):
  entrada = input().split()
  
#   if hashFull:
#     print('Toda memoria utilizada')
#     break
  
  if entrada[0] == 'ADD':
    myhash.hash_insert(myhash.tabela, int(entrada[1]))
    
  
  elif entrada[0] == 'CAP':
    pass #capturar espaço de memoria, caso vazio printar D e caso preenchido printar A: esapaço de memoria(classe)
  
  else: #entrada[0] == 'SCH'
    pass #vê se o valor corresponde a alguma chave e, caso pertença, printa essa chave(hasheada), não encontrado: print(NE)
  