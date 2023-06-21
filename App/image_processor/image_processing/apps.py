from django.apps import AppConfig
import joblib
import keras


class ImageProcessingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'image_processing'
    path = 'image_processor.image_processing'  # Шлях до модуля вашої програми
    model = None  # Початкове значення для моделі

    def ready(self):
        # Завантажуємо модель
        file = open('E:\\DNeiron\\Image_text_recognition_CRNN\\App\\image_processor\\image_processing\\Neiron\\modelBiggest.json',mode='r')
 
        # read all lines at once
        model_txt = file.read()

        self.model = keras.models.model_from_json(model_txt)
        self.model.load_weights('E:\\DNeiron\\Image_text_recognition_CRNN\\App\\image_processor\\image_processing\\Neiron\\BiggestModel.01-1.37.h5')