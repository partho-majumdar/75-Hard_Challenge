import nlpcloud


def ner(text):
    client = nlpcloud.Client(
        "llama-3-1-405b", "6dc6493331a49ca0b9a674fe3fd63e2e027350e4", gpu=True
    )

    response = client.entities(
        text,
        searched_entity="programming languages",
    )
    return response