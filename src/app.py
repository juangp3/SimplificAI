from flet import (
    Container,
    Icon,
    Page,
    Text,
    AppBar,
    PopupMenuButton,
    PopupMenuItem,
    colors,
    icons,
    margin,
    UserControl,
    Row,
    TextField,
    ElevatedButton,
    alignment,
    MainAxisAlignment,
    Column,
    CrossAxisAlignment,
    ProgressRing,
    ScrollMode,
    SnackBar
)
 
class App(UserControl):
    def __init__(self, page: Page):
        self.page = page
        self._add_appbar()

        row = Row(
            wrap=True,
        spacing=10,
        run_spacing=10,
        alignment=MainAxisAlignment.CENTER,
        controls=[
                Container(
                    content=
                TextField(
                    label="Enter text to make it simple",
                    multiline=True,
                    min_lines=3,
                    autofocus=True,
                    max_length=2000,
                ),                    
                    margin=10,
                    padding=10,
                    #alignment=alignment.center,
                    width=500,
                    height=150,
                    border_radius=10,
                    ink=True,
                    # bgcolor=colors.LIGHT_BLUE_100
                    on_click=lambda e: e.page.update(),
                ),
                ElevatedButton(text="Submit"),
                Container(
                    content=Text(
                        "",
                        max_lines=50,
                        selectable=True,
                    ),
                    margin=10,
                    padding=10,
                    # alignment=alignment.center,
                    width=500,
                    height=150,
                    border_radius=10,
                    ink=True,
                    on_long_press=self.copy_to_clipboard,
                )],
        # width=page.window_width,
    )
        self.page.add(row)
        # self.page.add(ProgressRing())
        
        
    def copy_to_clipboard(self, e):
        self.page.set_clipboard(e.control.content.value)
        self.page.show_snack_bar(SnackBar(Text(f"Text Copied"), open=True))

    def _add_appbar(self):
        self.appbar_items = [
            PopupMenuItem(text="Login"),
            PopupMenuItem(),  # divider
            PopupMenuItem(text="Settings")
        ]
        self.appbar_items = []
        self.appbar = AppBar(
            leading=Icon(icons.DATA_OBJECT_ROUNDED),
            leading_width=100,
            title=Text(f"Simplif.AI", font_family="Pacifico", size=32, text_align="start"),
            center_title=False,
            toolbar_height=75,
            bgcolor=colors.LIGHT_BLUE_ACCENT_700,
            actions=[
                Container(
                    content=PopupMenuButton(
                        items=self.appbar_items
                    ),
                    margin=margin.only(left=50, right=25)
                )
            ],
        )
        self.page.appbar = self.appbar
        self.page.horizontal_alignment = CrossAxisAlignment.CENTER
        self.page.vertical_alignment = MainAxisAlignment.START
        self.page.update()