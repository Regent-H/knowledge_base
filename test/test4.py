"""
执行 MinerU 命令
"""
import os
import subprocess
import time

# ========= 配置 =========
MINERU_EXE = r"C:\Users\13173\miniconda3\envs\venv_mineru302\Scripts\mineru.exe"
import_file_path = r"D:\question_of_work.pdf"
file_dir_path = r"D:\output"
# ========================

env = os.environ.copy()
env["MINERU_MODEL_SOURCE"] = "local"
env["MODELSCOPE_CACHE"] = r"D:\ai_models\modelscope_cache"

# 构造带引号的命令字符串，处理中文路径
cmd_str = f'"{MINERU_EXE}" -p "{import_file_path}" -o "{file_dir_path}" --backend pipeline'

process_start_time = time.time()

proc = subprocess.Popen(
    cmd_str,
    shell=True,          # 关键：交给cmd解析，避开CreateProcess参数bug
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    errors="replace",
    text=True,
    encoding="utf-8",
    bufsize=1
)

for line in proc.stdout:
    print(f"执行MinerU产生的日志：{line.rstrip()}")

processed_code = proc.wait()
process_end_time = time.time()

if processed_code == 0:
    print(f"\n✅ MinerU成功解析PDF文件，耗时:{process_end_time - process_start_time:.2f}s")
else:
    print(f"\n❌ MinerU解析PDF文件失败，return code: {processed_code}")
