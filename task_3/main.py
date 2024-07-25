import timeit
import pandas as pd
from boyer_moore import boyer_moore_search
from knuth_morris_pratt import kmp_search
from rabin_karp import rabin_karp_search


def measure_time(search_function, text, pattern):
    setup_code = f"from __main__ import {search_function.__name__}"
    stmt = f"{search_function.__name__}({repr(text)}, {repr(pattern)})"
    times = timeit.repeat(stmt, setup=setup_code, repeat=3, number=10)
    return min(times)

def load_file(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        return file.read()

def main():
    article1 = load_file('article_1.txt')
        
    search_string1 = "жадібного"
        
    # Вимірювання часу виконання для статті 1
    results_article1 = {
        "Boyer-Moore": [measure_time(boyer_moore_search, article1, search_string1)],
        "Knuth-Morris-Pratt": [measure_time(kmp_search, article1, search_string1)],
        "Rabin-Karp": [measure_time(rabin_karp_search, article1, search_string1)]
    }
    
    # Виводимо результати для статті 1

    df = pd.DataFrame(results_article1)
    print(df.to_markdown(index=False))
    
    article2 = load_file('article_2.txt')
        
    search_string2 = "прискорення пошуку"
        
    # Вимірювання часу виконання для статті 2
    results_article2 = {
        "Boyer-Moore": [measure_time(boyer_moore_search, article2, search_string2)],
        "Knuth-Morris-Pratt": [measure_time(kmp_search, article2, search_string2)],
        "Rabin-Karp": [measure_time(rabin_karp_search, article2, search_string2)]
    }
    
    # Виводимо результати для статті 2

    df = pd.DataFrame(results_article2)
    print(df.to_markdown(index=False))

if __name__ == "__main__":
    main()