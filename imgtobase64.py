import tkinter as tk
from tkinter import filedialog, messagebox
import base64
from PIL import Image, ImageTk
import io
import os

class ImageBase64Converter:
    def __init__(self, root):
        self.root = root
        self.root.title("图片与Base64转换器")

        # 获取显示器分辨率
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # 设置窗口初始大小为显示器分辨率的 80%
        self.window_width = int(screen_width * 0.7)
        self.window_height = int(screen_height * 0.7)
        self.root.geometry(f"{self.window_width}x{self.window_height}")

        # 图片地址输入栏
        self.image_path_label = tk.Label(root, text="图片地址:")
        self.image_path_entry = tk.Entry(root)
        self.browse_button = tk.Button(root, text="浏览", command=self.browse_image)

        # 显示图片的Label
        self.image_label = tk.Label(root)

        # 预览按钮
        self.preview_button = tk.Button(root, text="预览", command=self.preview_image)

        # 下载按钮
        self.download_button = tk.Button(root, text="下载", command=self.download_image)

        # 绑定窗口大小变化事件
        self.root.bind("<Configure>", self.resize_ui)

        # 存储原始图片和调整后的图片
        self.original_image = None
        self.resized_image = None

        # 设置图片的最小和最大显示尺寸
        self.min_image_size = 100  # 最小显示尺寸（宽度或高度）
        self.max_image_size = 800  # 最大显示尺寸（宽度或高度）

        # 初始化 UI 布局
        self.resize_ui()

    def resize_ui(self, event=None):
        """根据窗口大小动态调整 UI 布局"""
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()

        # 图片地址输入栏
        self.image_path_label.place(x=20, y=20, width=80, height=30)
        self.image_path_entry.place(x=110, y=20, width=window_width - 200, height=30)
        self.browse_button.place(x=window_width - 80, y=20, width=60, height=30)

        # 显示图片的区域
        self.image_label.place(x=20, y=70, width=window_width - 40, height=window_height - 150)

        # 预览按钮
        self.preview_button.place(x=window_width // 2 - 120, y=window_height - 60, width=100, height=40)

        # 下载按钮
        self.download_button.place(x=window_width // 2 + 20, y=window_height - 60, width=100, height=40)

    def browse_image(self):
        """浏览并选择图片文件"""
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
        if file_path:
            file_size = os.path.getsize(file_path) / (1024 * 1024)  # 文件大小（MB）
            if file_size > 10:  # 限制图片大小为 10MB
                messagebox.showwarning("警告", "图片文件过大，可能发生卡顿。")
                # return
            self.image_path_entry.delete(0, tk.END)
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
            max_height = window_height - 150  # 留出输入栏和按钮的空间

            # 限制图片的最大和最小显示尺寸
            max_width = min(max_width, self.max_image_size)
            max_height = min(max_height, self.max_image_size)
            max_width = max(max_width, self.min_image_size)
            max_height = max(max_height, self.min_image_size)

            # 保持宽高比调整图片大小
            self.resized_image = self.original_image.copy()
            self.resized_image.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)  # 使用 LANCZOS 替代 ANTIALIAS

            # 显示调整后的图片
            photo = ImageTk.PhotoImage(self.resized_image)
            self.image_label.config(image=photo)
            self.image_label.image = photo  # 保持引用，避免被垃圾回收

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageBase64Converter(root)
    root.mainloop()