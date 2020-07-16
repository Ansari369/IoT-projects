import json
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey='9txnOj7i6F1b8kxKdiIO96GYI7V_xxjE3v34uB_a1ERp')

with open('./food.jpg', 'rb') as images_file:
    classes = visual_recognition.classify(
        images_file,
        threshold='0.6',
	classifier_ids='Ansari_1983119437').get_result()
print(json.dumps(classes, indent=2))
