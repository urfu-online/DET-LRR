#  Уральский федеральный университет © 2021.
#  Цифровой университет/Цифровые образовательные технологии
from whitenoise.storage import CompressedManifestStaticFilesStorage


class WhiteNoiseStaticFilesStorage(CompressedManifestStaticFilesStorage):
    manifest_strict = False
