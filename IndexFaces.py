import boto3

s3_client=boto3.client(
    's3',
    aws_access_key_id=' AKIA47ESFIHZAOZIVK44 ',
    aws_secret_access_key='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',

)

collectionId='FaceRecognitionDoorLock'

rek_client=boto3.client(
    'rekognition',
    aws_access_key_id='AKIA47ESFIHZAOZIVK44',
    aws_secret_access_key='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',
    region_name='ap-south-1'

)

bucket = 'face-recognition-door'
all_objects = s3_client.list_objects(Bucket=bucket)

list_response =rek_client.list_collections(MaxResults=2)

if collectionId in list_response['CollectionsIds']:

    rek_client.delete_collection(CollectionId=collectionId)

rek_client.create_collection(CollectionId=collectionId)


for content in all_objects['Contents']:
    collection_name,collection_image = content['Key'].split('/')

    if Collection_image :
        label = collection_name
        print('Indexing:', label)
        image= content['Key']
        index_response = rek_client.index_faces(
            CollectionId=collectionId,
            Image={'S3Object':{'Bucket':bucket,'Name':image}},
            ExternalImageId=label,
            MaxFaces=1,
            QualityFilter="AUTO",
            DetectionAttributes=['ALL'])

        print('FaceId', index_response['FaceRecords'][0]['Face']['FaceId'])
        