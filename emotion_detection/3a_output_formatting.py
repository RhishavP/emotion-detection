from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def emotion_detector(text_to_analyze):
    """
    Analyze the input text and return emotions in a structured format.
    """

    if not text_to_analyze or text_to_analyze.strip() == "":
        return None

    try:
        authenticator = IAMAuthenticator("your-api-key")
        nlu = NaturalLanguageUnderstandingV1(
            version="2022-04-07",
            authenticator=authenticator
        )
        nlu.set_service_url("your-service-url")

        response = nlu.analyze(
            text=text_to_analyze,
            features=Features(emotion=EmotionOptions())
        ).get_result()

        emotions = response["emotion"]["document"]["emotion"]

        # Extract individual scores
        anger = emotions["anger"]
        disgust = emotions["disgust"]
        fear = emotions["fear"]
        joy = emotions["joy"]
        sadness = emotions["sadness"]

        # Determine dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)

        return {
            "anger": anger,
            "disgust": disgust,
            "fear": fear,
            "joy": joy,
            "sadness": sadness,
            "dominant_emotion": dominant_emotion
        }

    except Exception:
        return None
print(emotion_detector("I am so happy today!"))