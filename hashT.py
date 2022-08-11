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

    def hash_capture(T, chave) :
        if T[chave]:
            print(f'A: {T[chave]}') # printa o valor no espaço de memoria dado
        else:
            print('D')

      

capacidade = int(input())
myhash = HashTable(capacidade)
n_commands = int(input())


for x in range(n_commands):
  entrada = input().split()
  
  
  if entrada[0] == 'ADD':
    if myhash.hash_insert(myhash.tabela, int(entrada[1])) == 'hashIsFull':
        print('Toda memoria utilizada')
        break
  
  elif entrada[0] == 'CAP':
    myhash.hash_capture(myhash.tabela, int(entrada[1]))
  
  else: #entrada[0] == 'SCH'
    myhash.hash_search(myhash.tabela, int(entrada[1]))
