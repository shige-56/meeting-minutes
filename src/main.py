import openai
from utils import save_to_text_file

# OpenAI APIキーの設定
openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_meeting_summary_and_tasks(transcription):
    # 議事録の生成
    summary_prompt = f"以下の会話内容をもとに議事録を作成してください:\n\n{transcription}\n\n議事録:"
    summary_response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": summary_prompt}]
    )
    meeting_summary = summary_response.choices[0].message["content"]

    # タスクの抽出
    tasks_prompt = f"以下の会話内容からタスクを抽出し、それぞれ担当者を割り当ててください:\n\n{transcription}\n\nタスク:"
    tasks_response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": tasks_prompt}]
    )
    tasks = tasks_response.choices[0].message["content"]

    return meeting_summary, tasks

if __name__ == "__main__":
    # サンプルデータ読み込み
    with open("../transcription_samples/sample_transcription.txt", "r", encoding="utf-8") as file:
        transcription = file.read()

    # 議事録とタスクを生成
    meeting_summary, tasks = generate_meeting_summary_and_tasks(transcription)

    # テキストファイルに保存
    save_to_text_file("meeting_minutes_and_tasks.txt", meeting_summary, tasks)
