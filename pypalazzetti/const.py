"""Constants."""

from typing import Final

API_COMMAND_URL_TEMPLATE: Final = (
    "http://{host}/cgi-bin/sendmsg.lua?cmd={command_and_parameter}"
)

STATUSES: Final = {
    0: "OFF",
    1: "OFF_TIMER",
    2: "TESTFIRE",
    3: "HEATUP",
    4: "FUELING",
    5: "IGNTEST",
    6: "BURNING",
    7: "BURNINGMOD",
    8: "UNKNOWN",
    9: "COOLFLUID",
    10: "FIRESTOP",
    11: "CLEANFIRE",
    12: "COOL",
    50: "CLEANUP",
    51: "ECOMODE",
    241: "CHIMNEY_ALARM",
    243: "GRATE_ERROR",
    244: "PELLET_WATER_ERROR",
    245: "T05_ERROR",
    247: "HATCH_DOOR_OPEN",
    248: "PRESSURE_ERROR",
    249: "MAIN_PROBE_FAILURE",
    250: "FLUE_PROBE_FAILURE",
    252: "EXHAUST_TEMP_HIGH",
    253: "PELLET_FINISHED",
    501: "OFF",
    502: "FUELING",
    503: "IGNTEST",
    504: "BURNING",
    505: "FIREWOOD_FINISHED",
    506: "COOLING",
    507: "CLEANFIRE",
    1000: "GENERAL_ERROR",
    1001: "GENERAL_ERROR",
    1239: "DOOR_OPEN",
    1240: "TEMP_TOO_HIGH",
    1241: "CLEANING_WARNING",
    1243: "FUEL_ERROR",
    1244: "PELLET_WATER_ERROR",
    1245: "T05_ERROR",
    1247: "HATCH_DOOR_OPEN",
    1248: "PRESSURE_ERROR",
    1249: "MAIN_PROBE_FAILURE",
    1250: "FLUE_PROBE_FAILURE",
    1252: "EXHAUST_TEMP_HIGH",
    1253: "PELLET_FINISHED",
    1508: "GENERAL_ERROR",
}

HEATING_STATUSES = [2, 3, 4, 5, 6, 7, 51, 502, 503, 504]
OFF_STATUSES = [0, 1]

FAN_SILENT: Final = "SILENT"
FAN_HIGH: Final = "HIGH"
FAN_AUTO: Final = "AUTO"
FAN_MODES: Final = [FAN_SILENT, "1", "2", "3", "4", "5", FAN_HIGH, FAN_AUTO]

COMMAND_CHECK_ONLINE = "GET STAT"
COMMAND_UPDATE_PROPERTIES = "GET STDT"
COMMAND_UPDATE_STATE = "GET ALLS"
COMMAND_SET_TEMPERATURE = "SET SETP"
COMMAND_SET_FAN_SPEED = "SET RFAN"
COMMAND_SET_FAN_SILENT = "SET SLNT 1"
COMMAND_SET_POWER_MODE = "SET POWR"
COMMAND_SET_ON = "CMD ON"
COMMAND_SET_OFF = "CMD OFF"
