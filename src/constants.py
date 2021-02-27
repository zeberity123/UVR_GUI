"""
Store Appliation info and default data
"""
# pylint: disable=no-name-in-module, import-error
# -GUI-
from PySide2 import QtCore
# -Root imports-
from .inference import converter_v4

VERSION = "0.0.1"
APPLICATION_SHORTNAME = 'UVR'
APPLICATION_NAME = 'Ultimate Vocal Remover'
DEFAULT_SETTINGS = {
    # --Independent Data (Data not directly connected with widgets)--
    'inputPaths': [],
    # Directory to open when selecting a music file (Default: desktop)
    'inputsDirectory': QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.DesktopLocation),
    # Export path (Default: desktop)
    'exportDirectory': QtCore.QStandardPaths.writableLocation(QtCore.QStandardPaths.DesktopLocation),
    # Language in format {language}_{country} (Default: system language)
    'language': QtCore.QLocale.system().name(),
    # Presets for seperations
    'presets': {},
    # --Settings window -> Seperation Settings--
    # -Conversion-
    # Boolean
    'checkBox_gpuConversion': converter_v4.default_data['gpuConversion'],
    'checkBox_postProcess': converter_v4.default_data['postProcess'],
    'checkBox_tta': converter_v4.default_data['tta'],
    'checkBox_outputImage': converter_v4.default_data['outputImage'],
    'checkBox_stackOnly': converter_v4.default_data['stackOnly'],
    'checkBox_saveAllStacked': converter_v4.default_data['saveAllStacked'],
    'checkBox_modelFolder': converter_v4.default_data['modelFolder'],
    'checkBox_customParameters': converter_v4.default_data['customParameters'],
    'checkBox_stackPasses': False,
    # Combobox
    'comboBox_stackPasses': 1,
    # -Engine-
    'comboBox_engine': 'v4',
    'comboBox_resType': 'Kaiser Fast',
    # -Models-
    'comboBox_instrumental': '',
    'comboBox_stacked': '',
    # Sampling Rate (SR)
    'lineEdit_sr': converter_v4.default_data['sr'],
    'lineEdit_sr_stacked': converter_v4.default_data['sr'],
    # Hop Length
    'lineEdit_hopLength': converter_v4.default_data['hop_length'],
    'lineEdit_hopLength_stacked': converter_v4.default_data['hop_length'],
    # Window size
    'comboBox_winSize': converter_v4.default_data['window_size'],
    'comboBox_winSize_stacked': converter_v4.default_data['window_size'],
    # NFFT
    'lineEdit_nfft': converter_v4.default_data['n_fft'],
    'lineEdit_nfft_stacked': converter_v4.default_data['n_fft'],

    # --Settings window -> Preferences--
    # -Settings-
    # Command off
    'comboBox_command': 'Off',
    # Notify on seperation finish
    'checkBox_notifiyOnFinish': False,
    # Notify on application updates
    'checkBox_notifyUpdates': True,
    # Open settings on startup
    'checkBox_settingsStartup': True,
    # Disable animations
    'checkBox_disableAnimations': False,
    # Disable Shortcuts
    'checkBox_disableShortcuts': False,
    # Process multiple files at once
    'checkBox_multiThreading': False,
    # -Export Settings-
    # Autosave Instrumentals/Vocals
    'checkBox_autoSaveInstrumentals': False,
    'checkBox_autoSaveVocals': False,
}
