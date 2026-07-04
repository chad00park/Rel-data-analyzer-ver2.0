import os
import sys
import threading
import http.server
import socketserver
import webview

def start_server(port):
    # PyInstaller로 빌드된 경우와 개발 환경의 경로 처리
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    
    os.chdir(base_path)
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        httpd.serve_forever()

if __name__ == '__main__':
    port = 8543
    # 백그라운드에서 로컬 웹 서버 실행 (index.html 로드용)
    t = threading.Thread(target=start_server, args=(port,), daemon=True)
    t.start()
    
    # 윈도우 창 크기 설정 및 프로그램 실행
    webview.create_window(
        title='ReadOut Report Analyzer', 
        url=f'http://localhost:{port}/index.html',
        width=1300, 
        height=850
    )
    webview.start()
