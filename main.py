import flet as ft

def main(page: ft.Page):
    # Configurações básicas da página
    page.title = "Caixinhas Aesthetic"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#FFE4E1"  # Fundo rosa bebê

    # Funções chamadas quando os checkboxes mudam
    def checkbox1_changed(e):
        mensagem1.value = f"🎀 Você {'aceitou' if checkbox1.value else 'não aceitou'} as regras!"
        mensagem1.color = "#C2185B" if checkbox1.value else "#D81B60"
        mensagem1.update()

    def checkbox2_changed(e):
        mensagem2.value = f"💖 Você {'aceitou' if checkbox2.value else 'não aceitou'} a política de privacidade!"
        mensagem2.color = "#C2185B" if checkbox2.value else "#D81B60"
        mensagem2.update()

    def checkbox3_changed(e):
        mensagem3.value = f"🌸 Você {'assinou' if checkbox3.value else 'não assinou'} a newsletter!"
        mensagem3.color = "#C2185B" if checkbox3.value else "#D81B60"
        mensagem3.update()

    # Primeira caixinha
    checkbox1 = ft.Checkbox(
        label="🎀 Eu aceito as regras",
        value=False,
        on_change=checkbox1_changed,
        fill_color="#C2185B",  # Rosa escuro
        check_color="#FFFFFF",  # Branco
    )
    mensagem1 = ft.Text(
        value="✨ Aguardando sua escolha...",
        size=16,
        color="#C2185B",
    )

    # Segunda caixinha
    checkbox2 = ft.Checkbox(
        label="💖 Eu aceito a política de privacidade",
        value=False,
        on_change=checkbox2_changed,
        fill_color="#C2185B",  # Rosa escuro
        check_color="#FFFFFF",
    )
    mensagem2 = ft.Text(
        value="✨ Aguardando sua escolha...",
        size=16,
        color="#C2185B",
    )

    # Terceira caixinha
    checkbox3 = ft.Checkbox(
        label="🌸 Quero assinar a newsletter",
        value=False,
        on_change=checkbox3_changed,
        fill_color="#C2185B",  # Rosa escuro
        check_color="#FFFFFF",
    )
    mensagem3 = ft.Text(
        value="✨ Aguardando sua escolha...",
        size=16,
        color="#C2185B",
    )

    # Layout principal
    page.add(
        ft.Column(
            controls=[
                ft.Text(
                    "🎀 Caixinhas Aesthetic 🎀",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    color="#C2185B",  # Rosa escuro
                ),
                checkbox1,
                mensagem1,
                checkbox2,
                mensagem2,
                checkbox3,
                mensagem3,
            ],
            spacing=20,
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

# Executar o app no navegador
if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER)
