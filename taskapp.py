from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from playsound import playsound
import json
from watson_developer_cloud import VisualRecognitionV3
import json
import ibm_boto3
from ibm_botocore.client import Config, ClientError


visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey='9txnOj7i6F1b8kxKdiIO96GYI7V_xxjE3v34uB_a1ERp')

authenticator = IAMAuthenticator('ZmfQSpS-m85wNBln69v_ojQDkFIlhJMIrQP3w5Y3hegP')
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url('https://api.au-syd.text-to-speech.watson.cloud.ibm.com/instances/3e6111c0-3fec-4fe0-92d2-61e9250fc06b')

with open('./food.jpg', 'rb') as image_file:
    classes = visual_recognition.classify(
        image_file,
        threshold='0.6',
	classifier_ids='food').get_result()
print(json.dumps(classes, indent=2))

speak=json.loads(json.dumps(classes))

x=speak['images']

for i in x:
    for j in i['classifiers']:
        k=j['classes']
        for l in k:
            m=l['class']
            print(m)
            
with open('task.mp3', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            m,
            voice='en-US_AllisonVoice',
            accept='audio/mp3'        
        ).get_result().content)
playsound('task.mp3')


# Constants for IBM COS values
COS_ENDPOINT = "https://s3.jp-tok.cloud-object-storage.appdomain.cloud" # Current list avaiable at https://control.cloud-object-storage.cloud.ibm.com/v2/endpoints
COS_API_KEY_ID = "Rz4Bn5WfJ3NHLyoF3rQesiKjG6lXo-k8vnVBm3-rm_2z" # eg "W00YiRnLW4a3fTjMB-odB-2ySfTrFBIQQWanc--P3byk"
COS_AUTH_ENDPOINT = "https://iam.cloud.ibm.com/identity/token"
COS_RESOURCE_CRN = "crn:v1:bluemix:public:cloud-object-storage:global:a/d27055cdf70a4c8a82a0891135504b4c:be3efa61-d84f-4161-b654-255da6f7b06f::" # eg "crn:v1:bluemix:public:cloud-object-storage:global:a/3bf0d9003abfb5d29761c3e97696b71c:d6f04d83-6c4f-4a62-a165-696756d63903::"

 # Create resource
cos = ibm_boto3.resource("s3",
ibm_api_key_id=COS_API_KEY_ID,
ibm_service_instance_id=COS_RESOURCE_CRN,
 ibm_auth_endpoint=COS_AUTH_ENDPOINT,
config=Config(signature_version="oauth"),
endpoint_url=COS_ENDPOINT
)

def multi_part_upload(bucket_name, item_name, file_path):
    try:
        print("Starting file transfer for {0} to bucket: {1}\n".format(item_name, bucket_name))
        # set 5 MB chunks
        part_size = 1024 * 1024 * 5

        # set threadhold to 15 MB
        file_threshold = 1024 * 1024 * 15

        # set the transfer threshold and chunk size
        transfer_config = ibm_boto3.s3.transfer.TransferConfig(
        multipart_threshold=file_threshold,
        multipart_chunksize=part_size
        )

        # the upload_fileobj method will automatically execute a multi-part upload
        # in 5 MB chunks for all files over 15 MB
        with open(file_path, "rb") as file_data:
            cos.Object(bucket_name, item_name).upload_fileobj(
                Fileobj=file_data,
                Config=transfer_config
            )

        print("Transfer for {0} Complete!\n".format(item_name))
    except ClientError as be:
        print("CLIENT ERROR: {0}\n".format(be))
    except Exception as e:
        print("Unable to complete multi-part upload: {0}".format(e))

multi_part_upload("mohammadansari2", "ansari.mp3", "task.mp3")
