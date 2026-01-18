import re
from collections import Counter


def normalize_text(text: str) -> list[str]:
    text = text.lower()
    words = re.findall(r"[а-яa-z0-9]+", text, flags=re.IGNORECASE)
    return words


def count_sentences(text: str) -> int:
    sentences = re.findall(r"[.!?]+", text)
    return len(sentences)


def analyze_text(text: str, top_n: int = 10) -> dict:
    words = normalize_text(text)

    stats = {
        "characters": len(text),
        "characters_no_spaces": len(text.replace(" ", "")),
        "words": len(words),
        "sentences": count_sentences(text),
        "top_words": Counter(words).most_common(top_n),
    }
    return stats


def main():
    print("Text Analyzer — анализ текста")
    print("1) Ввести текст вручную")
    print("2) Прочитать текст из файла")
    choice = input("Выберите режим (1/2): ").strip()

    if choice == "1":
        text = input("\nВставьте текст и нажмите Enter:\n")
    elif choice == "2":
        path = input("Введите путь к файлу (например, text.txt): ").strip()
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        print("Неверный выбор.")
        return

    top_n_str = input("Сколько слов показать в топе? (по умолчанию 10): ").strip()
    top_n = int(top_n_str) if top_n_str.isdigit() else 10

    stats = analyze_text(text, top_n=top_n)

    print("\n--- Результаты ---")
    print(f"Символов (всего): {stats['characters']}")
    print(f"Символов (без пробелов): {stats['characters_no_spaces']}")
    print(f"Слов: {stats['words']}")
    print(f"Предложений: {stats['sentences']}")

    print("\nТоп слов:")
    for word, count in stats["top_words"]:
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
