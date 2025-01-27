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

### 下载发行版
- Windows：[发行版](https://github.com/TungYL-v2/imgtobase64/releases/)

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
# 使用步骤

## 1. 启动应用程序
- 运行Python脚本后，应用程序窗口将打开。
- 窗口大小默认为显示器分辨率的70%。

## 2. 选择图片文件
- 点击“📁 浏览”按钮，选择要转换的图片文件。
- 图片文件路径将显示在“图片地址”输入栏中。

## 3. 生成或输入密钥（可选）
- 如果需要加密图片，点击“🔑 生成密钥”按钮生成随机AES密钥。
- 密钥会显示在“密钥”输入栏中，也可手动输入密钥。

## 4. 加密图片并转换为Base64
- 点击“🔒 加密”按钮，执行加密并转换操作。
- 弹出文件保存对话框，选择保存Base64文本文件的位置。

## 5. 预览Base64图片
- 点击“👀 预览Base64图片”按钮，选择Base64文本文件。
- **加密文件需输入正确密钥**进行解密。
- 图片将在应用程序窗口中显示。

## 6. 下载图片
- 点击“💾 保存为图片”按钮，转换Base64为图片。
- 弹出文件保存对话框，选择图片保存路径和格式（如`.png`/`.jpg`）。

## 7. 清除预览
- 点击“❌ 清除预览”按钮，立即清空当前显示的图片。

## 8. 切换主题
- 点击“🌙 切换主题”按钮，在浅色/深色模式间切换界面风格。

## 📦 依赖说明

| 依赖库 | 版本要求 | 用途描述 |
|-------|----------|----------|
| [![customtkinter](https://img.shields.io/badge/customtkinter-5.2+-009688)](https://github.com/TomSchimansky/CustomTkinter) | ≥5.2 | 现代化GUI界面开发框架 |
| [![Pillow](https://img.shields.io/badge/Pillow-10.0+-398D9C)](https://python-pillow.org/) | ≥10.0 | 图像处理核心库（格式转换/尺寸调整） |
| [![pycryptodome](https://img.shields.io/badge/pycryptodome-3.20+-4A90E2)](https://www.pycryptodome.org/) | ≥3.20 | AES-128加密算法实现 |

---

## 📜 开源协议
[![MIT License](https://img.shields.io/badge/License-MIT-4DA1F9?style=flat-square)](https://opensource.org/licenses/MIT)  
本作品采用 **[MIT 许可证](LICENSE)** 授权，您可自由：
- 修改源代码
- 用于商业项目
- 进行二次分发
*（需保留原始许可声明）*

---

## 🤝 贡献指南
欢迎通过以下方式参与贡献：  
[![GitHub Issues](https://img.shields.io/github/issues/TungYL-v2/imgtobase64?logo=github)](https://github.com/TungYL-v2/imgtobase64/issues)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-28A745?logo=git)](https://github.com/TungYL-v2/imgtobase64/pulls)

### 贡献流程
1. 阅读 [贡献者公约](CODE_OF_CONDUCT.md)
2. Fork 项目仓库并创建特性分支
3. 提交符合规范的代码变更
4. 编写/更新单元测试
5. 通过 Pull Request 提交变更

---
