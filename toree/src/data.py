class Context:
    def __init__(self, layout, dir_count, file_count):
        self.layout = layout;
        self.dir_count = dir_count;
        self.file_count = file_count;

    def add_dir(self):
        self.dir_count += 1

    def add_file(self):
        self.file_count += 1
