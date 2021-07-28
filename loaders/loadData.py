import pandas as pd

def load(conn, file1="./data/train.csv", file2="./data/test.csv", **kwargs):
    train = pd.read_csv(file1, delimiter=";")
    train = train[["job", "marital", "education", "default", "housing", "loan", "contact", "poutcome", "y"]]
    train["trainSet"] = True
    test = pd.read_csv(file2, delimiter=";")
    test = test[["job", "marital", "education", "default", "housing", "loan", "contact", "poutcome", "y"]]
    test["trainSet"] = False
    data = pd.concat([train, test])
    data["Person"] = data.index
    data.reset_index(drop=True, inplace=True)

    print(data.head())
    print(data.shape)
    conn.upsertVertexDataFrame(data, "Person", "Person", {"train": "trainSet"})
    conn.upsertVertexDataFrame(data, "Employment", "job", {})
    conn.upsertVertexDataFrame(data, "MaritalStatus", "marital", {})
    conn.upsertVertexDataFrame(data, "Education", "education", {})
    conn.upsertVertexDataFrame(data, "DefaultStatus", "default", {})
    conn.upsertVertexDataFrame(data, "Housing", "housing", {})
    conn.upsertVertexDataFrame(data, "Loan", "loan", {})
    conn.upsertVertexDataFrame(data, "Contact", "contact", {})
    conn.upsertVertexDataFrame(data, "PreviousOutcome", "poutcome", {})
    conn.upsertVertexDataFrame(data, "Outcome", "y", {})

    conn.upsertEdgeDataFrame(data, "Person", "PERSON_HAS_EMPLOYMENT", "Employment", "Person", "job", {})
    conn.upsertEdgeDataFrame(data, "Person", "PERSON_HAS_MARITAL_STATUS", "MaritalStatus", "Person", "marital", {})
    conn.upsertEdgeDataFrame(data, "Person", "PERSON_HAS_EDUCATION", "Education", "Person", "education", {})
    conn.upsertEdgeDataFrame(data, "Person", "PERSON_HAS_DEFAULT_STATUS", "DefaultStatus", "Person", "default", {})
    conn.upsertEdgeDataFrame(data, "Person", "PERSON_HAS_HOUSING", "Housing", "Person", "housing", {})
    conn.upsertEdgeDataFrame(data, "Person", "PERSON_HAS_LOAN", "Loan", "Person", "loan", {})
    conn.upsertEdgeDataFrame(data, "Person", "PERSON_HAS_CONTACT", "Contact", "Person", "contact", {})
    conn.upsertEdgeDataFrame(data, "Person", "PERSON_HAS_PREVIOUS_OUTCOME", "PreviousOutcome", "Person", "poutcome", {})

    train = data[data["trainSet"] == True]
    train["confidence"] = 1
    conn.upsertEdgeDataFrame(train, "Person", "PERSON_HAS_OUTCOME", "Outcome", "Person", "y", {"confidence":"confidence"})
    