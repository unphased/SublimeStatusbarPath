import sublime
import sublime_plugin


class CurrentPathStatusCommand(sublime_plugin.EventListener):

    def on_activated(self, view):
        filename = view.file_name()
        if filename:
            print "SSP: "
            print dir(view)
            print "Window: "
            print dir(view.window())
            view.set_status('Path', filename)
