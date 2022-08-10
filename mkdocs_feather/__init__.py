from mkdocs.plugins import BasePlugin

class FeatherPlugin(BasePlugin):
    def on_config(self, config, **kwargs):
        return config