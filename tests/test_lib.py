from batchlib.utils import MAX_RECORD_SIZE, create_output_records


def test_basic_case():
    sample_input = ["aaaaaaaaaaaaaaaaaa", "bbbbbbbbbbbbbbbbb", "ccccccccccccc"]
    output = create_output_records(sample_input)
    assert output == [["aaaaaaaaaaaaaaaaaa", "bbbbbbbbbbbbbbbbb", "ccccccccccccc"]]


def test_empty_input():
    output = create_output_records([])
    assert output == []


def test_record_gt_1mb():
    sample_input = [
        "aaaaaaaaaaaaaaaaaa" * MAX_RECORD_SIZE,
        "bbbbbbbbbbbbbbbbb",
        "ccccccccccccc",
    ]
    output = create_output_records(sample_input)
    assert output == [["bbbbbbbbbbbbbbbbb", "ccccccccccccc"]]


def test_gt_5mb():
    sample_input = [
        "a" * MAX_RECORD_SIZE,
        "b" * MAX_RECORD_SIZE,
        "c" * MAX_RECORD_SIZE,
        "d" * MAX_RECORD_SIZE,
        "e" * MAX_RECORD_SIZE,
        "f" * MAX_RECORD_SIZE,
        "g" * MAX_RECORD_SIZE,
    ]
    output = create_output_records(sample_input)
    assert output == [
        [
            "a" * MAX_RECORD_SIZE,
            "b" * MAX_RECORD_SIZE,
            "c" * MAX_RECORD_SIZE,
            "d" * MAX_RECORD_SIZE,
            "e" * MAX_RECORD_SIZE,
        ],
        ["f" * MAX_RECORD_SIZE, "g" * MAX_RECORD_SIZE],
    ]


def test_max_500_record():
    sample_input1 = ["aaaaaaaaaaaaaaaaaa", "bbbbbbbbbbbbbbbbb"] * 350
    sample_input2 = ["aaaaaaaaaaaaaaaaaa", "bbbbbbbbbbbbbbbbb"] * 300 + [
        "ccccccccccccc",
        "ddddddddddddd",
    ] * 200
    output1 = create_output_records(sample_input1)
    output2 = create_output_records(sample_input2)
    assert output1 == [
        ["aaaaaaaaaaaaaaaaaa", "bbbbbbbbbbbbbbbbb"] * 250,
        ["aaaaaaaaaaaaaaaaaa", "bbbbbbbbbbbbbbbbb"] * 100,
    ]
    assert output2 == [
        ["aaaaaaaaaaaaaaaaaa", "bbbbbbbbbbbbbbbbb"] * 250,
        ["aaaaaaaaaaaaaaaaaa", "bbbbbbbbbbbbbbbbb"] * 50
        + ["ccccccccccccc", "ddddddddddddd"] * 200,
    ]
