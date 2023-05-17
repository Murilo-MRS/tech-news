import sys
from tech_news.analyzer.ratings import top_5_categories
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category,
)


def handle_selected_option(option):
    functions = {
        0: get_tech_news,
        1: search_by_title,
        2: search_by_date,
        3: search_by_category,
        4: top_5_categories,
        5: sys.exit,
    }

    return functions[option]


def handle_input(option):
    input_options = {
        0: "Digite quantas notícias serão buscadas: ",
        1: "Digite o título: ",
        2: "Digite a data no formato aaaa-mm-dd: ",
        3: "Digite a categoria: ",
    }

    return input(input_options[option])


def handle_output(option):
    if option == 0:
        input_data = handle_input(option)
        result = handle_selected_option(option)(int(input_data))
        print(result)
    elif option == 5:
        print("Encerrando script")
        handle_selected_option(option)
    elif option == 4:
        result = handle_selected_option(option)()
        print(result)
    elif option in range(1, 4):
        input_data = handle_input(option)
        result = handle_selected_option(option)(input_data)
        print(result)


# Requisitos 11 e 12
def analyzer_menu():
    OPTIONS_AVAIBLE = (
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por categoria;\n"
        " 4 - Listar top 5 categorias;\n"
        " 5 - Sair.\n"
    )
    try:
        chosen_option = int(input(OPTIONS_AVAIBLE))
        if chosen_option in range(6):
            handle_output(chosen_option)
        else:
            raise ValueError
    except ValueError:
        sys.stderr.write("Opção inválida\n")
