from src.app.integrations.get_rate import get_rate


def rate_dollar():
    data = get_rate()
    return data["Valute"]["USD"]["Value"]
