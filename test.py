def test_CreateDNASequence():
    DNA_OR = "a2b2"
    input_DNA = "aabb"
    output_DNA = ""
    pos = 0
    count = 0
    current = input_DNA[0]
    for i in input_DNA:
        pos += 1
        if current != i and current.upper() != i and current.lower() != i:
           output_DNA += current.lower()
           output_DNA += str(count)
           count = 0
        elif pos == len(input_DNA):
            output_DNA += i.lower()
            output_DNA += str(count + 1)
        current = i
        count += 1
    print(output_DNA == DNA_OR)



