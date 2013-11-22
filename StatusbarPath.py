import sublime
import sublime_plugin


class CurrentPathStatusCommand(sublime_plugin.EventListener):

    def on_activated(self, view):
        filename = view.file_name()
        if filename:
            for folder in view.window().folders():
                filename = filename.replace(folder, '.')
            view.set_status('zPath', filename)
