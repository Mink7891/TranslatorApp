

import flet as ft
from translate import Translator


def main(page: ft.Page):
    page.title = "Translator"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = "light"

    def toggle_theme(e):
        page.theme_mode = "dark" if page.theme_mode == "light" else "light"
        theme_button.icon = ft.icons.BRIGHTNESS_2 if page.theme_mode == "dark" else ft.icons.BRIGHTNESS_5
        theme_button.update()
        page.update()

    title = ft.Row(
        [
            ft.Icon(name=ft.icons.LANGUAGE, size=40, animate_scale=300),
            ft.Text("Переводчик", size=32,
                    weight=ft.FontWeight.BOLD, animate_scale=300),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    source_language_dropdown = ft.Dropdown(
        options=[
            ft.dropdown.Option(key="ru", text="Русский"),
            ft.dropdown.Option(key="en", text="Английский")
        ],
        width=400,
        label="С языка",
        value="ru",
        animate_opacity=300,
        animate_scale=300
    )
    target_language_dropdown = ft.Dropdown(
        options=[
            ft.dropdown.Option(key="ru", text="Русский"),
            ft.dropdown.Option(key="en", text="Английский")
        ],
        width=400,
        label="На язык",
        value="en",
        animate_opacity=300,
        animate_scale=300
    )

    language_selection = ft.Row(
        [source_language_dropdown, target_language_dropdown],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    input_text = ft.TextField(
        label="Введите текст",
        multiline=True,
        min_lines=3,
        max_lines=5,
        width=400,
        animate_opacity=500,
    )
    output_text = ft.TextField(
        label="Результат перевода",
        multiline=True,
        min_lines=3,
        max_lines=5,
        width=400,
        read_only=True,
        animate_opacity=500
    )

    text_selection = ft.Row(
        [input_text, output_text],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    translate_button = ft.ElevatedButton(
        "Перевести",
        width=250,
        height=40,
        on_click=lambda e: translate(input_text.value),
        animate_opacity=300,
        animate_scale=300
    )

    theme_button = ft.IconButton(
        icon=ft.icons.BRIGHTNESS_6,
        tooltip="Переключить тему",
        on_click=toggle_theme,
        animate_rotation=500
    )

    def translate(text):
        translator = Translator(
            from_lang=source_language_dropdown.value,
            to_lang=target_language_dropdown.value
        )
        translation = translator.translate(text)
        output_text.value = translation
        output_text.update()

    page.add(
        title,
        theme_button,
        language_selection,
        text_selection,
        translate_button
    )


ft.app(target=main)
