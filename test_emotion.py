from emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):

    def test_detect_emotion_with_valid_text(self):
        text = "I am so happy today!"
        result = emotion_detector(text)
        self.assertIsInstance(result, dict)
        self.assertIn('joy', result)

    def test_detect_emotion_with_empty_text(self):
        text = ""
        result = emotion_detector(text)
        self.assertEqual(result, "No text provided for emotion detection.")

    def test_emotion_analysis_with_valid_text(self):
        text = "I am feeling sad."
        result = emotion_detector(text)
        self.assertIsInstance(result, dict)
        self.assertIn('sadness', result)

    def test_emotion_analysis_with_empty_text(self):
        text = ""
        result = emotion_detector(text)
        self.assertEqual(result, "No text provided for emotion detection.")
    
if __name__ == '__main__':
    unittest.main()