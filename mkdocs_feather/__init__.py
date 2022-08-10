from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import get_files
import os

class FeatherPlugin(BasePlugin):
    def on_config(self, config, **kwargs):
        self.add_markdown_extension(config, "fenced_code")
        return config

    def on_files(self, files, config):
        self.inject_assets(files, config)

    def inject_assets(self, files, config):
        root = os.path.join(os.path.dirname(__file__), "assets")
        docs_dir = config["docs_dir"]
        config2 = dict(config, docs_dir=root)
        assets = get_files(config2)
        for f in assets:
            files.append(f)

        extra_css = [
            'codemirror/lib/codemirror.css',
            'mkdocs-feather/style.css'
        ]
        extra_javascript = [
            'https://code.jquery.com/jquery-3.6.0.min.js',
            'codemirror/lib/codemirror.js',
            'codemirror/addon/mode/simple.js',
            'codemirror/mode/python/python.js',
            'codemirror/keymap/sublime.js',
            'mkdocs-feather/js/feather.js',
        ]

        config['extra_css'] = extra_css + config['extra_css']
        config['extra_javascript'] = extra_javascript + config['extra_javascript']

    def add_markdown_extension(self, config, name):
        exts = config['markdown_extensions']
        if  name not in exts:
            exts.append(name)
