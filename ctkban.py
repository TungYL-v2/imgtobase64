import base64
import io
import os
from PIL import Image, ImageTk
import customtkinter as ctk
from tkinter import filedialog, messagebox

class ImageBase64Converter:
    def __init__(self, root):
        self.root = root
        self.root.title("图片与Base64转换器")

        # 设置主题和颜色模式
        ctk.set_appearance_mode("System")  # 可选：System, Dark, Light
        ctk.set_default_color_theme("blue")  # 可选：blue, green, dark-blue

        # 获取显示器分辨率
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # 设置窗口初始大小为显示器分辨率的 70%
        self.window_width = int(screen_width * 0.7)
        self.window_height = int(screen_height * 0.7)
        self.root.geometry(f"{self.window_width}x{self.window_height}")

        # 存储原始图片和调整后的图片
        self.original_image = None
        self.resized_image = None

        # 设置图片的最小和最大显示尺寸
        self.min_image_size = 100  # 最小显示尺寸（宽度或高度）
        self.max_image_size = 800  # 最大显示尺寸（宽度或高度）

        # 创建 UI 组件
        self.create_widgets()

        # 绑定窗口大小变化事件
        self.root.bind("<Configure>", self.resize_ui)

    def create_widgets(self):
        """创建并初始化 UI 组件"""
        # 主容器
        self.main_frame = ctk.CTkFrame(self.root, corner_radius=15)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # 图片地址输入栏
        self.image_path_label = ctk.CTkLabel(self.main_frame, text="图片地址:", font=("Arial", 14))
        self.image_path_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.image_path_entry = ctk.CTkEntry(self.main_frame, font=("Arial", 12), width=400, corner_radius=10)
        self.image_path_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.browse_button = ctk.CTkButton(
            self.main_frame, text="📁 浏览", command=self.browse_image, font=("Arial", 12), width=100, corner_radius=10,
            fg_color="#4CAF50", hover_color="#45a049"
        )
        self.browse_button.grid(row=0, column=2, padx=10, pady=10)

        # 显示图片的区域
        self.image_label = ctk.CTkLabel(
            self.main_frame, text="", width=self.window_width - 40, height=self.window_height - 200, corner_radius=15
        )
        self.image_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        # 动态设置图片显示区域的背景颜色
        self.update_image_label_theme()

        # 按钮区域
        self.button_frame = ctk.CTkFrame(self.main_frame, corner_radius=15, fg_color="transparent")
        self.button_frame.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

        self.preview_button = ctk.CTkButton(
            self.button_frame, text="👀 预览", command=self.preview_image, font=("Arial", 12), width=120, corner_radius=10,
            fg_color="#2196F3", hover_color="#1e88e5"
        )
        self.preview_button.pack(side="left", padx=10, pady=10)

        self.download_button = ctk.CTkButton(
            self.button_frame, text="💾 下载", command=self.download_image, font=("Arial", 12), width=120, corner_radius=10,
            fg_color="#FF9800", hover_color="#fb8c00"
        )
        self.download_button.pack(side="left", padx=10, pady=10)

        # 主题切换按钮
        self.theme_button = ctk.CTkButton(
            self.button_frame, text="🌙 切换主题", command=self.toggle_theme, font=("Arial", 12), width=120, corner_radius=10,
            fg_color="#9C27B0", hover_color="#8e24aa"
        )
        self.theme_button.pack(side="right", padx=10, pady=10)

        # 配置网格布局的权重
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)

    def update_image_label_theme(self):
        """根据当前主题更新图片显示区域的背景颜色"""
        current_mode = ctk.get_appearance_mode()
        if current_mode == "Light":
            self.image_label.configure(fg_color="#ffffff", text_color="#000000")  # 浅色主题
        else:
            self.image_label.configure(fg_color="#2e2e2e", text_color="#ffffff")  # 深色主题

    def resize_ui(self, event=None):
        """根据窗口大小动态调整 UI 布局"""
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()

        # 调整图片显示区域的大小
        self.image_label.configure(width=window_width - 40, height=window_height - 200)

    def browse_image(self):
        """浏览并选择图片文件"""
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
        if file_path:
            file_size = os.path.getsize(file_path) / (1024 * 1024)  # 文件大小（MB）
            if file_size > 10:  # 限制图片大小为 10MB
                messagebox.showwarning("警告", "图片文件过大，可能发生卡顿。")
            self.image_path_entry.delete(0, "end")
            self.image_path_entry.insert(0, file_path)
            self.convert_image_to_base64(file_path)

    def convert_image_to_base64(self, image_path):
        """将图片转换为Base64代码并保存到用户选择的位置"""
        try:
            with open(image_path, "rb") as image_file:
                base64_code = base64.b64encode(image_file.read()).decode("utf-8")

            # 获取图片文件名（不含扩展名）
            image_name = os.path.splitext(os.path.basename(image_path))[0]

            # 弹出文件保存对话框，让用户选择保存位置
            save_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text Files", "*.txt")],
                title="保存 Base64 代码",
                initialfile=image_name  # 自动填充图片文件名
            )
            if save_path:
                with open(save_path, "w") as file:
                    file.write(base64_code)
                messagebox.showinfo("成功", f"Base64 代码已保存到：\n{save_path}")

        except Exception as e:
            messagebox.showerror("错误", f"无法读取图片: {e}")

    def preview_image(self):
        """从用户选择的文件读取Base64代码并显示图片"""
        try:
            # 打开文件选择对话框，让用户选择保存的 Base64 文件
            file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
            if not file_path:
                return

            # 读取文件内容
            with open(file_path, "r") as file:
                base64_code = file.read().strip()

            # 显示图片
            image_data = base64.b64decode(base64_code)
            self.original_image = Image.open(io.BytesIO(image_data))
            self.resize_image()  # 初始调整图片大小
        except Exception as e:
            messagebox.showerror("错误", f"无法显示图片: {e}")

    def download_image(self):
        """下载Base64代码对应的图片"""
        try:
            # 打开文件选择对话框，让用户选择保存的 Base64 文件
            file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
            if not file_path:
                return

            # 读取文件内容
            with open(file_path, "r") as file:
                base64_code = file.read().strip()

            # 获取文件名（不含扩展名）
            file_name = os.path.splitext(os.path.basename(file_path))[0]

            # 保存图片
            image_data = base64.b64decode(base64_code)
            save_path = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG Files", "*.png"), ("JPEG Files", "*.jpg")],
                title="保存图片",
                initialfile=file_name  # 自动填充文件名
            )
            if save_path:
                with open(save_path, "wb") as image_file:
                    image_file.write(image_data)
                messagebox.showinfo("成功", "图片下载成功！")
        except Exception as e:
            messagebox.showerror("错误", f"无法下载图片: {e}")

    def resize_image(self, event=None):
        """根据窗口大小动态调整图片尺寸"""
        if self.original_image:
            # 获取窗口的当前大小
            window_width = self.root.winfo_width()
            window_height = self.root.winfo_height()

            # 计算图片的最大显示尺寸（留出一些边距）
            max_width = window_width - 40
            max_height = window_height - 200  # 留出输入栏和按钮的空间

            # 限制图片的最大和最小显示尺寸
            max_width = min(max_width, self.max_image_size)
            max_height = min(max_height, self.max_image_size)
            max_width = max(max_width, self.min_image_size)
            max_height = max(max_height, self.min_image_size)

            # 保持宽高比调整图片大小
            self.resized_image = self.original_image.copy()
            self.resized_image.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)

            # 显示调整后的图片
            photo = ImageTk.PhotoImage(self.resized_image)
            self.image_label.configure(image=photo)
            self.image_label.image = photo  # 保持引用，避免被垃圾回收

    def toggle_theme(self):
        """切换主题"""
        current_mode = ctk.get_appearance_mode()
        if current_mode == "Light":
            ctk.set_appearance_mode("Dark")
        else:
            ctk.set_appearance_mode("Light")
        # 更新图片显示区域的背景颜色
        self.update_image_label_theme()

if __name__ == "__main__":
    root = ctk.CTk()
    app = ImageBase64Converter(root)
    root.mainloop()