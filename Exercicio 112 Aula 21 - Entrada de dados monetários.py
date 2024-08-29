
from ex112.utilidadescev import moeda
from ex112.utilidadescev import dado


p = dado.leiadinheiro('Digite o preço: R$')
moeda.resumo(p , 32 , 12)  # type: ignore

