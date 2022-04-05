# QUESTIONS

# 1. Platform
# 2. Software Type
# 3. Code Size
# 4. Team Size
# 5. Test Level
# 6. Testing Practices
# 7. Frequency
# 8. Severity
# 9. Consequences
# 10. Causes
# 11. Mitigations
# 12. Wishes

import numpy as np


# COLUMNS

# -- 1. PLATFORM

platform_question = "For which platforms do you develop?"
platform_columns = [
    "platform: Desktop",
    "platform: Mobile",
    "platform: Web (Back-end)",
    "platform: Web (Front-end)",
    "platform: WebAssembly",
    "platform: Server / Infrastructure",
    "platform: IoT / Embedded",
    "platform: Classic AUTOSAR ECU",
    "platform: Adaptive AUTOSAR ECU",
    "platform: Consoles (Xbox / PlayStation / Nintendo etc.)",
    "platform: Not decided yet (research / proof of concept)",
    "platform: I don't develop anything",
    "platform: Other",
#     "platform: Other (free text)",
]

# -- 2. SOFTWARE TYPE

softwareType_question = "What types of software do you develop?"
softwareType_columns = [
    "softwareType: Automotive Chassis",
    "softwareType: Automotive Drive Train",
    "softwareType: Automated Driving, Driver Assistance",
    "softwareType: Augmented Reality / Virtual Reality",
    "softwareType: Business Intelligence / Data Science / Machine Learning",
    "softwareType: Blockchain",
    "softwareType: Database / Data Storage",
    "softwareType: Education / Training",
    "softwareType: Entertainment / Infotainment",
    "softwareType: Fintech (Finance)",
    "softwareType: Games",
    "softwareType: Hardware",
    "softwareType: Home Automation",
    "softwareType: IT Infrastructure",
    "softwareType: Libraries / Frameworks",
    "softwareType: Programming Tools",
    "softwareType: Security",
    "softwareType: System Software (e.g. OS driver)",
    "softwareType: Utilities (small apps for small tasks)",
    "softwareType: Websites",
    "softwareType: Other",
#     "softwareType: Other (free text)",
]


# -- 3. CODE SIZE

codeSize_question = "How large is the code base of your main project by lines of source code (LOC)?"
codeSize_values = [
    'less than 1k LOC',
    '1k - 10k LOC',
    '10k - 100k LOC',
    '100k - 1M LOC',
    '1M - 10M LOC',
    'more than 10M LOC',
    'Not answered'
]
codeSize_values_to_int = {
    'less than 1k LOC': 0,
    '1k - 10k LOC': 1,
    '10k - 100k LOC': 2,
    '100k - 1M LOC': 3,
    '1M - 10M LOC': 4,
    'more than 10M LOC': 5,
    'Not answered': np.NaN
}


# -- 4. TEAM SIZE

teamSize_question = "How many developers are working on your product or project?"
teamSize_values = [
    'Just me',
    '2 - 5',
    '6 - 10',
    '11 - 20',
    '21 - 100',
    'More than 100 developers',
    'Not answered'
]
teamSize_values_to_int = {
    'Just me': 0,
    '2 - 5': 1,
    '6 - 10': 2,
    '11 - 20': 3,
    '21 - 100': 4,
    'More than 100 developers': 5,
    'Not answered': np.NaN
}


# -- 5. TEST LEVEL

testLevel_question = "What kinds of tests do you typically work with?"
testLevel_columns = [
    "testLevel: Unit Tests",
    "testLevel: Component Tests",
    "testLevel: Integration Tests",
    "testLevel: System Tests",
    "testLevel: Software in the loop Tests (i)",
    "testLevel: Platform in the loop Tests",
    "testLevel: Hardware in the loop Tests",
    "testLevel: Other",
#     "testLevel: Other (free text)",
]


# -- 6. TESTING PRACTICES

testingPractices_question = "Which of these testing practices do you use?"
testingPractices_columns = [
    "testingPractices: Manual testing",
    "testingPractices: Automated testing",
    "testingPractices: Continuous Integration",
    "testingPractices: Regression Testing",
    "testingPractices: Fuzzing",
    "testingPractices: Property based testing",
    "testingPractices: Parameterized tests",
    "testingPractices: Test generation",
    "testingPractices: Other",
#     "testingPractices: Other (free text)",
]


# -- 7. FREQUENCY (FL01)

frequency_question = "How often do you experience flaky failures?"
frequency_values = [
    'Never',
    'A few times a year',
    'Monthly',
    'Weekly',
    'Daily',
    'Multiple times per day',
    'Not answered'
]
frequency_value_without_not_answered = [ x for x in frequency_values if x != "Not answered" ]
frequency_values_to_int = {
    'Never': 0,
    'A few times a year': 1,
    'Monthly': 2,
    'Weekly': 3,
    'Daily': 4,
    'Multiple times per day': 5,
    'Not answered': np.NaN
}

# -- 8. SEVERITY (FL02)

severity_question = "How problematic is flakiness for you?"
severity_values = [
    'Not a problem',
    'A minor problem',
    'A moderate problem',
    'A serious problem',
    'Not answered'
]
severity_value_without_not_answered = [ x for x in severity_values if x != "Not answered" ]
severity_values_to_int = {
    'Not a problem': 0,
    'A minor problem': 1,
    'A moderate problem': 2,
    'A serious problem': 3,
    'Not answered': np.NaN
}

# -- 9. CONSEQUENCES (FL03)

consequences_question = "Which negative effects of flaky tests have you experienced?"
#
consequences_trust_columns = [
    "consequences: Rerun of failing tests without analyzing the failure",
    "consequences: Rerun of passing tests assuming hidden bugs",
]
consequences_waste_columns = [
    "consequences: Developer time gets wasted inspecting flaky failures",
    "consequences: Computing power is spent rerunning flaky tests"
]
consequences_hamperDevelopment_columns = [
    "consequences: Merging pull-requests is harder because this requires a passing test suite",
    "consequences: Delayed releases",
]
consequences_columns = consequences_trust_columns + consequences_waste_columns + consequences_hamperDevelopment_columns
#
consequences_other_columns_rating = [
    "consequences: Other: %input:FL06_01%",
    "consequences: Other: %input:FL06_02%",
    "consequences: Other: %input:FL06_03%",
]
consequences_other_columns_freeText = [
    "otherConsequences: otherConsequences1",
    "otherConsequences: otherConsequences2",
    "otherConsequences: otherConsequences3",
]
#
consequences_a_to_aShort = {
    'Rerun of failing tests without analyzing the failure': 'Rerun failures without analyzing',
    'Rerun of passing tests assuming hidden bugs': 'Rerun passes suspecting hidden bugs',
    'Merging pull-requests is harder because this requires a passing test suite': 'Merging PRs is harder',
    'Delayed releases': 'Delayed releases',
    'Developer time gets wasted inspecting flaky failures': 'Wasting developer time',
    'Computing power is spent rerunning flaky tests': 'Wasting computational resources',
    'Other:': 'Other'
}
consequences_qa_map = {
    f"consequences: {k}": f"consequences: {v}"
    for k, v in consequences_a_to_aShort.items()
}

# -- 10. ROOT CAUSE (FL04)

rootCause_question = "What are the root causes of the flakiness you experienced?"
rootCause_columns = [
    "rootCause: Making asynchronous calls without waiting for the result properly (thread.sleep)",
    "rootCause: Race conditions, deadlocks or other concurrency related errors",
    "rootCause: Prior test did not cleanup properly after running (i)",
    "rootCause: Another test that should run before your test and set up the environment was not executed (successfully) (i)",
    "rootCause: Could not acquire resources because of a resource leak (i)",
    "rootCause: Remote connection failure (i)",
    "rootCause: Local bad socket management",
    "rootCause: Relying on the system time (i)",
    "rootCause: Accessing values that were already deleted by the garbage collector or relying on the garbage collector to have already cleaned up",
    "rootCause: Using randomness without accounting for all possible values",
    "rootCause: Rounding errors when using floating-point operations",
    "rootCause: Assuming a specific order when iterating over unordered collections",
    "rootCause: Asserting a too restrictive range (i)",
    "rootCause: Single test takes too long (Test case timeout)",
    "rootCause: All tests together take too long (Test suite timeout)",
    "rootCause: Relying on a specific platform (e.g. 32/64 bit, Kernel version)",
    "rootCause: The test infrastructure fails to provide a proper environment (e.g. installing dependencies)",
    "rootCause: Reading values from uninitialized variables",
    "rootCause: Differences between compilers likeundefined behavior or compiler optimizations",
    "rootCause: Using random, non-seeded values for testing",
    "rootCause: Unknown Cause"
]
#
rootCause_other_columns_rating = [
    "rootCause: Other: %input:FL08_01%",
    "rootCause: Other: %input:FL08_02%",
    "rootCause: Other: %input:FL08_03%",
]
rootCause_other_columns_freeText = [
    "otherRootCauses: otherRootCause1",
    "otherRootCauses: otherRootCause2",
    "otherRootCauses: otherRootCause3",
]
#
rootCause_a_to_aShort = {
    'Making asynchronous calls without waiting for the result properly (thread.sleep)': 'Async Wait',
    'Race conditions, deadlocks or other concurrency related errors': 'Concurrency',
    'Prior test did not cleanup properly after running (i)': 'Order-dependency (victim)',
    'Another test that should run before your test and set up the environment was not executed (successfully) (i)':
        'Order-dependency (brittle)',
    'Could not acquire resources because of a resource leak (i)': 'Resource Leaks',
    'Remote connection failure (i)': 'Network (remote)',
    'Local bad socket management': 'Network (local)',
    'Relying on the system time (i)': 'Time',
    'Accessing values that were already deleted by the garbage collector or relying on the garbage collector to have already cleaned up': 'IO (garbage collector)',
    'Using randomness without accounting for all possible values': 'Randomness',
    'Rounding errors when using floating-point operations': 'Floating point',
    'Assuming a specific order when iterating over unordered collections': 'Unordered collection',
    'Asserting a too restrictive range (i)': 'Too restrictive range',
    'Single test takes too long (Test case timeout)': 'Test case timeout',
    'All tests together take too long (Test suite timeout)': 'Test suite timeout',
    'Relying on a specific platform (e.g. 32/64 bit, Kernel version)': 'Platform dependency',
    'The test infrastructure fails to provide a proper environment (e.g. installing dependencies)': 'Infrastructure',
    'Reading values from uninitialized variables': 'Uninitialized variables',
    'Differences between compilers likeundefined behavior or compiler optimizations': 'Compiler differences',
    'Using random, non-seeded values for testing': 'non-seeded Testing',
    'Unknown Cause': 'Unknown Cause',
    'Other:': 'Other'
}
rootCause_qa_map = {
    f"rootCause: {k}": f"rootCause: {v}"
    for k, v in rootCause_a_to_aShort.items()
}

# -- 11. MITIGATION STRATEGIES (FL05)

mitigations_question = "What is your current strategy to deal with flakiness?"
mitigations_columns = [
    "mitigationStrategies: Rerun failing tests",
    "mitigationStrategies: Rerun test in different environment",
    "mitigationStrategies: Shuffle test order",
    "mitigationStrategies: Mark test as flaky (i)",
    "mitigationStrategies: Disable test case",
    "mitigationStrategies: Automatically disable tests that show flaky behavior",
    "mitigationStrategies: Automatically file bug report / issue",
    "mitigationStrategies: Automatically detect flaky tests (i)",
    "mitigationStrategies: Automatically debug flaky failures (i)",
    "mitigationStrategies: Visualize Flakiness (i)",
    "mitigationStrategies: Quantify flakiness (i)",
    "mitigationStrategies: Encourage developers to fix their flaky tests through incentives or penalties"
]
#
mitigations_other_columns_rating = [
    "mitigationStrategies: Other: %input:FL10_01%",
    "mitigationStrategies: Other: %input:FL10_02%",
    "mitigationStrategies: Other: %input:FL10_03%",
]
mitigations_other_columns_freeText = [
    "otherMitigations: otherMitigations1",
    "otherMitigations: otherMitigations2",
    "otherMitigations: otherMitigations3",
]
#
mitigations_a_to_aShort = {
    'Rerun failing tests': 'Rerun',
    'Rerun test in different environment': 'Rerun in different environment',
    'Shuffle test order': 'Shuffle test order',
    'Mark test as flaky (i)': 'Flag',
    'Disable test case': 'Disable',
    'Automatically disable tests that show flaky behavior': 'Auto disable',
    'Automatically file bug report / issue': 'Auto report',
    'Automatically detect flaky tests (i)': 'Auto detect',
    'Automatically debug flaky failures (i)': 'Auto debug',
    'Visualize Flakiness (i)': 'Visualize',
    'Quantify flakiness (i)': 'Quantify',
    'Encourage developers to fix their flaky tests through incentives or penalties': 'Incentives & Penalties',
    'Other:': 'Other'
}
mitigations_qa_map = {
    f"mitigationStrategies: {k}": f"mitigationStrategies: {v}"
    for k, v in mitigations_a_to_aShort.items()
}


# -- 12. WISHES (FL06)

wishes_question = "What tool or information would you like to have in order to help you deal with flaky tests?"
wishes_column = "wishes: [01]"


# OTHER VALUES

likert_values = ['Never', 'Rarely', 'Sometimes', 'Very Often', 'Always']
likert_values_to_int = {
    'Never': 0,
    'Rarely': 1,
    'Sometimes': 2,
    'Very Often': 3,
    'Always': 4,
    "Not answered": np.NaN
}

multiple_choice_values = ["Checked", "Not checked"]
multiple_choice_values_to_int = {
    "Not checked": 0,
    "Checked": 1,
    "Not answered": np.NaN
}



# HIERARCHICAL STRUCTURE (idea)

# {
#     "": {
#         "id": ,
#         "columns": ,
#         "values": ,
#         "values_to_int": ,
#         "question_long": ,
#         "a_to_aShort": ,
#     },
# }

demographic_questions = [
    "platform", "softwareType", "codeSize", "teamSize", "testLevel", "testingPractices"
]
flaky_questions = [
    "frequency", "severity", "consequences", "rootCause", "mitigations"
]
questions = demographic_questions + flaky_questions

qmap = {
    "platform": {
        "id": "de01",
        "type": "multiple-choice",
        "columns": platform_columns,
        "values": multiple_choice_values,
        "values_to_int": multiple_choice_values_to_int,
        "question_long": platform_question,
        "a_to_aShort": None,
    },
    "softwareType": {
        "id": "de02",
        "type": "multiple-choice",
        "columns": softwareType_columns,
        "values": multiple_choice_values,
        "values_to_int": multiple_choice_values_to_int,
        "question_long": softwareType_question,
        "a_to_aShort": None,
    },
    "codeSize": {
        "id": "de03",
        "type": "singe-choice",
        "columns": ["codeSize"],
        "values": codeSize_values,
        "values_to_int": codeSize_values_to_int,
        "question_long": codeSize_question,
        "a_to_aShort": None,
    },
    "teamSize": {
        "id": "de04",
        "type": "singe-choice",
        "columns": ["teamSize"],
        "values": teamSize_values,
        "values_to_int": teamSize_values_to_int,
        "question_long": teamSize_question,
        "a_to_aShort": None,
    },
    "testLevel": {
        "id": "de05",
        "type": "multiple-choice",
        "columns": testLevel_columns,
        "values": multiple_choice_values,
        "values_to_int": multiple_choice_values_to_int,
        "question_long": testLevel_question,
        "a_to_aShort": None,
    },
    "testingPractices" : {
        "id": "de06",
        "type": "multiple-choice",
        "columns": testingPractices_columns,
        "values": multiple_choice_values,
        "values_to_int": multiple_choice_values_to_int,
        "question_long": testingPractices_question,
        "a_to_aShort": None,
    },
    "frequency": {
        "id": "fl01",
        "type": "singe-choice",
        "columns": ["frequency"],
        "values": frequency_values,
        "values_to_int": frequency_values_to_int,
        "question_long": frequency_question,
        "a_to_aShort": None,
    },
    "severity": {
        "id": "fl02",
        "type": "singe-choice",
        "columns": ["severity"],
        "values": severity_values,
        "values_to_int": severity_values_to_int,
        "question_long": severity_question,
        "a_to_aShort": None,
    },
    "consequences": {
        "id": "fl03",
        "type": "likert-matrix",
        "columns": consequences_columns,
        "values": likert_values,
        "values_to_int": likert_values_to_int,
        "question_long": consequences_question,
        "a_to_aShort": consequences_a_to_aShort,
        "qa_to_qaShort": consequences_qa_map,
        "other_columns_rating" : consequences_other_columns_rating,
        "other_columns_freeText" : consequences_other_columns_freeText,
    },
    "rootCause": {
        "id": "fl04",
        "type": "likert-matrix",
        "columns": rootCause_columns,
        "values": likert_values,
        "values_to_int": likert_values_to_int,
        "question_long": rootCause_question,
        "a_to_aShort": rootCause_a_to_aShort,
        "qa_to_qaShort": rootCause_qa_map,
        "other_columns_rating" : rootCause_other_columns_rating,
        "other_columns_freeText" : rootCause_other_columns_freeText,
    },
    "mitigations": {
        "id": "fl05",
        "type": "likert-matrix",
        "columns": mitigations_columns,
        "values": likert_values,
        "values_to_int": likert_values_to_int,
        "question_long": mitigations_question,
        "a_to_aShort": mitigations_a_to_aShort,
        "qa_to_qaShort": mitigations_qa_map,
        "other_columns_rating" : mitigations_other_columns_rating,
        "other_columns_freeText" : mitigations_other_columns_freeText,
    },
    "wishes": {
        "id": "fl06",
        "type": "free-text",
        "question_long": wishes_question,
        "columns": [wishes_column],
    },
}


# GROUPED COLUMNS

demographic_question_columns = \
    platform_columns + \
    softwareType_columns + \
    ["codeSize"] + \
    ["teamSize"] + \
    testLevel_columns + \
    testingPractices_columns

flakyExperience_question_columns = \
    ["frequency"] + \
    ["severity"] + \
    consequences_columns + \
    rootCause_columns + \
    mitigations_columns

flakyExperience_question_columns_incl_freeText = \
    ["frequency"] + \
    ["severity"] + \
    consequences_columns + \
    consequences_other_columns_freeText + \
    rootCause_columns + \
    rootCause_other_columns_freeText + \
    mitigations_columns + \
    mitigations_other_columns_freeText


all_question_columns = \
    demographic_question_columns + \
    flakyExperience_question_columns + \
    [wishes_column]

all_question_columns_incl_freeText = \
    demographic_question_columns + \
    flakyExperience_question_columns_incl_freeText + \
    [wishes_column]


# PROLIFIC DEMOGRAPHIC COLUMNS

all_prolific_demographic_cols = [
    "age",
    "num_approvals",
    "num_rejections",
    "prolific_score",
    "Country of Birth",
    "Current Country of Residence",
    "Employment Status",
    "First Langauge",
    "Knowledge of software development techniques",
    "Nationality",
    "Sex",
    "Student Status"
]

interesting_prolific_demographic_cols = [
    "age",
    "Country of Birth",
    "Current Country of Residence",
    "Employment Status",
    "First Language",
    "Nationality",
    "Sex",
    "Student Status",
    "Knowledge of software development techniques "
]