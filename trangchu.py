import flet as ft 
from flet import *

class MainMenu(ft.Container):
    def __init__(self):
        super().__init__()        
        self.width = 350        
        self.border_radius = border_radius.only(top_left=30, top_right=30, bottom_left=10, bottom_right=10)        
        self.bgcolor = "#089908"        
        self.page = ft.Page
        self.padding = padding.only(top=60, left=24, right=24, bottom=24)             
        self.content = ft.Column(            
            controls=[    
                ft.Container(                    
                    content=ft.Column(
                        controls=[ 
                            ft.Container(
                                padding=padding.only(left=10, right=10),
                                content=ft.ResponsiveRow(
                                    controls=[
                                        ft.Column(col={"xs":12}, controls=[ft.Text("DANH MỤC CỦA ỨNG DỤNG", size=18, color="#FFFFFF", weight=ft.FontWeight.W_600)])                                                                                                               
                                    ]                                        
                                )       
                            )                                                                                                  
                        ]                                                                                          
                    )                                                           
                ),                                                      
                ft.Container(                  
                    bgcolor="#ffffff",      
                    border_radius=20,
                    padding = 10,                    
                    content=ft.Column(
                        controls=[
                            ft.Row(controls=[ft.Text("", size=0)]),
                            ft.ResponsiveRow(controls=[
                                ft.Column(col={"xs": 12}, controls=[ft.Text("Giải phương trình", size=17, weight=ft.FontWeight.W_600)])   
                            ]), 
                            ft.Row(controls=[ft.Text("", size=0)]),
                            ft.Container(
                                padding=padding.only(left=25, right=25),
                                content=ft.ResponsiveRow(                                
                                    controls=[
                                        ft.Column(col={"xs":6}, controls=[ ElevatedButton("  Bậc 1  ", on_click=lambda _: self.page.go("/bac1"))]),
                                        ft.Column(col={"xs":6}, controls=[ ElevatedButton("  Bậc 2  ", on_click=lambda _: self.page.go("/bac2"))]),
                                        ft.Row(controls=[ft.Text("", size=0)]),
                                        ft.Column(col={"xs":6}, controls=[ ElevatedButton("  Bậc 3  ", on_click=lambda _: self.page.go("/bac3"))]),
                                        ft.Column(col={"xs":6}, controls=[ ElevatedButton("  Bậc 4  ", on_click=lambda _: self.page.go("/bac4"))]),
                                        ft.Row(controls=[ft.Text("", size=0)]),
                                        ft.Column(col={"xs":6}, controls=[ ElevatedButton("  MT 1  ", on_click=lambda _: self.page.go("/maytinh1"))]),
                                        ft.Column(col={"xs":6}, controls=[ ElevatedButton("  MT 2  ", on_click=lambda _: self.page.go("/maytinh2"))]),
                                        ft.Row(controls=[ft.Text("", size=0)]),
                                        ft.Column(col={"xs":6}, controls=[ ElevatedButton("  MT 3  ", on_click=lambda _: self.page.go("/maytinh3"))]),
                                        ft.Column(col={"xs":6}, controls=[ ElevatedButton("  MT 4  ", on_click=lambda _: self.page.go("/maytinh4"))]),                                        
                                        ft.Row(controls=[ft.Text("", size=0)])   
                                    ]
                                )
                            ),                             
                            ft.Container(
                                padding=padding.only(left=25, right=25),
                                content=ft.ResponsiveRow(                                
                                    controls=[
                                        ft.Column(col={"xs":12}, controls=[ ElevatedButton("  Hệ pt 2 ẩn  ", on_click=lambda _: self.page.go("/hept2an"))]), 
                                        ft.Row(controls=[ft.Text("", size=0)]),
                                        ft.Column(col={"xs":12}, controls=[ ElevatedButton("  Hệ pt 3 ẩn  ", on_click=lambda _: self.page.go("/hept3an"))]),
                                        ft.Row(controls=[ft.Text("", size=0)]), 
                                        ft.Column(col={"xs":12}, controls=[ ElevatedButton("  Hướng dẫn sử dụng  ", on_click=lambda _: self.page.go("/huongdansudung"))]),                                                                            
                                        ft.Row(controls=[ft.Text("", size=0)]),
                                        ft.Row(controls=[ft.Text("", size=0)]),
                                        ft.Row(controls=[ft.Text("", size=0)])
                                    ]
                                )
                            )                                             
                        ],height=370, scroll=ft.ScrollMode.ALWAYS
                    )
                )            
            ]            
        )      
     