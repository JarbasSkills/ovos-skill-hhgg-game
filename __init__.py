from ovos_workshop.decorators import conversational_intent, intent_handler
from pyfrotz.ovos import FrotzSkill
from pyfrotz.parsers import hhgg_intro_parser

class HHGGSkill(FrotzSkill):
    def __init__(self, *args, **kwargs):
        # game is english only, apply bidirectional translation
        super().__init__(game_id="hhgg",
                         game_lang="en-us",
                         intro_parser=hhgg_intro_parser,
                         game_data=f'{self.root_dir}/res/{self.game_id}.z5',
                         *args, **kwargs)

    @intent_handler("play.intent")
    def handle_play(self, message=None):
        self.start_game(load_save=True)

    # intents
    @conversational_intent("exit.intent")
    def handle_exit(self, message=None):
        self.exit_game()

    @conversational_intent("restart_game.intent")
    def handle_restart(self, message=None):
        self.start_game(load_save=False)

    @conversational_intent("save.intent")
    def handle_save(self, message=None):
        self.save_game()
