import os
from steam_data.steam_analizer.analizer import SteamAnalizer

class TestPlataformTags:
    def setup_method(self):
        csv_file = os.path.join(os.path.dirname(__file__), "dataset", "steam_games.csv")
        self.analizer = SteamAnalizer(csv_file)
        self.analizer.process_csv()
        self.analizer.process_data()
    
    def test_plataform_tags(self):
        print(self.analizer.plataform_tags.get_info())
        assert True
