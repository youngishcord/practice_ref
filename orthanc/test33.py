from pprint import pprint
import requests
import json

def main() -> None:

    #url = f'http://localhost:8042/changes'
    #url = f"http://localhost:8042/series/9598b8eb-563ee80b-2e34356d-976da9c4-9110f727/"

    data = {
        "Expand": True,
        "RequestedTags":["PatientID", "PatientName"]
    }

    q = {
    "Level": "Series",
    "Expand": True,
    "Query": {
      "BodyPartExamined":"SPINE"
    },
    "RequestedTags": ["PatientName", "PatientID", "StudyDescription", "StudyDate", "StudyInstanceUID", "ModalitiesInStudy", "NumberOfStudyRelatedSeries"]
    }

    w = {
    "Expand": True,
    "RequestedTags": ["PatientName", "PatientID", "StudyDescription", "StudyDate", "StudyInstanceUID", "ModalitiesInStudy", "NumberOfStudyRelatedSeries"]
    }
    print(json.dumps(q))

    a = requests.get('http://localhost:8042/series/9598b8eb-563ee80b-2e34356d-976da9c4-9110f727?requestedTags=PatientName;PatientBirthDate;PatientID;PatientSex;SeriesDate;Manufacturer;ManufacturerModelName;StudyInstanceUID')
    #############################################################################################ЭТО УСПЕХ ДАМЫ И ГОСПОДА
    #a = requests.get(url, data=json.dumps(data))
    print(a)
    a = a.content.decode('utf-8')
    print(a)

if __name__ == '__main__':
    main()