def task(camel_case_str: str) -> str:
    return "".join(filter(str.islower, word))  # отфильтровать только буквы нижнего регистра


if __name__ == "__main__":
    word = "AbCdEfGh"
    print(task(word))


