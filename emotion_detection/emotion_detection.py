from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def emotion_detector(text_to_analyze):
    if not text_to_analyze or text_to_analyze.strip() == "":
        return "No text provided for emotion detection."

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

        dominant_emotion = max(emotions, key=emotions.get)

        return {
            "anger": emotions["anger"],
            "disgust": emotions["disgust"],
            "fear": emotions["fear"],
            "joy": emotions["joy"],
            "sadness": emotions["sadness"],
            "dominant_emotion": dominant_emotion
        }

    except Exception as e:
        return f"Error analyzing emotion: {str(e)}"
print(emotion_detector("I am so happy today!")) 