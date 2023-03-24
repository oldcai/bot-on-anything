import imgkit
import markdown


def html_to_png(html, output_path, css=None):
    # Define default CSS for the table
    if css is None:
        css = """
        <style>
            table {
                border-collapse: collapse;
                width: 100%;
                font-family: Arial, sans-serif;
            }
            th, td {
                border: 1px solid #ddd;
                padding: 8px;
                text-align: left;
            }
            th {
                background-color: #f2f2f2;
                font-weight: bold;
            }
            tr:nth-child(even) {
                background-color: #f2f2f2;
            }
            tr:hover {
                background-color: #ddd;
            }
        </style>
        """

    # Wrap the table with the provided CSS
    styled_table = f"<html><head>{css}</head><body>{html}</body></html>"

    # Set imgkit options
    options = {
        "quiet": "",
        "format": "png",
        "encoding": "UTF-8",
        "width": "600",
    }

    # Convert the styled HTML table to a PNG image
    return imgkit.from_string(styled_table, output_path, options=options)


def markdown_to_png(markdown_text, output_path=False):
    html = markdown.markdown(markdown_text, extensions=['tables'])
    return html_to_png(html, output_path)


if __name__ == '__main__':
    markdown_text = '''
| 市场 | 走势 | 定义 | 备注 |
|--- | --- | --- | --- |
| 黄金 | 上行 | A段 | 前面有调整结构，现在上行 |
| 白银 | 多端运行 | 无 | 无 |
| 原油 | 上行 | A段 | 主力动能，后面等待盘整 |
| 欧元/美元 | 空头 | 反逻辑 | 反逻辑保持敏感度 |
| 暴美 | 无 | 无 | 无法判断 |
| 美瑞 | 无 | 无 | 暂无直接机会 |
| 澳美 | 等待B段整理 | 等待 | 行情反复，需要等待整理 |
| 美加 | 等待B段整理 | 等待 | 行情反复，需要等待整理 |
| 纽美 | 行情反复 | 无 | 有空头反逻辑敏感度 |
| 英镑/日元 | 等待整理 | 等待 | 等待宏观相匹配整理后关注 |
'''

    output_file = "../../table.png"
    markdown_to_png(markdown_text, output_file)
