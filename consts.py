
CHAT_TOURNAMENT_FINISHED_AGO = 12 * 60  # [min]
CHAT_TOURNAMENT_STARTS_IN = 6 * 60  # [min]
CHAT_SWISS_STARTED_AGO = 6 * 60  # [min]
MAX_LEN_TOURNEY_NAME_SHORT = 25
MAX_LEN_TOURNEY_NAME_LONG = 33
NUM_RECENT_BROADCASTS_TO_FETCH = 20

API_TOURNEY_PAGE_DELAY = 1.0  # [s]
IDX_NO_PAGE_UPDATE = 0
API_CHAT_REFRESH_PERIOD = [1, 5, 25, 60]  # [s]
PERIOD_UPDATE_TOURNAMENTS = 60  # [s]
TIME_FREQUENT_MESSAGES = 5  # [s]
MAX_TIME_FREQUENT_MESSAGES = 60  # [s]
NUM_FREQUENT_MESSAGES = 9
NUM_MSGS_BEFORE = 10
NUM_MSGS_AFTER = 10
TIMEOUT_RANGE = [25, 25]  # [min]
DELAY_ERROR_READ_MOD_LOG = 60  # [min]

CHAT_NUM_VISIBLE_MSGS = 450
CHAT_MAX_NUM_MSGS = 500
CHAT_FREQUENT_MSGS_MIN_SCORE = [15, 30]
CHAT_BEGINNING_MESSAGES_TEXT = '"name":"Chat room","lines":['
CHAT_END_MESSAGES_TEXT = '],"userId":'
TOURNEY_STANDING_BEGINNING_TEXT = '"standing":{"page":1,"players":['
TOURNEY_STANDING_ENDING_TEXT = ']},"socketVersion":'
HR = '<hr class="my-0" style="border-top:dotted 2px;"/>'
CHAT_UPDATE_SWISS = False  # loading messages from swiss tourneys doesn't work at the moment anyway
DO_AUTO_TIMEOUTS = False
MULTI_MSG_MIN_TIMEOUT_SCORE = 300
MAX_LEN_TEXT = 140
CHAT_NUM_PLAYED_GAMES = [100, 250]
CHAT_CREATED_DAYS_AGO = [30, 60]
STD_SHORT_MESSAGES = ["hi", "hello", "good luck", "bye", "gl", "hf", "thanks", "gg", "wp", "ggs", "ty", "gtg", "thx", "u2"]
