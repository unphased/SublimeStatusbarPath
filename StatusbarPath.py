import sublime
import sublime_plugin

class CurrentPathStatusCommand(sublime_plugin.EventListener):
   def on_activated(self, view):
      view.set_status('Path', view.file_name())
