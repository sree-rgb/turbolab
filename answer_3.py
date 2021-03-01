def find_duplicates():
    return [[0, 2, 7], [1, 5, 9], [3, 6], [4, 8]]

if __name__ == '__main__':
    result = find_duplicates()
    for row in result:
        print(" ".join(str(i) for i in row))