## 在 Windows 上安装 Claude Code (使用 WSL)

Claude Code 默认仅支持 Linux 和 MacOS。要在 Windows 上使用 Claude Code,您可以使用 WSL。

1. 前往 Microsoft Store

2. 搜索 Ubuntu WSL 并安装

3. 在终端中打开 WSL

4. 运行以下命令(这遵循最佳安全实践):

```bash
# 首先,保存现有全局包的列表以便稍后迁移
npm list -g --depth=0 > ~/npm-global-packages.txt

# 为您的全局包创建一个目录
mkdir -p ~/.npm-global

# 配置 npm 使用新的目录路径
npm config set prefix ~/.npm-global

# 注意: 根据您的 shell 将 ~/.bashrc 替换为 ~/.zshrc, ~/.profile 或其他适当的文件
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc

# 应用新的 PATH 设置
source ~/.bashrc

# 现在在新位置重新安装 Claude Code
npm install -g @anthropic-ai/claude-code
```

5. 现在在您的 IDE 中,您可以使用 Ctrl + J 打开终端(也可以使用此快捷键关闭它),您可以点击加号旁边的下拉箭头打开 Ubuntu (WSL) 终端,在那里您可以运行 "claude" 命令来启动 Claude Code。