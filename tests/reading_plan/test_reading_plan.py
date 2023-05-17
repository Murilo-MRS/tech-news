from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501
import pytest


@pytest.fixture
def mock_news():
    return [
        {
            "url": "https://blog.betrybe.com/tecnologia/site-responsivo/",
            "title": "Site responsivo: o que é e 10 dicas para aplicar",
            "timestamp": "10/05/2023",
            "writer": "Lucas Marchiori",
            "reading_time": 7,
            "summary": "Com o avanço da tecnologia, grande parte das pessoas possui um celular para realizar suas tarefas. Por isso, hoje em dia pessoas programadoras dificilmente fazem aplicações somente para desktops ou notebooks e criar um site responsivo passou a ser prioridade para as organizações.",  # noqa: E501
            "category": "Tecnologia",
        },
        {
            "url": "https://blog.betrybe.com/tecnologia/modelo-as-a-service/",
            "title": "SaaS, GaaS, IaaS, DaaS, PaaS:"
            " entenda o modelo as a service",
            "timestamp": "27/04/2023",
            "writer": "Cairo Noleto",
            "reading_time": 10,
            "summary": "Você sabe o que é computação em nuvem? Se você já usou armazenamento no Google Drive ou editou documentos em softwares on-line, já utilizou o modelo as a service, que é a base da distribuição de recursos de computação em nuvem no mercado.",  # noqa: E501
            "category": "Tecnologia",
        },
        {
            "url": "https://blog.betrybe.com/tecnologia/"
            "tecnologia-na-educacao/",
            "title": "Tecnologia na educação: 7 benefícios para"
            " aplicar em sala de aula",
            "timestamp": "20/04/2023",
            "writer": "Cairo Noleto",
            "reading_time": 20,
            "summary": "A tecnologia na educação é uma realidade que veio para ficar. Afinal, a tecnologia está presente em todos os aspectos da nossa vida, e na educação não poderia ser diferente. Por isso, é importante que as pessoas profissionais da área estejam preparadas para utilizar a tecnologia a favor da educação.",  # noqa: E501
            "category": "Tecnologia",
        },
        {
            "url": "https://blog.betrybe.com/tecnologia/fastapi-e-flask/",
            "title": "FastAPI e Flask: frameworks para APIs em Python",
            "timestamp": "13/04/2023",
            "writer": "Lucas Marchiori",
            "reading_time": 30,
            "summary": "Python é uma linguagem de programação que vem crescendo muito nos últimos anos. Por isso, é natural que a comunidade tenha criado diversos frameworks para facilitar o desenvolvimento de aplicações. Neste artigo, vamos falar sobre dois deles: FastAPI e Flask.",  # noqa: E501
            "category": "Tecnologia",
        },
    ]


@pytest.fixture
def mock_expected():
    return {
        "readable": [
            {
                "unfilled_time": 3,
                "chosen_news": [
                    (
                        "Site responsivo: o que é e 10 dicas para aplicar",
                        7,
                    ),
                    (
                        "SaaS, GaaS, IaaS, DaaS, PaaS:"
                        " entenda o modelo as a service",
                        10,
                    ),
                ],
            },
            {
                "unfilled_time": 0,
                "chosen_news": [
                    (
                        (
                            "Tecnologia na educação: 7 benefícios para"
                            " aplicar em sala de aula"
                        ),
                        20,
                    )
                ],
            },
        ],
        "unreadable": [
            ("FastAPI e Flask: frameworks para APIs em Python", 30),
        ],
    }


def test_reading_plan_group_news(mocker, mock_news, mock_expected):
    with pytest.raises(
        ValueError, match="Valor 'available_time' deve ser maior que zero"
    ):
        ReadingPlanService.group_news_for_available_time(-3)

    mocker.patch.object(
        ReadingPlanService, "_db_news_proxy", return_value=mock_news
    )

    result = ReadingPlanService().group_news_for_available_time(20)
    assert result == mock_expected
