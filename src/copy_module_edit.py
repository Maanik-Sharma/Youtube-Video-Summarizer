# # src\copy_module_edit.py
# import os
# import importlib.util


import os
import importlib.util
import logging

class ModuleEditor:
    def __init__(self, module_name):
        self.module_name = module_name
        self.base_dir = self._find_module_base_dir()
        self.frontend_dir = os.path.join(self.base_dir, 'frontend')
        self.index_html_path = os.path.join(self.frontend_dir, 'index.html')
        self.logger = logging.getLogger(__name__)

    def _find_module_base_dir(self):
        spec = importlib.util.find_spec(self.module_name)
        if spec is None:
            raise ImportError(f"Module {self.module_name} not found")
        return os.path.dirname(spec.origin)

    def read_file(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            self.logger.error(f"File not found: {file_path}")
            return ""
        except IOError as e:
            self.logger.error(f"Error reading file {file_path}: {e}")
            return ""

    def write_file(self, file_path, content):
        try:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            self.logger.info(f"File written: {file_path}")
        except IOError as e:
            self.logger.error(f"Error writing file {file_path}: {e}")

    def modify_index_html(self):
        new_index_html_content = """
        # Your modified index.html content here
        """
        self.write_file(self.index_html_path, new_index_html_content.strip())

    def modify_frontend_files(self):
        self.modify_index_html()


# class ModuleEditor:
#     def __init__(self, module_name):
#         self.module_name = module_name
        
#         self.base_dir = self._find_module_base_dir()
#         self.frontend_dir = os.path.join(self.base_dir, 'frontend')

#         self.index_html_path = os.path.join(self.frontend_dir, 'index.html')

#     def _find_module_base_dir(self):
#         spec = importlib.util.find_spec(self.module_name)
#         if spec is None:
#             raise ImportError(f"Module {self.module_name} not found")
#         return os.path.dirname(spec.origin)

#     def read_file(self, file_path):
#         with open(file_path, 'r', encoding='utf-8') as file:
#             return file.read()

#     def write_file(self, file_path, content):
#             print(f"File path: {file_path}")  # Add this line for debugging
#             with open(file_path, 'w', encoding='utf-8') as file:
#                  file.write(content)
#         # with open(file_path, 'w', encoding='utf-8') as file:
           

#     def modify_index_html(self):
#         new_index_html_content = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
#   <meta charset="UTF-8" />
#   <meta http-equiv="X-UA-Compatible" content="IE=edge" />
#   <meta name="viewport" content="width=device-width, initial-scale=1.0" />
#   <title>st-copy-to-clipboard</title>
#   <script src="./streamlit-component-lib.js"></script>
#   <script src="./main.js"></script>
#   <style>
#     /* Dark mode styles */
#     body.dark-mode {
#       background-color: #0e1117;
#       color: #fff;
#     }
#   </style>
# </head>
# <body class="dark-mode">
#   <div id="root">
#     <button id="text-element" class="st-copy-to-clipboard-btn"></button>
#     <button id="copy-button" class="st-copy-to-clipboard-btn">📋</button>
#   </div>
# </body>
# </html>
#             """
#         self.write_file(self.index_html_path, new_index_html_content.strip())


#     def modify_frontend_files(self):
#         self.modify_index_html()


