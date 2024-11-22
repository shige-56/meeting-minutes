def save_to_text_file(filename, meeting_summary, tasks):
    # ファイルに保存
    with open(filename, "w", encoding="utf-8") as file:
        file.write("【議事録】\n")
        file.write(meeting_summary)
        file.write("\n\n")
        file.write("【タスク一覧】\n")
        file.write(tasks)

    print(f"ファイルに保存しました: {filename}")
