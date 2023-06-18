import flet
from flet import (
    Page,
    colors,
    theme,
    ScrollMode
)
from app import App
 
if __name__ == "__main__":
 
    def main(page: Page):
 
        page.title = "Simplif.AI - Let's not complicate!"
        #page.padding = 0
        page.theme_mode = flet.ThemeMode.LIGHT
        page.theme = theme.Theme(font_family="Verdana")
        page.theme = theme.Theme(color_scheme_seed=colors.BLUE_GREY_200)
        page.theme.page_transitions.windows = "cupertino"
        page.fonts = {"AkayaKanadaka": "/AkayaKanadaka-Regular.ttf"}
        page.bgcolor = colors.BLUE_GREY_200
        page.scroll = ScrollMode.ALWAYS
        app = App(page)
        page.update()
        #page.add(Text("Body!"))
        #page.add(app)
        #page.update()
 
    flet.app(target=main, port=8552, view=flet.WEB_BROWSER)