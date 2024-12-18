from pyfrotz.ovos import FrotzSkill
from pyfrotz.parsers import hhgg_intro_parser


class HHGGSkill(FrotzSkill):
    def __init__(self, *args, **kwargs):
        # game is english only, apply bidirectional translation
        super().__init__(*args,
                         game_id="hhgg",
                         game_lang="en-us",
                         intro_parser=hhgg_intro_parser,
                         game_data=f'{self.root_dir}/res/{self.game_id}.z5',
                         **kwargs)
