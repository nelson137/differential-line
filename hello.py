import sys

import gi

gi.require_version("Gtk", "4.0")

from gi.repository import GLib, Gtk


class MyApplication(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.example.MyGtkApplication")
        GLib.set_application_name('My Gtk Application')

    def do_activate(self):
        window = Gtk.ApplicationWindow(application=self, title="Hello World")
        window.present()



def main():
    app = MyApplication()
    return app.run(sys.argv)


if __name__ == '__main__':
    sys.exit(main())
