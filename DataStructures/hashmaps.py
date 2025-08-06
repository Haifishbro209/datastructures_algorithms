from collections import defaultdict, Counter, OrderedDict
from typing import Dict, List, Any

## hashmaps are dictionaies

#100% vibe coded one prompt

def basic_hashmap_operations():
    hashmap = {}
    
    hashmap["key1"] = "value1"
    hashmap["key2"] = "value2"
    hashmap["key3"] = "value3"
    
    print("Basic hashmap:", hashmap)
    print("Access value:", hashmap["key1"])
    print("Get with default:", hashmap.get("key4", "default_value"))
    
    hashmap["key1"] = "updated_value"
    print("After update:", hashmap)
    
    del hashmap["key2"]
    print("After deletion:", hashmap)
    
    print("Keys:", list(hashmap.keys()))
    print("Values:", list(hashmap.values()))
    print("Items:", list(hashmap.items()))

def hashmap_initialization_methods():
    empty_dict = {}
    
    dict_with_values = {"name": "John", "age": 30, "city": "New York"}
    
    dict_from_list = dict([("a", 1), ("b", 2), ("c", 3)])
    
    dict_comprehension = {x: x**2 for x in range(5)}
    
    dict_with_constructor = dict(name="Alice", age=25, city="London")
    
    return empty_dict, dict_with_values, dict_from_list, dict_comprehension, dict_with_constructor

def hashmap_membership_and_iteration():
    fruits = {"apple": 5, "banana": 3, "orange": 8, "grape": 12}
    
    print("apple" in fruits)
    print("watermelon" in fruits)
    print("apple" not in fruits)
    
    for key in fruits:
        print(f"Key: {key}")
    
    for value in fruits.values():
        print(f"Value: {value}")
    
    for key, value in fruits.items():
        print(f"{key}: {value}")

def hashmap_methods_demonstration():
    student_grades = {"Alice": 85, "Bob": 92, "Charlie": 78}
    
    copy_grades = student_grades.copy()
    
    student_grades.update({"David": 88, "Eve": 95})
    
    alice_grade = student_grades.pop("Alice", None)
    
    last_item = student_grades.popitem()
    
    student_grades.setdefault("Frank", 80)
    
    student_grades.clear()
    
    return copy_grades, alice_grade, last_item

def defaultdict_examples():
    dd_list = defaultdict(list)
    dd_list["fruits"].append("apple")
    dd_list["fruits"].append("banana")
    dd_list["vegetables"].append("carrot")
    
    dd_int = defaultdict(int)
    dd_int["count"] += 1
    dd_int["total"] += 5
    
    dd_set = defaultdict(set)
    dd_set["numbers"].add(1)
    dd_set["numbers"].add(2)
    dd_set["numbers"].add(1)
    
    return dd_list, dd_int, dd_set

def counter_examples():
    text = "hello world hello python"
    word_count = Counter(text.split())
    
    numbers = [1, 2, 3, 1, 2, 1, 4, 5, 4]
    number_count = Counter(numbers)
    
    most_common_words = word_count.most_common(2)
    
    combined_counter = word_count + Counter(["hello", "new", "word"])
    
    return word_count, number_count, most_common_words, combined_counter

def ordered_dict_examples():
    od = OrderedDict()
    od["first"] = 1
    od["second"] = 2
    od["third"] = 3
    
    od.move_to_end("first")
    
    last_item = od.popitem(last=True)
    first_item = od.popitem(last=False)
    
    return od, last_item, first_item

def nested_hashmaps():
    company = {
        "employees": {
            "john": {"age": 30, "department": "engineering", "salary": 75000},
            "jane": {"age": 28, "department": "marketing", "salary": 65000},
            "bob": {"age": 35, "department": "engineering", "salary": 85000}
        },
        "departments": {
            "engineering": {"budget": 500000, "head": "alice"},
            "marketing": {"budget": 200000, "head": "charlie"}
        }
    }
    
    john_salary = company["employees"]["john"]["salary"]
    eng_budget = company["departments"]["engineering"]["budget"]
    
    return company, john_salary, eng_budget

def hashmap_as_cache():
    cache = {}
    
    def fibonacci_with_cache(n):
        if n in cache:
            return cache[n]
        
        if n <= 1:
            result = n
        else:
            result = fibonacci_with_cache(n-1) + fibonacci_with_cache(n-2)
        
        cache[n] = result
        return result
    
    fib_10 = fibonacci_with_cache(10)
    return cache, fib_10

def hashmap_for_grouping():
    students = [
        {"name": "Alice", "grade": "A", "subject": "Math"},
        {"name": "Bob", "grade": "B", "subject": "Math"},
        {"name": "Charlie", "grade": "A", "subject": "Science"},
        {"name": "David", "grade": "B", "subject": "Science"},
        {"name": "Eve", "grade": "A", "subject": "Math"}
    ]
    
    grouped_by_grade = defaultdict(list)
    for student in students:
        grouped_by_grade[student["grade"]].append(student["name"])
    
    grouped_by_subject = defaultdict(list)
    for student in students:
        grouped_by_subject[student["subject"]].append(student["name"])
    
    return dict(grouped_by_grade), dict(grouped_by_subject)

def hashmap_frequency_analysis():
    def character_frequency(text):
        return Counter(text.lower())
    
    def word_frequency(text):
        words = text.lower().split()
        return Counter(words)
    
    def find_duplicates(numbers):
        count = Counter(numbers)
        return [num for num, freq in count.items() if freq > 1]
    
    sample_text = "Hello World Hello Python Programming"
    char_freq = character_frequency(sample_text)
    word_freq = word_frequency(sample_text)
    
    sample_numbers = [1, 2, 3, 2, 4, 5, 1, 6, 7, 3]
    duplicates = find_duplicates(sample_numbers)
    
    return char_freq, word_freq, duplicates

def hashmap_set_operations():
    dict1 = {"a": 1, "b": 2, "c": 3}
    dict2 = {"b": 2, "c": 4, "d": 5}
    
    common_keys = set(dict1.keys()) & set(dict2.keys())
    
    all_keys = set(dict1.keys()) | set(dict2.keys())
    
    keys_only_in_dict1 = set(dict1.keys()) - set(dict2.keys())
    
    merged_dict = {**dict1, **dict2}
    
    return common_keys, all_keys, keys_only_in_dict1, merged_dict

def hashmap_performance_examples():
    import time
    
    large_dict = {i: i**2 for i in range(100000)}
    
    start_time = time.time()
    lookup_result = large_dict.get(50000)
    lookup_time = time.time() - start_time
    
    start_time = time.time()
    large_dict[99999] = 999999
    insertion_time = time.time() - start_time
    
    start_time = time.time()
    del large_dict[50000]
    deletion_time = time.time() - start_time
    
    return lookup_result, lookup_time, insertion_time, deletion_time

def hashmap_comprehensions():
    numbers = [1, 2, 3, 4, 5]
    
    squares = {x: x**2 for x in numbers}
    
    even_squares = {x: x**2 for x in numbers if x % 2 == 0}
    
    string_lengths = {word: len(word) for word in ["hello", "world", "python"]}
    
    inverted_dict = {v: k for k, v in squares.items()}
    
    return squares, even_squares, string_lengths, inverted_dict

def run_all_examples():
    print("=== Basic Hashmap Operations ===")
    basic_hashmap_operations()
    
    print("\n=== Initialization Methods ===")
    init_results = hashmap_initialization_methods()
    for i, result in enumerate(init_results):
        print(f"Method {i+1}: {result}")
    
    print("\n=== Membership and Iteration ===")
    hashmap_membership_and_iteration()
    
    print("\n=== Methods Demonstration ===")
    methods_results = hashmap_methods_demonstration()
    print("Results:", methods_results)
    
    print("\n=== DefaultDict Examples ===")
    dd_results = defaultdict_examples()
    for dd in dd_results:
        print(dict(dd))
    
    print("\n=== Counter Examples ===")
    counter_results = counter_examples()
    for result in counter_results:
        print(result)
    
    print("\n=== Nested Hashmaps ===")
    nested_results = nested_hashmaps()
    print("John's salary:", nested_results[1])
    print("Engineering budget:", nested_results[2])
    
    print("\n=== Hashmap as Cache ===")
    cache_results = hashmap_as_cache()
    print("Cache:", cache_results[0])
    print("Fibonacci(10):", cache_results[1])
    
    print("\n=== Grouping with Hashmaps ===")
    grouping_results = hashmap_for_grouping()
    print("By grade:", grouping_results[0])
    print("By subject:", grouping_results[1])
    
    print("\n=== Frequency Analysis ===")
    freq_results = hashmap_frequency_analysis()
    print("Character frequency:", freq_results[0])
    print("Word frequency:", freq_results[1])
    print("Duplicates:", freq_results[2])
    
    print("\n=== Set Operations ===")
    set_results = hashmap_set_operations()
    print("Common keys:", set_results[0])
    print("All keys:", set_results[1])
    print("Keys only in dict1:", set_results[2])
    print("Merged dict:", set_results[3])
    
    print("\n=== Comprehensions ===")
    comp_results = hashmap_comprehensions()
    for result in comp_results:
        print(result)

if __name__ == "__main__":
    run_all_examples()