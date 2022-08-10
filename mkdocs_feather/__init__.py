from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import get_files
import os

class FeatherPlugin(BasePlugin):
    def on_config(self, config, **kwargs):
        self.add_markdown_extension(config, "fenced_code")
        return config

    def _get_modes(self):
        return self.config.get("modes") or ['python']

    def on_files(self, files, config):
        self.inject_assets(files, config)

    def inject_assets(self, files, config):
        root = os.path.join(os.path.dirname(__file__))
        docs_dir = config["docs_dir"]
        config2 = dict(config, docs_dir=root)
        assets = get_files(config2)
        for f in assets:
            if "assets" in f.src_path and (f.src_path.endswith(".js") or f.src_path.endswith(".css")):
                files.append(f)

        extra_css = [
            'assets/mkdocs-feather/codemirror/lib/codemirror.css',
            'assets/mkdocs-feather/feather.css'
        ]
        extra_javascript = [
            'assets/mkdocs-feather/jquery-3.6.0.min.js',
            'assets/mkdocs-feather/codemirror/lib/codemirror.js',
            'assets/mkdocs-feather/codemirror/addon/mode/simple.js',
            'assets/mkdocs-feather/codemirror/keymap/sublime.js',
        ]

        mode_js = 'assets/mkdocs-feather/codemirror/mode/{mode}/{mode}.js'
        extra_javascript += [mode_js.format(mode=mode) for mode in self._get_modes()]

        extra_javascript += [
            'assets/mkdocs-feather/feather.js',
        ]

        config['extra_css'] = extra_css + config['extra_css']
        config['extra_javascript'] = extra_javascript + config['extra_javascript']

    def add_markdown_extension(self, config, name):
        exts = config['markdown_extensions']
        if  name not in exts:
            exts.append(name)
