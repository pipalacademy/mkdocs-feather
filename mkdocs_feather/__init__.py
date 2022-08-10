from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import get_files
import os

class FeatherPlugin(BasePlugin):
    def on_config(self, config, **kwargs):
        self.add_markdown_extension(config, "fenced_code")
        print("on_config", config)
        return config

    def on_files(self, files, config):
        self.inject_assets(files, config)

    def inject_assets(self, files, config):
        root = os.path.join(os.path.dirname(__file__), "assets")
        print("inject_assets", root)
        docs_dir = config["docs_dir"]
        config2 = dict(config, docs_dir=root)
        assets = get_files(config2)

        css = []
        js = []
        for file in assets:
            path = file.src_path.replace("\\", "/")
            if path.endswith(".css"):
                files.append(file)
                css.append(path)
            elif path.endswith(".js"):
                files.append(file)
                js.append(path)

        config["extra_css"] = css
        config["extra_javascript"] = js

    def add_markdown_extension(self, config, name):
        exts = config['markdown_extensions']
        if  name not in exts:
            exts.append(name)
