import pandas as pd

class ModuleDatabase():
    """
    The class definition for the ModuleDatabase class.
    """

    def __init__(self) -> None:
        """
        Constructor for the ModuleDatabase class.
        """
        location = "db_files/module_data.csv"
        self.db_module = pd.read_csv(location, sep='|', encoding='utf-8', index_col="module_id")
        # Clean the 'content' column by converting it to a list
        # self.db_module['content'] = self.db_module['content'].apply(lambda x: ast.literal_eval(x))

    def get_module(self, week):
        return self.db_module.iloc[week].to_numpy()

    def get_module_name(self, week):
        return self.db_module.iloc[week].iloc[1]

    def get_module_list(self):
        self.db_module['']

    def showSample(self):
        return self.db_module.sample()

    def get_db(self):
        return self.db_module