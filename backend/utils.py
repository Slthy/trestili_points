from datetime import datetime


CATEGORIES_DICT: dict[str, str] = {
    ' Esordienti (P):': 'Esordienti (P)',
    ' Giovanissimi:': 'Giovanissimi',
    ' Esordienti B:': 'Esordienti B',
    ' Esordienti A:': 'Esordienti A',
    ' Ragazzi:': 'Ragazzi',
    ' Juniores:': 'Juniores',
    ' Cadetti:': 'Cadetti',
    ' Senior:': 'Senior'
}

GENDER_INDEX_DICT = {
    0: 'W',
    1: 'M'
}

CATEGORY_CODES_FOR_HTML = [ "tbody_assoluta_f", "tbody_assoluta_m"]

GENDER_BY_INDEX_DICT: dict = {
    "tbody_assoluta_f" : "assoluti_f",
    "tbody_assoluta_m" : "assoluti_m",
    #"tbody_cat_1003_F" : "ragazzi_f",
    #"tbody_cat_1004_F" : "juniores_f",
    #"tbody_cat_1005_F" : "cadetti_f",
    #"tbody_cat_1006_F" : "senior_f",
    #"tbody_cat_3_M" : "ragazzi_m",
    #"tbody_cat_4_M" : "juniores_m",
    #"tbody_cat_5_M" : "cadetti_m",
    #"tbody_cat_6_M" : "senior_m",
}

RACE_FROM_RESULT_TO_STARTLIST_DICT: dict = {
    '50 SL': '50 Stile Libero',
    '50 DO': '50 Dorso',
    '50 RA': '50 Rana',
    '50 FA': '50 Farfalla',
    '100 SL': '100 Stile Libero',
    '100 DO': '100 Dorso',
    '100 RA': '100 Rana',
    '100 FA': '100 Farfalla',
    '100 MI': '100 Misti',
    '200 SL': '200 Stile Libero',
    '200 DO': '200 Dorso',
    '200 RA': '200 Rana',
    '200 FA': '200 Farfalla',
    '200 MI': '200 Misti',
    '400 SL': '400 Stile Libero',
    '400 MI': '400 Misti',
    '800 SL': '800 Stile Libero',
    '1500 SL': '1500 Stile Libero'
}

FINVENETO_TO_FINA_DICT: dict = {
    '50 SL': ('50', 'FREE'),
    '50 DO': ('50', 'BACK'),
    '50 RA': ('50', 'BREAST'),
    '50 FA': ('50', 'FLY'),
    '100 SL': ('100', 'FREE'),
    '100 DO': ('100', 'BACK'),
    '100 RA': ('100', 'BREAST'),
    '100 FA': ('100', 'FLY'),
    '100 MI': ('100', 'MEDLEY'),
    '200 SL': ('200', 'FREE'),
    '200 DO': ('200', 'BACK'),
    '200 RA': ('200', 'BREAST'),
    '200 FA': ('200', 'FLY'),
    '200 MI': ('200', 'MEDLEY'),
    '400 SL': ('400', 'FREE'),
    '400 MI': ('400', 'MEDLEY'),
    '800 SL': ('800', 'FREE'),
    '1500 SL': ('1500', 'FREE')
}

FINVENETO_TO_FINA_COURSES_DICT: dict = {
    '25': 'SCM',
    '50': 'LCM',
}


FINA_2023_BASETIMES = {
    "50_BACK_F_LCM": 26.98,
    "50_BACK_F_SCM": 25.27,
    "50_BACK_M_LCM": 23.8,
    "50_BACK_M_SCM": 22.22,
    "50_BREAST_F_LCM": 29.3,
    "50_BREAST_F_SCM": 28.56,
    "50_BREAST_M_LCM": 25.95,
    "50_BREAST_M_SCM": 24.95,
    "50_FLY_F_LCM": 24.43,
    "50_FLY_F_SCM": 24.38,
    "50_FLY_M_LCM": 22.27,
    "50_FLY_M_SCM": 21.75,
    "50_FREE_F_LCM": 23.67,
    "50_FREE_F_SCM": 22.93,
    "50_FREE_M_LCM": 20.91,
    "50_FREE_M_SCM": 20.16,
    "100_BACK_F_LCM": 57.45,
    "100_BACK_F_SCM": 54.89,
    "100_BACK_M_LCM": 51.85,
    "100_BACK_M_SCM": 48.33,
    "100_BREAST_F_LCM": 64.13,
    "100_BREAST_F_SCM": 62.36,
    "100_BREAST_M_LCM": 56.88,
    "100_BREAST_M_SCM": 55.28,
    "100_FLY_F_LCM": 55.48,
    "100_FLY_F_SCM": 54.59,
    "100_FLY_M_LCM": 49.45,
    "100_FLY_M_SCM": 47.78,
    "100_FREE_F_LCM": 51.71,
    "100_FREE_F_SCM": 50.25,
    "100_FREE_M_LCM": 46.91,
    "100_FREE_M_SCM": 44.84,
    "100_MEDLEY_F_SCM": 56.51,
    "100_MEDLEY_M_SCM": 49.28, #placeholder value until updated
    "100_MEDLEY_F_LCM": 56.51, #placeholder value until updated
    "100_MEDLEY_M_LCM": 49.28,
    "200_BACK_F_LCM": 123.35,
    "200_BACK_F_SCM": 118.94,
    "200_BACK_M_LCM": 111.92,
    "200_BACK_M_SCM": 105.63,
    "200_BREAST_F_LCM": 138.95,
    "200_BREAST_F_SCM": 134.57,
    "200_BREAST_M_LCM": 126.12,
    "200_BREAST_M_SCM": 120.16,
    "200_FLY_F_LCM": 121.81,
    "200_FLY_F_SCM": 119.61,
    "200_FLY_M_LCM": 110.73,
    "200_FLY_M_SCM": 108.24,
    "200_FREE_F_LCM": 112.98,
    "200_FREE_F_SCM": 110.31,
    "200_FREE_M_LCM": 102,
    "200_FREE_M_SCM": 99.37,
    "200_MEDLEY_F_LCM": 126.12,
    "200_MEDLEY_F_SCM": 121.86,
    "200_MEDLEY_M_LCM": 114,
    "200_MEDLEY_M_SCM": 109.63,
    "400_FREE_F_LCM": 236.46,
    "400_FREE_F_SCM": 233.92,
    "400_FREE_M_LCM": 220.07,
    "400_FREE_M_SCM": 212.25,
    "400_MEDLEY_F_LCM": 266.36,
    "400_MEDLEY_F_SCM": 258.94,
    "400_MEDLEY_M_LCM": 243.84,
    "400_MEDLEY_M_SCM": 234.81,
    "800_FREE_F_LCM": 484.79,
    "800_FREE_F_SCM": 479.34,
    "800_FREE_M_LCM": 452.12,
    "800_FREE_M_SCM": 443.42,
    "1500_FREE_F_LCM": 920.48,
    "1500_FREE_F_SCM": 918.01,
    "1500_FREE_M_LCM": 871.02,
    "1500_FREE_M_SCM": 846.88
}

def get_fina_points(time: int, race_length: str, discipline: str, gender: str, course: str):
    basetime = FINA_2023_BASETIMES[f'{race_length}_{discipline}_{gender}_{course}']
    time_float = time_to_timedelta(time).total_seconds()
    return round(1000*(basetime/time_float)**3)

time_to_timedelta = lambda t : datetime.strptime(t, "%H:%M:%S.%f") - datetime(1900,1,1)

def format_time(time: str) -> str:
    # Time too short, invalid (e.g. "dnf")
    if '*' in time: # remove '*' from entrytimes
        time = time.replace('*', '')
        
    if len(time) < 4:
        return "NT"
    
    if len(time) < 9:  # time with minutes, seconds, decimals
        return datetime.strptime(time, "%M:%S.%f").strftime("%H:%M:%S.%f")[:-4]
    
    if len(time) == 10:
        return time + '0'

    return time