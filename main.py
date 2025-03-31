import flet as ft
from db import main_db
from datetime import datetime


def main(page: ft.Page):
    page.title = 'Todo List'
    page.padding = 40
    page.bgcolor = ft.Colors.GREY_800
    page.theme_mode = ft.ThemeMode.DARK

    task_list = ft.Column(spacing=10)

    def load_tasks():
        task_list.controls.clear()
        for task_id, task_text, created_at in main_db.get_tasks():
            task_list.controls.append(create_task_row(task_id, task_text, created_at))
        page.update()

    def create_task_row(task_id, task_text, created_at):
        task_field = ft.TextField(value=task_text, expand=True, dense=True, read_only=True)

        def enable_edit(e):
            task_field.read_only = False
            page.update()

        def save_edit(e):
            main_db.update_task_db(task_id, task_field.value)
            task_field.read_only = True

            load_tasks()

        return ft.Row([
            task_field,
            ft.Text(created_at, size=12),
            ft.IconButton(ft.Icons.EDIT, icon_color=ft.Colors.YELLOW_400, on_click=enable_edit),
            ft.IconButton(ft.Icons.SAVE, icon_color=ft.Colors.GREEN_400, on_click=save_edit)
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
    
    def add_task(e):
        if task_input.value.strip():
            task_id = main_db.add_task_db(task_input.value)
            task_list.controls.append(create_task_row(task_id, task_input.value, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            task_input.value = ""
            page.update()

    task_input = ft.TextField(hint_text='Добавьте задачу', expand=True, dense=True, on_submit=add_task)
    add_button = ft.ElevatedButton("Добавить", on_click=add_task, icon=ft.Icons.ADD)

    page.add(
        ft.Column([
            ft.Row([task_input, add_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            task_list
        ])
    )

    load_tasks()


if __name__ == '__main__':
    main_db.init_db()
    ft.app(target=main)