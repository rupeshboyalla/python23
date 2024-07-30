# let results = [
# (result: "PASS", name: "Stress test"),
# (result: "FAIL", name: "UI test"),
# (result: "FAIL", name: "Functional test"),
# (result: "PASS", name: "System test"),
# (result: "FAIL", name: "Network test")
# ]


# Pass -> 2 and name = "Stress test", "System test"
from collections import defaultdict


def testResultParsing(parseTestResults: tuple):
    """

    :type parseTestResults: List[Tuple[str, str]]
    """
    lookUpTable = defaultdict(list)
    for ele in parseTestResults:
        lookUpTable[ele[0]].append(ele[1])
    for key, value in lookUpTable.items():
        print(f"test result: {key} --> {len(value)}, test names: {value}")


testResults = [
    ("PASS", "Stress test"),
    ("FAIL", "UI test"),
    ("FAIL", "Functional test"),
    ("PASS", "System test"),
    ("FAIL", "Network test")
]

print(testResultParsing(testResults))
