from typing import Callable


def costumer_service(repositories: dict) -> dict:

    def add(costumer: tuple) -> None:
        # name = input('Nome: ').strip()
        # cpf = input('CPF:').strip()
        # data_nascimento = input('data de nascimento (DD/MM/AAAA): ').strip()
        # endereco = input('Endereço: ').strip()
        pass

    def update(costumer, ID: int) -> None:
        pass
        # result = costumer['get_costumer_by_id'](ID)

        # values_dict = {
        #     'nome': result[1],
        #     'cpf': result[2],
        #     'data_nascimento': result[3],
        #     'endereço': result[4], }

        # print(result, '\n dê enter para manter os valores atuais.')
        # for key in values_dict:
        #     novo_valor = input(f"novo valor para {c}: ").strip()
        #     if novo_valor != "":
        #         dados[key] = novo_valor

        # return (values_dict['nome'],
        #         values_dict['cpf'],
        #         values_dict['data_nascimento'],
        #         values_dict['endereço'], ID)

    def get_all() -> list[tuple]:

        return repositories['all']()

    return {'add': add,
            'update': update,
            'all': get_all, }
