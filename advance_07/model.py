class SomeModel:
    def predict(self, message: str):
        pass


def custom_prediction(message: str) -> float:
    cnt = 0
    len_mes = len(message)
    for i in message:
        if i.isdigit():
            cnt += 1
    return cnt / len_mes


def predict_message_mood(
    message: str,
    model: SomeModel,
    bad_thresholds: float = 0.3,
    good_thresholds: float = 0.8,
) -> str:
    if len(message) == 0:
        return "Empty message"
    pred = model.predict(message)
    if pred < bad_thresholds:
        return "неуд"
    if pred > good_thresholds:
        return "отл"
    return "норм"
