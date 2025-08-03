class WindowConfig:
    """
        Applies a driver's instance settings and returns it to its initial settings before running the reporting process
        
        Methods:
            - static setupt() -> returns a configured window  
        
    """

    @staticmethod
    def setup(window):
        window.maximize_window()
        # Add more settings here.
        return window