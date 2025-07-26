import matplotlib
import flet as ft
import base64
import time

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from flet.matplotlib_chart import MatplotlibChart
from io import BytesIO


def main(page: ft.Page):
    page.title = 'Kapitsa pendulum'
    page.window.width = 1024
    page.window.min_width = 880
    page.window.height = 720
    page.window.min_height = 680

    page.theme_mode = ft.ThemeMode.DARK
    page.theme = ft.Theme(
        color_scheme=ft.ColorScheme(
            primary=ft.colors.INDIGO,
            secondary=ft.colors.PINK,
            surface=ft.colors.BLUE_GREY_900,
            on_primary=ft.colors.WHITE,
        ),
        use_material3=True,
    )

    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    matplotlib.use("svg")

    img = ft.Image(src="mipt.png", width=500, height=400)

    chart_container = ft.Container(
        content=img,
        margin=10,
        padding=10,
        border=ft.border.all(1, ft.colors.WHITE),
        alignment=ft.alignment.center,
        width=600,
        height=600,
        border_radius=10,
        ink=True,
        on_long_press='hello',
        disabled=False,
    )

    def m_change(e):
        pass

    def l_change(e):
        pass

    def A_change(e):
        pass

    def omega_change(e):
        pass

    def b_change(e):
        pass

    def theta_change(e):
        pass

    def start(e):
        m_field.disabled = True
        l_field.disabled = True
        A_field.disabled = True
        omega_field.disabled = True
        b_field.disabled = True
        theta_field.disabled = True
        start_btn.disabled = True
        stop_btn.disabled = False
        save_btn.disabled = True
        page.update()

        fig, ax = plt.subplots()
        x = np.linspace(0, 2 * np.pi, 100)
        line, = ax.plot(x, np.sin(x))

        for i in range(100):
            line.set_ydata(np.sin(x + i / 10))

            buf = BytesIO()
            fig.savefig(buf, format='png')
            buf.seek(0)

            img.src_base64 = base64.b64encode(buf.read()).decode("utf-8")
            img.update()
            time.sleep(0.05)

        # ani = FuncAnimation(pendulum.fig, pendulum.animate, frames=len(pendulum.t), interval=20, blit=True, repeat=True)
        # print(pendulum.x_tr)
        # plt.title(f'Маятник Капицы ({pendulum.omega} рад/с)')
        # plt.xlabel('x (м)')
        # plt.ylabel('y (м)')
        # plt.plot(pendulum.x_tr, pendulum.y_tr)

    def stop(e):
        img = ft.Image(src="mipt.png", width=500, height=400)
        chart_container.content = img
        m_field.disabled = False
        l_field.disabled = False
        A_field.disabled = False
        omega_field.disabled = False
        b_field.disabled = False
        theta_field.disabled = False
        start_btn.disabled = False
        stop_btn.disabled = True
        save_btn.disabled = False
        page.update()

    def save(e):
        pass

    m_field = ft.TextField(label='Масса груза', on_change=m_change, border_color=ft.colors.WHITE,
                           width=200, multiline=True, value=1.0, disabled=False)
    l_field = ft.TextField(label='Длина маятника', on_change=l_change, border_color=ft.colors.WHITE,
                           width=200, multiline=True, value=2.0, disabled=False)
    A_field = ft.TextField(label='Амплитуда колебаний подвеса', on_change=A_change, border_color=ft.colors.WHITE,
                           width=200, multiline=True, value=0.1, disabled=False)
    omega_field = ft.TextField(label='Частота колебаний подвеса', on_change=omega_change, border_color=ft.colors.WHITE,
                               width=200, multiline=True, value=50, disabled=False)
    b_field = ft.TextField(label='Коэффициент затухания', on_change=b_change, border_color=ft.colors.WHITE,
                           width=200, multiline=True, value=0, disabled=False)
    theta_field = ft.TextField(label='Начальный угол отклонения', on_change=theta_change, border_color=ft.colors.WHITE,
                               width=200, multiline=True, value=100, disabled=False)
    start_btn = ft.FloatingActionButton(icon=ft.icons.START, disabled=False, bgcolor=ft.colors.BACKGROUND,
                                        on_click=start, disabled_elevation=True)
    stop_btn = ft.FloatingActionButton(icon=ft.icons.STOP, disabled=True, bgcolor=ft.colors.BACKGROUND,
                                       on_click=stop)
    save_btn = ft.FloatingActionButton(icon=ft.icons.SAVE_ALT, disabled=True, bgcolor=ft.colors.BACKGROUND,
                                       on_click=save)

    page.add(
        ft.Row(
            controls=[
                chart_container,
                ft.Column(
                    controls=[
                        ft.Text(value='Параметры\nмаятника', size=30, color=ft.colors.WHITE),
                        m_field,
                        l_field,
                        A_field,
                        omega_field,
                        b_field,
                        theta_field,
                        ft.Row(
                            controls=[
                                start_btn,
                                stop_btn,
                                save_btn,
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        )
                    ]
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


if __name__ == '__main__':
    ft.app(target=main)
