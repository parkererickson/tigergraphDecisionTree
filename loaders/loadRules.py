import pandas as pd

def load(conn, file1="./data/dTreeEdges.csv", **kwargs):
    df = pd.read_csv(file1)
    rules = df[(df["SourceType"] == "SubRule")]
    conn.upsertVertexDataFrame(rules, "SubRule", "Source", {"ruleType": "SourceRuleType"})
    rules = df[(df["TargetType"] == "SubRule")]
    conn.upsertVertexDataFrame(rules, "SubRule", "Target", {"ruleType": "TargetRuleType"})

    for edgeType in df["EdgeType"].unique():
        edges = df[(df["EdgeType"] == edgeType)]
        sourceType = edges["SourceType"].unique()[0]
        targetType = edges["TargetType"].unique()[0]
        conn.upsertEdgeDataFrame(edges, sourceType, edgeType, targetType, "Source", "Target", {})
