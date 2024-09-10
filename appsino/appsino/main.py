import flet as ft


def main(page: ft.Page):
    page.title="¿me perdonas?"
    page.bgcolor="pink"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    
    lbl1=ft.Text("¿me perdonas?",
                style=ft.TextStyle(size=40,weight="blod"))
    img1=ft.Image(src="triste.png",widch=200,height=200)
    btnS1=ft.ElevatedButton("Si",
                            color="green",
                            width=100,
                            height=50
                            )
    btnNo=ft.ElevatedButton("No",
                            color="red",
                            widht=100,
                            height=50
                            )
    page.add(
        ft.Column(
            [
                lbl1,
                img1,
                ft.Row(
                    [btn]
                )
            ]
        )
    )
    

ft.app(main)
