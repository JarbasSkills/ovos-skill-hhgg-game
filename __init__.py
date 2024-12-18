from pyfrotz.ovos import FrotzSkill
from pyfrotz.parsers import hhgg_intro_parser


class HHGGSkill(FrotzSkill):
    def __init__(self, *args, **kwargs):
        # game is english only, apply bidirectional translation
        # TODO - dedicated icon, use pyfrotz icon for now
        skill_icon = "https://raw.githubusercontent.com/TigreGotico/pyFrotz/refs/heads/dev/pyfrotz/gui/all/pyfrotz.png"
        bg = "http://infocom.elsewhere.org/gallery/hhgttg/front_th.jpg"
        super().__init__(*args,
                         game_id="hhgg",
                         game_lang="en-us",
                         intro_parser=hhgg_intro_parser,
                         game_data=f'{self.root_dir}/res/{self.game_id}.z5',
                         skill_icon=skill_icon,
                         game_image=bg,
                         **kwargs)
