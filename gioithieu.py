import flet as ft 
from flet import *

class Gioithieu(ft.Container):
    def __init__(self):
        super().__init__()        
        self.width = 350        
        self.border_radius = border_radius.only(top_left=30, top_right=30, bottom_left=10, bottom_right=10)        
        self.bgcolor = "#089908"        
        self.page = ft.Page
        self.padding = padding.only(top=60, left=24, right=24, bottom=24)   
        self.text1 = ft.Text("Công ty TNHH Phụng Mai Trâm là đơn vị chuyên cung cấp các dịch vụ thiết kế website chuẩn SEO, thân thiện với người dùng.", color="#000000", weight=ft.FontWeight.BOLD     
        )
        self.text2 = ft.Text("Tên: Giải phương trình \nVersion = 1.0.0 \nMô tả: Ứng dụng máy tính \nTác giả: Công ty TNHH Phụng Mai Trâm", color="#000000", weight=ft.FontWeight.BOLD       
        )            
        self.content = ft.Column(            
            controls=[    
                ft.Container(                    
                    content=ft.Column(
                        controls=[ 
                            ft.Container(
                                padding=padding.only(left=20, right=20),
                                content=ft.ResponsiveRow(
                                    controls=[
                                        ft.Column(col={"xs":12}, controls=[ft.Text("PHUNG MAI TRAM ., LTD", size=18, color="#FFFFFF", weight=ft.FontWeight.W_600)])                                                                                                               
                                    ]                                        
                                )       
                            )                                                                                                  
                        ]                                                                                          
                    )                                                           
                ),                                                      
                ft.Container(                  
                    bgcolor="#ffffff",      
                    border_radius=20,
                    padding = padding.only(top=20, left=15, right=15, bottom=20),                                       
                    content=ft.Column(
                        controls=[   
                            ft.ResponsiveRow(controls=[
                                ft.Column(col={"xs": 12}, controls=[ft.Text("1. Giới thiệu", size=18, weight=ft.FontWeight.W_700)]),   
                            ]),
                            ft.ResponsiveRow(controls=[
                                ft.Column(col={"xs": 12}, controls=[self.text1]),   
                            ]),
                            ft.ResponsiveRow(controls=[
                                ft.Column(col={"xs": 12}, controls=[ft.Text("2. Thông tin ứng dụng", size=18, weight=ft.FontWeight.W_700)]),   
                            ]),
                            ft.ResponsiveRow(controls=[
                                ft.Column(col={"xs": 12}, controls=[self.text2]),   
                            ]),                            
                            ft.Row(controls=[ft.Text("", size=0)]),
                            ft.Row(controls=[ft.Text("", size=0)])                                                                                                      
                        ],height=350, scroll=ft.ScrollMode.ALWAYS
                    )
                )            
            ]            
        )      
     