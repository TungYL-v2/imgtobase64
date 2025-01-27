# 🖼️ 图片与 Base64 转换器

[![Python](https://img.shields.io/badge/Python-3.7%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-4DA1F9)](https://opensource.org/licenses/MIT)
[![GUI](https://img.shields.io/badge/GUI-CustomTkinter-009688)](https://github.com/TomSchimansky/CustomTkinter)

一款基于 Python 的现代化桌面应用，支持图片与 Base64 编码互转，集成 AES 加密功能，提供更安全的数据处理方案。

![Demo Screenshot](https://github.com/TungYL-v2/imgtobase64/blob/main/main.png) <!-- 建议替换实际截图 -->
---

## ✨ 核心功能

### 🖼️ 双向转换
- **图片 → Base64**：支持 JPG/PNG/BMP 等常见格式
- **Base64 → 图片**：实时预览解码结果，一键保存文件

### 🔐 安全增强
- AES-128 加密/解密（CBC模式，PKCS7填充）
- 随机密钥生成器（16字节）
- 加密后Base64编码格式存储

### 🎨 用户体验
- 现代化 GUI 界面（支持深色/浅色主题）
- 实时图片预览功能
- 拖放文件支持（规划中）
- 多语言支持（规划中）

---

## 🛠️ 快速开始

### 环境要求
- Python 3.7+
- Windows/macOS/Linux

### 安装步骤

#### 克隆仓库
```
git clone https://github.com/TungYL-v2/imgtobase64.git
cd image-base64-converter
```
#### 安装依赖
```
pip install -r requirements.txt
```
#### 运行程序
```
python main.py
```
### 使用方法

- **选择图片**：
  - 点击“浏览”按钮选择本地图片文件。
  - 图片路径将显示在输入框中。

- **生成密钥（可选）**：
  - 点击“生成密钥”按钮生成一个 128 位的随机密钥。
  - 密钥将显示在密钥输入框中。

- **转换为 Base64**：
  - 点击“转换为 Base64”按钮，将图片转换为 Base64 编码。
  - 如果输入了密钥，图片数据将被加密后再编码。

- **预览图片**：
  - 点击“预览”按钮，从 Base64 编码中解码并显示图片。
  - 如果输入了密钥，图片数据将被解密后再解码。

- **下载图片**：
  - 点击“下载”按钮，将 Base64 编码的图片保存为本地文件。（优先下载预览的图片）

- **切换主题**：
  - 点击“切换主题”按钮，在浅色和深色主题之间切换。

### 项目结构

```plaintext
image-base64-converter/
├── main.py                # 主程序入口
├── requirements.txt       # 项目依赖
├── README.md              # 项目说明文档
```
### 依赖库

- **customtkinter**：用于创建现代风格的 GUI 界面。
- **Pillow**：用于处理图片（打开、调整大小、保存等）。
- **pycryptodome**：用于实现 AES 加密和解密功能。

### 许可证

本项目基于 [MIT 许可证](https://opensource.org/licenses/MIT) 开源。

### 贡献

欢迎提交 Issue 和 Pull Request！如果你有任何问题或建议，请随时联系。
