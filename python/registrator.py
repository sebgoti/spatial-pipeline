import itk

class Registrator:
    def __init__(self, param_files, mov):
        self.param_files = param_files
        self.moving_file = mov.split('/')[-1].split('_')[0][1:]
        
    def _print_successful(self):
        print(self.moving_file)