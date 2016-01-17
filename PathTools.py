import os

import sublime
import sublime_plugin


def get_relative_path_to_git_repo(file_name):
    current_dir = os.path.dirname(file_name)
    while True:
        if '.git' in os.listdir(current_dir):
            relative_path = os.path.relpath(file_name, current_dir)
            return relative_path, True
        elif current_dir == '/':
            return current_dir, False
        current_dir = os.path.dirname(current_dir)


class CopyRelativePathCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        relative_path, found = get_relative_path_to_git_repo(self.view.file_name())
        sublime.set_clipboard(relative_path)
        if found:
            sublime.set_clipboard(relative_path)
        else:
            sublime.status_message("Could not find parent git repo. Copied file path: %s" % relative_path)
        return

    def is_enabled(self):
        return bool(self.view.file_name() and len(self.view.file_name()) > 0)

class CopyRelativePathWithTicksCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        relative_path, found = get_relative_path_to_git_repo(self.view.file_name())
        relative_path_with_ticks = '`%s`' % (relative_path)
        if found:
            sublime.set_clipboard(relative_path_with_ticks)
        else:
            sublime.status_message("Could not find parent git repo. Copied file path: %s" % relative_path_with_ticks)
        return

    def is_enabled(self):
        return bool(self.view.file_name() and len(self.view.file_name()) > 0)


class CopyRelativePathWithLineNumCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        relative_path, found = get_relative_path_to_git_repo(self.view.file_name())
        line_num = self.view.rowcol(self.view.sel()[0].begin())[0] + 1
        relative_path_with_line_num = '%s:%s' % (relative_path, line_num)
        if found:
            sublime.set_clipboard(relative_path_with_line_num)
        else:
            sublime.status_message("Could not find parent git repo. Copied file path: %s" % relative_path_with_line_num)
        return

    def is_enabled(self):
        return bool(self.view.file_name() and len(self.view.file_name()) > 0)


class CopyRelativePathWithLineNumAndTicksCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        relative_path, found = get_relative_path_to_git_repo(self.view.file_name())
        line_num = self.view.rowcol(self.view.sel()[0].begin())[0] + 1
        relative_path_with_line_num = '`%s:%s`' % (relative_path, line_num)
        if found:
            sublime.set_clipboard(relative_path_with_line_num)
        else:
            sublime.status_message("Could not find parent git repo. Copied file path: %s" % relative_path_with_line_num)
        return

    def is_enabled(self):
        return bool(self.view.file_name() and len(self.view.file_name()) > 0)
