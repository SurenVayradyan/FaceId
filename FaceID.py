from deepface import DeepFace
import json

from deepface.basemodels import ArcFace


def face_verify(img_1, img_2):
    try:
        result_dict = DeepFace.verify(img1_path=img_1, img2_path=img_2, model_name='ArcFace')
        with open('result.json', 'w') as file:
            json.dump(result_dict, file, indent=1, ensure_ascii=False)#indent разделяет строки, ensure форматирует кириллицу

        if result_dict.get('verified'):
            return 'Один и тот же человек. Проверка пройдена!'
        return '!!!Разные люди. Проверка не пройдена!!!'

    except Exception as _ex:
        return _ex

def face_analyze():
    try:
        result_dict = DeepFace.analyze(img_path='Faces/S.jpg', actions=['age', 'gender', 'race', 'emotion']) #путь и название фото для анализа

        with open('face_analyze.json', 'w') as file:
            json.dump(result_dict, file, indent=4, ensure_ascii=False)

        return result_dict

    except Exception as _ex:
        return _ex

def main():
    print(face_verify(img_1='Faces/FM2.jpg', img_2='Faces/S.jpg')) #сравнение по фото людей на единтичность
    print(face_analyze()) # возраст, гендер, раса, эмоция

if __name__ == '__main__':
    main()