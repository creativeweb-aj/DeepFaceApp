import os
from flask import Blueprint, request, render_template
from werkzeug.utils import secure_filename
from config.extension import UPLOAD_FOLDER
from src.SharedServices.MainService import MainService, StatusType
from deepface import DeepFace

FindFaceApi = Blueprint('find face view', __name__)


@FindFaceApi.route('/')
def index():
    return render_template("find-face/index.html")


@FindFaceApi.route('/upload-images', methods=['POST'])
def uploadImages():
    images = request.files['images']
    filename = secure_filename(images.filename)
    images.save(os.path.join(UPLOAD_FOLDER + '/albums/' + filename))
    response = {
        "status": StatusType.success.value,
        "data": None,
        "message": MainService.message('en').image_uploaded.value
    }
    return MainService.response(data=response, status_code=200)


@FindFaceApi.route('/upload-target-images', methods=['POST'])
def uploadTargetImages():
    image = request.files['image']
    filename = secure_filename(image.filename)
    image.save(os.path.join(UPLOAD_FOLDER + '/target/' + filename))
    response = {
        "status": StatusType.success.value,
        "data": None,
        "message": MainService.message('en').image_uploaded.value
    }
    return MainService.response(data=response, status_code=200)


@FindFaceApi.route('/find-face', methods=['POST'])
def findFace():
    data = request.get_json()
    fileName = data.get('file_name', None)
    file = os.path.join(UPLOAD_FOLDER + '/target/' + fileName)
    dbPath = os.path.join(UPLOAD_FOLDER + '/albums/')
    models = [
        "VGG-Face",
        "Facenet",
        "Facenet512",
        "Open Face",
        "DeepFace",
        "DeepID",
        "ArcFace",
        "Dlib",
        "SFace",
    ]
    dfs = DeepFace.find(
        img_path=file,
        db_path=dbPath,
        model_name=models[1],
        normalization='base',
        distance_metric="cosine"
    )
    dfFiles = dfs[0]['identity']
    images = []
    for dfFile in dfFiles:
        fileName = dfFile.split('//')[-1]
        filePath = request.host_url + 'static/uploads/albums/' + fileName
        images.append(filePath)
    response = {
        "status": StatusType.success.value,
        "data": {'images': images},
        "message": MainService.message('en').data_sent.value
    }
    return MainService.response(data=response, status_code=200)
