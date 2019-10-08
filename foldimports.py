import sublime, sublime_plugin

def fold_imports(view):
  import_statements = view.find_all(r'^import')

  if len(import_statements) > 0:
    start = view.line(import_statements[0]).begin() + 7
    end = view.line(import_statements[-1]).end()

    if not view.fold(sublime.Region(start, end)):
      view.unfold(sublime.Region(start, end))

def fold_copyright(view):
  # our std pb copy claim
  copyright = view.find_all(r'^ \* Copyright')
  copyright_end = view.find_all(r'^ \* All rights reserved\.')
  if len(copyright) > 0:
    start = view.line(copyright[0]).begin()
    end = view.line(copyright_end[0]).end()

    # fold including preceding newline break and comment closing
    view.fold(sublime.Region(start - 1, end + 4))

# class ToggleImportsCommand(sublime_plugin.TextCommand):
#   def run(self, edit):
#     fold_imports(self.view)


class ToggleImportsListener(sublime_plugin.EventListener):
  # when new tab with gets opened
  def on_load(self, view):
    fold_imports(view)
    fold_copyright(view)

