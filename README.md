servidor master possui uma msg(teste) em hash
cliente pergunta se tem algum tipo de validação
servidor responde que tem 3 bytes zero antes

for i in range (0, 10000000):
  s=hashlib.sha256()
  s.update(strict.pack("I", i)+b'vitorialeticia')
  s.hexdigest()
  input(str(i)+''+a)
