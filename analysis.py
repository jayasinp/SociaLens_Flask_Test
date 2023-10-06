
import networkx as nx
import pandas as pd
import json
import os

graph_sheets = [
    'net_0_Friends',
    'net_1_Influential',
    'net_2_Feedback',
    'net_3_MoreTime',
    'net_4_Advice',
    'net_5_Disrespect',
    'net_affiliation_0_SchoolActivit'
]

def generate_graphs(sheets_dict):
 #graph objects
    graphs_dict = {}
    for sheet in graph_sheets:
        G = nx.DiGraph()
        for index, row in sheets_dict[sheet].iterrows():
            source = row['Source']
            target = row['Target']
            G.add_edge(source, target)
        graphs_dict[sheet] = G
    return graphs_dict

def social_network_analysis(graphs_dict):
#SNA degrees centrality
    analysis_results = {}
    for sheet in graph_sheets:
        G = graphs_dict[sheet]
        degrees = dict(G.degree())
        sorted_degrees = sorted(degrees.items(), key=lambda x: x[1], reverse=True)
        analysis_results[sheet] = sorted_degrees
    return analysis_results

def generate_statistics(sheets_dict):
#descriptive statistics with describe()
    participants_df = sheets_dict['participants']
    columns_to_describe = ['Perc_Effort', 'Attendance','Perc_Academic','CompleteYears','House']
    desc_stats = participants_df[columns_to_describe].describe()
    return desc_stats

def export_as_json(data, filename, upload_folder):
#export to json
    filepath = os.path.join(upload_folder, filename)
    with open(filepath, 'w') as json_file:
        json.dump(data, json_file, default=int)