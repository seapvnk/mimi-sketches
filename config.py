SCREEN_SIZE = (1024, 640)
WINDOW_TITLE = 'mimi'

COLLISION_LAYERS = [2, 3, 4]

PERSON_ANIMATIONS = [
    # idle
    ('PERSON_IDLE_RIGHT', ((0, 80), 5), 0.3),
    ('PERSON_IDLE_UP',   ((192, 80), 5), 0.3),
    ('PERSON_IDLE_LEFT',  ((384, 80), 5), 0.3),
    ('PERSON_IDLE_DOWN',  ((576, 80), 5), 0.3),
    # walking/running
    ('PERSON_RUN_RIGHT', ((0, 144), 5), 0.2),
    ('PERSON_RUN_UP',   ((192, 144), 5), 0.2),
    ('PERSON_RUN_LEFT',  ((384, 144), 5), 0.2),
    ('PERSON_RUN_DOWN',  ((576, 144), 5), 0.2)
]
