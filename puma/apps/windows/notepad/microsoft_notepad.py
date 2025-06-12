from puma.apps.android.appium_actions import supported_version
from puma.state_graph.state_win_graph import StateGraph
from puma.state_graph.winstate import SimpleState, compose_clicks


@supported_version("Windows 10")
class Notepad(StateGraph):

    text_state = SimpleState(['File', 'Edit', 'Format', 'View', 'Help'], initial_state=True)
    about_state = SimpleState(['This product is licensed under'], parent_state=text_state)

    text_state.to(about_state, compose_clicks(['Help', 'About Notepad']))

    def __init__(self):
        ...